"""comicset ingest — process photos through identification + grading pipelines."""
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


def _find_images(photos_dir: Path) -> list[Path]:
    """Find all image files in the directory, sorted by name."""
    images = []
    for p in sorted(photos_dir.iterdir()):
        if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS:
            images.append(p)
    return images


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


async def _process_image(
    image_path: Path,
    grader,
    identifier,
    output_dir: Path,
    skip_identify: bool,
    skip_grade: bool,
) -> ComicAnnotation | None:
    """Process a single image: identify, grade, and create annotation."""
    print(f"  Processing: {image_path.name}...", end=" ", flush=True)
    start = time.time()

    title = None
    issue_number = None
    publisher = None
    year = None
    gcd_issue_id = None
    reference_cover_path = None

    # --- Identification ---
    if identifier and not skip_identify:
        try:
            identification, ranked, match_status = identifier.identify(image_path)
            if identification:
                title = identification.series_title
                issue_number = identification.issue_number
                publisher = identification.publisher
                year = identification.year
            if ranked:
                gcd_issue_id = ranked[0].candidate.gcd_issue_id

                # Try to find a reference cover
                from comic_identifier.config import get_settings
                settings = get_settings()
                ref_path = settings.reference_covers_raw_root / f"{gcd_issue_id}.jpg"
                if not ref_path.exists():
                    ref_path = settings.reference_covers_normalized_root / f"{gcd_issue_id}.png"
                if ref_path.exists():
                    # Copy reference cover to dataset
                    ref_dest = output_dir / "reference_covers" / ref_path.name
                    ref_dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(ref_path, ref_dest)
                    reference_cover_path = f"reference_covers/{ref_path.name}"

            print(f"ID: {title} #{issue_number}", end=" ", flush=True)
        except Exception as exc:
            logger.debug("Identification failed for %s: %s", image_path.name, exc)
            print("ID: failed", end=" ", flush=True)
    else:
        print("ID: skipped", end=" ", flush=True)

    # --- Grading ---
    ai_grade = None
    ai_confidence = None
    ai_defects = []
    ai_reasoning = None

    if grader and not skip_grade:
        try:
            comic_context = f"{title or ''} #{issue_number or ''}".strip()
            result = await grader.grade(
                image_path,
                comic_context=comic_context if comic_context else None,
            )
            ai_grade = result.numeric_grade
            ai_confidence = result.confidence
            ai_reasoning = result.reasoning
            ai_defects = [
                DefectAnnotation(
                    description=d.description,
                    severity=d.severity,
                    zone=d.zone,
                )
                for d in result.defects
            ]
            print(f"Grade: {ai_grade}", end=" ", flush=True)
        except Exception as exc:
            logger.debug("Grading failed for %s: %s", image_path.name, exc)
            print("Grade: failed", end=" ", flush=True)
    else:
        print("Grade: skipped", end=" ", flush=True)

    slug = _slugify(title or image_path.stem, issue_number)
    elapsed = time.time() - start
    print(f"({elapsed:.1f}s)")

    # Copy image to dataset
    dest = output_dir / "images" / f"{slug}_front.jpg"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(image_path, dest)

    return ComicAnnotation(
        slug=slug,
        title=f"{title or ''} #{issue_number or ''}".strip() or image_path.stem,
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
        views=[
            ImageView(
                role="front",
                image_path=f"images/{slug}_front.jpg",
                image_source="user_photo",
                is_primary=True,
            ),
        ],
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

    print(f"Found {len(images)} images in {photos_dir}")

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

    print(f"\nOutput: {output_dir}")
    print(f"Processing {len(images)} images...\n")

    # Process each image
    entries: dict[str, ComicAnnotation] = {}
    used_slugs: set[str] = set()

    for image_path in images:
        annotation = await _process_image(
            image_path, grader, identifier, output_dir,
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

    # Summary
    identified = sum(1 for e in entries.values() if e.gcd_issue_id)
    graded = sum(1 for e in entries.values() if e.ai_draft_grade is not None)
    with_ref = sum(1 for e in entries.values() if e.reference_cover_path)

    print(f"\n{'='*60}")
    print(f"Ingest Complete — {args.name}")
    print(f"{'='*60}")
    print(f"Images processed: {len(entries)}")
    print(f"Identified:       {identified}/{len(entries)}")
    print(f"AI-graded:        {graded}/{len(entries)}")
    print(f"Reference covers: {with_ref}/{len(entries)}")
    print(f"\nDataset saved to: {output_dir}")
    print(f"  manifest.jsonl:   {len(entries)} entries")
    print(f"  annotations.json: {len(entries)} entries (AI drafts — add human grades next)")
    print("\nNext steps:")
    print(f"  1. Grade all {len(entries)} comics independently (you + Marcus)")
    print(f"  2. Run: comicset icc {output_dir} --grades grades.csv")
    print(f"  3. Run: comicset annotate {output_dir}")
    print(f"{'='*60}")


def run_ingest(args):
    asyncio.run(_run_ingest(args))
