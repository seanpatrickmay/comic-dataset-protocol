"""Main CLI entry point for comicset."""
from __future__ import annotations

import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="comicset",
        description="Comic grading dataset construction tools",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- ingest ---
    ingest_parser = subparsers.add_parser(
        "ingest",
        help="Process photos: identify comics, grade them, build dataset",
    )
    ingest_parser.add_argument("photos_dir", help="Directory of comic photos")
    ingest_parser.add_argument("--name", required=True, help="Dataset name (e.g., phase1_v1)")
    ingest_parser.add_argument("--output-dir", default="datasets", help="Root output directory")
    ingest_parser.add_argument(
        "--backend-dir",
        default=None,
        help="Path to comic backend repo (auto-detected from COMIC_BACKEND_DIR env or ../comic/backend)",
    )
    ingest_parser.add_argument("--skip-identify", action="store_true", help="Skip identification (grade only)")
    ingest_parser.add_argument("--skip-grade", action="store_true", help="Skip grading (identify only)")

    # --- validate ---
    validate_parser = subparsers.add_parser("validate", help="Validate dataset completeness and correctness")
    validate_parser.add_argument("dataset_dir", help="Path to dataset directory")
    validate_parser.add_argument("--backend-dir", default=None, help="Path to comic backend repo")

    # --- icc ---
    icc_parser = subparsers.add_parser("icc", help="Compute inter-rater agreement (ICC)")
    icc_parser.add_argument("dataset_dir", help="Path to dataset directory")
    icc_parser.add_argument("--grades", required=True, help="CSV with slug,sean_grade,marcus_grade")

    # --- status ---
    status_parser = subparsers.add_parser("status", help="Show dataset coverage and completeness")
    status_parser.add_argument("dataset_dir", help="Path to dataset directory")

    # --- annotate ---
    annotate_parser = subparsers.add_parser("annotate", help="Launch annotation web UI")
    annotate_parser.add_argument("dataset_dir", help="Path to dataset directory")
    annotate_parser.add_argument("--port", type=int, default=8000, help="Port for web UI")
    annotate_parser.add_argument("--backend-dir", default=None, help="Path to comic backend repo")

    # --- deploy ---
    deploy_parser = subparsers.add_parser("deploy", help="Package dataset for the grading harness")
    deploy_parser.add_argument("dataset_dir", help="Path to dataset directory")
    deploy_parser.add_argument("--target", required=True, help="Target test_sets directory")
    deploy_parser.add_argument("--backend-dir", default=None, help="Path to comic backend repo")

    args = parser.parse_args()

    if args.command == "ingest":
        from .ingest import run_ingest
        run_ingest(args)
    elif args.command == "validate":
        from .validate import run_validate
        run_validate(args)
    elif args.command == "icc":
        from .icc import run_icc
        run_icc(args)
    elif args.command == "status":
        from .status import run_status
        run_status(args)
    elif args.command == "annotate":
        from .annotate import run_annotate
        run_annotate(args)
    elif args.command == "deploy":
        from .deploy import run_deploy
        run_deploy(args)


if __name__ == "__main__":
    main()
