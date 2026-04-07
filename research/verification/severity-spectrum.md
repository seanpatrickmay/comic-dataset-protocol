# Verification: Severity Spectrum Research
**Axis**: Defect Severity Calibration  
**Date**: 2026-04-07  
**Verifier**: fact-checker agent

---

## Verdict: PASS with one cross-file discrepancy and one ambiguity in crease tier boundaries

Severity spectrum measurements are grounded in Overstreet grade-anchored criteria. The major finding is a tear minor threshold discrepancy with defect-creation.md, and a crease boundary description that could be misread. The mm-level thresholds (e.g., <1mm for minor crease width, 1–3mm for blunted corner) are clearly labeled as inferred from grade language, not directly published by CGC — this is an appropriate epistemic caveat.

---

## CGC/Overstreet Threshold Claims

### Crease minor: "<0.5mm wide, <2" long, no color break" = grade 8.0–9.2

**Status: PARTIALLY VERIFIED — width threshold is an inference**

The ≤2" length threshold is consistent with the 8.0 VF Overstreet criterion ("1/4" crease acceptable if color is not broken" at grade 8.0, interpreted as the green/yellow boundary). However:

- The specific width threshold of "<0.5mm" is not from any published CGC or Overstreet source. It is an inferred measurement from the grade descriptions. The file correctly marks confidence as HIGH for grade-anchored thresholds and MEDIUM for the "exact minor/moderate boundary."
- The grade range "8.0–9.2" for minor creases is consistent with Overstreet but note: at 9.2–9.4, CGC allows only a 1/16" (1.6mm) bend with no color break — any crease (fiber break) at all would push below 9.2 in practice.

**Impact**: The width threshold is used to guide physical specimen creation, not grading. Minor inaccuracy acceptable.

### Crease "Key thresholds" box: "Crease ≤1/4" without color break = green (minor)"

**Status: POTENTIALLY MISLEADING**

The severity tier table immediately above says minor = "<0.5mm wide, <2" long." But the key thresholds box then says "≤1/4" without color break = green (minor)." The 1/4" = 6.4mm length threshold for "green" contradicts the <2" = ~50mm in the tier table.

Reading more carefully: "1/4" crease acceptable if not color-broken" is from the Overstreet 8.0 VF definition, which is the **boundary** grade for green tier. The ≤2" in the tier table is the green tier's maximum extent. These are measuring different things (one is a minimum for grade 8.0, the other is a ceiling on what qualifies as minor). However, the juxtaposition without explanation could cause confusion about whether minor creases must be ≤1/4" or ≤2".

**Correction needed**: The key thresholds box should be clarified. "≤1/4" without color break: acceptable at grade 8.0 (green/yellow boundary)" — this is not saying all minor creases must be ≤1/4". See corrections.md.

### Spine roll: "Roll width <1/4" = minor (grade 7.0–8.5)"

**Status: VERIFIED for grade range; width measurement is inference**

The CGC Crease Guide states "severity ranges from slight shifts to widths exceeding one inch, with torquing causing fanning along the top or bottom edge, usually not exceeding 1/4"." The file correctly extracts this. The grade range 7.0–8.5 for minor spine roll is consistent with community sources and CGC's description of spine roll at these grades.

### Blunted corner: "9.6 NM+: one corner may be almost imperceptibly blunted"

**Status: VERIFIED**

Directly from Overstreet Access grading definitions: "one corner may be almost imperceptibly blunted, but still almost sharp and cut square" at 9.6. Correctly quoted.

### Spine stress: "Stress lines >1" long are reclassified as creases"

**Status: VERIFIED**

The file cites the CGC Crease Guide for this rule. The rule that stress lines >1" become creases is stated directly in CGC documentation. Confidence correctly rated HIGH.

### Tear minor: "≤1/8" (3mm)"

**Status: VERIFIED for bindery tear context — DISCREPANCY with defect-creation.md**

Severity-spectrum.md: minor tear = ≤1/8" (3mm). Correctly sourced from the 9.8 allowable bindery tear threshold and 9.4 criterion.

Defect-creation.md: minor tear = "<1/4" = minor."

These are different numbers. The 1/8" threshold from severity-spectrum.md is correct for the high-grade context (9.0+). The 1/4" in defect-creation.md is more permissive and better represents general minor tear context at lower grades (FN/VF range). Both are defensible but the files should agree on which context each applies to. See corrections.md.

### Stain sizes: "Diameter ≤5mm = minor; 5–25mm = moderate; >25mm = major"

**Status: MEDIUM CONFIDENCE — community-derived, not CGC official**

CGC explicitly does not publish size thresholds for stains. The file correctly acknowledges this: "Note on CGC: No explicit mm thresholds published. The size/shade/severity language is qualitative. The above measurements are derived from grade-anchoring." The MEDIUM confidence rating is appropriate. The community threshold cited ("minor water stains generally acceptable up to Fine if nickel-sized or smaller") is consistent with the 5–10mm range (a nickel is ~21mm diameter — slightly larger than stated).

**Minor discrepancy**: A nickel is ~21mm diameter, which is in the "moderate" range (5–25mm) per the table. The community saying "nickel-sized or smaller" as acceptable at Fine grade would put it at the upper end of moderate, not within minor. This is not a protocol-breaking issue but should be noted.

---

## Cross-File Consistency

| Claim | severity-spectrum.md | defect-creation.md | Status |
|---|---|---|---|
| Subscription crease severity | "color-breaking top-to-bottom = major/red, grade 5.5 or lower" | "heavy (color-breaking): 4.0–5.5" | CONSISTENT |
| Stress line reclassification | ">1" long = crease" | ">1" long = crease" | CONSISTENT |
| Minor tear length | "≤1/8" (3mm)" | "<1/4" = minor" | DISCREPANCY (see above) |
| Corner minor threshold | "<1mm flat section" | Not specified numerically | NO CONTRADICTION |
| Spine roll minor | "roll width <1/4"" | Grade range 8.0–9.0 for light roll | CONSISTENT |
