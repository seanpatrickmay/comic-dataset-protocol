"""comicset icc — inter-rater agreement analysis."""
from __future__ import annotations

import csv
from pathlib import Path

from .schema import load_dataset, save_dataset


def _compute_icc_31(ratings_a: list[float], ratings_b: list[float]) -> tuple[float, float, float]:
    """Compute ICC(3,1) — Two-Way Mixed, Absolute Agreement, Single Measures.

    Returns (icc, ci_low, ci_high) with 95% CI.
    """
    n = len(ratings_a)
    assert n == len(ratings_b) and n >= 3

    k = 2  # two raters
    grand_mean = sum(ratings_a + ratings_b) / (n * k)

    # Between-subjects mean square
    subject_means = [(a + b) / k for a, b in zip(ratings_a, ratings_b)]
    ms_between = k * sum((m - grand_mean) ** 2 for m in subject_means) / (n - 1)

    # Within-subjects mean square
    ss_within = sum(
        (a - m) ** 2 + (b - m) ** 2
        for a, b, m in zip(ratings_a, ratings_b, subject_means)
    )
    ms_within = ss_within / (n * (k - 1))

    # Rater mean square
    rater_means = [sum(ratings_a) / n, sum(ratings_b) / n]
    ms_rater = n * sum((rm - grand_mean) ** 2 for rm in rater_means) / (k - 1)

    # Error mean square
    ms_error = (ss_within - ms_rater * (k - 1) / n) if n > 1 else ms_within
    ms_error = max(ms_error, 1e-10)

    # ICC(3,1)
    icc = (ms_between - ms_error) / (ms_between + (k - 1) * ms_error)

    # F-test based CI (Shrout & Fleiss, 1979)
    f_value = ms_between / ms_error if ms_error > 0 else 1.0
    df1 = n - 1
    df2 = (n - 1) * (k - 1)

    # Approximate 95% CI using F distribution bounds
    # Lower bound
    try:
        from scipy.stats import f as f_dist
        f_low = f_value / f_dist.ppf(0.975, df1, df2)
        f_high = f_value / f_dist.ppf(0.025, df1, df2)
    except ImportError:
        # Rough approximation without scipy
        f_low = f_value * 0.5
        f_high = f_value * 2.0

    ci_low = max(-1.0, (f_low - 1) / (f_low + k - 1))
    ci_high = min(1.0, (f_high - 1) / (f_high + k - 1))

    return icc, ci_low, ci_high


def _grade_tier(grade: float) -> str:
    if grade >= 8.5:
        return "High (8.5+)"
    elif grade >= 5.5:
        return "Mid (5.5-8.4)"
    else:
        return "Low (≤5.4)"


def run_icc(args):
    dataset_dir = Path(args.dataset_dir).resolve()
    grades_path = Path(args.grades).resolve()

    # Load grades CSV
    grades: dict[str, tuple[float, float]] = {}
    with open(grades_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = row.get("slug", "").strip()
            try:
                g1 = float(row.get("sean_grade", row.get("grader_1", "")))
                g2 = float(row.get("marcus_grade", row.get("grader_2", "")))
                grades[slug] = (g1, g2)
            except (ValueError, TypeError):
                print(f"  Warning: skipping row with invalid grades: {slug}")

    if len(grades) < 3:
        print("Error: need at least 3 comics with valid grades from both raters")
        return

    # Compute ICC
    slugs = sorted(grades.keys())
    ratings_a = [grades[s][0] for s in slugs]
    ratings_b = [grades[s][1] for s in slugs]

    icc, ci_low, ci_high = _compute_icc_31(ratings_a, ratings_b)
    status = "✓ PASS" if icc >= 0.75 else "✗ FAIL"

    # Compute per-item stats
    diffs = [(s, grades[s][0], grades[s][1], abs(grades[s][0] - grades[s][1])) for s in slugs]
    diffs.sort(key=lambda x: x[3], reverse=True)

    mean_a = sum(ratings_a) / len(ratings_a)
    mean_b = sum(ratings_b) / len(ratings_b)
    offset = mean_a - mean_b

    # Per-tier ICC
    tier_data: dict[str, tuple[list[float], list[float]]] = {}
    for s in slugs:
        midpoint = (grades[s][0] + grades[s][1]) / 2
        tier = _grade_tier(midpoint)
        if tier not in tier_data:
            tier_data[tier] = ([], [])
        tier_data[tier][0].append(grades[s][0])
        tier_data[tier][1].append(grades[s][1])

    # Output
    print(f"\n{'═'*60}")
    print(f"Grade Agreement Analysis — {dataset_dir.name}")
    print(f"{'═'*60}")
    print(f"\nICC(3,1): {icc:.3f} [{ci_low:.3f}, {ci_high:.3f}] (95% CI)")
    print(f"Status: {status} (threshold: ≥ 0.75)")
    print(f"\nSystematic offset: Sean grades {abs(offset):.2f} {'higher' if offset > 0 else 'lower'} on average")
    print(f"Mean absolute difference: {sum(d[3] for d in diffs) / len(diffs):.2f}")

    # Per-tier breakdown
    print("\nPer-tier ICC:")
    for tier in ["High (8.5+)", "Mid (5.5-8.4)", "Low (≤5.4)"]:
        if tier in tier_data and len(tier_data[tier][0]) >= 3:
            t_icc, _, _ = _compute_icc_31(tier_data[tier][0], tier_data[tier][1])
            n_tier = len(tier_data[tier][0])
            print(f"  {tier}: ICC {t_icc:.3f} (n={n_tier})")
        elif tier in tier_data:
            print(f"  {tier}: n={len(tier_data[tier][0])} (too few for ICC)")

    # Disagreements
    big_diffs = [d for d in diffs if d[3] > 1.0]
    if big_diffs:
        print(f"\nDisagreements > 1.0 grade point ({len(big_diffs)} comics):")
        for slug, g1, g2, diff in big_diffs:
            print(f"  {slug:40s} Sean: {g1:4.1f}   Marcus: {g2:4.1f}   Δ={diff:.1f}")
    else:
        print("\nNo disagreements > 1.0 grade point ✓")

    print(f"\nAll {len(slugs)} comics:")
    for slug, g1, g2, diff in diffs[:10]:
        marker = " ← discuss" if diff > 1.0 else ""
        print(f"  {slug:40s} {g1:4.1f}  {g2:4.1f}  Δ={diff:.1f}{marker}")
    if len(diffs) > 10:
        print(f"  ... and {len(diffs) - 10} more (all within Δ≤{diffs[10][3]:.1f})")

    # Write grades into dataset
    try:
        dataset = load_dataset(dataset_dir)
        reconciled = 0
        needs_discussion = 0
        for slug, (g1, g2) in grades.items():
            if slug not in dataset.entries:
                continue
            entry = dataset.entries[slug]
            diff = abs(g1 - g2)
            if diff <= 1.0:
                midpoint = (g1 + g2) / 2
                entry.expected_grade_low = round(midpoint - 0.5, 1)
                entry.expected_grade_high = round(midpoint + 0.5, 1)
                entry.grade_tier = _grade_tier(midpoint).split(" ")[0].lower()
                reconciled += 1
            else:
                needs_discussion += 1

        save_dataset(dataset, dataset_dir)
        print(f"\nGrade ranges written: {reconciled} reconciled, {needs_discussion} need discussion")
    except FileNotFoundError:
        print(f"\nWarning: no annotations.json found in {dataset_dir} — grades not written")

    print(f"{'═'*60}\n")
