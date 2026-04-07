# Verification: Statistical Design Research
**Axis**: Statistical Design — Optimal Allocation of 70 Physical Comics  
**Date**: 2026-04-07  
**Verifier**: fact-checker agent

---

## Verdict: PASS for most claims — ONE MATERIAL ERROR in corrected CI table

The statistical design file's core calculations are sound. The Wilson CI values, Buderer sample sizes, and two-proportion power calculations are all correct. One material error was found: the "corrected effective CI" table in Section 4 uses an incorrect method and produces values that are too optimistic by approximately 1.5pp. This matters because it affects how Phase 1 results can be reported.

---

## Statistical Calculations: Spot-Checked

### Wilson CI at n=210, p=0.85 → ±4.8pp

**Status: VERIFIED**

Computed: ±4.83pp. Paper says ±4.8pp. Correct.

### Wilson CI at n=70, p=0.85 → ±8.3pp

**Status: VERIFIED**

Computed: ±8.35pp. Paper says ±8.3pp. Correct.

### Per-tier CI table (15/22/18/10/5 comics × 3 = 45/66/54/30/15 images)

**Status: VERIFIED**

| Tier | Images | Paper's CI | Computed CI | Result |
|---|---|---|---|---|
| High | 45 | ±10.4pp | ±10.4pp | CORRECT |
| Mid-High | 66 | ±8.6pp | ±8.6pp | CORRECT |
| Mid-Low | 54 | ±9.5pp | ±9.5pp | CORRECT |
| Low | 30 | ±12.7pp | ±12.7pp | CORRECT |
| Very Low | 15 | ±17.6pp | ±17.6pp | CORRECT |

All values confirmed.

### Buderer formula: N = 28 for S=0.80, w=±15pp

**Status: VERIFIED (rounding)**

Computed: N = 1.96² × 0.80 × 0.20 / 0.15² = 27.3, rounds to 28. Paper says 28. Correct.

### Two-proportion power: n=97 per tier for 90% vs. 75% accuracy, 80% power

**Status: VERIFIED**

Computed: n = (1.96 + 0.842)² × [0.90×0.10 + 0.75×0.25] / (0.15)² = 97.0. Paper says 97. Correct.

### Neyman allocation ratios: 0.25:0.50:0.40:0.35 → 11:22:18:14 (rounding to 15:22:18:10)

**Status: VERIFIED with minor rounding note**

Computed Neyman fractions × 65 comics: 10.8 : 21.7 : 17.3 : 15.2 = rounds to 11:22:17:15.

Paper rounds to 11:22:18:14 (using 18 instead of 17, and 14 instead of 15), then adjusts to 15:22:18:10 for practical reasons. These adjustments are explicitly described as practical judgment calls and the rounding difference is not material. The Neyman logic is sound.

---

## MATERIAL ERROR: Corrected Effective CI Table (Section 4)

### Claim: "70×3=210 images → corrected effective CI of ±5.9pp"

**Status: INCORRECT**

The paper computes: "±8.3pp / √(210/87) ≈ ±5.9pp"

This formula is not standard. The correct approach when accounting for within-comic clustering (DEFF = 2.4, eff_n = 87.5):
- Apply Wilson CI directly to effective_n = 87.5 → **±7.5pp**
- The paper's formula (dividing the n=70 CI by √(N_raw/eff_N)) gives ±3.1pp, not ±5.9pp

The paper's stated ±5.9pp is not reproducible from any standard formula. The correct DEFF-corrected CI for 210 clustered images is **±7.5pp** (not ±5.9pp).

**Why this matters**: The paper uses ±5.9pp to argue that 3-condition photography "crosses into reportable territory" for phase comparisons. At the correct ±7.5pp, the conclusion holds (it is still an improvement over ±8.3pp for a single condition), but the margin is tighter. The correction does not change the recommendation to photograph all 70 comics in 3 conditions, but it does change the headline CI claim.

See corrections.md for the corrected table.

### The partial-condition corrected CI table has inconsistent values

The corrected CI scenarios table shows:
- All 70×3=210 → ±5.9pp
- 50×3+20×1=170 → ±6.8pp
- 35×3+35×1=140 → ±7.5pp

These values cannot be reproduced with any consistent formula. Wilson applied to raw N gives ±4.8/±5.4/±5.9pp respectively. Wilson applied to DEFF-corrected effective N gives ±7.5/±7.7/±7.9pp. The table values are intermediate and appear to be rough estimates rather than computed values.

**Practical impact**: The table should be replaced with corrected values, but the directional ranking is correct (more conditions → tighter CI).

---

## ICC Claims

### "Below n=20, ICC CI half-width exceeds 0.15"

**Status: SLIGHTLY OFF**

Using the Bonett-approximation formula for ICC CI, at n=20, ρ=0.8, k=2 raters: half-width ≈ ±0.114 — below 0.15. At n=14, it reaches ~0.15. The claim that "below n=20" the half-width exceeds 0.15 is conservative; n<14 would be a more accurate threshold.

**Impact**: The conclusion to use at least 20 comics for ICC estimation is still correct (even at ±0.11, this is wide). The specific threshold claim is slightly imprecise but does not change the protocol recommendation.

### "n=30 double-graded specimens: CI approximately ±0.10"

**Status: SLIGHTLY OFF**

Computed half-width at n=30 ≈ ±0.092. The paper says ±0.10. Close enough; this is within rounding.

### "n=39: ICC CI half-width approximately ±0.12"

**Status: SLIGHTLY OFF (conservative)**

Computed: ±0.081. The paper says ±0.12. The paper's estimate is about 50% more conservative than computed. This is the safer direction (reporting a wider CI than actual), so it does not change any conclusions. But protocol users should know the actual CI at n=39 is approximately ±0.08, not ±0.12.

---

## D-Optimal Design Application

### Claim: "compound-defect specimens are highest information yield per comic"

**Status: MEDIUM CONFIDENCE — verified as reasonable extension**

D-optimal theory (Fisher information maximization) is well-established. Its application to AI evaluation design is a reasoned extension, not a direct citation from evaluation literature. The file correctly marks this MEDIUM confidence. The argument is logically sound.

---

## No Dangerous Claims Found

No hazardous procedures or setup errors. Statistical claims have directional correctness even where specific numbers are slightly off.
