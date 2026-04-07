# Corrections Log
**Date**: 2026-04-07  
**Verifier**: fact-checker agent

All corrections below represent claims verified to be wrong or materially imprecise. Only claims that would change a protocol decision or a reportable number are listed here. Minor citation style issues and low-stakes approximations are documented in per-axis verification files only.

---

## CORRECTION 1 — MATERIAL
**File**: `statistical-design.md`, Section 4 (Three-Condition Photography Multiplier)  
**Location**: "Practical scenarios for partial 3-condition application" table; and narrative claim "true effective CI of ±8.3pp / √(210/87) ≈ ±5.9pp"

**Original claim**: "70 comics × 3 conditions = 210 images → corrected effective CI ≈ ±5.9pp"

**Corrected claim**: The DEFF-corrected CI for 210 clustered images (DEFF=2.4, eff_n=87.5) is **±7.5pp**, not ±5.9pp.

**Method**: Wilson CI applied to effective_n = 210/2.4 = 87.5 → ±7.5pp. The paper's formula (±8.3pp / √(210/87)) is not a standard clustering correction method and does not reproduce any correct value.

**Corrected table** (replacing the "Practical scenarios" table in Section 4):

| Scenario | Raw images | Effective N (DEFF=2.4) | Corrected CI |
|---|---|---|---|
| All 70 × 3 = 210 | 210 | 87.5 | **±7.5pp** |
| 50 × 3 + 20 × 1 = 170 | 170 | 82.5 | **±7.7pp** |
| 35 × 3 + 35 × 1 = 140 | 140 | 78.8 | **±7.9pp** |

**Impact on conclusions**: The 3-condition protocol still improves over single-condition (±8.3pp), but the improvement is ±7.5pp vs. ±8.3pp — a 0.8pp gain. The stated gain of 2.4pp (from ±8.3pp down to ±5.9pp) is approximately 3× too optimistic. The recommendation to photograph all 70 comics in 3 conditions is still valid, but Phase 1 results should be described as approximately ±7.5pp effective CI, not ±5.9pp.

---

## CORRECTION 2 — MINOR SAFETY GAP
**File**: `defect-creation.md`, Section 4 (Stain Defects), Foxing Simulation Option A

**Original claim**: "Safety note (Option A): Ferrous sulfate is a mild irritant. Use gloves, avoid ingestion. Not acutely hazardous at these concentrations."

**Corrected/supplemented claim**: Add eye protection. FeSO₄ aqueous solution at these concentrations (0.01–0.05%) is an eye irritant. The most realistic accident during dropper application is a splash to the eyes, not ingestion.

**Corrected text**: "Safety note (Option A): Ferrous sulfate is a mild irritant. Wear gloves and safety glasses when handling. Avoid ingestion. Not acutely hazardous at these concentrations but can cause eye irritation on splash."

**Impact**: Low probability but non-zero risk. Straightforward to correct.

---

## CORRECTION 3 — MODERATE (Cross-File Discrepancy)
**Files**: `severity-spectrum.md` (Section 2.4) vs. `defect-creation.md` (Section 5)

**Discrepancy**: Both files define the minor/moderate boundary for tears, but use different numbers:
- **severity-spectrum.md**: Minor tear = ≤1/8" (3mm)
- **defect-creation.md**: Minor tear = <1/4" (6mm)

**Analysis**: Both are defensible but apply to different grade contexts:
- 1/8" is the correct threshold for high-grade context (9.0+), where bindery tear allowances of ≤1/8" are the standard.
- 1/4" is more appropriate in mid-grade (FN/VF, 6.0–8.0) context where larger minor tears are tolerated.

**Recommended resolution**: Severity-spectrum.md should be the authoritative source for severity tier thresholds used in specimen creation. Add a note to defect-creation.md:

"CGC grades tears primarily by total length. For specimens targeting grade 9.0+ range: minor = ≤1/8" (3mm). For specimens targeting FN/VF range (6.0–8.0): minor may extend to 1/4" (6mm). Tier definitions in severity-spectrum.md use the high-grade threshold (≤1/8")."

**Impact**: Affects which tear specimens get labeled "minor" in the dataset. Without this clarification, a specimen created per defect-creation.md guidance (up to 1/4") might be labeled minor but actually photograph as moderate per severity-spectrum.md criteria.

---

## CORRECTION 4 — CLARIFICATION (Potential Misread)
**File**: `severity-spectrum.md`, Section 2.1 (Crease Key Thresholds box)

**Issue**: The key thresholds box states "Crease ≤1/4" without color break = green (minor)" but this is the Overstreet 8.0 VF boundary criterion, not a universal ceiling on "minor" crease length. The tier table above it says minor = ≤2" long.

**Risk**: A reader of the key thresholds box might conclude all minor creases must be ≤1/4". The 1/4" figure is the borderline criterion that determines whether a crease is acceptable at grade 8.0 — not a universal minor/moderate boundary.

**Recommended addition to key thresholds box**: "Note: ≤1/4" is the Overstreet 8.0 VF boundary criterion (minimum for green tier classification at grade 8.0). Minor creases can extend up to 2" without color break and still be green tier at grades below 8.0."

---

## Claims Verified Correct (Decision-Level Summary)

| Claim | File | Verdict |
|---|---|---|
| Wilson CI ±4.8pp at n=210, p=0.85 | statistical-design.md | CORRECT |
| Wilson CI ±8.3pp at n=70, p=0.85 | statistical-design.md | CORRECT |
| Per-tier CI table (all 5 rows) | statistical-design.md | CORRECT |
| Buderer N=28 for S=0.80, w=±15pp | statistical-design.md | CORRECT |
| Two-prop power n=97 for 15pp difference | statistical-design.md | CORRECT |
| Conservation raking angle 5–15° from surface | photography-science.md | CORRECT |
| Overstreet 9.4 NM: 1/16" bend limit | grading-calibration.md, severity-spectrum.md | CORRECT |
| Overstreet 9.0 VF/NM: 1/8" bend limit | grading-calibration.md, severity-spectrum.md | CORRECT |
| Stress lines >1" reclassified as creases | severity-spectrum.md, defect-creation.md | CORRECT |
| Tape policy 2013: functional tape ignored | compound-defects.md | CORRECT |
| Detached cover cap: 4.0; + spine split cap: 1.8 | compound-defects.md | CORRECT |
| Minor-only cap trace (−0.955 raw → capped at −0.3) | compound-defects.md | CORRECT |
| Koo & Mae 2016 ICC thresholds (0.75/0.90) | grading-calibration.md | CORRECT |
| ICC(3,1) model selection for fixed raters | grading-calibration.md | CORRECT |
| FeSO₄ at 0.01–0.05%: mild irritant, not acutely hazardous | defect-creation.md | CORRECT (incomplete — add eye protection) |
| Oven aging: 80°C, 65% RH (ISO 5630-3) | defect-creation.md | CORRECT |
| CGC 109 defects / 7 categories | defect-creation.md, grading-calibration.md | CORRECT |
| CGC process: 3 graders, head grader prevails | grading-calibration.md | CORRECT |
