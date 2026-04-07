# Research: Compound Defect Combinations for AI Grading System Testing

**Axis:** Compound Defect Interactions
**Date:** 2026-04-07
**Researcher:** compound-defects-agent
**Sources consulted:** 12 live-fetched sources (CGC official, Overstreet, Heritage Auctions, Mile High Comics, community forums)

---

## Executive Summary

Compound defect testing is the highest-value unsolved evaluation problem for the AI grading pipeline. Single-defect specimens verify that individual penalty values are approximately correct. Compound specimens verify that the algorithm's *interactions* — cap selection, diminishing returns, area weighting, the minor-only cap — behave correctly. These interactions are where the AI is most likely to err, because they require the model to correctly identify multiple defects *and* correctly reason about their combined effect.

Key findings:
1. CGC grades holistically, not formulaically. Their "lowest cap wins" behavior is real but implicit. The algorithm's explicit cap selection is a reasonable approximation, but the compound effect of penalties sometimes dominates the cap — a distinction CGC graders make intuitively that the AI must learn explicitly.
2. The four real-world compound patterns that dominate CGC submissions are: storage degradation clusters (soiling + tanning + corner wear), mechanical reading wear clusters (spine roll + stress + reader crease), water damage + owner repair attempts (water damage + tape), and structural failure clusters (spine split + detached cover or loose staple).
3. Six specific compound specimens are prioritized below. They are ranked by: (a) likelihood the AI grades wrong, (b) algorithmic properties tested, (c) feasibility of controlled creation.

---

## Section 1: Real-World Compound Defect Patterns

### Claim 1.1: Storage Degradation Cluster is the Most Common Real-World Compound Pattern

**Claim:** Comics stored without bags in contact with other comics develop a characteristic cluster: soiling on the cover surface, tanning/yellowing of pages, and blunted corners from stacking pressure — all at similar severity levels.

**Evidence:**
- CGC's own grading guide notes that "the most common type of soiling develops from comic books stored back-to-back with no bag or protection, a common practice in the early days of fandom." This mechanism also causes tanning (exposure to adjacent comic acidity) and corner wear (stacking weight).
- The Overstreet grading standard describes a grade 5.0 (VG/FN) as explicitly permitting "blunted corners... minor staining, soiling, discoloration, and/or foxing" simultaneously — these were written together because they commonly co-occur.
- CGC's grading guide states tanning "involves the darkening of comic paper through exposure to the elements" with moderate tanning lowering grades to 8.0–9.0 and heavy tanning to 6.0 or lower.

**Algorithm implications:**
- Soiling (substance, -0.2/-0.5/-1.5, cap 9.0) + tanning (-0.2/-0.5/-1.5, cap 9.0) + corner blunting (missing_part, -0.2/-0.5/-1.5, cap 9.0) on covers and corners: all three caps are identical at 9.0, so the effective cap is 9.0 regardless of how many are present. The distinguishing factor is total penalty, not cap selection.
- Three moderate defects: total penalty = (-0.5 × 1.0 cover) + (-0.5 × 0.9 tanning via pages) + (-0.5 × 0.85 corners) = roughly -1.5 to -1.8 points total. Starting from 9.0 model grade, adjusted result ~ 7.0–7.5. This aligns with CGC practice.
- **AI failure mode:** The AI may correctly identify all three defects but apply the diminishing returns rule incorrectly. Soiling, tanning, and corner blunting are *different* keywords — each gets full penalty on its first instance. Diminishing returns only applies if the *same* keyword appears multiple times (e.g., two separate soiling instances). The AI may wrongly apply diminishing returns across different defect types.

**Confidence:** HIGH (3+ concordant sources, durable fact about physical mechanism)

---

### Claim 1.2: Spine Roll + Spine Stress is the Canonical Mechanical Reading Wear Combination

**Claim:** Spine roll and stress lines nearly always co-occur in read copies because they share the same physical mechanism. CGC's grading standards explicitly describe them together at multiple grade levels.

**Evidence:**
- CGC's Crease guide states: "Spine rolls occur when the cover and pages curl around the back of the book during reading, causing torque and fanning along the left edge of the back cover. They frequently result in staple tears and spine splits." The same bending motion that creates spine roll generates stress lines at the bend points.
- Overstreet defines a 7.0 (FN/VF) as having "the slightest spine roll... as well as a possible moderate color break, and slight staple tears and a small accumulation of light stress lines." This is written as a *single grade definition*, confirming they are expected to co-occur.
- The Overstreet 6.0 (FN) grade explicitly permits "a minor spine roll" *and* "a few slight stress lines" simultaneously.
- CGC notes that stress lines "affect over 99% of vintage comics" and that most grade between 8.0–9.4.

**Algorithm implications:**
- Spine roll (crease, -0.3/-0.7/-2.0, cap 8.0) + stress lines (crease, -0.2/-0.5/-1.5, cap 9.0): different keywords, different areas (spine), no diminishing returns between them.
- Both are spine defects: area weight 0.9 for both.
- Minor spine roll + minor stress (multiple): penalty = (-0.3 × 0.9) + (-0.2 × 0.9 × 3 instances with diminishing returns) = -0.27 + (-0.18 + -0.09 + -0.045) = -0.585. With minor-only cap at -0.3, total penalty is capped at -0.3.
- **Critical test:** If all defects are minor, the minor-only cap (-0.3) should trigger. Starting from a 9.0 model grade: 9.0 - 0.3 = 8.7, snapped to 8.5. Without the cap it would go to ~8.5 anyway from penalties. The cap only matters when there are many minor defects accumulating past -0.3.
- **AI failure mode:** The AI may detect spine roll as moderate (it's visible) but stress lines as minor, mixing severities. This kills the minor-only cap. The expected grade drops more steeply than CGC would give for a lightly read copy.

**Confidence:** HIGH (multiple concordant official sources)

---

### Claim 1.3: Water Damage + Tape Repair is a Known Real-World Attempt at Masking

**Claim:** Owners who found water-damaged comics often applied tape to "fix" buckled corners, reinforce spine splits, or hold detached covers, creating a compound where both the original damage and an added substance defect exist.

**Evidence:**
- CGC's tape policy (updated May 3, 2013) explicitly distinguishes functional tape from decorative tape: "CGC will ignore the presence of tape if it serves a function (such as fixing a tear or spine split) and instead grade the book as if it was not present." However, the *underlying defect being hidden remains fully penalized*.
- The Substance guide confirms: "Tape reattachment on comic books... in grading, these repairs are considered as if the part is still detached, impacting the overall grade — for instance, a detached centerfold may receive a 7.0 grade by itself, but if reattached with tape, the grade may lower further to 6.0 or 6.5."
- The Stain guide confirms water damage "grades ranging from 0.5 to 9.0" depending on severity.
- The compound of water damage (stain, -0.5/-1.5/-3.5, cap 6.0) + tape (substance, -0.5/-1.0/-3.0, cap 7.0) creates a situation where two different caps apply: 6.0 and 7.0. The *lowest cap wins* — the final grade cannot exceed 6.0.

**Algorithm implications:**
- Water damage cap = 6.0; tape cap = 7.0. Effective cap = 6.0. This is the canonical "lowest cap wins" test case.
- Moderate water damage (-1.5 × 1.0 cover weight) + minor tape (-0.5 × 1.0 cover weight) starting from an 8.0 model grade: adjusted = 8.0 - 1.5 - 0.5 = 6.0. With cap also at 6.0, both mechanisms agree. The test is whether the AI correctly applies the 6.0 cap rather than 7.0.
- **AI failure mode 1:** The AI sees the tape and correctly detects it, but uses the tape cap (7.0) instead of the water damage cap (6.0). Final grade = 7.0 instead of 6.0 — one full grade point too high.
- **AI failure mode 2:** Per CGC's 2013 policy, if the tape is *functional* (covering the water-damaged area), CGC would grade as if the tape is not present. The AI cannot know the CGC policy and may penalize the tape separately. This creates a situation where the AI double-penalizes (tape penalty + water damage penalty) when CGC would only penalize the water damage.

**Confidence:** HIGH (direct CGC policy statement, live-verified 2026-04-07)

---

### Claim 1.4: Structural Failure Cluster (Spine Split + Detached Cover) Represents Extreme Compound Damage

**Claim:** Fully split spines often result in covers beginning to detach, as the binding integrity fails. CGC explicitly grades this combination to a maximum of 1.8.

**Evidence:**
- CGC's Tear guide states: "Grades for detached covers typically max out at 4.0... while fully split spines alongside detachment can't exceed 1.8."
- The Crease guide notes that spine rolls "frequently result in staple tears and spine splits" — showing how progressive mechanical damage creates compound structural defects.
- The algorithm has: detached cover (tear, -1.5/-2.5/-5.0, cap 4.0) + spine split (tear, -0.5/-1.0/-3.0, cap 7.0). Lowest cap = 4.0.

**Algorithm implications:**
- With both moderate: penalty = (-2.5 × 0.9 spine) + (-2.5 × 1.0 cover) = -2.25 + -2.5 = -4.75. Starting from 6.0 model grade: 6.0 - 4.75 = 1.25, snapped to 1.0. Cap at 4.0 would give 4.0. The *penalty* dominates over the cap here — result is 1.0, not 4.0.
- **Critical algorithmic property:** This tests whether the AI correctly handles the case where accumulated penalties push the grade *below* the cap. The cap is an *upper bound*, not a target grade.
- CGC's documented maximum of 1.8 for fully split spine + detachment corresponds to major severity for both defects. The algorithm's result of ~1.0 for moderate severity is more aggressive than CGC would be. This may be a calibration issue.

**Confidence:** HIGH (direct CGC statement on maximum grade for this compound)

---

## Section 2: Algorithm-Testing Combinations

### Claim 2.1: Different-Cap Combinations — Cap Selection Logic

**Claim:** The most direct test of cap selection is two defects with substantially different caps where the lower cap is the non-obvious one.

**Best test case:** Water damage (cap 6.0) + corner blunting (cap 9.0)

**Expected behavior:**
- Water damage cap = 6.0, corner blunting cap = 9.0. Effective cap = 6.0.
- Starting grade 8.0: penalties bring it down, then cap at 6.0 applies.
- **AI failure mode:** AI correctly detects both but assigns the final grade based on the corner blunting cap (9.0), resulting in a grade of ~7.0-7.5 instead of capped at 6.0.
- **Why this is a good test:** Corner blunting is visually prominent and the AI may anchor on it. Water damage may look less severe but carries a structurally lower cap.

**Second test case:** Tape (cap 7.0) + spine split (cap 7.0)

**Expected behavior:**
- Both caps are 7.0. Under current CGC policy, if tape is functional (repairing the spine split), CGC grades the split as-is and ignores the tape. The algorithm does NOT implement this policy — it will double-penalize. This is a known algorithm limitation worth documenting as an expected failure.

**Confidence:** MEDIUM (algorithm behavior is calculable; AI behavior is predicted based on observed patterns, not tested)

---

### Claim 2.2: Same Defect Type in Multiple Locations — Diminishing Returns

**Claim:** The diminishing returns rule (2nd instance = 50%, 3rd+ = 25%) is tested by creating the *same defect keyword* in multiple locations on one comic.

**Best test case:** Three separate creases (same keyword, different zones)

**Algorithm trace:**
- Crease 1 (moderate, cover): -0.5 × 1.0 × 1.0 = -0.50
- Crease 2 (moderate, cover): -0.5 × 1.0 × 0.5 = -0.25
- Crease 3 (moderate, cover): -0.5 × 1.0 × 0.25 = -0.125
- Total: -0.875

**Without diminishing returns:** -0.5 × 3 = -1.5

**The gap:** 0.625 grade points. On a 9.0 starting grade, the difference is between 8.0 (with diminishing returns) and 7.5 (without). This is a full CGC grade step.

**AI failure mode:** The AI reports three "crease" defects, but the grading algorithm's keyword-matching deduplication may not recognize them as the same type if described differently ("diagonal fold," "cover crease," "crease along bottom"). The diminishing returns rule depends on exact keyword matching, which depends on the description matching the defect chart keyword.

**Confidence:** MEDIUM (algorithm behavior calculable; AI description variability is the unknown)

---

### Claim 2.3: Minor-Only Cap Test — Many Small Defects

**Claim:** The minor-only cap (-0.3 total penalty maximum) should trigger when 4+ minor defects are present and total penalty would otherwise exceed -0.3.

**Best test case:** Six minor defects across multiple types and locations

**Algorithm trace:**
- Minor soiling (cover, -0.2 × 1.0): -0.20
- Minor tanning (pages, -0.2 × 0.6): -0.12
- Minor corner blunting × 2 (corners, -0.2 × 0.85 = -0.17; 2nd instance × 0.5 = -0.085): -0.255
- Minor foxing (cover, -0.2 × 1.0): -0.20
- Minor stress (spine, -0.2 × 0.9): -0.18
- Raw total: -0.955
- Minor-only cap applies: total capped at -0.3.

**Starting from 9.0 model grade:** 9.0 - 0.3 = 8.7, snapped to 8.5.

**Without the cap:** 9.0 - 0.955 = 8.045, snapped to 8.0.

**The gap:** 0.5 grade points (8.5 vs 8.0).

**AI failure mode 1:** One of the six defects gets reported as moderate instead of minor (e.g., the AI sees the foxing as moderate). This kills the minor-only cap — the final grade drops to ~7.5 instead of 8.5. The AI's tendency to over-report severity is the primary risk.

**AI failure mode 2:** AI correctly reports all minor but misses one or two defects. Fewer defects = lower raw penalty = cap still applies, but the grade calculation may accidentally match the expected result for the wrong reason.

**Confidence:** MEDIUM (algorithmic behavior is deterministic once defects are known; AI defect detection and severity is the variable)

---

### Claim 2.4: Mix of Minor + Major — Minor-Only Cap Should NOT Apply

**Claim:** If even one defect is moderate or major, the minor-only cap must not trigger. This is a correctness test, not just a boundary test.

**Best test case:** Five minor defects + one major defect

**Algorithm trace with correct behavior:**
- Five minor defects (various): raw penalty ~ -0.6 (without cap)
- One major crease (-1.5 × 1.0 cover × 1.0 multiplier): -1.5
- Total: -2.1
- all_minor = False (major crease present) → minor-only cap does NOT apply
- Starting from 9.0: 9.0 - 2.1 = 6.9, snapped to 7.0.

**AI failure mode:** The AI reports the major crease as moderate instead of major. Now total penalty is -0.5 × 1.0 + -0.6 minor = -1.1. Snapped to 7.5 or 8.0. Significant grade inflation from severity under-reporting.

**Confidence:** MEDIUM

---

### Claim 2.5: Area Weighting Differentiation — Same Defect, Different Zones

**Claim:** A crease on the cover and a crease on a page of equal visual severity should receive different penalty weights due to area weighting (cover = 1.0, pages = 0.6).

**Best test case:** Identical crease severity in two locations — cover vs. interior page

**Algorithm trace:**
- Moderate crease on cover: -0.5 × 1.0 = -0.50
- Moderate crease on page: -0.5 × 0.6 = -0.30
- Difference: -0.20 grade points per defect

**AI failure mode:** The AI may not be sensitive to whether a crease is on the cover vs. interior and may assign the same severity to both, resulting in equal penalty weights at the model layer before the area weighting multiplier is applied. The area weighting should correct for this, but only if the defect's `area` field is correctly set to "cover" vs. "pages".

**Confidence:** MEDIUM

---

## Section 3: Non-Obvious Grade Interactions

### Claim 3.1: Many Minor Defects vs. One Major Defect — Which Grades Lower?

**Claim:** At the mid-grade range (7.0–8.5), a comic with one major defect typically grades lower than a comic with 4–6 minor defects, because the minor-only cap limits total minor penalty to -0.3 while a single major defect can carry a penalty of -1.5 to -2.0.

**Evidence:**
- Overstreet's language at FN 6.0 states grade reflects "an accumulation of minor defects OR one or two moderate defects" — the word "or" explicitly treats these as equivalent at that grade.
- Mile High Comics grading standards state: "If more than one of the above allowable flaws appears in the same comic, we almost automatically downgrade to Very Fine." This reflects the convention that *any* accumulation triggers downgrade — but the key is the *severity threshold*.
- The algorithm's minor-only cap (-0.3) means a comic with 10 minor defects receives the same total penalty adjustment as one with 3 minor defects. The cap is the dominant mechanism, not the count.

**Algorithm result:**
- Starting from 9.0, 10 minor defects: adjusted to 8.7, snapped to 8.5.
- Starting from 9.0, 1 major crease: 9.0 - 1.5 = 7.5.
- **Counter-intuitive result:** The 10-minor-defect comic (8.5) grades *higher* than the 1-major-defect comic (7.5). The AI may not grasp this, as visually the 10-minor comic looks more damaged overall.

**Confidence:** HIGH (algorithm behavior is deterministic; CGC language corroborates)

---

### Claim 3.2: Water Damage (Cap 6.0) + Tape (Cap 7.0) — Which Cap Governs?

**Claim:** When two defects have different caps, the lowest cap wins regardless of which defect appears "worse" visually.

**Evidence:**
- The grading algorithm applies: `if effective_cap < cap: cap = effective_cap` iterating across all defects. First defect encountered with cap 7.0 sets cap to 7.0. Second defect with cap 6.0 overrides to 6.0. Order-independent — final cap is always the minimum.
- CGC's stain guide confirms water damage grades from 0.5–9.0 with a practical ceiling of 6.0 for significant damage. CGC's substance guide confirms tape grades to ~4.0 for extensive application, 8.0–9.0 for minor tape.
- **Practical result:** A comic with minor tape (cap 7.0 under normal circumstances) and moderate water damage (cap 6.0) cannot exceed 6.0 despite the tape being visually minor. The water damage cap dominates.

**AI failure mode:** The AI may grade based on overall visual impression, anchoring on the tape as the most "obvious" intervention and applying its cap (7.0). The water damage may read as yellowing or rippling that the AI attributes to age rather than water damage, missing the 6.0 cap entirely.

**Confidence:** HIGH (algorithm behavior deterministic; AI failure mode is hypothetical but mechanistically grounded)

---

### Claim 3.3: Spine Split (Cap 7.0) + Corner Blunting (No Structural Cap) — Penalty vs. Cap

**Claim:** When one defect has a low cap and another has no structural cap, the final grade depends on whether penalty accumulation or the cap is binding.

**Evidence:**
- Spine split: cap 7.0, major penalty -3.0. Corner blunting: cap 9.0, moderate penalty -0.5.
- If model grade = 9.0 (model doesn't see the spine split clearly):
  - Penalties: -3.0 × 0.9 (spine) + -0.5 × 0.85 (corners) = -2.7 + -0.425 = -3.125
  - Adjusted: 9.0 - 3.125 = 5.875, snapped to 6.0
  - Cap: 7.0
  - Cap is not binding — penalty pushes below cap.
- If model grade = 7.0 (model sees the spine split):
  - Penalties: -3.0 × 0.9 + -0.5 × 0.85 = -3.125
  - Adjusted: 7.0 - 3.125 = 3.875, snapped to 4.0
  - Cap: 7.0
  - Cap is not binding — penalty pushes well below cap again.
- **Counter-intuitive result:** The cap (7.0) for spine split never actually constrains the result when spine split is major severity — the penalty alone drives the grade far below 7.0.

**AI failure mode:** The AI may detect the spine split and cap the grade at 7.0, treating the cap as the *target* grade rather than an *upper bound*. The model assigns 7.0 when the correct answer is 4.0-5.0. This is the most dangerous cap misinterpretation pattern.

**Confidence:** HIGH (deterministic from algorithm code)

---

## Section 4: Recommended Compound Specimen List (4–6 Comics)

Listed in priority order. Rankings reflect: (1) likelihood of AI error, (2) algorithmic properties tested, (3) feasibility of controlled creation on a sacrificial comic.

---

### Specimen C-1: Storage Degradation Cluster
**Defects:** Minor-to-moderate soiling (cover) + light tanning (pages) + blunted corners (2–3 corners)
**Expected grade:** 7.0–8.0 (depending on severity)
**Algorithm property tested:** Penalty accumulation across different defect types with same cap; no diminishing returns between different keywords
**AI failure mode:** Applies diminishing returns across soiling/tanning/corner wear (wrong); or misidentifies tanning as a more severe stain type
**Creation feasibility:** HIGH — expose a comic to a damp cardboard environment for 48h, stack under weight to blunt corners. Soiling can be added with a soft graphite smear on cover margins.
**Priority:** 1 (most common real-world pattern; AI must handle gracefully)

---

### Specimen C-2: Minor-Only Cap Test (Many Minor Defects)
**Defects:** 5–6 minor defects: 2 minor creases, minor foxing (2–3 spots), minor soiling, minor stress lines (2–3)
**Expected grade:** 8.5 (model 9.0, minor-only cap applies → -0.3 → 8.7 → 8.5)
**Algorithm property tested:** Minor-only cap (-0.3 total) is the binding constraint, not individual penalties
**AI failure mode:** Reports one defect as moderate, killing the minor-only cap; result becomes 7.5–8.0 instead of 8.5
**Creation feasibility:** MEDIUM — requires creating multiple small-scale defects without letting any one become moderate. Stress lines from light spine bending. Foxing by aging a small area with humidity.
**Priority:** 2 (directly tests the most algorithmically unusual rule in the system)

---

### Specimen C-3: Water Damage + Tape Repair
**Defects:** Moderate water damage (corner or bottom edge) + tape repair attempt on affected area
**Expected grade:** 6.0 (water damage cap dominates over tape cap 7.0; CGC policy: tape ignored if functional but underlying damage fully scored)
**Algorithm property tested:** Lowest cap wins; CGC functional-tape policy (known algorithm deviation — the algorithm will double-penalize where CGC would not)
**AI failure mode 1:** Applies tape cap (7.0) instead of water damage cap (6.0) — 1 grade point too high
**AI failure mode 2:** Double-penalizes tape + water damage when CGC policy would ignore functional tape
**Creation feasibility:** HIGH — apply water to a corner, let dry/warp, then apply scotch tape over the water-damaged area
**Priority:** 3 (tests the most documented real-world cap interaction and a known CGC policy nuance)

---

### Specimen C-4: Same Defect, Multiple Locations (Diminishing Returns)
**Defects:** Three moderate creases at different zones (top-right corner, cover center, bottom edge) — all described as "crease"
**Expected grade:** 7.5 (with diminishing returns) vs. 7.0 (without)
**Algorithm property tested:** Diminishing returns (2nd=50%, 3rd=25%) for same keyword across locations
**AI failure mode 1:** Describes creases with varying vocabulary ("fold," "crease," "bend"), causing keyword mismatch and no diminishing returns applied
**AI failure mode 2:** Reports creases as minor instead of moderate, triggering minor-only cap and masking the diminishing-returns mechanism
**Creation feasibility:** MEDIUM — create three controlled diagonal creases at specified zones using a bone folder
**Priority:** 4

---

### Specimen C-5: Minor + Major Mix (Minor-Only Cap Should NOT Apply)
**Defects:** Four minor defects (soiling, tanning, minor foxing, minor corner wear) + one major crease (1-inch diagonal crease through cover center)
**Expected grade:** 6.0–6.5 (major crease dominates at -1.5 × 1.0; minor-only cap should NOT apply)
**Algorithm property tested:** Minor-only cap correctly skipped when any non-minor defect is present
**AI failure mode:** Rates the major crease as moderate (-0.5 instead of -1.5). Minor-only cap incorrectly applies. Grade inflates to 8.5 when correct answer is 6.0.
**Creation feasibility:** HIGH — create a single large crease intentionally; age other defects separately
**Priority:** 5

---

### Specimen C-6: Structural Failure — Spine Split + Loose Cover
**Defects:** Major spine split (full length) + partially detached cover at one staple
**Expected grade:** 3.0–4.0 per algorithm (penalty-dominated, not cap-dominated); CGC's documented maximum for full split + detachment is 1.8
**Algorithm property tested:** Penalty accumulation dominating over cap; exposes calibration gap between algorithm and CGC practice
**AI failure mode:** Applies detached cover cap (4.0) as target grade rather than upper bound; reports 4.0 when actual grade should be 2.0–3.0
**Creation feasibility:** LOW-MEDIUM — requires creating a genuine full spine split, which destroys the comic permanently and is difficult to control precisely
**Priority:** 6 (important for algorithm validation but destructive creation risk)

---

## Section 5: CGC Treatment of Compound Defects

### Claim 5.1: CGC Uses Holistic Judgment, Not Additive Formula

**Claim:** CGC does not apply an explicit additive penalty formula. Graders reach a consensus grade through holistic assessment, with multiple graders entering grades into CGC's system. The "accumulation of defects" language in grade definitions reflects this holistic approach.

**Evidence:**
- CGC's grading process page: "Grading is a team effort, with multiple CGC professionals examining every collectible... CGC's graders enter a grade for each collectible into CGC's computer system. A consensus is then reached."
- CGC explicitly states it "doesn't publicly release how it grades its comics." The grading methodology is proprietary.
- The Overstreet guide (which CGC references) uses qualitative accumulation language: "an accumulation of small defects" rather than specific penalty points.
- Grade definitions at 8.0 VF describe "a moderate defect OR an accumulation of small defects" — the explicit "or" establishes equivalence without specifying a formula for converting count to grade.

**Implication for AI testing:** There is no authoritative published CGC compound formula to validate against. Ground truth must come from CGC-certified specimens (actual CGC slabs) or high-consensus expert panels (ICC ≥ 0.75).

**Confidence:** HIGH (multiple concordant official sources; direct CGC statement on non-disclosure)

---

### Claim 5.2: CGC's Compound Grading is Primarily Cap-Driven at Extreme Cases, Penalty-Driven at Mid-Range

**Claim:** For extreme structural damage (detached cover, missing page, full spine split), CGC's documented maximums suggest their compound grading is cap-driven — the worst single defect determines the ceiling, and additional defects add only modest further reduction. For mid-grade conditions (VF to FN), accumulation of defects is the dominant mechanism.

**Evidence:**
- CGC explicitly states detached cover maxes at 4.0 regardless of other defects, and spine split + detachment cannot exceed 1.8. This is a hard cap, not an accumulation result.
- For mid-grades, the Overstreet language uses "accumulation of minor defects OR one or two moderate defects" as equivalent conditions for FN (6.0). This suggests neither is substantially harder than the other — both push the grade to approximately the same level.
- Mile High Comics standards for Very Fine: "While this category allows for many minor flaws, it does not allow for them in combination. If, for example, a comic had a small tear and two very small corner folds, we would then probably lower the grade to 'Fine.'" One grade step down for a combination of three minor defects.

**Implication for algorithm:** The current algorithm applies caps as upper bounds with penalty accumulation below the cap. This matches CGC's structural approach. The calibration issue is whether individual penalty values are properly set — particularly for compound cases at mid-grade where the holistic judgment of "this looks like an FN" may not decompose cleanly into individual penalties.

**Confidence:** MEDIUM (cap values for extreme cases confirmed; mid-range mechanism is inferred from qualitative language)

---

### Claim 5.3: CGC Functional-Tape Policy Creates Algorithm Deviation

**Claim:** CGC's 2013 policy change — ignoring tape that serves a repair function and grading the underlying defect directly — is not implemented in the algorithm. The algorithm will penalize both the tape and the underlying defect, producing a grade lower than CGC would give for functional tape over a defect.

**Evidence:**
- CGC 2013 policy (live-verified): "CGC will ignore the presence of tape if it serves a function (such as fixing a tear or spine split) and instead grade the book as if it was not present. The existing defect will be graded accordingly."
- The algorithm's defect chart entry for tape: keyword "tape", substance category, -0.5/-1.0/-3.0 penalties, cap 7.0. There is no conditional logic to skip tape penalty when tape is functional.
- Expected deviation: a spine split (moderate, -1.0 × 0.9 = -0.9) with functional tape repair. Algorithm gives: -0.9 (split) + -0.5 (tape) × 1.0 = -1.4. CGC would give: -0.9 (split only). Difference: 0.5 grade points.

**Implication for testing:** The water damage + tape specimen (C-3) should document this deviation in the expected results. The "AI error" on this specimen is partly by design — the algorithm has an acknowledged gap from CGC policy.

**Confidence:** HIGH (CGC policy live-verified 2026-04-07; algorithm code confirmed)

---

## Section 6: Uncertainty and Open Questions

1. **Diminishing returns across the same defect at extreme accumulation:** If a comic has 8+ stress lines, all minor, the diminishing returns rule (25% for 3rd+) means the marginal contribution approaches zero. Does CGC treat 8 minor stress lines as worse than 3? The grade definitions suggest yes (they distinguish "slight" from "notable accumulation" of stress lines). The algorithm may under-penalize severe accumulations of the same defect type.

2. **Compound cap interactions when both caps are very low:** Detached cover (cap 4.0) + water damage (cap 6.0) + tape (cap 7.0). Lowest cap = 4.0. The algorithm correctly applies this, but CGC may treat detached cover as so dominant that other defects barely matter. Testing this would require a CGC-certified specimen with all three defects.

3. **Area weighting calibration for cross-zone compounds:** A stain on the spine (area weight 0.9 for spine) vs. a stain on the cover (area weight 1.0) — the 10% difference is small. Does CGC actually weight spine stains lower than cover stains? This is an algorithm design assumption without direct CGC confirmation.

4. **Tape + water damage CGC policy edge case:** CGC's policy says tape is ignored if it "serves a function." What if the tape doesn't fully repair the damage (e.g., tape over a partially water-warped area that is still warped)? Is the tape then functional or decorative? This edge case is not addressed in available documentation.

---

## Sources

| ID | URL | Type | Accessed | Claims Supported |
|----|-----|------|----------|-----------------|
| src-001 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide | official | 2026-04-07 | 1.1, 1.2, 1.3, 5.1 |
| src-002 | https://www.cgccomics.com/news/article/3327/CGC-Modifies-Stance-on-Grading-Submissions-with-Tape/ | official | 2026-04-07 | 1.3, 5.3 |
| src-003 | https://www.cgccomics.com/news/article/10326/common-comic-book-grading-defects/ | official | 2026-04-07 | 1.1, 5.1 |
| src-004 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/crease | official | 2026-04-07 | 1.2 |
| src-005 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/tear | official | 2026-04-07 | 1.4, 3.2 |
| src-006 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/stain | official | 2026-04-07 | 1.3, 3.2 |
| src-007 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/substance | official | 2026-04-07 | 1.3, 5.3 |
| src-008 | https://www.overstreetaccess.com/grading-definitions/ | official | 2026-04-07 | 2.2, 3.1, 5.2 |
| src-009 | https://www.milehighcomics.com/information/grade.html | community | 2026-04-07 | 3.1, 5.2 |
| src-010 | https://www.cgccomics.com/grading/grading-scale/ | official | 2026-04-07 | 2.3, 5.1, 5.2 |
| src-011 | https://www.cgccomics.com/grading/grading-process/ | official | 2026-04-07 | 5.1 |
| src-012 | https://www.comiccollectorlive.com/forum/default.aspx?g=posts&t=4807 | community | 2026-04-07 | 1.2 |
