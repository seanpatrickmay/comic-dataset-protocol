"""Backend integration — imports from the comic grading pipeline."""
from __future__ import annotations

import os
import sys
from pathlib import Path


def resolve_backend_dir(cli_arg: str | None = None) -> Path:
    """Find the comic backend directory."""
    if cli_arg:
        p = Path(cli_arg).resolve()
        if (p / "comic_identifier").is_dir():
            return p
        raise FileNotFoundError(f"Backend not found at {p} (no comic_identifier/ subdirectory)")

    env = os.getenv("COMIC_BACKEND_DIR")
    if env:
        p = Path(env).resolve()
        if (p / "comic_identifier").is_dir():
            return p

    # Auto-detect: sibling directory
    for candidate in [
        Path(__file__).resolve().parents[2] / "comic" / "backend",
        Path.cwd().parent / "comic" / "backend",
        Path.home() / "Desktop" / "Current Projects" / "comic" / "backend",
    ]:
        if candidate.is_dir() and (candidate / "comic_identifier").is_dir():
            return candidate

    return None


def add_backend_to_path(backend_dir: Path) -> None:
    """Add the backend directory to sys.path so we can import from it."""
    backend_str = str(backend_dir)
    if backend_str not in sys.path:
        sys.path.insert(0, backend_str)


def get_identifier(backend_dir: Path):
    """Get a HybridIdentifier instance. Requires database."""
    add_backend_to_path(backend_dir)
    from comic_identifier.config import get_settings
    from comic_identifier.repository import CatalogRepository
    from comic_identifier.vision import ClaudeVisionIdentifier
    from comic_identifier.corpus import CoverCorpusService
    from comic_identifier.identifier import HybridIdentifier
    from comic_identifier.storage import LocalObjectStorage

    settings = get_settings()
    repository = CatalogRepository(settings)
    storage = LocalObjectStorage(settings)
    vision = ClaudeVisionIdentifier(settings)
    corpus = CoverCorpusService(settings, repository, storage)
    return HybridIdentifier(settings, repository, vision, corpus)


def get_grader(backend_dir: Path):
    """Get a ClaudeGrader instance. Only needs API key."""
    add_backend_to_path(backend_dir)
    from comic_identifier.config import get_settings
    from comic_identifier.grading import ClaudeGrader

    settings = get_settings()
    return ClaudeGrader(settings)


def get_defect_keywords(backend_dir: Path) -> set[str]:
    """Get all valid defect chart keywords from the backend."""
    add_backend_to_path(backend_dir)
    from comic_identifier.defect_chart import DEFECT_ENTRY_BY_KEYWORD
    return set(DEFECT_ENTRY_BY_KEYWORD.keys())


def get_defect_categories(backend_dir: Path) -> dict[str, list[str]]:
    """Get defect categories mapped to their keywords."""
    add_backend_to_path(backend_dir)
    from comic_identifier.defect_chart import DEFECT_CATEGORIES
    return {cat: [e.keyword for e in entries] for cat, entries in DEFECT_CATEGORIES.items()}
