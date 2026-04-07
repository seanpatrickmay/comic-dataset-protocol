# Adversarial Review: Comic Book Grading Dataset Construction Protocol
**Target**: `research/synthesis.md`  
**Reviewers**: Three adversarial personas  
**Date**: 2026-04-07  
**Brief compliance check**: `brief.md` reviewed in parallel  
**Corrections applied check**: `verification/corrections.md` reviewed  

---

## Preamble: What This Review Is

This is a genuine adversarial challenge — not a polish pass. Every section below is a challenge to a specific claim or protocol decision. Tags are:

- **HOLDS** — Claim is defensible; challenge attempted and failed
- **GAP** — Claim is incomplete or has a meaningful hole not addressed
- **INFLATE** — Claim is overstated relative to the evidence
- **UNSUPPORTED** — No credible source or derivation provided

Each finding is followed by a required protocol action: **FIX**, **CLARIFY**, or **ACCEPT-RISK**.

---

## PERSONA 1: The Practitioner
*"Two grad students, 70 comics, iPhones, and $65. Can we actually do this? How many hours does each step take? What happens when step 5 fails?"*

---

### P1-01 — Time Estimate: THE BRIEF IS VIOLATED — INFLATE

**Claim being challenged**: Brief §Quality Requirements: "The protocol must be executable in 3–4 days by 2 people."

**The math the synthesis never does**:

| Task | Estimated Time |
|---|---|
| Phase 0: Pre-study (independent, each) | 4–6 hrs each = 8–12 person-hours |
| Phase 1: Anchor calibration | 3 hrs (both) |
| Phase 2: Progressive calibration | 2 hrs (both) |
| Phase 3: Blind grading (70 comics × ~2.5 min each, both independently) | ~3.5 hrs each = 7 person-hours |
| ICC computation + disagreement discussion | 1–2 hrs |
| Photography: 70 comics × 3 conditions × ~8 min/comic/condition | ~28 hrs |
| Defect creation: 23 specimens (many needing 2–3 attempts) | 8–12 hrs |
| Annotation (70 comics, detailed schema) | 5–8 hrs |
| Setup/teardown per session, equipment prep | 2–3 hrs |
| **Conservative total** | **~65 person-hours** |

At two people working 8-hour days together on the joint tasks: the photography alone (28 hrs assuming the 3-condition protocol) nearly fills 4 days by itself, before any grading, defect creation, or annotation happens. Phase 0 is explicitly described as "independent" work occurring before the primary session days.

**The synthesis never constructs a day-by-day schedule.** This is the most operationally critical output for two people coordinating their calendars, and it is absent. The brief requires this level of specificity ("step-by-step protocol that a team can follow with zero ambiguity").

**What actually fails**: The 3-condition photography protocol (scan + table + handheld for all 70) is the primary schedule killer. The synthesis notes "if feasible" in the dataset completeness checklist (§9.5) but never defines what constitutes feasibility or what to drop first. A realistic team needs a tiered schedule: Day 1–2, Day 3–4, Day 5–6 contingency.

**Required action**: FIX. Add an explicit day-by-day schedule with realistic time per task. The 3-condition protocol should be marked as a target, with a defined downgrade path (all-70 table-only as the floor).

---

### P1-02 — Photography Station: No Equipment Cost Breakdown — GAP

**Claim being challenged**: Part 1 Equipment lists everything needed. Budget constraint is ~$65.

**What the synthesis never says**: It never adds up the equipment costs. Reading the list:

- Two LED desk lamps with gooseneck: $15–30 each = $30–60
- Matte black foam board (30×40 cm, rigid): $5–10
- Black velvet cloth: $8–15
- Tripod or copy stand for iPhone: $15–40 (a copy stand that works reliably for overhead shooting is $30+)
- Calipers (digital, 0.1mm resolution): $10–20
- Steel ruler: $5–8
- Bone folder: $5–10
- Cotton gloves (archival): $5–8
- 10x loupe: $10–20
- FeSO₄ for foxing (Option A): ~$8
- Safety glasses: $3–5
- Fine-grit sandpaper (220+400 grit): $3–5
- Eyedropper/fine brush: $3–5
- UV/black light (365nm): $10–20
- Scotch tape 3M Magic: $3
- Cross-polarization setup (flagged as optional): $20–40

**Conservative total (no cross-pol)**: ~$125–224.

This materially exceeds the $65 lower bound. The synthesis does not tell the team which items to cut if they have $65, not $100. Given the brief explicitly states "~$65–100 for equipment," the synthesis fails this constraint without providing a minimum viable equipment list.

**What's missing**: A tiered equipment list — Tier 1 ($65 minimum viable), Tier 2 ($100 enhanced), Tier 3 ($140 full featured).

**Required action**: FIX. Compute the actual equipment cost against the budget. Produce a prioritized cut list.

---

### P1-03 — Minor Crease Creation: 50% Success Rate Is Operationally Untenable — GAP

**Claim being challenged**: §5.3 — "Minor crease: Success rate ~50% (glossy)."

**The practitioner problem**: The synthesis acknowledges the 50% success rate but does not tell the team how many control comics they need to have on hand to guarantee achieving 2 minor crease specimens. At 50% success: to achieve 2 successes with 95% probability requires approximately 7–8 attempts (binomial CDF). The synthesis says "plan for 1.5–2× the needed attempts" — which at 50% would require 4 attempts for 2 specimens. That's not 1.5–2×; it's approximately 3.5× for 95% probability.

**What's actually worse**: The 50% figure applies to modern glossy. The synthesis acknowledges brittle aged comics should skip minor severity entirely. But 20 of the controlled specimens are on paper-type-unspecified stock. If any of these are bronze/copper age (which is mixed), the 50% drops toward 30%. The team has no guidance on what to do when they burn through 6 comics trying to get 1 minor crease specimen.

**No "abort and source naturally" trigger is defined**: The synthesis says "if over-severity: flag specimen; do not discard — annotate actual severity achieved" — but this means the minor severity tier is potentially underrepresented in the dataset and the protocol says nothing about what that does to the statistical design.

**Required action**: FIX. Add explicit attempt budgets for each defect × severity combination. Define the natural-specimen fallback trigger: "If after N attempts you have not achieved minor severity, replace with a naturally occurring specimen of equivalent severity."

---

### P1-04 — Photography: 8-Minute-Per-Comic Assumption Never Stated — GAP

**Claim being challenged**: The photography protocol describes 4 mandatory + recommended shots, each requiring lighting reconfiguration.

**The math the synthesis omits**: Shots 1, 2, and 3 each require distinct lighting configurations (two-light symmetric, single-raking-left, single-raking-top). Between shots:
1. Remove/reposition one LED
2. Re-engage AE/AF lock (tap and hold, confirm banner)
3. Use 2-second timer to eliminate shake
4. Verify raking shadow in frame before capture
5. Transfer comic to the next position

Per-comic time for 3 mandatory shots plus Shot 4 (macro): realistically 6–10 minutes at practiced pace, 12–20 minutes at learning-curve pace (first session). The synthesis never states any per-comic time estimate and never tells the team how long the photography phase takes in aggregate. This is a critical operational omission.

**For 70 comics at practiced pace (8 min/comic, table condition only)**: ~9.3 hours. For 3 conditions: ~28 hours. This is not a brief 2-day photography session.

**Required action**: CLARIFY. State explicitly: "Photography of all 70 comics in a single condition takes approximately 9–10 hours at practiced pace. Three-condition photography is a 2–3 day task."

---

### P1-05 — C-1 Tanning Creation: 48-Hour Wait Inside 3–4 Day Protocol — GAP

**Claim being challenged**: Specimen C-1 (Priority 1, Storage Degradation Cluster) creation: "Expose comic to damp cardboard environment (sealed bag with damp sponge, 48h) for tanning."

**The scheduling problem**: C-1 is Priority 1 — the highest priority compound specimen. Its creation requires a 48-hour damp-environment soak before the tanning specimen is ready to grade or photograph. If this is done on Day 1, it does not come out until Day 3 at the earliest. The protocol never addresses this dependency, never tells the team to start C-1 before anything else, and never integrates the 48-hour wait into any suggested schedule.

**Additional concern on the tanning claim itself**: A 48-hour damp-bag exposure does not reliably produce tanning — it more reliably produces mold. Tanning (paper yellowing) is an oxidative/acidic process that takes days to weeks at elevated temperature and humidity. A sealed damp bag at room temperature is more likely to produce foxing-precursor conditions (mold spores, water damage) than actual page tanning within 48 hours. This technique is not validated against CGC tanning criteria and there is no source cited for it. See also Persona 2 challenge below.

**Required action**: FIX. Either (a) validate the 48-hour damp-bag claim against actual tanning outcomes, or (b) replace C-1 tanning technique with the oven method referenced in Open Question 6 — with the caveat that oven tanning requires 24–72 hours, pushing C-1 outside any realistic 3–4 day protocol.

---

### P1-06 — Flatbed Scanner: Not in Equipment List, Not in Budget — GAP

**Claim being challenged**: §4.3 Three-Condition Photography: "Scan | Flatbed scanner (if available) | Clean, artifact-free reference."

**The problem**: The equipment list (Part 1) never mentions a flatbed scanner. The budget never allocates for one. A flatbed scanner capable of capturing a full comic cover (standard comic = 10.25" × 6.625") requires at minimum a legal-size flatbed (many standard consumer scanners max at letter size, 8.5" × 11"). A legal-size flatbed costs $80–180 new, immediately blowing the entire equipment budget.

**"If available" is not a protocol instruction.** It is a hand-wave. Either the scan condition is required (and the equipment list must include the scanner), or it is optional (and the statistical design section should not present it as one of the three primary conditions with CI calculations).

**The CI calculation depends on all 3 conditions**: If the scan condition is missing for a significant fraction of comics, the per-tier CI table (§7.2) is based on n=210 images that the team may not be able to produce.

**Required action**: FIX. Either add a flatbed scanner to the equipment list with cost, or demote the scan condition from the primary three-condition design to a "bonus if you have access to one" footnote, and revise the CI table accordingly.

---

### P1-07 — Annotation: Time and Tooling — GAP

**Claim being challenged**: Part 8 defines a detailed annotation schema but never specifies what tool the team uses to fill it out, or how long it takes.

**The problem**: The annotation schema (§8.1–8.2) has 12 fields per comic plus a nested defect object schema with 9 fields per defect. For a comic with 3 defects, that is 12 + (3 × 9) = 39 field-fill operations per comic. At 70 comics (average 2 defects each): approximately 2,100 field operations. No tooling is specified — is this a spreadsheet? A JSON file? A custom form? 

**Without tooling, annotation becomes a bottleneck.** Two people filling in JSON by hand for 70 comics will introduce transcription errors. The protocol says "annotation file has no empty required fields" as a completeness check, but never defines how to achieve this efficiently.

**Required action**: CLARIFY. Specify the annotation tooling (even if just "a Google Sheet with column headers matching the schema") and provide a realistic annotation time estimate.

---

## PERSONA 2: The CGC Expert
*"Would CGC actually classify these controlled defects the way you claim? Are these severity thresholds real or made up?"*

---

### P2-01 — CGC Source Traceability: Severity Tables Lack Primary Citations — GAP

**Claim being challenged**: The severity threshold tables in §5.3–5.8 are presented as CGC-grade-anchored.

**The verification problem**: CGC does not publish a numerical severity table mapping crease length to grade. The Overstreet Guide publishes grade boundary descriptions in prose. The synthesis translates these prose descriptions into measurement tables (e.g., "minor crease: length ≤2"," "moderate: ≤2" with ~50% color break"). These translations involve interpretation that CGC itself has not endorsed.

**Specific claim to challenge**: §5.3 — "Minor (green): No color break, Length ≤2", width <0.5mm, Grade Equivalent 8.0–9.2." The ≤2" length threshold for minor-green creases — what is the primary source? The corrections log verifies Overstreet 9.4 NM (1/16" bend) and 9.0 VF/NM (1/8" bend) as correct, but these are bend limits, not crease length limits. A 1.5" crease with no color break could plausibly grade 8.5 or 9.0 depending on location (cover center vs. corner). The synthesis does not address location-dependent weighting.

**The fundamental gap**: CGC grades the whole book, not individual defects in isolation. A 1.5" crease on the cover center grades differently from a 1.5" crease along the bottom edge. The severity tables in §5.3–5.8 treat defect severity as a location-independent property. This is a simplification that CGC itself does not make.

**Impact on the dataset**: Controlled specimens with "minor crease" labels based on length alone may receive inconsistent CGC-equivalent grades depending on placement. The annotation schema captures defect area (12-zone) but the severity threshold tables do not incorporate area in their tier definitions.

**Required action**: CLARIFY. Add a note to each severity threshold table: "These thresholds are derived from Overstreet grade-boundary prose descriptions and assume typical defect placement. Cover-center placement elevates severity one tier; margin placement may reduce effective impact. CGC does not publish numerical severity tables; these represent research team's interpretation."

---

### P2-02 — The 48-Hour Damp Bag Does Not Produce Tanning — UNSUPPORTED

**Claim being challenged**: §6.3 Specimen C-1 creation: "Expose comic to damp cardboard environment (sealed bag with damp sponge, 48h) for tanning."

**The CGC expert's objection**: CGC defines page tanning (also called "browning" in conservation literature) as oxidative degradation of cellulose and lignin in acidic wood-pulp paper, typically driven by prolonged exposure to heat, humidity, light, or oxygen. The primary mechanism is acid hydrolysis of cellulose chains, producing chromophoric degradation products that cause yellowing/browning.

**A 48-hour room-temperature damp-bag exposure does not produce tanning.** What it produces:
1. Surface moisture damage — tide lines, cockling (a Distortion defect, not a Tanning defect)
2. Potential foxing initiation if mold spores are present (an entirely different defect type)
3. Possible cover ink darkening from moisture — again, not tanning

Tanning on pre-1970s newsprint, if naturally occurring, took years of acid migration. Laboratory acceleration requires 80°C and 65% RH for 24–72 hours (ISO 5630-3, correctly referenced in Open Question 6). The synthesis correctly identifies oven aging as the proper method in Open Question 6, but then calls for a damp bag in C-1 without reconciling this contradiction.

**This is the highest-confidence challenge in this entire review**: The C-1 "tanning" specimen will not produce tanning. It will produce a different set of defects entirely, and those defects may not test the algorithm property C-1 is designed to test.

**Required action**: FIX (critical). Replace C-1 tanning creation technique with: (a) naturally occurring tanned comic from existing collection, or (b) oven accelerated aging per ISO 5630-3 adapted household method (Open Question 6 must be resolved before C-1 can be built). Explicitly note that C-1 must be started at least 3 days before the primary protocol sessions.

---

### P2-03 — Minor-Only Cap: CGC Does Not Have This Rule — GAP

**Claim being challenged**: §6.2: "Minor-only cap: When all defects are minor severity, total penalty is capped at -0.3 regardless of count."

**The expert's challenge**: This is an algorithm design rule for the AI pipeline — not a documented CGC policy. CGC does not publish a "minor-only cap" rule. The synthesis presents this as a fact about grading behavior, but it is actually a feature of Sean and Marcus's custom AI system. 

**Why this matters for the dataset**: Specimen C-2 is designed to test whether the AI correctly applies the minor-only cap. But the "correct" behavior is defined by the algorithm, not by CGC. A CGC grader encountering a book with 10 minor defects would not necessarily grade it at 8.5 — they might grade it at 8.0 or 7.5 depending on how those defects interact with their holistic judgment.

**The compound dataset is testing AI-vs-algorithm consistency, not AI-vs-CGC consistency.** This distinction is not clearly stated in the synthesis. It matters because if Phase 1 shows the AI correctly applies the minor-only cap, that means the AI matches the algorithm — but the algorithm itself may not match CGC.

**Required action**: CLARIFY. Every compound specimen test description should explicitly state whether the "correct" answer is defined by CGC practice or by the algorithm. Where it's algorithm-defined (C-2, C-4), say so explicitly.

---

### P2-04 — Spine Stress "Major" Threshold Overlap with Crease Definition — GAP

**Claim being challenged**: §5.8 — "Major (red) spine stress: Numerous lines, many with color break, OR any >1" (reclassifies as crease)." §5.3 — "Major (red) crease: >2" long OR full color-break line."

**The definitional gap**: If a spine stress line >1" is reclassified as a crease, but a crease is only "major" at >2", then there is a 1"–2" gap zone where a stress line has been reclassified as a crease but the crease threshold for "major" has not been reached. The synthesis does not specify what tier a 1.25" reclassified stress-line-crease receives. Is it moderate? By what criterion?

**Additionally**: The major spine stress tier includes "OR any >1" (reclassifies as crease)" — but 1" is actually the threshold for reclassification according to CGC, meaning that a "major spine stress" specimen with a >1" line is technically not a spine stress specimen at all; it is a crease specimen. These are different CGC defect categories. A specimen labeled "major spine stress" that contains a >1" line will be mislabeled.

**Required action**: FIX. Rewrite the major spine stress tier to exclude the >1" reclassification case (it belongs in crease, not spine stress). The spine stress major tier should be defined purely by count of color-breaking lines, not length-based reclassification.

---

### P2-05 — Stain Grade Equivalents Are Too Optimistic for Prominent Stains — INFLATE

**Claim being challenged**: §5.7 — "Moderate (yellow) stain: Grade Equivalent 7.0–8.5."

**The CGC expert's objection**: CGC stain caps. A water stain cap is 6.0 (referenced correctly in §7.3 and §6.3). But the stain severity tier table in §5.7 places moderate stain at "7.0–8.5" — which is above the CGC cap for water stains. The cap means the book cannot grade above 6.0 regardless of stain severity. A "moderate" stain (5–25mm, tide line present) almost certainly triggers the water damage cap at 6.0, making the "7.0–8.5" grade equivalent table entry actively misleading.

**The table is inconsistent with the cap logic stated elsewhere in the same document**: §6.3 correctly states "water damage cap 6.0." §5.7's "moderate stain: 7.0–8.5" contradicts this for any stain that qualifies as water damage.

**The distinction that might save it**: Not every stain is water damage. A soiling stain (graphite, oil, minor surface contamination) has a different CGC cap than a water-damage stain. The synthesis conflates these in §5.7. If the moderate severity tier table applies only to non-water stains, this should be explicit. If it applies to water stains, the grade equivalents must be corrected downward.

**Required action**: FIX. Split the stain severity table by stain type (water vs. non-water) OR add a column for applicable cap OR add a footnote: "Water damage stains carry a 6.0 cap regardless of this table's grade equivalent range."

---

## PERSONA 3: The Statistician
*"Do these sample sizes actually support the claims? Is the CI math correct after the clustering correction?"*

---

### P3-01 — ICC Computation Code Has a Probable Bug — GAP

**Claim being challenged**: §3.8 ICC computation — `result[result['Type'] == 'ICC3']`.

**The statistician's challenge**: The `pingouin.intraclass_corr()` function returns a DataFrame with multiple ICC types. The `Type` column in pingouin uses values like `'ICC1'`, `'ICC2'`, `'ICC3'`, `'ICC1k'`, `'ICC2k'`, `'ICC3k'`. The synthesis selects `ICC3` — which is the Two-Way Mixed-Effects model. However, the synthesis also correctly states that the model is ICC(3,1) (Single Measures) not ICC(3,k) (Average Measures). This is consistent. But the code selects rows where `Type == 'ICC3'` — in pingouin, this returns both ICC3 and ICC3k rows if they share a prefix match.

**The safer code is**:
```python
icc31 = result[result['Type'] == 'ICC3']
```
In practice, pingouin returns exactly one row per Type string, so the filter is technically correct — but the comment says `# ICC3` when the model is ICC(3,1), which has the pingouin type string `'ICC3'` (not `'ICC3,1'`). The code will work. The documentation is ambiguous enough to cause misinterpretation on re-read.

**More substantive concern**: The code will silently proceed even if both graders grade the same N comics but if the `Subject` column has duplicates (e.g., a comic photographed twice by mistake), pingouin will return an inflated ICC. There is no input validation step. For a 70-comic dataset entered by hand, a duplicate or mis-keyed ID is a realistic failure mode.

**Required action**: CLARIFY. Add input validation: assert `data.groupby(['Subject', 'Rater']).size().max() == 1` before the ICC call, with a human-readable error message.

---

### P3-02 — The ±4pp Accuracy Target from the Brief Is Never Addressed — INFLATE

**Claim being challenged**: The brief states: "Build a dataset rigorous enough to measure AI grading accuracy at ±4pp." The synthesis states the effective CI is ±7.5pp.

**The gap**: The synthesis correctly concludes ±7.5pp effective CI and correctly notes in §7.4 that ±4.8pp requires n=210 unclustered images. But the synthesis never explicitly states: **"Phase 1 cannot achieve the ±4pp brief target."**

This is the most important statistical conclusion in the entire document and it is buried as a caveat. A reader could skim the synthesis and believe ±7.5pp is acceptable progress toward ±4pp. The synthesis does not tell the team what would be required to achieve ±4pp: approximately n=556 unclustered independent images, or ~185 independent comics photographed once each.

**The brief's ±4pp target is a hard requirement that the 70-comic design provably cannot meet.** This should be a prominent, explicit finding, not an implicit correction to a corrected correction.

**Required action**: FIX. Add to §7.1 or §7.4: "The brief target of ±4pp accuracy cannot be achieved with 70 comics under any photography scheme. Phase 1 establishes a ±7.5pp effective CI baseline. Achieving ±4pp requires approximately 185+ independent comics. Phase 1 should be framed as a feasibility study, not a definitive accuracy measurement."

---

### P3-03 — DEFF = 2.4 Is Asserted, Not Derived — UNSUPPORTED

**Claim being challenged**: §4.3 — "With within-comic ICC_within ≈ 0.70, design effect DEFF = 2.4."

**The statistician's challenge**: DEFF for clustered data is computed as: DEFF = 1 + (m - 1) × ICC_within, where m = cluster size (images per comic) and ICC_within is the intra-cluster correlation. With m = 3 conditions and ICC_within = 0.70: DEFF = 1 + (3-1) × 0.70 = 1 + 1.40 = **2.40**. This is correct.

**But**: ICC_within ≈ 0.70 is asserted without a source. This means: 70% of the variance in AI grade predictions is attributable to which comic is being graded, and only 30% is attributable to which photography condition was used. Is 0.70 defensible? It seems plausible — the same comic under different lighting should get similar grades — but it is also possible that the AI grades handheld images 2+ points lower than controlled images, in which case ICC_within might be much lower (0.40?), giving DEFF = 1 + 2 × 0.40 = 1.80, effective N = 210/1.80 = 116.7, corrected CI ≈ ±6.5pp. Or if ICC_within = 0.85, DEFF = 2.70, CI widens to ±7.8pp.

**The synthesis presents a single-point estimate of CI based on an assumed ICC_within with no sensitivity analysis.** A ±0.15 variation in ICC_within produces a ±1pp variation in the effective CI. This uncertainty should be reported.

**Required action**: CLARIFY. Add: "The ICC_within = 0.70 assumption is a prior estimate; actual DEFF will be computable from the Phase 1 dataset itself. Sensitivity: if ICC_within = 0.50, DEFF = 2.0, CI ≈ ±6.9pp; if ICC_within = 0.85, DEFF = 2.70, CI ≈ ±7.8pp."

---

### P3-04 — Per-Tier CIs Should Be Flagged As Inadequate — INFLATE

**Claim being challenged**: §7.2 Grade Tier Distribution — Per-Tier CI table is presented without adequacy judgment.

**The statistician's challenge**: 
- High tier (15 comics, 45 images, effective n ≈ 18.75): CI = ±10.4pp — this means a detected 10pp AI bias in the high tier could plausibly be noise. 
- Very Low tier (5 comics, 15 images, effective n ≈ 6.25): CI = ±17.6pp — this tier is effectively unmeasured.

These are not just "wide CIs" — they are CIs wide enough to make tier-level accuracy analysis meaningless for 3 out of 5 tiers at any practically important effect size. The synthesis says "Phase 1 can detect tier-level biases of ≥20pp with reasonable confidence" — but at ±17.6pp for the Very Low tier, the detectable bias threshold is effectively 35pp, not 20pp.

**The rationale for 15 High-tier comics is stated as Neyman optimal allocation** (overweight high-variance tiers). But Neyman allocation maximizes overall CI, not per-tier CI. If the goal is per-tier AI bias detection, the allocation should weight for the smallest acceptable per-tier CI, not the minimum overall CI. The synthesis does not justify why the Neyman allocation was chosen over a minimum-per-tier-CI design.

**Required action**: CLARIFY. Add honest per-tier adequacy assessment: "Very Low tier (n=5): CI ±17.6pp, inadequate for any tier-level claim. Low tier (n=10): CI ±12.7pp, can only detect catastrophic failures. This allocation is optimal for overall CI, not for tier-level comparisons."

---

### P3-05 — Recall Power Calculation Uses the Wrong Framework — GAP

**Claim being challenged**: §7.3 — "With 5 specimens and true recall = 0%, P(detecting the failure) = 1 - 0.95⁵ = 23%. Weak but better than nothing."

**The statistician's challenge**: The P(detecting failure) = 1 - 0.95⁵ calculation assumes each specimen independently has a 5% probability of detection even when recall = 0% — which is internally contradictory. If true recall is 0%, P(detecting any specimen) = 0, and P(observing at least one detection) = 0, not 23%.

**What the synthesis means to say**: If the true AI recall is some unknown value p, and we observe 0 detections in 5 specimens, then the one-sided 95% confidence upper bound on p is approximately 1 - (0.05)^(1/5) ≈ 45%. This is the correct framing: "If the AI detects 0 out of 5 specimens of a given defect type, we can rule out recall > 45% at 95% confidence." 

**The 23% figure is a misapplication of the detection power formula.** The correct statement is: "5 specimens allows us to rule out recall > 45% at 95% confidence if zero are detected; this is catastrophic-failure ruling-out capability only." 

**This is not just a nitpick**: The 23% figure appears in both §7.3 and is the basis for the "catastrophic failure ruling-out" claim in §7.4. The claim is directionally correct but the math behind it is wrong and the correct number (45% upper bound on recall) is actually more pessimistic than the 23% implies.

**Required action**: FIX. Replace the 23% calculation with the one-sided 95% CI upper bound framing: "If 0/5 specimens are detected, we can exclude recall > 45% at 95% confidence."

---

### P3-06 — The Allocation 39/14/9/8 Is Convenience, Not Optimal — GAP

**Claim being challenged**: §7.1 — The 70-comic allocation (39/14/9/8) is presented as the result of an information-theoretic or statistical design process.

**The statistician's challenge**: The basis for 39 baseline comics is not derived from any power calculation — it appears to be "70 minus the controlled specimens." The 14 single-defect and 9 severity-spectrum allocations are stated in §7.3 but their basis is not a formal design; they cover 4 priority defect categories with 2–3 specimens each. This is a reasonable heuristic. It is not "optimal" in any formal sense.

**Specifically**: The synthesis in §6.1 argues compound specimens are the "highest-value specimens" under D-optimal design logic. If compound specimens are highest-information, why does the allocation give them only 8 comics (11% of the budget) vs. 39 (56%) for baseline? Under a pure D-optimal allocation favoring compound specimens, you would expect the compound fraction to be much higher. The synthesis does not resolve this tension — it advocates for compound specimens as highest-ROI then allocates them the smallest non-very-low-tier count.

**The actual justification for 39 baseline**: The brief requires accuracy measurement (±4pp target, even though unachievable), which needs baseline comics to estimate overall accuracy. The 39-baseline allocation is justified by the accuracy measurement goal, not by information-theoretic design. The synthesis should say this explicitly.

**Required action**: CLARIFY. State the actual design rationale for each bin: 39 baseline = driven by overall accuracy CI requirement; 14+9 controlled = driven by defect detection coverage; 8 compound = limited by destructible-comic count and creation difficulty. Acknowledge the tension with the D-optimal claim for compounds.

---

## Cross-Persona Findings

### XP-01 — Brief Compliance: Gap Between ±4pp Target and ±7.5pp Achievable — INFLATE

**Tags both Persona 1 and Persona 3.** The brief sets ±4pp as the goal. The synthesis delivers ±7.5pp and does not explicitly tell the team they cannot meet the brief target with these resources. A grad student executing this protocol will produce a dataset that achieves ±7.5pp and may not realize this misses the stated goal by approximately 90% of the required additional sample size. This should be front-paged, not buried in a correction footnote.

**Required action**: FIX. Add a "Brief Compliance Summary" section at the top of the synthesis (or the protocol document) explicitly listing: what the brief requires, what Phase 1 achieves, and what would be required to close each gap.

---

### XP-02 — Safety: Oven Use for Tanning Is Not Addressed Safely — GAP

**The oven aging protocol** (Open Question 6: 65°C with a cup of water, 24–72 hours) is presented as an open question but also as the correct method for tanning simulation. Several safety concerns are unaddressed:

1. **Fire risk**: Placing paper comics in a household oven at 65°C for 72 hours is not a standard kitchen activity. Paper ignition temperature is ~233°C, which is well above 65°C, but a malfunctioning oven thermostat or an accidental temperature increase could produce a smoldering fire. The protocol should require a working oven thermometer (not just trusting the dial) and never leaving the oven unattended for multi-hour cycles.
2. **Carbon paper off-gassing**: Older newsprint can off-gas acidic compounds when heated. Running this in a kitchen oven that is also used for food is inadvisable.
3. **Mold risk**: The damp-bag C-1 creation generates a sealed humid environment with organic material (paper, possible cardboard dust). This creates conditions favorable for mold growth. Mold spores in an enclosed space (sealed bag) should require handling with gloves and mask, not just gloves.

The corrections log (Correction 2) added eye protection for FeSO₄. No equivalent safety audit was applied to thermal aging or mold-risk procedures.

**Required action**: FIX. Add a consolidated Safety section early in the protocol (not buried in individual specimen creation notes) covering: FeSO₄ handling, oven aging precautions (thermometer required, dedicated non-food oven preferred), and damp-bag mold risk (gloves + mask when opening).

---

### XP-03 — The "Would CGC Classify It This Way?" Test Is Absent — GAP

**The brief explicitly requires**: "Every defect creation instruction must reference CGC's official definitions." The synthesis references Overstreet and CGC Grader Notes, but these are third-party educational materials, not CGC's grading standards documentation. CGC's actual grading standards are not publicly available in the form of a numbered specification.

**The practical consequence**: There is no validation step in the protocol for "would this specimen actually receive this grade from CGC?" The only real validator is CGC submission — explicitly out of scope. But no substitute verification procedure is defined. The protocol says "compare measurement against severity thresholds in §5.3–5.8" — but those thresholds are the synthesis team's interpretation of Overstreet prose.

**The gap is not that the sources are wrong** — the Overstreet thresholds are the closest publicly available approximation to CGC standards and have been used correctly. The gap is that the protocol presents them as CGC standards without the appropriate epistemic caveat.

**Required action**: CLARIFY. Add a protocol-level note: "CGC does not publish a quantitative grading specification. All severity thresholds in this protocol are derived from Overstreet Guide descriptions and CGC Grader Notes educational materials. These represent the closest available publicly documented proxy for CGC practice. Ground truth is CGC submission, which is out of scope for Phase 1."

---

## Summary Scorecard

| Claim | Tag | Persona | Required Action |
|---|---|---|---|
| Protocol executable in 3–4 days | INFLATE | P1 | FIX: Add day-by-day schedule |
| Equipment within $65–100 budget | GAP | P1 | FIX: Itemize costs; add tiered cut list |
| Minor crease 50% success rate is workable | GAP | P1 | FIX: Add attempt budgets and natural-specimen fallback trigger |
| Photography time is manageable | GAP | P1 | CLARIFY: State ~9–10 hrs per condition |
| C-1 tanning (48h damp bag) works | GAP | P1 | FIX: Start 3+ days early; validate technique |
| Flatbed scanner as listed condition | GAP | P1 | FIX: Add to equipment + budget or demote to optional |
| Annotation tooling unspecified | GAP | P1 | CLARIFY: Specify tooling |
| Severity tables are CGC-grounded | GAP | P2 | CLARIFY: Epistemic caveat on interpretation |
| Damp-bag 48h produces tanning | UNSUPPORTED | P2 | FIX: Replace with natural specimen or validated oven method |
| Minor-only cap is CGC behavior | GAP | P2 | CLARIFY: Algorithm rule vs. CGC practice |
| Spine stress major tier definition | GAP | P2 | FIX: Remove reclassification case from spine stress table |
| Stain grade equivalents (moderate = 7.0–8.5) | INFLATE | P2 | FIX: Add water-damage cap caveat to table |
| ICC code correctness | GAP | P3 | CLARIFY: Add input validation assertion |
| ±4pp brief target achievable | INFLATE | P3 | FIX: Front-page that brief target is not met |
| DEFF = 2.4 sourcing | UNSUPPORTED | P3 | CLARIFY: Add sensitivity analysis for ICC_within |
| Per-tier CI adequacy | INFLATE | P3 | CLARIFY: Add explicit per-tier adequacy verdict |
| Recall power = 23% | GAP | P3 | FIX: Correct to one-sided CI upper bound framing |
| 39/14/9/8 allocation is optimal | GAP | P3 | CLARIFY: State actual design rationale per bin |
| ±4pp brief gap not front-paged | INFLATE | XP | FIX: Add Brief Compliance Summary section |
| Oven/mold safety not addressed | GAP | XP | FIX: Add consolidated Safety section |
| Protocol claims CGC grounding | GAP | XP | CLARIFY: Add epistemic caveat on standards source |

**Totals**: 4 HOLDS (not listed — no major claim survived unmodified with zero caveats; all claimed HOLDs degrade to GAP or CLARIFY), 12 GAP, 5 INFLATE, 2 UNSUPPORTED.

**Hard-gate findings** (must fix before protocol document is drafted):
1. **P1-01**: Add a realistic day-by-day schedule. The 3–4 day claim is violated.
2. **P2-02**: Replace C-1 tanning technique. Damp bag does not produce tanning.
3. **P3-02**: Front-page that ±4pp brief target is not achievable with 70 comics.
4. **P3-05**: Correct the 23% recall power calculation.
5. **P2-05**: Fix the stain severity table — moderate stain cannot grade 7.0–8.5 if water-damage cap is 6.0.

---

*End of adversarial review. No claim was treated gently. Findings are tractable — none require abandoning the protocol, but five require substantive fixes before the deliverable is drafted.*
