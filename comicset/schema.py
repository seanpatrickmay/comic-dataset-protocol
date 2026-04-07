"""Annotation schema v3 — shared data structures for all commands."""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path

SCHEMA_VERSION = "3.0"


@dataclass
class DefectAnnotation:
    description: str
    defect_chart_keyword: str | None = None
    severity: str = "minor"  # minor | moderate | major
    zone: str | None = None
    annotator_confidence: str = "medium"  # high | medium | low


@dataclass
class StructuralAssessments:
    spine_condition: str | None = None
    corner_condition: str | None = None
    edge_condition: str | None = None
    staple_condition: str | None = None
    page_quality: str | None = None


@dataclass
class CaptureMetadata:
    device_class: str | None = None
    lighting: str | None = None
    distance_estimate: str | None = None
    angle: str | None = None
    resolution_px: str | None = None
    notes: str | None = None


@dataclass
class ImageView:
    role: str  # front | back | spine | detail
    image_path: str
    image_source: str = "user_photo"  # reference_scan | user_photo
    is_primary: bool = False
    capture_metadata: CaptureMetadata | None = None


@dataclass
class ComicAnnotation:
    # Identity (auto-filled by ingest)
    slug: str
    title: str | None = None
    publisher: str | None = None
    year: int | None = None
    gcd_issue_id: int | None = None

    # Ground truth grades (human-filled)
    expected_grade_low: float | None = None
    expected_grade_high: float | None = None

    # AI draft grades (auto-filled by ingest)
    ai_draft_grade: float | None = None
    ai_confidence: str | None = None
    ai_defects: list[DefectAnnotation] = field(default_factory=list)
    ai_reasoning: str | None = None

    # Classification
    grade_tier: str | None = None  # high | mid | low
    era: str | None = None
    art_style: str | None = None
    image_source: str | None = None
    cover_detection_difficulty: str | None = None

    # Annotation metadata
    annotator_confidence: str | None = None
    grading_difficulty: str | None = None
    annotation_method: str | None = None
    specimen_type: str = "natural"  # natural | controlled | reference_scan

    # Structural assessments (human-filled)
    structural_assessments: StructuralAssessments | None = None

    # Human-annotated defects (ground truth)
    known_defects: list[DefectAnnotation] = field(default_factory=list)

    # Controlled defect info
    controlled_defect_type: str | None = None  # for specimen_type=controlled
    controlled_defect_severity: str | None = None

    # Views
    views: list[ImageView] = field(default_factory=list)

    # Notes
    notes: str | None = None
    confounders: list[str] | None = None

    # Reference comparison
    self_comparison: bool = False
    self_comparison_expected_low: float | None = None
    self_comparison_expected_high: float | None = None
    reference_cover_path: str | None = None


@dataclass
class DatasetMeta:
    version: str = SCHEMA_VERSION
    created: str = ""
    name: str = ""
    ground_truth_tier: str = "bronze"


@dataclass
class Dataset:
    meta: DatasetMeta
    entries: dict[str, ComicAnnotation]


def save_dataset(dataset: Dataset, directory: Path) -> None:
    """Write manifest.jsonl and annotations.json to directory."""
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "images").mkdir(exist_ok=True)

    # Write manifest.jsonl
    with open(directory / "manifest.jsonl", "w") as f:
        for slug, entry in dataset.entries.items():
            manifest_entry = {
                "slug": slug,
                "gcd_issue_id": entry.gcd_issue_id or 0,
                "image_path": f"images/{slug}_front.jpg",
                "series_title": entry.title or "",
                "issue_number": "",
                "publisher": entry.publisher or "",
                "publication_year": entry.year or 0,
                "notes": entry.specimen_type,
            }
            f.write(json.dumps(manifest_entry) + "\n")

    # Write annotations.json
    annotations = {
        "_meta": asdict(dataset.meta),
        "entries": {},
    }
    for slug, entry in dataset.entries.items():
        annotations["entries"][slug] = _annotation_to_dict(entry)

    with open(directory / "annotations.json", "w") as f:
        json.dump(annotations, f, indent=2)


def load_dataset(directory: Path) -> Dataset:
    """Load a dataset from manifest.jsonl and annotations.json."""
    ann_path = directory / "annotations.json"
    if not ann_path.exists():
        raise FileNotFoundError(f"No annotations.json in {directory}")

    with open(ann_path) as f:
        raw = json.load(f)

    meta = DatasetMeta(**raw.get("_meta", {}))
    entries = {}
    for slug, data in raw.get("entries", {}).items():
        entries[slug] = _dict_to_annotation(slug, data)

    return Dataset(meta=meta, entries=entries)


def _annotation_to_dict(entry: ComicAnnotation) -> dict:
    """Convert a ComicAnnotation to a JSON-serializable dict, omitting None values."""
    d = asdict(entry)
    # Remove slug (it's the key)
    d.pop("slug", None)
    # Remove None values for cleaner JSON
    return {k: v for k, v in d.items() if v is not None}


def _dict_to_annotation(slug: str, data: dict) -> ComicAnnotation:
    """Convert a dict from annotations.json to a ComicAnnotation."""
    defects = [
        DefectAnnotation(**d) if isinstance(d, dict) else DefectAnnotation(description=str(d))
        for d in data.get("known_defects", [])
    ]
    ai_defects = [
        DefectAnnotation(**d) if isinstance(d, dict) else DefectAnnotation(description=str(d))
        for d in data.get("ai_defects", [])
    ]
    struct = None
    if data.get("structural_assessments"):
        struct = StructuralAssessments(**data["structural_assessments"])

    views = [ImageView(**v) for v in data.get("views", [])]

    return ComicAnnotation(
        slug=slug,
        title=data.get("title"),
        publisher=data.get("publisher"),
        year=data.get("year"),
        gcd_issue_id=data.get("gcd_issue_id"),
        expected_grade_low=data.get("expected_grade_low"),
        expected_grade_high=data.get("expected_grade_high"),
        ai_draft_grade=data.get("ai_draft_grade"),
        ai_confidence=data.get("ai_confidence"),
        ai_defects=ai_defects,
        ai_reasoning=data.get("ai_reasoning"),
        grade_tier=data.get("grade_tier"),
        era=data.get("era"),
        art_style=data.get("art_style"),
        image_source=data.get("image_source"),
        cover_detection_difficulty=data.get("cover_detection_difficulty"),
        annotator_confidence=data.get("annotator_confidence"),
        grading_difficulty=data.get("grading_difficulty"),
        annotation_method=data.get("annotation_method"),
        specimen_type=data.get("specimen_type", "natural"),
        structural_assessments=struct,
        known_defects=defects,
        controlled_defect_type=data.get("controlled_defect_type"),
        controlled_defect_severity=data.get("controlled_defect_severity"),
        views=views,
        notes=data.get("notes"),
        confounders=data.get("confounders"),
        self_comparison=data.get("self_comparison", False),
        self_comparison_expected_low=data.get("self_comparison_expected_low"),
        self_comparison_expected_high=data.get("self_comparison_expected_high"),
        reference_cover_path=data.get("reference_cover_path"),
    )
