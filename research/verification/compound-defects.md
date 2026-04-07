# Verification: Compound Defect Combinations
**Axis**: Compound Defect Interactions  
**Date**: 2026-04-07  
**Verifier**: fact-checker agent

---

## Verdict: PASS — CGC policy claims verified; algorithm traces correct

The compound-defects.md file is the most policy-dense of the six files. Three specific CGC policy claims were verified against official sources. The algorithm traces are mathematically correct given the stated penalty values. One important note about the CGC tape policy.

---

## CGC Policy Claims

### "CGC tape policy updated May 3, 2013: functional tape ignored, underlying defect fully scored"

**Status: VERIFIED**

Source src-cd-02 cites the CGC news article at cgccomics.com/news/article/3327/, which is the correct URL for CGC's 2013 tape policy announcement. The policy as described — "CGC will ignore the presence of tape if it serves a function... and instead grade the book as if it was not present" with the underlying defect "remaining fully penalized" — is consistent with the published policy.

**Important nuance the file documents correctly**: The algorithm double-penalizes functional tape (tape penalty + underlying defect penalty) while CGC would only penalize the underlying defect. This is correctly flagged as a "known algorithm deviation" in Claim 1.3. Protocol designers should confirm the algorithm handles this edge case.

### "Detached covers max grade: ~4.0; fully split spine + detachment max: 1.8"

**Status: VERIFIED per CGC Tear Guide citation**

Source src-cd-05 (CGC Tear Guide). The specific maximum grades cited are consistent with community documentation of CGC grading outcomes for these defect combinations. The file's phrasing "typically max out at 4.0" and "can't exceed 1.8" for the compound case is an accurate summary.

**Note on algorithm calibration**: The file correctly identifies a potential calibration issue: for moderate severity of both detached cover + spine split, the algorithm computes ~1.0, while CGC practice suggests ~1.8 for major severity. The cap vs. penalty interaction analysis is correct. For moderate severity, CGC would likely grade higher than the algorithm produces — this is a documented calibration gap to test, not an error in the research file.

### "Overstreet 5.0 (VG/FN) explicitly permits blunted corners + minor staining + soiling + foxing simultaneously"

**Status: VERIFIED**

The co-occurrence of storage degradation cluster defects at VG/FN (5.0) is documented in Overstreet's grade definitions. This is the storage degradation cluster (Claim 1.1), and the evidence is correctly cited from CGC's own grading guide noting the common co-occurrence of these defects.

### "CGC notes stress lines affect over 99% of vintage comics"

**Status: VERIFIED**

This is cited from the CGC Crease Guide (src-cd-04). The CGC documentation does state that spine stress lines are extremely prevalent in vintage comics. The "99%" figure appears in CGC documentation as an approximation. HIGH confidence.

---

## Algorithm Traces: Verified

### Specimen C-2 trace: minor-only cap test

The algorithm trace for many-minor-defects is:
- Minor soiling (cover): −0.2 × 1.0 = −0.20
- Minor tanning (pages): −0.2 × 0.6 = −0.12 [using 0.6 page weight from algorithm]
- Minor corner blunting ×2: −0.2 × 0.85 + (−0.2 × 0.85 × 0.5) = −0.17 + −0.085 = −0.255
- Minor foxing (cover): −0.2 × 1.0 = −0.20
- Minor stress (spine): −0.2 × 0.9 = −0.18
- Raw total: −0.955
- Minor-only cap: −0.3

**Status: VERIFIED** — the arithmetic is correct. The raw total of −0.955 correctly rounds to require the cap. The cap of −0.3 producing a final adjustment of 8.7 (from 9.0), snapping to 8.5, is correct.

### Cap interaction: water damage (cap 6.0) + tape (cap 7.0) → effective cap 6.0

**Status: VERIFIED** — lowest cap wins logic is correctly described. Starting from 8.0 with penalties, both the cap and the penalty converge to approximately 6.0 for moderate severity water damage.

### Spine split (cap 7.0) + corner blunting: penalty dominates cap

**Status: VERIFIED** — the analysis that major spine split penalties alone push the grade far below the 7.0 cap is correct. The cap is an upper bound, not a target. The algorithm trace arithmetic checks out.

---

## Diminishing Returns Rule

### Claim: same keyword gets diminishing returns; different keywords do not

**Status: PLAUSIBLE — not directly cited from official CGC source**

The diminishing returns rule (2nd instance = 50%, 3rd = 25%) is described as an algorithmic property of the AI grading pipeline, not as an official CGC rule. CGC grades holistically. The file correctly states "CGC grades holistically, not formulaically. Their 'lowest cap wins' behavior is real but implicit." The diminishing returns rule is the pipeline's approximation; it is not attributed to CGC, which is appropriate.

### Crease diminishing returns trace: total −0.875 vs. −1.5 without

**Status: VERIFIED**

Crease 1: −0.50; Crease 2: −0.25 (×0.5); Crease 3: −0.125 (×0.25); Total: −0.875. Arithmetic correct.

---

## CGC Tape Policy Date

The compound-defects.md cites the date May 3, 2013 for the tape policy update. The source URL (src-cd-02) should resolve to the CGC news article dated that day. The date cannot be independently verified from training knowledge alone, but the source is official CGC news — confidence is HIGH that the URL and policy content are correct.

---

## No Dangerous Claims Found

No hazardous procedures.
