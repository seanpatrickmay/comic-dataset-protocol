"""comicset validate — check dataset completeness and correctness."""
from __future__ import annotations

from pathlib import Path

from .schema import load_dataset


def run_validate(args):
    dataset_dir = Path(args.dataset_dir).resolve()
    print(f"\nValidating: {dataset_dir}\n")

    errors = 0
    warnings = 0

    # Load dataset
    try:
        dataset = load_dataset(dataset_dir)
    except FileNotFoundError as exc:
        print(f"  ✗ {exc}")
        return

    print(f"  Schema version: {dataset.meta.version}")
    print(f"  Entries: {len(dataset.entries)}")

    # Check images exist
    images_dir = dataset_dir / "images"
    if not images_dir.is_dir():
        print("  ✗ images/ directory not found")
        errors += 1
    else:
        missing_images = []
        for slug, entry in dataset.entries.items():
            for view in entry.views:
                img_path = dataset_dir / view.image_path
                if not img_path.exists():
                    missing_images.append(view.image_path)
            # Also check manifest-referenced path
            front_path = images_dir / f"{slug}_front.jpg"
            if not front_path.exists():
                png_path = images_dir / f"{slug}_front.png"
                if not png_path.exists() and not any(v.role == "front" for v in entry.views):
                    missing_images.append(f"images/{slug}_front.jpg")

        if missing_images:
            print(f"  ✗ Missing images ({len(missing_images)}):")
            for p in missing_images[:5]:
                print(f"      {p}")
            if len(missing_images) > 5:
                print(f"      ... and {len(missing_images) - 5} more")
            errors += len(missing_images)
        else:
            total_images = sum(len(list(images_dir.glob(f"{slug}*"))) for slug in dataset.entries)
            print(f"  ✓ All referenced images present ({total_images} files)")

    # Check grades
    graded = sum(1 for e in dataset.entries.values() if e.expected_grade_low is not None)
    ungraded = len(dataset.entries) - graded
    if ungraded > 0:
        print(f"  ⚠ {ungraded}/{len(dataset.entries)} entries have no human grade ranges")
        warnings += ungraded
    else:
        print(f"  ✓ All {graded} entries have grade ranges")

    # Check grade ranges are valid
    for slug, entry in dataset.entries.items():
        if entry.expected_grade_low is not None and entry.expected_grade_high is not None:
            if entry.expected_grade_low > entry.expected_grade_high:
                print(f"  ✗ {slug}: grade_low ({entry.expected_grade_low}) > grade_high ({entry.expected_grade_high})")
                errors += 1
            if entry.expected_grade_low < 0.5 or entry.expected_grade_high > 10.0:
                print(f"  ✗ {slug}: grade range [{entry.expected_grade_low}, {entry.expected_grade_high}] outside CGC scale")
                errors += 1

    # Check defect keywords against backend chart
    backend_dir = None
    if hasattr(args, "backend_dir") and args.backend_dir:
        from .backend import resolve_backend_dir, get_defect_keywords
        backend_dir = resolve_backend_dir(args.backend_dir)
    else:
        from .backend import resolve_backend_dir, get_defect_keywords
        backend_dir = resolve_backend_dir()

    if backend_dir:
        valid_keywords = get_defect_keywords(backend_dir)
        bad_keywords = []
        for slug, entry in dataset.entries.items():
            for defect in entry.known_defects:
                if defect.defect_chart_keyword and defect.defect_chart_keyword not in valid_keywords:
                    bad_keywords.append((slug, defect.defect_chart_keyword))

        if bad_keywords:
            print(f"  ✗ Invalid defect_chart_keywords ({len(bad_keywords)}):")
            for slug, kw in bad_keywords[:5]:
                print(f"      {slug}: '{kw}'")
            errors += len(bad_keywords)
        else:
            annotated_defects = sum(len(e.known_defects) for e in dataset.entries.values())
            if annotated_defects > 0:
                print(f"  ✓ All {annotated_defects} defect keywords valid against defect chart")
            else:
                print("  ⚠ No defects annotated yet")
                warnings += 1
    else:
        print("  ⚠ Backend not found — cannot validate defect keywords")
        warnings += 1

    # Summary
    print(f"\n{'─'*40}")
    if errors == 0 and warnings == 0:
        print("  ✓ VALID — dataset is ready for deployment")
    elif errors == 0:
        print(f"  ⚠ {warnings} warning(s) — dataset is usable but incomplete")
    else:
        print(f"  ✗ {errors} error(s), {warnings} warning(s) — fix errors before deployment")
    print()
