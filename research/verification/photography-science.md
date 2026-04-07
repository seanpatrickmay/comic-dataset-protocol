# Verification: Photography Science
**Axis**: Photography for Defect Detection  
**Date**: 2026-04-07  
**Verifier**: fact-checker agent

---

## Verdict: PASS with minor caveats

The photography-science.md file is well-sourced and internally consistent. The primary claims are supported by official conservation sources. Three minor issues are noted; none require protocol changes.

---

## Claim-by-Claim Results

### Claim 1.2 — Optimal raking angle 5–15° from surface plane

**Status: VERIFIED**

The AIC Conservation Wiki (src-002) explicitly states "typically between 5 and 15 degrees." This is correctly quoted. The practical floor of 10° for consumer LED panels is a reasonable engineering caveat, not a scientific claim. No issue.

### Claim 1.2 / 2.1 — "Photography Science" describes raking angle as from the **surface plane** (not from vertical)

**Status: CORRECT — and important to preserve**

The document correctly states "5–15° from the plane of the surface (i.e., 75–85° from vertical)." This is the correct conservation science convention. Confusion between "from surface" vs. "from vertical" would cause a 90° error in setup. The protocol should retain explicit parenthetical clarification. No correction needed; flag for training material.

### Claim 3.1 — iPhone main camera minimum focus distance ~25 cm

**Status: PLAUSIBLE, LOW CONFIDENCE SOURCE**

Source is an Apple Community forum thread (src-012), which is community-tier. The actual iPhone 16 Pro minimum focus distance for the main (1x, 24mm equivalent) lens is approximately 20–25 cm depending on model year. The claim "approximately 25 cm" is approximately correct. However, the ultra-wide macro minimum focus distance is closer to 2 cm for the 0.5x lens, not necessarily "as close as 2 cm" for a full-frame shot — at 2 cm the image circle is extremely narrow. This is a minor inaccuracy of no protocol consequence.

**Impact**: None. Use 25–35 cm working distance; the exact floor does not change the workflow.

### Claim 3.3 — "Deep Fusion cannot be disabled on iPhone 12+"

**Status: UNVERIFIED — potentially outdated**

Source is a 2019 Macworld article (src-016) about iPhone 11. By iPhone 14+, some settings shifted. The underlying recommendation (leave Deep Fusion active, use ProRAW if you want to bypass) is sound practice. The specific claim about disable-ability on current hardware should be treated as MEDIUM confidence.

**Impact**: None on protocol. The recommendation — leave defaults, use ProRAW for A/B testing — is unaffected.

### Claim 4.1 — Black background for defect photography

**Status: VERIFIED for topographic shots; MINOR CAVEAT for stain detection**

The claim is correct and well-sourced. The document itself acknowledges (Claim 4.2) that a gray background may be preferable for tanning/stain color detection — this self-caveat is appropriate and should be preserved in the protocol.

---

## Cross-File Consistency

Photography-science.md and severity-spectrum.md agree that raking light is required for stress lines, bends, and cockling. No contradiction found.

The 10–15° raking angle recommendation in photography-science.md is consistent with the creation technique guidance in severity-spectrum.md and defect-creation.md, which reference raking light visibility as the test for stress lines and minor bends.

---

## No Dangerous Claims Found

No hazardous procedures, chemical safety issues, or setup errors that could create false defects in ways that would invalidate the dataset.
