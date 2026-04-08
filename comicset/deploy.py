"""comicset deploy — package dataset for the grading harness."""
from __future__ import annotations

import shutil
from pathlib import Path

from .schema import load_dataset
from .validate import run_validate


def run_deploy(args):
    dataset_dir = Path(args.dataset_dir).resolve()
    target_dir = Path(args.target).resolve()

    print(f"\nDeploying: {dataset_dir}")
    print(f"Target:    {target_dir}\n")

    # Run validation first
    print("Running validation...")
    run_validate(args)

    # Load dataset
    dataset = load_dataset(dataset_dir)

    # Check minimum requirements
    graded = sum(1 for e in dataset.entries.values() if e.expected_grade_low is not None)
    if graded == 0:
        print("✗ Cannot deploy — no entries have human grade ranges")
        print("  Run: comicset icc to add grades first")
        return

    # Confirm
    print(f"\nReady to deploy {len(dataset.entries)} entries ({graded} graded) to {target_dir}")
    response = input("Continue? [y/N] ").strip().lower()
    if response != "y":
        print("Aborted.")
        return

    # Copy
    if target_dir.exists():
        print(f"  Warning: {target_dir} exists, will overwrite")

    target_dir.mkdir(parents=True, exist_ok=True)

    # Copy images
    src_images = dataset_dir / "images"
    dst_images = target_dir / "images"
    if src_images.is_dir():
        if dst_images.exists():
            shutil.rmtree(dst_images)
        shutil.copytree(src_images, dst_images)
        print("  ✓ Copied images/")

    # Copy manifest and annotations
    for filename in ["manifest.jsonl", "annotations.json"]:
        src = dataset_dir / filename
        if src.exists():
            shutil.copy2(src, target_dir / filename)
            print(f"  ✓ Copied {filename}")

    # Copy reference covers if present
    ref_covers = dataset_dir / "reference_covers"
    if ref_covers.is_dir():
        dst_ref = target_dir / "reference_covers"
        if dst_ref.exists():
            shutil.rmtree(dst_ref)
        shutil.copytree(ref_covers, dst_ref)
        print("  ✓ Copied reference_covers/")

    print(f"\n✓ Deployed to {target_dir}")
    print("\nRun the harness:")
    print(f"  cd {target_dir.parent.parent}")
    print(f"  PYTHONPATH=. python3 tests/harness_grading.py --test-set {target_dir.name}")
    print()
