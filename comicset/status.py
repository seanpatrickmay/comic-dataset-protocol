"""comicset status — dataset coverage dashboard."""
from __future__ import annotations

from pathlib import Path

from .schema import load_dataset


def run_status(args):
    dataset_dir = Path(args.dataset_dir).resolve()
    dataset = load_dataset(dataset_dir)
    entries = dataset.entries

    total = len(entries)
    graded = sum(1 for e in entries.values() if e.expected_grade_low is not None)
    ai_graded = sum(1 for e in entries.values() if e.ai_draft_grade is not None)
    identified = sum(1 for e in entries.values() if e.gcd_issue_id)
    with_ref = sum(1 for e in entries.values() if e.reference_cover_path)
    annotated_defects = sum(len(e.known_defects) for e in entries.values())

    # Grade tier distribution
    tiers = {"high": 0, "mid": 0, "low": 0, "ungraded": 0}
    for e in entries.values():
        if e.expected_grade_low is not None and e.expected_grade_high is not None:
            midpoint = (e.expected_grade_low + e.expected_grade_high) / 2
            if midpoint >= 8.5:
                tiers["high"] += 1
            elif midpoint >= 5.5:
                tiers["mid"] += 1
            else:
                tiers["low"] += 1
        else:
            tiers["ungraded"] += 1

    # Specimen types
    specimen_counts = {}
    for e in entries.values():
        st = e.specimen_type or "natural"
        specimen_counts[st] = specimen_counts.get(st, 0) + 1

    # Defect category coverage
    defect_cats: dict[str, int] = {}
    for e in entries.values():
        for d in e.known_defects:
            if d.defect_chart_keyword:
                # We'd need the chart to map keyword → category, just count keywords for now
                defect_cats[d.defect_chart_keyword] = defect_cats.get(d.defect_chart_keyword, 0) + 1

    # Print
    bar = "═" * 60
    print(f"\n{bar}")
    print(f"Dataset Status — {dataset.meta.name or dataset_dir.name}")
    print(f"{bar}")
    print(f"\nComics:      {total}")
    print(f"Identified:  {identified}/{total}")
    print(f"AI-graded:   {ai_graded}/{total}")
    print(f"Human-graded:{graded}/{total}")
    print(f"Ref covers:  {with_ref}/{total}")
    print(f"Defects:     {annotated_defects} total across {sum(1 for e in entries.values() if e.known_defects)} comics")

    print(f"\nGrade Tier Distribution:")
    for tier, count in [("High (8.5+)", tiers["high"]), ("Mid (5.5-8.4)", tiers["mid"]), ("Low (≤5.4)", tiers["low"])]:
        bar_str = "█" * count
        print(f"  {tier:15s} {count:3d}  {bar_str}")
    if tiers["ungraded"]:
        print(f"  {'Ungraded':15s} {tiers['ungraded']:3d}")

    print(f"\nSpecimen Types:")
    for st, count in sorted(specimen_counts.items()):
        print(f"  {st:15s} {count}")

    if defect_cats:
        print(f"\nDefect Keywords (annotated):")
        for kw, count in sorted(defect_cats.items(), key=lambda x: -x[1]):
            print(f"  {kw:25s} {count}")

    print(f"\n{bar}\n")
