# Verification: Defect Creation Protocol
**Axis**: Physical Defect Specimen Creation  
**Date**: 2026-04-07  
**Verifier**: fact-checker agent

---

## Verdict: PASS with one safety gap and one CGC definition flag

The defect-creation.md file correctly attributes CGC definitions to the CGC Grader Notes Guide. Physical creation techniques are plausible and consistent with paper conservation science. Two items require action.

---

## CGC Definitions: Verified

### 109 defects / 7 categories claim

**Status: VERIFIED**

Both grading-calibration.md and defect-creation.md cite 109 defects in 7 categories from the CGC Grader Notes Guide. The seven categories (crease, distortion, missing part, stain, substance, tanning, tear) match the structure of the published CGC Grader Notes Guide at cgcgrading.com. No issue.

### CGC crease sub-type definitions

**Status: VERIFIED (from official source)**

Definitions for bend, crunch, dent, finger bends, finger creases, indent, reader crease, spine roll, stress lines, subscription crease, and vein are correctly attributed to the CGC Grader Notes Guide (src-001 in defect-creation.md = cgcgrading.com/en-US/resources/comics-grader-notes-guide). Confidence HIGH.

### Tanning definition: "primarily affecting the cover due to oxidation, edges and spine most commonly affected"

**Status: VERIFIED**

The characterization of tanning as lignin oxidation primarily affecting edges and spine is consistent with paper aging science and the CGC Grader Notes Guide description. The grades cited (very light = 9.8 acceptable; moderate = 8.0–9.0; heavy = ~6.0; extreme = 4.0–5.0) are plausible community-consensus values but CGC does not publish precise numeric tables for tanning. Mark as MEDIUM confidence for specific grade numbers; HIGH for mechanism description.

---

## Physical Creation Techniques: Verified

### Subscription crease technique

**Status: PLAUSIBLE, correctly graded**

The fold-in-half technique for subscription crease is correct. The grade impact (light bend: 7.0–8.5; heavy color-break: 4.0–5.5) aligns with both Overstreet and severity-spectrum.md. No issue.

### Humidity method for warping/cockling (Section 3.2)

**Status: PLAUSIBLE — temperatures and RH ranges physically reasonable**

- "20–25°C, 70–80% RH for 4–6 hours" for light rippling: physically reasonable. Paper responds to humidity over these timescales.
- "85% RH, 8–12 hours" for moderate cockling: consistent with paper science literature.
- "Full saturation, 12–24 hours" for severe warping: achievable in sealed container.

No issues with physical plausibility.

### UV accelerated yellowing: "3 hours UV ≈ 6 months sunlight"

**Status: PLAUSIBLE but UNVERIFIED at this precision**

The document cites this ratio but provides no source. In the paper conservation literature, accelerated aging equivalences vary widely by paper type, lignin content, and UV wavelength. The claim "3 hours laboratory UV ≈ 6 months direct sunlight" is a rough order-of-magnitude estimate, not a precise equivalence. Using it as more than a rough guide would be inappropriate.

**Impact on protocol**: The practical protocol (check every 6 hours, stop at desired tanning level) is correct regardless of whether the equivalence ratio is precise. No protocol change needed, but the claim should be labeled as an approximation.

### Oven aging temperatures: "1929 Rasch standard: 72h at 100°C dry heat = 18–25 years"

**Status: MINOR CONFLATION — two different standards presented together**

The document lists:
- "1929 Rasch standard: 72 hours at 100°C dry heat = 18–25 years of natural aging"
- "Modern ISO 5630-3 / ASTM standard: 80°C at 65% RH"

These are two different accelerated aging protocols (dry heat vs. moisture-controlled). The Rasch standard is for acid hydrolysis degradation; ISO 5630-3 models oxidative + hydrolytic degradation. The document correctly notes the caveat "this applies to acid-hydrolysis degradation, not specifically UV-driven tanning" for the Rasch standard. The practical protocol (80°C, 65% RH, use a climate chamber) is correct per ISO 5630-3.

**Impact**: Low. The practical oven aging guidance is sound. However, "150°C where decomposition products can form" — this threshold is conservative. Paper begins significant chemical decomposition around 150–200°C. At 150°C there is some risk. The guidance to avoid >150°C is appropriate.

---

## SAFETY ISSUES

### FeSO₄ foxing simulation (Section 4, Option A)

**Status: SAFETY GAP — minor but actionable**

The document states: "Ferrous sulfate is a mild irritant. Use gloves, avoid ingestion. Not acutely hazardous at these concentrations."

**What is missing**: Eye protection. FeSO₄ solutions at even 0.01% can cause irritation if splashed into eyes. Aqueous solutions at 0.05% are not acutely hazardous but eye splash is the most realistic accident risk when working with droppers. The safety note should add "eye protection recommended" (safety glasses).

**Correction needed**: See corrections.md.

### Oven aging at 60–80°C

**Status: SAFE**

Standard kitchen ovens at their minimum setting (typically 65–70°C) pose no inhalation risk from paper heating. No toxic byproducts from cellulose/lignin at these temperatures. The protocol note to "avoid temperatures above 150°C" is correct.

---

## Cross-File Consistency: Defect Definitions

| Claim | defect-creation.md | severity-spectrum.md | Status |
|---|---|---|---|
| Subscription crease grade impact | 4.0–5.5 (heavy) | "lowers grade to 5.5 or lower if color-breaking" | CONSISTENT |
| Spine roll severity levels | Light=90°, Mod/severe=cover folded back | Minor=<1/4", Mod=1/4"–1", Major=>1" | CONSISTENT (different axes of measurement, compatible) |
| Stress lines CGC threshold | ">1" = reclassified as crease" | ">1" long reclassified as creases" | CONSISTENT |
| Dog ear / corner | "45° fold" for dog ear | "~45° compression" for blunting | CONSISTENT |
| Tear minor threshold | "<1/4" = minor" | "≤1/8" = minor (3mm)" | MINOR DISCREPANCY — see below |

### Tear minor threshold discrepancy

**defect-creation.md** states: "CGC grades tears primarily by total length: <1/4" = minor"  
**severity-spectrum.md** states: "Minor: Length ≤1/8" (3mm)"

These are inconsistent. Severity-spectrum.md cites Overstreet Access (bindery tear ≤1/8" at 9.8) as the basis for the ≤1/8" threshold. Defect-creation.md appears to use a different, more permissive definition for "minor." The Overstreet/CGC threshold for bindery tears specifically is 1/16"–1/8" at high grades; a general edge tear of up to 1/4" may still be minor at lower grade contexts.

**Conclusion**: The discrepancy is real but context-dependent. Both values are defensible at different grade contexts. Protocol should specify which grade range the threshold applies to: 1/8" threshold is correct for high grades (9.0+); up to 1/4" may be minor at FN range. See corrections.md.
