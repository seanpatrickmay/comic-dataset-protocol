"""comicset ingest — process photos through identification + grading pipelines.

Expects a flat folder of photos taken in a fixed 4-shot sequence per comic:
  1. Front cover  (identified → names the comic)
  2. Back cover
  3. Interior spread 1 (center/staples — shows page color + centerfold condition)
  4. Interior spread 2 (near back — back pages yellow more)

Photos are sorted by filename (timestamp order from iPhone).
Every 4 images = one comic.
"""
from __future__ import annotations

import asyncio
import logging
import re
import shutil
import time
from datetime import datetime
from pathlib import Path

from .backend import resolve_backend_dir, get_grader, add_backend_to_path
from .schema import (
    ComicAnnotation,
    Dataset,
    DatasetMeta,
    DefectAnnotation,
    ImageView,
    save_dataset,
)

logger = logging.getLogger(__name__)

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".heic", ".heif"}
SHOTS_PER_COMIC = 4
SHOT_ROLES = ["front", "back", "interior-1", "interior-2"]


def _find_images(photos_dir: Path) -> list[Path]:
    """Find all image files in the directory, sorted by name."""
    return sorted(
        (p for p in photos_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS),
        key=lambda p: p.name,
    )


def _slugify(title: str, issue: str | None) -> str:
    """Generate a slug from title and issue number."""
    raw = f"{title} {issue or ''}".strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", raw).strip("-")
    return slug or "unknown"


def _make_unique_slug(slug: str, existing: set[str]) -> str:
    """Ensure slug is unique by appending a suffix if needed."""
    if slug not in existing:
        return slug
    for i in range(2, 100):
        candidate = f"{slug}-{i}"
        if candidate not in existing:
            return candidate
    return f"{slug}-{int(time.time())}"


def _identify_cover(image_path: Path, identifier) -> tuple[str | None, str | None, str | None, int | None, int | None]:
    """Run identification on a front cover image.

    Returns (title, issue_number, publisher, year, gcd_issue_id).
    """
    try:
        identification, ranked, _ = identifier.identify(image_path)
        title = identification.series_title if identification else None
        issue = identification.issue_number if identification else None
        publisher = identification.publisher if identification else None
        year = identification.year if identification else None
        gcd_id = ranked[0].candidate.gcd_issue_id if ranked else None
        return title, issue, publisher, year, gcd_id
    except Exception as exc:
        logger.debug("Identification failed for %s: %s", image_path.name, exc)
        return None, None, None, None, None


def _copy_reference_cover(gcd_issue_id: int, output_dir: Path) -> str | None:
    """Copy reference cover from corpus to dataset. Returns relative path or None."""
    try:
        from comic_identifier.config import get_settings
        settings = get_settings()
        for ref_path in [
            settings.reference_covers_raw_root / f"{gcd_issue_id}.jpg",
            settings.reference_covers_normalized_root / f"{gcd_issue_id}.png",
        ]:
            if ref_path.exists():
                ref_dest = output_dir / "reference_covers" / ref_path.name
                ref_dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ref_path, ref_dest)
                return f"reference_covers/{ref_path.name}"
    except Exception:
        pass
    return None


async def _grade_comic(
    grader,
    front_path: Path,
    back_path: Path | None,
    spine_path: Path | None,
    internal_paths: list[Path],
    comic_context: str | None,
    reference_path: Path | None,
) -> tuple[float | None, str | None, list[DefectAnnotation], str | None]:
    """Grade a comic with all available images. Returns (grade, confidence, defects, reasoning)."""
    try:
        result = await grader.grade(
            front_path,
            comic_context=comic_context,
            reference_image_path=reference_path,
            back_image_path=back_path,
            spine_image_path=spine_path,
            internal_image_paths=internal_paths or None,
        )
        defects = [
            DefectAnnotation(
                description=d.description,
                severity=d.severity,
                zone=d.zone,
            )
            for d in result.defects
        ]
        return result.numeric_grade, result.confidence, defects, result.reasoning
    except Exception as exc:
        logger.debug("Grading failed: %s", exc)
        return None, None, [], None


async def _process_group(
    group_index: int,
    images: list[Path],
    identifier,
    grader,
    output_dir: Path,
    skip_identify: bool,
    skip_grade: bool,
) -> ComicAnnotation | None:
    """Process a group of 6 images as one comic."""
    print(f"\n  Comic {group_index + 1}: {images[0].name} (+{len(images)-1} more)")

    # --- Identify from front cover ---
    title = None
    issue_number = None
    publisher = None
    year = None
    gcd_issue_id = None
    reference_cover_path = None

    if identifier and not skip_identify:
        title, issue_number, publisher, year, gcd_issue_id = _identify_cover(images[0], identifier)
        if title:
            print(f"    ID: {title} #{issue_number}")
        else:
            print("    ID: not recognized")

        if gcd_issue_id:
            reference_cover_path = _copy_reference_cover(gcd_issue_id, output_dir)
            if reference_cover_path:
                print("    Reference cover: found")

    # --- Build slug and copy images ---
    slug = _slugify(title or f"comic-{group_index + 1:03d}", issue_number)
    images_dir = output_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)

    views: list[ImageView] = []
    copied_paths: dict[str, Path] = {}

    for i, (img_path, role) in enumerate(zip(images, SHOT_ROLES)):
        dest_name = f"{slug}_{role}.jpg"
        dest = images_dir / dest_name
        shutil.copy2(img_path, dest)
        is_primary = (role == "front")
        views.append(ImageView(
            role=role,
            image_path=f"images/{dest_name}",
            image_source="user_photo",
            is_primary=is_primary,
        ))
        copied_paths[role] = dest

    # --- Grade with all images ---
    ai_grade = None
    ai_confidence = None
    ai_defects: list[DefectAnnotation] = []
    ai_reasoning = None

    if grader and not skip_grade:
        comic_context = f"{title or ''} #{issue_number or ''}".strip() or None

        # Resolve reference image for grading
        ref_grade_path = None
        if reference_cover_path:
            ref_grade_path = output_dir / reference_cover_path

        ai_grade, ai_confidence, ai_defects, ai_reasoning = await _grade_comic(
            grader,
            front_path=copied_paths["front"],
            back_path=copied_paths.get("back"),
            spine_path=None,
            internal_paths=[copied_paths[r] for r in SHOT_ROLES[2:] if r in copied_paths],
            comic_context=comic_context,
            reference_path=ref_grade_path,
        )
        if ai_grade is not None:
            print(f"    Grade: {ai_grade} ({ai_confidence} confidence, {len(ai_defects)} defects)")
        else:
            print("    Grade: failed")

    return ComicAnnotation(
        slug=slug,
        title=f"{title or ''} #{issue_number or ''}".strip() or f"Comic {group_index + 1:03d}",
        publisher=publisher,
        year=year,
        gcd_issue_id=gcd_issue_id,
        ai_draft_grade=ai_grade,
        ai_confidence=ai_confidence,
        ai_defects=ai_defects,
        ai_reasoning=ai_reasoning,
        image_source="user_photo",
        annotation_method="ai_draft",
        reference_cover_path=reference_cover_path,
        views=views,
    )


async def _run_ingest(args) -> None:
    photos_dir = Path(args.photos_dir).resolve()
    if not photos_dir.is_dir():
        print(f"Error: {photos_dir} is not a directory")
        return

    images = _find_images(photos_dir)
    if not images:
        print(f"Error: no images found in {photos_dir}")
        return

    n_comics = len(images) // SHOTS_PER_COMIC
    remainder = len(images) % SHOTS_PER_COMIC

    print(f"Found {len(images)} images in {photos_dir}")
    print(f"At {SHOTS_PER_COMIC} shots per comic: {n_comics} comics")
    if remainder:
        print(f"  Warning: {remainder} leftover image(s) — last comic has only {remainder} shots")

    # Resolve backend
    backend_dir = resolve_backend_dir(args.backend_dir)
    if backend_dir:
        print(f"Backend: {backend_dir}")
        add_backend_to_path(backend_dir)
    else:
        print("Warning: Backend not found — identification and grading will be skipped")

    # Set up pipelines
    grader = None
    identifier = None

    if backend_dir and not args.skip_grade:
        try:
            grader = get_grader(backend_dir)
            print("Grading pipeline: ready")
        except Exception as exc:
            print(f"Grading pipeline: unavailable ({exc})")

    if backend_dir and not args.skip_identify:
        try:
            from .backend import get_identifier
            identifier = get_identifier(backend_dir)
            print("Identification pipeline: ready")
        except Exception as exc:
            print(f"Identification pipeline: unavailable ({exc})")

    # Create output directory
    output_dir = Path(args.output_dir) / args.name
    output_dir.mkdir(parents=True, exist_ok=True)

    # Group images into comics (every SHOTS_PER_COMIC images = one comic)
    groups: list[list[Path]] = []
    for i in range(0, len(images), SHOTS_PER_COMIC):
        groups.append(images[i:i + SHOTS_PER_COMIC])

    print(f"\nOutput: {output_dir}")
    print(f"Processing {len(groups)} comics ({len(images)} images)...")

    # Process each group
    entries: dict[str, ComicAnnotation] = {}
    used_slugs: set[str] = set()
    start_total = time.time()

    for i, group in enumerate(groups):
        annotation = await _process_group(
            i, group, identifier, grader, output_dir,
            skip_identify=args.skip_identify or identifier is None,
            skip_grade=args.skip_grade or grader is None,
        )
        if annotation:
            slug = _make_unique_slug(annotation.slug, used_slugs)
            annotation.slug = slug
            used_slugs.add(slug)
            entries[slug] = annotation

    # Build and save dataset
    dataset = Dataset(
        meta=DatasetMeta(
            version="3.0",
            created=datetime.now().strftime("%Y-%m-%d"),
            name=args.name,
        ),
        entries=entries,
    )
    save_dataset(dataset, output_dir)

    elapsed = time.time() - start_total

    # Summary
    identified = sum(1 for e in entries.values() if e.gcd_issue_id)
    graded = sum(1 for e in entries.values() if e.ai_draft_grade is not None)
    with_ref = sum(1 for e in entries.values() if e.reference_cover_path)
    total_views = sum(len(e.views) for e in entries.values())

    print(f"\n{'='*60}")
    print(f"Ingest Complete — {args.name} ({elapsed:.0f}s)")
    print(f"{'='*60}")
    print(f"Comics:           {len(entries)}")
    print(f"Total images:     {total_views}")
    print(f"Identified:       {identified}/{len(entries)}")
    print(f"AI-graded:        {graded}/{len(entries)}")
    print(f"Reference covers: {with_ref}/{len(entries)}")
    print(f"\nDataset saved to: {output_dir}")
    print("\nNext steps:")
    print(f"  1. Grade all {len(entries)} comics independently (you + Marcus)")
    print(f"  2. Run: comicset icc {output_dir} --grades grades.csv")
    print(f"  3. Run: comicset annotate {output_dir}")
    print(f"{'='*60}")


def run_ingest(args):
    asyncio.run(_run_ingest(args))
