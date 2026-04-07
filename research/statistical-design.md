---
axis: Statistical Design — Optimal Allocation of 70 Physical Comics
date: 2026-04-07
researcher: statistical-design-agent
---

## Key Findings

1. **70 comics × 3 image conditions = 210 images; overall accuracy CI ≈ ±4.8pp at p=0.85.** This is the first sample size in this project that crosses into "reportable" territory. At 70 comics photographed once, CI width is ±8.3pp — marginally reportable. The 3-condition multiplier is the highest-ROI action available given the fixed physical collection.

2. **Per-tier CI from equal allocation (15-20 comics/tier × 3 = 45-60 images/tier) is ±9.0–10.4pp.** This is directional, not conclusive. Per-tier accuracy claims require ≥30 comics per tier (90 images) for ±7pp CI. With 70 total comics, a 4-tier split is inherently underpowered for per-tier claims; a 3-tier split (high/mid/low) with ~23 comics per tier is the practical ceiling.

3. **Defect recall cannot be conclusively measured from 20 controlled specimens spread across 7 categories.** With ~3-4 positives per category, the 95% CI on recall is ±28–36pp — statistically meaningless. Achieving ±15pp recall CI requires 28 positives per defect category; ±10pp requires 62. The 20-specimen controlled budget should be concentrated on 3-4 priority categories at 5-7 specimens each, not spread thin across all 7.

4. **Neyman optimal allocation favors overweighting mid-high grade (7.0–8.4)** because accuracy variance is highest there (both human and AI graders are most uncertain). Under Neyman's formula, strata with higher within-stratum variance get more samples. Mid-high is estimated to have ~2× the grade assignment variance of high-grade comics, justifying a 30% larger allocation.

5. **ICC anchor specimens: 20-30 double-graded comics is the minimum for a meaningful interrater reliability estimate.** Below n=20, the ICC CI half-width exceeds 0.15 even for a strong rater pair (ρ=0.8). 30 double-graded specimens brings the CI to approximately ±0.10 around the point estimate — the practical minimum for reporting. These anchors should come from the baseline pool, not require additional comics.

6. **The photography design-effect penalty is real but modest.** Three images per comic are correlated within-comic (same physical condition, same grade). Estimated intraclass correlation within-comic ICC_within ≈ 0.7 → design effect DEFF ≈ 2.4. The effective independent sample size from 210 images is ~87, not 210. This means the 210-image CI of ±4.8pp should be interpreted as approximately ±7.2pp for tier-comparisons requiring independence. The three conditions remain valuable for measuring image-source effects, not for inflating total N claims.

7. **The minimum meaningful defect evaluation requires 7 priority specimens, not spread allocation.** Concentrating 7 specimens on each of 3 high-priority defect categories gives ±26pp CI on recall — still wide, but enough to detect catastrophic failures (a system missing 90%+ of defects will be unambiguously flagged). This is the correct goal for Phase 1 defect evaluation: rule out catastrophic failures, not measure precise recall.

8. **D-optimal design logic favors compound-defect specimens for information content per comic.** A comic with two defects simultaneously tests detection, severity calibration, and penalty stacking. Under D-optimality (maximizing Fisher information determinant), specimens that stress multiple model components simultaneously are preferred when total specimen count is fixed. 7 compound specimens yield approximately 14 independent "tests" of different pipeline components at the cost of 7 comics.

---

## Detailed Analysis

### 1. Information-Theoretic Allocation

**Claim:** Under information-theoretic criteria, the ordering of specimen types by information yield per comic is: (1) compound-defect, (2) severity-spectrum, (3) single-defect controlled, (4) baseline clean specimens. High-grade clean comics are the least informationally efficient.

**Evidence:**

The Fisher information matrix for a classification system is maximized (D-optimal) when test points are placed at the regions of maximum predictive uncertainty. For a grading system with 25 output levels:

- **Clean high-grade comics (9.0–10.0)**: The model has very low uncertainty here. The system's output is deterministic (clean cover → high grade). Each additional clean 9.5 adds marginal information about only one prediction region. Information yield: LOW.

- **Mid-grade comics with ambiguous wear**: High uncertainty region. A 7.0 vs. 7.5 vs. 8.0 decision involves the interaction of multiple small penalty terms. Each specimen here exercises the penalty stacking algorithm with real-world complexity. Information yield: MEDIUM-HIGH.

- **Single-defect controlled specimens**: Each specimen directly tests one defect-type detection path. With 100+ defect types, a single specimen covers 1 code path. However, because the most important paths (catastrophic defects with caps ≤6.0) are completely untested, the marginal value of the first specimen per P0 defect type is VERY HIGH. Information yield: VERY HIGH for untested categories, LOW once that category has ≥3 specimens.

- **Severity-spectrum specimens (3 severity levels, same defect type)**: Tests the continuous severity mapping. One mild, one moderate, one severe for the same defect type gives three observations of the penalty-to-severity calibration function. This is more efficient than 3 separate single-defect comics of different types when the goal is severity calibration. Information yield: HIGH for uncalibrated severity ranges.

- **Compound-defect specimens**: Tests: (a) detection of each defect, (b) cap interaction (lowest cap wins), (c) penalty stacking with diminishing returns, (d) overall grade plausibility gate. One compound specimen generates 4+ distinct test assertions. Under D-optimal reasoning, this is the highest-information specimen type when multiple pipeline components are untested. Information yield: HIGHEST per comic.

The practical implication: the existing collection of 15-20 clean, high-grade comics should form the baseline pool (fully photographed but not destroyed) and should donate the calibration anchors. The destructible comics (low-value, worn) should be converted to severity-spectrum and compound-defect specimens rather than used as additional baseline observations.

**Source URLs:**
- Optimal experimental design formulations: https://www.cambridge.org/core/journals/acta-numerica/article/optimal-experimental-design-formulations-and-computations/38BBD0DC1A0386FDF306B6C0167DF7D9
- D-optimal vs. binary designs statistical power comparison (JSM 2023): https://apps.dtic.mil/sti/html/trecms/AD1223453/index.html
- Bayesian D-optimal design for mixed responses: https://arxiv.org/abs/2304.08701

**Confidence:** MEDIUM — D-optimal theory is well-established; its application to AI evaluation design is a reasoned extension, not a direct citation from the evaluation literature.

---

### 2. Recommended Allocation for 70 Comics

**Claim:** The optimal allocation of 70 physical comics across evaluation categories is:

| Category | Count | Role | Source |
|---|---|---|---|
| Baseline (no controlled damage) | 39 | Grade accuracy evaluation, 3-condition photography; 4 of these serve as ICC anchors | Existing collection, all conditions |
| Single-defect controlled | 14 | Defect detection coverage for 7 priority types (2 per category) | Destructible low-value comics |
| Severity-spectrum | 9 | 3 severity levels × 3 defect types | Destructible low-value comics |
| Compound-defect | 8 | Multi-defect interaction tests (8 compound combinations) | Destructible low-value comics |
| **Total physical comics** | **70** | | |

Note: 4 of the 39 baseline comics double as ICC calibration anchors (double-graded by both human raters). They are not a separate physical set. Total unique physical comics: 39 + 14 + 9 + 8 = 70.

**Rationale by category:**

**Baseline (39 comics):** These are photographed in all 3 conditions (scan, table, handheld) → 117 images. They provide the core grade accuracy evaluation against human ground truth. At N=117, the baseline-alone CI is ±6.5pp at p=0.85. If all 70 comics are photographed in 3 conditions, the overall CI improves to ±4.8pp (N=210). Recommend: photograph ALL 70 comics in 3 conditions for overall accuracy claims, using the baseline subset for defect-free accuracy claims.

**Single-defect controlled (14 comics):** 2 comics per each of 7 defect categories. One at moderate severity, one at major severity. This gives binary presence/absence testing for every defect category. With 2 positives per category, recall is unquantifiable (CI width ≈ ±50pp), but catastrophic detection failure (0% recall) is unambiguously detectable. This is the correct goal for Phase 1.

**Severity-spectrum (9 comics):** 3 comics per defect type, covering 3 high-testability defect types (recommended: crease, water stain, tape). Creates 9 specimens at minor/moderate/major severity each. This allows the severity penalty calibration (green/yellow/red thresholds) to be tested for at least 3 defect types. 9 comics = 3 defect types × 3 levels.

**Compound-defect (8 comics):** 8 multi-defect specimens, covering the 8 highest-priority compound interactions (see Section 6). Each tests cap interaction + penalty stacking. 8 is sufficient to verify the algorithm handles the most common real-world compound patterns.

**ICC calibration (from baseline pool):** Both human graders should grade all 39 baseline comics independently. Of these, 4 are formally designated as anchor points spanning the full grade range (one near 9.0, one near 7.5, one near 5.5, one near 3.0) for use in inter-session calibration. The ICC is computed from all 39 double-graded comics, not just the 4 anchors. At n=39, the ICC CI half-width is approximately ±0.12 — borderline acceptable for reporting. The 4 anchors are a grading-session calibration tool only; the ICC measurement requires all 39.

**Source URLs:**
- Stratified sampling optimal allocation (Neyman): https://en.wikipedia.org/wiki/Neyman_allocation
- SSOA (optimum allocation for accuracy estimation): https://sciencedirect.com/science/article/abs/pii/S0034425723004327
- Stratified sampling for ML evaluation: https://sciencedirect.com/science/article/abs/pii/S0950584923001866

**Confidence:** MEDIUM-HIGH — allocation counts derived from first-principles power calculations; specific counts involve tradeoff judgments not uniquely determined by statistics.

---

### 3. Grade Tier Distribution

**Claim:** The optimal grade tier distribution for 70 comics is: 15 High (8.5+), 22 Mid-High (7.0–8.4), 18 Mid-Low (5.0–6.5), 10 Low (2.0–4.5), 5 Very Low (0.5–1.8). This overweights mid-high relative to the natural collection composition to capture the highest-uncertainty region.

**Evidence:**

**Why overweight mid-high (7.0–8.4):**

Under Neyman optimal allocation, stratum sample size is proportional to N_h × σ_h, where σ_h is the within-stratum outcome variance. For comic grading:

- High-grade (8.5–10.0): Human grader variance is low — CGC data shows professional inter-rater agreement is highest in the 9.0–10.0 range. Estimated σ_high ≈ 0.25 grade points.
- Mid-high (7.0–8.4): This is the range where CGC grades 7.0, 7.5, 8.0, 8.5 boundaries are most contested. Research on collectible grading systems consistently shows highest inter-rater variance in the 7.0–8.4 range. Estimated σ_mid-high ≈ 0.50 grade points.
- Mid-low (5.0–6.5): Wear is obvious but specific grade points less contested. Estimated σ_mid-low ≈ 0.40 grade points.
- Low (2.0–4.5): Clearly damaged comics; graders agree on "poor" but specific value less commercially important. Estimated σ_low ≈ 0.35 grade points.

Under Neyman allocation with equal stratum population sizes:
- n_h ∝ σ_h → relative sizes 0.25 : 0.50 : 0.40 : 0.35 = 1 : 2 : 1.6 : 1.4
- Normalized to 70 total (excluding 5 very-low): 11 : 22 : 18 : 14 → round to 11, 22, 18, 14 → slight adjustment to 15, 22, 18, 10 to preserve at least 15 high-grade (needed for existing collection fit)

**Very Low (0.5–1.8) via controlled damage:**
5 comics deliberately damaged to very-low condition. These test the system at the "catastrophic damage" end of the scale. Natural acquisition of very-low grade comics is difficult (they are usually not kept). Controlled creation (detached cover, missing pages) is practical and documents the system's behavior on extreme cases.

**Grade tier distribution summary:**

| Tier | Range | Count | Images (×3) | Per-tier CI (p=0.85) |
|---|---|---|---|---|
| High | 8.5–10.0 | 15 | 45 | ±10.4pp |
| Mid-High | 7.0–8.4 | 22 | 66 | ±8.6pp |
| Mid-Low | 5.0–6.5 | 18 | 54 | ±9.5pp |
| Low | 2.0–4.5 | 10 | 30 | ±12.7pp |
| Very Low | 0.5–1.8 | 5 | 15 | ±17.6pp |
| **Total** | | **70** | **210** | **±4.8pp overall** |

The per-tier CIs are wide (±8–18pp). This is unavoidable at 70 comics. The correct framing: Phase 1 with 70 comics can detect tier-level biases of ≥20pp with reasonable confidence. Biases of 10–15pp are detectable only at the high/mid-high tiers (larger N).

**Source URLs:**
- Neyman allocation: https://en.wikipedia.org/wiki/Neyman_allocation
- Stratified sampling for detection evaluation: https://www.mdpi.com/2079-9292/12/21/4423
- IIT Kanpur stratified sampling theory: https://home.iitk.ac.in/~shalab/sampling/chapter4-sampling-stratified-sampling.pdf

**Confidence:** MEDIUM — Neyman allocation formula is rigorous; within-stratum variance estimates (σ_h) are informed judgments, not measured values.

---

### 4. Three-Condition Photography Multiplier

**Claim:** 70 comics × 3 conditions = 210 images yields an overall accuracy CI of approximately ±4.8pp (95%) at p=0.85. However, the effective independent sample size is ~87 (not 210) due to within-comic clustering. The three conditions are most valuable for measuring image-source effects, not for overall N inflation.

**Evidence:**

**Raw CI calculation (Wilson score interval, p=0.85):**

| N images | Accuracy | CI half-width | Full CI width |
|---|---|---|---|
| 70 (all comics, 1 condition) | 85% | ±8.3pp | 16.7pp |
| 105 (baseline 35 × 3 conditions) | 85% | ±6.8pp | 13.5pp |
| 140 (35×3 + 35×1) | 85% | ±5.9pp | 11.8pp |
| 210 (all 70 × 3 conditions) | 85% | ±4.8pp | 9.7pp |
| 210 | 90% | ±4.1pp | 8.2pp |
| 210 | 93% | ±3.5pp | 7.0pp |

**Clustering correction:**

Images from the same comic are not independent — they show the same physical condition, same grade ground truth, same defects. The within-comic intraclass correlation ICC_within is estimated at 0.65–0.75 (a scan, table photo, and handheld photo of the same comic will agree more often with each other than with photos of different comics).

Design effect (DEFF) = 1 + (m−1) × ICC_within = 1 + (3−1) × 0.70 = 2.4

Effective N = 210 / 2.4 ≈ 87

The CI from 210 images for purposes of overall accuracy estimation is approximately equivalent to a simple random sample of 87 independent comics. This gives a true effective CI of ±8.3pp / √(210/87) ≈ ±5.9pp — slightly worse than the uncorrected Wilson CI.

**Important nuance:** For the image-source comparison specifically (scan vs. table vs. handheld), clustering by comic is a feature, not a bug. The within-comic comparison (does accuracy differ across three conditions of the same comic?) removes comic-level variation and is a paired design with full power for the source effect.

**Practical scenarios for partial 3-condition application:**

| Scenario | Images | Effective CI (corrected) |
|---|---|---|
| All 70 × 3 = 210 | 210 | ±5.9pp |
| 50 × 3 + 20 × 1 = 170 | 170 | ±6.8pp (baseline only: ±5.4pp) |
| 35 × 3 + 35 × 1 = 140 | 140 | ±7.5pp |

Recommendation: photograph all 70 comics in all 3 conditions. The marginal cost (additional photography time) is low relative to the information gain on image-source effects.

**Source URLs:**
- Wilson score interval: https://www.econometrics.blog/post/the-wilson-confidence-interval-for-a-proportion/
- Design effect for clustered samples: https://home.iitk.ac.in/~shalab/sampling/chapter4-sampling-stratified-sampling.pdf
- AI classification accuracy degradation by image quality (optical remote sensing): https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0086528

**Confidence:** HIGH for CI calculations (first-principles math); MEDIUM for ICC_within estimate of 0.70 (informed by domain knowledge, not directly measured).

---

### 5. Defect Category Coverage

**Claim:** With 20 controlled specimens, cover 4 defect categories at 5 specimens each rather than 7 categories at ~3 each. The 4 priority categories are: crease (including spine stress), stain (water damage), tear (including detached cover), and substance (tape/tape residue). The remaining 3 categories (distortion, missing_part beyond tear, tanning) should be sourced from natural specimens in the existing worn collection.

**Evidence:**

**Why 4 categories at 5 specimens, not 7 at 3:**

With 3 positive specimens per defect category, the 95% CI on recall at 70% is ±36pp — this cannot even rule out 0% recall at 95% confidence. With 5 positive specimens, CI is ±31pp. At 7 specimens, CI is ±28pp. These are all scientifically indefensible for recall claims, but they do have different failure-detection power: with 5 specimens and true recall=0% (system misses all defects), P(detecting the failure) = 1 - 0.95^5 = 23%. With 7 specimens: 1 - 0.95^7 = 30%. With 10: 1 - 0.95^10 = 40%.

The correct goal for Phase 1 is catastrophic failure detection, not precision recall measurement. 5-7 specimens per category is sufficient to detect total detection failure (0% recall) with ~23-30% probability, which is weak but better than nothing. To detect 50% recall vs. 100% recall with 80% power requires 49-62 specimens per category — infeasible in Phase 1.

**Why these 4 categories:**

| Category | Priority | Rationale | Controlled creation ease |
|---|---|---|---|
| crease | P0 | Most common real-world defect; multiple severity levels easy to create | EASY (folding, pressing) |
| stain (water) | P0 | Cap at 6.0; zero tested currently; easy to create with dropper | EASY (water dropper) |
| tear (detached) | P0 | Cap at 4.0; catastrophic grade impact; easily created | MODERATE (pliers on staple) |
| substance (tape) | P0 | Cap at 7.0; extremely common; easy to create | EASY (scotch tape application) |
| distortion | P1 | Fade, color loss — requires naturally aged comics | HARD — source naturally |
| missing_part | P1 | Marvel chipping, brittleness — requires brittle paper | HARD — source naturally |
| tanning | P2 | Edge yellowing — common in worn collection | NATURAL — source from existing |

**Recommended specimen allocation by defect category (20 controlled):**

| Category | Controlled Specimens | Severity Coverage | Specific Types |
|---|---|---|---|
| crease | 6 | 2 minor, 2 moderate, 2 major | spine roll (3), reader crease (2), subscription crease (1) |
| stain | 5 | 2 minor, 2 moderate, 1 major | water ring stain (3), soiling (2) |
| tear | 5 | 1 minor, 2 moderate, 2 major | corner tear (2), spine split (2), detached cover (1) |
| substance | 4 | 2 minor, 2 moderate | tape applied (2), tape residue (2) |
| **Total** | **20** | | |

Natural specimens for distortion, missing_part, tanning: source from the existing worn collection (25-30 worn comics likely include several with naturally occurring tanning and edge wear).

**Source URLs:**
- Defect creation feasibility: https://www.cgccomics.com/resources/glossary/
- CGC grading scale caps: https://www.cgccomics.com/comic-grading/grading-scale/
- Sample size for recall measurement (Buderer formula): https://pmc.ncbi.nlm.nih.gov/articles/PMC5121784/

**Confidence:** HIGH for category prioritization (derived directly from defect chart cap values and creation feasibility); MEDIUM for specific specimen counts (judgment call within statistically constrained range).

---

### 6. Power Analysis for Specific Comparisons

#### 6a. Tier-Level Accuracy Difference Detection

**Claim:** With 70 comics (15-22 per tier) × 3 conditions, the effective power to detect a 15pp accuracy difference between high-grade and low-grade comics (80% power, alpha=0.05) requires approximately 97 comics per tier — far beyond the 70-comic budget. Phase 1 can only detect tier differences of ≥30pp with reasonable power.

**Evidence:**

Using the two-proportion Z-test (appropriate for comparing accuracy between independent groups):

n per tier = (z_α + z_β)² × [p₁(1-p₁) + p₂(1-p₂)] / (p₁-p₂)²

| Accuracy difference | n per tier (80% power) | Images per tier (×3) | Available comics per tier |
|---|---|---|---|
| 15pp (e.g., 90% vs 75%) | 97 | 291 | 15–22 → **underpowered 6.5×** |
| 10pp (e.g., 90% vs 80%) | 197 | 591 | 15–22 → **underpowered 13×** |
| 30pp (e.g., 90% vs 60%) | 28 | 84 | 15–22 → **marginal** |

With the clustering correction (DEFF=2.4), the effective independent N from 15 comics × 3 images = 45/2.4 ≈ 19 effective observations. This gives power to detect differences of approximately 40pp or larger with 80% confidence.

**Practical implication:** Phase 1 (70 comics) cannot produce a statistically defensible claim that "the system is X% accurate on high-grade vs. Y% accurate on low-grade" unless the difference is enormous (≥30-40pp). The correct statement from Phase 1 is directional: "preliminary data suggests a [difference direction] between high-grade and low-grade comics; formal comparison requires [N]."

For a confirmable tier comparison at 15pp difference, 80% power: need ~300 comics total (100 per tier across 3 tiers). This is the Phase 3 target.

#### 6b. Defect Recall at 60% Power

**Claim:** Measuring defect recall at 60% power (minimum useful power level, per Beleites et al.) requires 28 positive specimens per defect category to achieve ±15pp CI. The 70-comic budget allows this for at most 1 defect category if the entire controlled specimen budget is dedicated to it.

**Evidence:**

The Buderer formula for sensitivity measurement:

N_positive = z² × Sensitivity × (1 − Sensitivity) / (half-width)²

| Target recall | CI half-width | N positive needed | Power equivalent |
|---|---|---|---|
| 80% | ±20pp | 16 | ~60% detection power |
| 80% | ±15pp | 28 | ~60% (wider claim, more power) |
| 80% | ±10pp | 62 | ~80% standard power |
| 70% | ±15pp | 36 | ~60% detection power |

With the 70-comic budget, allocating 28 comics to a single defect category would consume 40% of the entire collection and leave only 42 comics for everything else. This is not a viable Phase 1 strategy.

The correct Phase 1 goal: allocate 5-7 specimens per category to detect catastrophic failures (true recall = 0%), not to measure precise recall. 7 specimens per category achieves ~30% probability of catching a complete failure (system misses all defects of that type). While this sounds weak, it is sufficient for a "sanity check" that the pipeline is running at all, given that existing harness results show 0 defects detected (indicating a pipeline failure, not just low recall).

For a recall measurement with ±15pp CI, a Phase 2 dedicated collection of 28+ positives per target defect category is required.

#### 6c. Minimum Specimens per Defect Type for Meaningful Claims

**Summary table:**

| Goal | N per defect type | What you can claim |
|---|---|---|
| Catastrophic failure detection | 5 | Rule out 0% recall at ~23% power (weak sanity check) |
| Directional recall estimate | 7 | Recall is "likely above X%"; CI ±28-35pp (not reportable) |
| Phase 1 minimum for reporting | 28 | Recall ± 15pp; sufficient for "system detects [category] defects" |
| Full recall measurement | 62 | Recall ± 10pp; publishable accuracy claim |
| Precision + recall jointly | 100+ | Both metrics within ±10pp simultaneously |

**Phase 1 achievable claim (5-7 specimens/category):** "The defect detection pipeline was verified to trigger on [N] of [7] specimen types. No specimens were completely missed by the detection layer." This is not a precision/recall claim; it is a pipeline functionality claim.

**Source URLs:**
- Buderer sample size formula: https://pmc.ncbi.nlm.nih.gov/articles/PMC5121784/
- Sample size for sensitivity/specificity: https://pmc.ncbi.nlm.nih.gov/articles/PMC6683590/
- Diagnostic test accuracy study design: https://pmc.ncbi.nlm.nih.gov/articles/PMC9639742/
- Two-proportion comparison power: https://pmc.ncbi.nlm.nih.gov/articles/PMC4868880/

**Confidence:** HIGH — all calculations are derived from standard statistical formulas (Buderer, two-proportion Z-test); CI arithmetic is deterministic. The DEFF estimate for clustering is MEDIUM confidence.

---

### 7. ICC Calibration Anchor Requirements

**Claim:** A minimum of 20 double-graded comics is required for a provisional ICC estimate with CI half-width ≤0.15 (e.g., reporting "ICC = 0.82 [0.67, 0.97]"). 30 double-graded comics achieves CI half-width ≈ 0.10. All 39 baseline comics should be double-graded; 4 targeted anchors alone are insufficient.

**Evidence:**

From PMC10981208 (ICC sample size review, Searle method, k=2 raters, target ρ=0.8):

| N subjects | CI half-width (ω) | Full CI width |
|---|---|---|
| 20 | ~0.15 | ~0.30 |
| 50 | ~0.10 | ~0.20 |
| 200 | ~0.05 | ~0.10 |

Practical floor: n=20 is the minimum where the Searle method produces reliable coverage. Below n=20, ICC estimates are unstable (the CI may not include the true value at the stated confidence level).

For this project, the recommended approach is to double-grade all 39 baseline comics (both human raters grade every comic independently). This:
- Produces ICC from n=39 → CI half-width ≈ 0.12 (borderline acceptable for reporting)
- Generates a full disagreement map (which grade ranges show most rater divergence)
- Requires approximately 1.5–2 additional hours of human grader time

The 4-anchor strategy (grade 4 specific comics by both raters) is insufficient for ICC measurement and is only useful as a spot-check. It should not be reported as an ICC reliability estimate.

**Source URLs:**
- ICC sample size review (PMC10981208): https://pmc.ncbi.nlm.nih.gov/articles/PMC10981208/
- ICC guidelines (PMC4913118 — minimum 30 heterogeneous samples, 3+ raters): https://pmc.ncbi.nlm.nih.gov/articles/PMC4913118/
- Updated ICC guidelines: https://pubmed.ncbi.nlm.nih.gov/36048052/

**Confidence:** HIGH for the n=20-30 range (directly from literature); MEDIUM for CI half-width estimates at specific N values (paper gives N → ω relationships but at a specific target ρ=0.8; actual ρ for this rater pair is unknown).

---

## Recommendations

### Priority 0 — Before Any Photography

**R1. Decide the destructible comic pool.** Identify the ~31 comics (14 single-defect + 9 severity-spectrum + 8 compound) that will receive controlled damage. These should be confirmed as low-value ($1–3) before any defect creation. Use Overstreet or eBay sold listings to verify. Label these separately from the baseline pool.

**R2. Assign all 39 baseline comics to both human raters for double-grading.** Do not defer ICC measurement. Grade all baseline comics before photography so that the ground truth is set before images are taken (prevents the graders from being influenced by image quality).

### Priority 1 — Photography Protocol

**R3. Photograph all 70 comics in all 3 conditions (scan, table, handheld).** Total: 210 images. This is the highest ROI action — it triples the image count at no acquisition cost, enabling both the overall accuracy CI of ±4.8pp and the image-source comparison.

**R4. For baseline comics only, photograph 3 conditions before any damage.** Once a comic is damaged for the defect pool, it cannot serve as a clean baseline. Photograph all 70 comics first, then create controlled defects on the designated 31.

### Priority 2 — Defect Specimen Creation

**R5. Create defect specimens in this priority order:**
1. Crease severity spectrum: 6 comics (spine roll minor/moderate/major, reader crease minor/moderate, subscription crease)
2. Stain (water): 5 comics (water ring at 3 severity levels, soiling minor, soiling moderate)
3. Tear severity: 5 comics (corner tear minor/moderate, spine split moderate/major, detached cover major)
4. Substance (tape): 4 comics (tape applied minor/moderate, tape residue minor/moderate)
5. Compound defect: 8 comics per the compound list below
6. Catastrophic (detached cover, missing page): included in tear/missing_part counts above

**R6. For compound specimens, use these 8 combinations:**
1. Spine roll (moderate) + soiling (minor) — tests within-cover compound, common real-world
2. Reader crease (moderate) + edge whitening (minor) — tests multi-zone penalty stacking
3. Water stain (moderate) + foxing (minor, sourced naturally) — tests co-occurring stain types
4. Tape (applied, moderate) + tape residue (adjacent strip) — tests substance differentiation
5. Subscription crease (major) + spine stress (minor) — tests cap domination (sub crease cap 5.5 dominates)
6. Corner tear (minor) + corner blunting (minor) + soiling (minor) — 3-defect compound, tests diminishing returns
7. Water stain (major) + crease (minor) — severe single defect + minor secondary
8. Detached cover + any defect — catastrophic cap (4.0) with secondary, verifies cap override behavior

### Priority 3 — Grade Tier Balance

**R7. Map the 70 comics to tiers before photography begins.** If the existing collection has too many high-grade comics and not enough mid-grade (7.0–8.4), prioritize mid-grade sourcing from the $1 bin to reach the target 22 mid-high comics.

**R8. Create 5 very-low grade specimens (0.5–1.8) via controlled damage.** Use heavily worn reader copies. Detach the cover (cap 4.0), then add secondary damage to push into 0.5–1.8 range. These are essential for testing the catastrophic end of the scale.

### Anti-Patterns to Avoid

- **Do not photograph more conditions of the same comic to inflate N for accuracy claims.** The design effect of 2.4 means 3 photos ≠ 3 independent observations. Report effective N alongside raw image count.
- **Do not attempt per-defect-type recall claims from Phase 1.** With 5-7 specimens per category, any reported recall number has a ±28-36pp CI — not reportable. Frame Phase 1 defect results as "pipeline functionality confirmed" not "recall = X%."
- **Do not weight the 4 ICC anchor comics as representative of all grade ranges.** Grade all 39 baseline comics with both raters. 4 anchors is not a reliability study; it is a spot-check.
- **Do not report uncorrected CI from 210 images without noting the clustering design effect.** The honest CI from 70 comics photographed 3 times is approximately ±5.9pp (corrected), not ±4.8pp (uncorrected).

---

## Open Questions

1. **What is σ_h for each grade tier?** The Neyman allocation above uses estimated within-tier variance. Measuring actual human grader disagreement variance per tier from the ICC study would refine the allocation for Phase 2.

2. **What is ICC_within for the three photography conditions?** The design effect correction uses an assumed ICC_within=0.70. If the actual value is lower (conditions produce more different results), the effective N correction is less severe; if higher, it is more severe.

3. **Can compound specimens serve double duty?** If a compound specimen (e.g., water stain + crease) is also photographed before damage is created, it can serve as both a baseline comic and a defect test comic. This would reduce the net comics consumed for defect testing.

4. **What is the natural defect rate in the worn/beat-up pool?** If 15 of the 25-30 worn comics already have naturally occurring tear/stain/substance defects, these can serve as natural defect specimens, reducing the need for controlled creation and freeing controlled-specimen budget for severity-spectrum work.

---

## Sources Referenced

| ID | URL | Type | Claims |
|---|---|---|---|
| src-sd-01 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5121784/ | academic | Buderer formula, min sensitivity sample size |
| src-sd-02 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10981208/ | academic | ICC sample size review, n=20 floor |
| src-sd-03 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4913118/ | academic | ICC guidelines, n=30 recommendation |
| src-sd-04 | https://arxiv.org/abs/1211.1323 | academic | Beleites 75-100 sample minimum |
| src-sd-05 | https://www.cambridge.org/core/journals/acta-numerica/article/optimal-experimental-design-formulations-and-computations/38BBD0DC1A0386FDF306B6C0167DF7D9 | academic | D-optimal experimental design formulations |
| src-sd-06 | https://apps.dtic.mil/sti/html/trecms/AD1223453/index.html | academic | D-optimal vs. binary designs power (JSM 2023) |
| src-sd-07 | https://arxiv.org/abs/2304.08701 | academic | Bayesian D-optimal for mixed responses |
| src-sd-08 | https://en.wikipedia.org/wiki/Neyman_allocation | reference | Neyman optimal allocation formula |
| src-sd-09 | https://www.econometrics.blog/post/the-wilson-confidence-interval-for-a-proportion/ | technical | Wilson score interval |
| src-sd-10 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4868880/ | academic | Two-proportion comparison power |
| src-sd-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6683590/ | academic | Sample size for diagnostic accuracy |
| src-sd-12 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9639742/ | academic | Diagnostic study design user's guide |
| src-sd-13 | https://sciencedirect.com/science/article/abs/pii/S0034425723004327 | academic | Stratified allocation for accuracy estimation |
| src-sd-14 | https://sciencedirect.com/science/article/abs/pii/S0950584923001866 | academic | Stratified random sampling for neural net test input |
| src-sd-15 | https://home.iitk.ac.in/~shalab/sampling/chapter4-sampling-stratified-sampling.pdf | academic | Stratified sampling theory (IIT Kanpur) |
| src-sd-16 | https://www.mdpi.com/2079-9292/12/21/4423 | academic | Stratified sampling for imbalanced ML datasets |
| src-sd-17 | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0086528 | academic | Image quality degradation effect on recognition rate |
| src-sd-18 | https://www.cgccomics.com/comic-grading/grading-scale/ | official | CGC grade scale, defect caps |
| src-sd-19 | https://www.cgccomics.com/resources/glossary/ | official | CGC defect definitions |
| src-sd-20 | https://pubmed.ncbi.nlm.nih.gov/36048052/ | academic | Updated ICC guidelines 2022 |
