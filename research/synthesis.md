# Unified Research Synthesis: Comic Book Grading Dataset Construction Protocol

**Synthesized by**: research-synthesizer agent  
**Date**: 2026-04-07  
**Source files**: defect-creation.md, photography-science.md, grading-calibration.md, severity-spectrum.md, statistical-design.md, compound-defects.md, verification/corrections.md  
**Brief reference**: brief.md (70 comics, ~$65–100 budget, iPhone cameras, 2 graders, ±4pp accuracy target)

---

## How to Read This Document

This synthesis is the complete knowledge base for building the final protocol document. Every section traces to at least one research file. Corrections from verification/corrections.md are applied inline — do not use the original research files for the specific numbers that were corrected here.

The synthesis is organized as a coherent workflow narrative:

1. Equipment
2. Photography station setup
3. Grader calibration
4. Photography protocol
5. Defect creation and severity thresholds
6. Compound defect specimens
7. Statistical design and allocation
8. Annotation
9. Quality checkpoints
10. Open questions requiring physical experimentation

---

## Part 1: Equipment

### 1.1 Camera Equipment

**Primary camera**: iPhone main (1x) lens for all full-cover shots. Minimum working distance: 25 cm. Optimal range: 25–35 cm. Do not use ultra-wide (macro) for full-cover shots — barrel distortion mimics warping defects and will create false positives.

**Detail shots**: iPhone ultra-wide (macro) at 8–15 cm for close-up defect documentation. Enable Lens Correction (Settings → Camera → Lens Correction) to reduce barrel distortion. Position defect at image center, not at corners.

**Camera settings**:
- Format: HEIF Max (48MP). Sufficient for AI analysis at 1568px. ProRAW not required unless you intend to revisit the dataset with future models — the bit-depth advantage is irrelevant to the vision API.
- Deep Fusion: leave active (default). Enhances paper surface texture and fine defect visibility.
- Smart HDR: leave active. Helpful for dynamic range on covers with dark and light areas.
- AE/AF Lock: tap and hold the comic surface until "AE/AF LOCK" banner appears. Required for multi-shot sequences — the iPhone will otherwise auto-brighten raking-light shots and destroy shadow contrast.

**Sources**: photography-science.md §3.1, §3.2, §3.3, §3.4

---

### 1.2 Lighting Equipment

**Standard diffuse lighting (Shot 1)**:
- Two LED panels at 45° from left and right sides. Daylight-balanced (5500–6500K). Consumer LED desk lamps with flexible gooseneck arms work.
- Never use a single off-axis LED for standard shots — creates glare hotspots that mimic stains.

**Raking light (Shots 2 and 3)**:
- One LED panel with a narrow output. Barn doors, a focused beam, or a shop LED strip taped to a cardboard shield all work.
- One light stand or stack of books to position light at table edge, angled 10–15° from the comic surface.
- Single-sided only. Never add a second raking light on the opposite side — shadows are the signal; fill-in destroys them.

**Background**: Matte black foam board or black velvet cloth. Velvet is preferred for raking shots (maximum light absorption). Rigid foam board is better for standard shots (stays flat). Maintain at least 20 cm between comic edges and background edges to prevent background from entering the light field and reflecting light back onto the cover.

**Color temperature verification**: Shoot a white card under the same LED setup before the first session. If paper looks orange or warm, use a different LED or set a custom white balance. Warm color cast mimics age tanning.

**Sources**: photography-science.md §2.1, §2.2, §4.1, §6.1–6.5; defect-creation.md §8

---

### 1.3 Grading Tools

| Tool | Purpose | Spec |
|---|---|---|
| Desk lamp with flexible neck | Defect inspection at multiple angles | Daylight bulb, minimum 600 lm |
| 10x–12x loupe or magnifying glass | Close defect inspection | Any quality loupe; 10x standard |
| Steel ruler (metric, 30 cm) | Measuring crease length, spine splits | Stainless steel, 1mm graduations |
| Calipers | Corner blunting measurement, tear length | Digital preferred, 0.1mm resolution |
| Cotton gloves | Handling without fingerprint transfer | Standard archival gloves |
| UV/black light | Restoration detection (not condition grading per se) | 365nm UV LED is sufficient |
| Laminated defect reference card | Quick defect/threshold lookup during grading | Print from protocol document |

**Sources**: grading-calibration.md §6.1; severity-spectrum.md §5.1

---

### 1.4 Defect Creation Tools

| Tool | Purpose |
|---|---|
| Bone folder | Creases (subscription, reader crease, spine roll) |
| Steel ruler | Fold guides; straight tears |
| Metal tweezers | Initiating controlled minor tears |
| Sharp scissors | Controlled-length tears, corner chips |
| Scalpel or craft knife | Slices; fine-controlled incisions |
| Fine-grit sandpaper (220, 400 grit) | Corner wear, fraying |
| Eyedropper | Water stains, coffee/tea stains |
| Fine artist brush | Minor stain spots |
| Distilled water | Water stains (tap water adds mineral residue) |
| Coffee or tea (diluted) | Moderate/major stains |
| Scotch tape (3M Magic) | Substance/tape defects |
| Safety glasses + gloves | Required for FeSO₄ foxing simulation (Option A) |

**Sources**: defect-creation.md §2.2–8.2; severity-spectrum.md §3.1–3.6; verification/corrections.md Correction 2

---

## Part 2: Photography Station Setup

### 2.1 Station Layout

The photography station handles three shot types: standard diffuse, raking left, and raking top. A fourth macro shot is done with a repositioned iPhone. All shots use a fixed overhead camera position.

**Setup**:
1. Place matte black foam board flat on a desk (30×40 cm minimum, larger is better).
2. Mount iPhone directly overhead on a copy stand, tripod, or stable book stack so the comic fills roughly 80% of the frame at 25–35 cm height. Confirm perpendicularity by checking that all four corners of the comic are equidistant from frame edges.
3. For Shot 1 (standard): Place two LED panels at 45° from the left and right edges, equidistant, at the same height as the comic surface (not angled downward). Equidistant placement cancels specular hotspots.
4. For Shot 2 (raking left): Remove right LED. Position left LED at table edge, aimed horizontally across the comic at 10–15° above the surface plane. Light travels right across the cover.
5. For Shot 3 (raking top): Move LED to top edge, aimed downward across the comic at 10–15° above the surface plane. Light travels downward across the cover.
6. For Shot 4 (macro detail): Switch to ultra-wide camera. Hold or mount iPhone 8–15 cm above the primary defect area. Use the same 45° diffuse lighting from Shot 1.

**Critical calibration for raking angle**: Practical test — hold a flashlight 30–40 cm from the comic at roughly table level (10° elevation) and scan across the cover. Creases and rolls become immediately visible as dark shadows. This is the correct working angle. Too steep (>20°) washes out subtle defects; too shallow (<5°) requires impractically long light source distance.

**Sources**: photography-science.md §2.1, §2.4, §5.1; brief.md (budget constraint: no custom equipment)

---

### 2.2 Glossy Cover Management

Glossy covers (post-1990) produce specular hotspots that can be mistaken by AI for stains or discoloration. Two management strategies:

**Angle management (no cost)**: With the camera overhead at 90° and light at 45°, specular reflection goes at 45° away from camera — not into the lens. This is already handled by the standard 45° two-light setup if done correctly.

**Cross-polarization (for problem covers, ~$20–40)**: Polarizing gel sheets on light sources + circular CPL filter on iPhone camera lens eliminates specular reflections entirely. Adds ~10 minutes setup per session. Use only for covers where glare was visible in Shot 1 review. Do NOT use cross-polarization for raking shots — it reduces shadow contrast and defeats the topographic detection purpose.

**Sources**: photography-science.md §4.3, §5.2

---

### 2.3 Error Prevention

The following photography errors create false defect signals and must be prevented:

| Error | Mechanism | Prevention |
|---|---|---|
| Single-source glare | Bright oval hotspot mimics stain | Always use two symmetric 45° lights for Shot 1 |
| Shadow edge artifact | Background warp casts fake crease line | Keep foam board rigidly flat; tape down all corners |
| Barrel distortion | Ultra-wide lens makes edges curve, mimicking warping | Only use ultra-wide for detail crops, not full-cover |
| Motion blur | iPhone shake at macro/raking distances creates smear mimicking foxing | Use AE/AF Lock + 2-second timer; keep ISO <400 |
| Warm color cast | Tungsten light makes white paper look tanned | Daylight (5500–6500K) LEDs only |
| Raking gradient | Bright/dark sides in raking shot look like fading | Label raking shots explicitly in metadata; never use as color reference |

**Sources**: photography-science.md §6.1–6.6

---

## Part 3: Grader Calibration

### 3.1 The Calibration Problem

Two non-professional graders can achieve ICC ≥ 0.75 ("good" inter-rater reliability per Koo & Mae 2016) with structured preparation. The primary failure mode is upward bias — inexperienced graders routinely grade 1–2 full categories higher than professionals. Every calibration exercise must counteract this.

The correct ICC model for Sean and Marcus as the two fixed raters of interest: **ICC(3,1)** — Two-Way Mixed-Effects, Absolute Agreement, Single Measures.

**Sources**: grading-calibration.md §3.1, §5.1

---

### 3.2 Pre-Study Materials (Phase 0, ~4–6 hours each, independent)

In priority order:

1. **CGC Grader Notes Guide** (free, cgcgrading.com): Full walk-through of all 109 defect types across 7 categories. Study the photographs. This is the canonical vocabulary reference.
2. **Udemy course "Learn to Grade Comic Books"** (~$15–20 on sale, ~8 hours): 27 actual CGC-graded comics at every grade level 0.1–10.0. Use 1.5x speed.
3. **Overstreet grade boundary definitions** (overstreetaccess.com/grading-definitions/): Measurable physical criteria per grade boundary. The 9.4 vs. 9.0 boundary (most commercially important) and the 8.0 vs. 7.5 boundary should be memorized.
4. **Personal defect checklist**: Compile a laminated card listing the 7 defect categories and the boundary measurements for each major grade transition. Use the thresholds in Part 5 of this synthesis.

**Sources**: grading-calibration.md §1.1–1.3

---

### 3.3 Grade Boundary Reference (Key Transitions)

| Grade | Name | Crease Max | Bend Max | Corner | Spine |
|---|---|---|---|---|---|
| 9.8 | NM/M | None | ≤1/8" invisible straight-on | Sharp | ≤2 minor stress ticks |
| 9.4 | NM | None | ≤1/16" no color break | Sharp, ever-so-slight blunting | Minor stress ok |
| 9.0 | VF/NM | None | ≤1/8" no color break | ~9.4 level | Minor stress |
| 8.5 | VF+ | Minor creases ≤3" no color break | — | Slight blunting | Slight roll ok |
| 8.0 | VF | Color break ≤1/4" | — | Minute wear, blunted | Moderate stress |
| 7.0 | FN/VF | Moderate color-break creases | — | Slight blunting | Possible 1/4" spine split |
| 6.0 | FN | 1/4" spine split | — | More blunting | Visible roll |
| 4.0 | VG | Multiple moderate defects | — | May have small missing piece | Detachment at 1 staple possible |
| 0.5 | Poor | Severe structural damage | — | — | Possible missing pages |

**Sources**: grading-calibration.md §2.1–2.2; severity-spectrum.md §1.1

---

### 3.4 Calibration Session Protocol (Phases 1–2)

**Phase 1: Anchor Calibration (3 hours, both graders together)**

1. Select 10–15 anchor comics spanning the full range: one each in NM, VF, FN, VG, GD, PR categories. Use the most visually clear examples — no borderline cases in Phase 1.
2. Grade each independently. Write grade down. Reveal simultaneously (not sequentially — prevents anchoring bias).
3. For every comic with ≥0.5 point disagreement: identify specific defects, compare defect lists, measure dimensions with ruler/calipers, reach consensus, write a decision rule for that defect class.
4. Anti-bias rule: grade before looking up any price information. Cover the comic title during calibration exercises (reduces familiarity/key issue bias).

**Phase 2: Progressive Calibration (2 hours, both graders together)**

- Round A: 10 extreme-case comics (obvious 9.8 vs. obvious 2.0). Builds shared vocabulary.
- Round B: 10 moderate-case comics in VF range (7.5–8.5). This is where most disagreement surfaces.
- Round C: 10 deliberate boundary pairs — a 9.4 vs. 9.0 pair, 8.5 vs. 8.0 pair, 7.0 vs. 6.5 pair.
- After each round: compute percent agreement (within 0.5 = agreement). If <80%, revisit decision rules.

**Phase 3: Blind Production Grading (both graders independently)**

Grade all 70 comics independently. Record grade on paper before any discussion. Never announce a grade verbally during a session before the other person has written theirs. After all 70 are complete: reveal, compute ICC.

**Sources**: grading-calibration.md §4.2

---

### 3.5 Grading Session Design

- Block size: 20–25 comics per 90-minute session. Break for 15 minutes between blocks.
- Spread across 3–4 sessions over 2–3 days; do not marathon in one day.
- Grade in random order. Do not sort by condition — creates contrast effects that bias ordinal ratings.
- Grade high-value or ambiguous comics early in each session, not late.
- Recording form fields per comic: Comic ID (not title), first-impression grade range, defects noted with location and measurement, final grade, confidence (1–5), borderline flag (yes/no).

**Sources**: grading-calibration.md §3.6, §6.2–6.4

---

### 3.6 Examination Sequence (Per Comic)

1. **First impression** (5 seconds, book closed): Set preliminary grade range.
2. **Cover examination** (30–60 seconds): Front cover at multiple angles — check gloss, stains, creases, tears. Spine: ticks, stress lines, roll, color breaks at staples. Corners: sharp (NM) vs. rounded (VG range). Back cover: same.
3. **Spine and staple inspection** (15–30 seconds): Measure any splits. Check staple rust, tears, detachment.
4. **Interior examination** (30–60 seconds): Page color (white → cream → off-white → tan → brown = NM → VF → FN/VG → low). Brittleness (any = ≤1.8). Centerfold attachment. Writing, stamps, water damage.
5. **Grade assignment**: Start from the ceiling (what does this look like at first glance?), then work down by defect. Worst single defect determines the ceiling. Accumulation of smaller defects can push grade further below the ceiling.
6. **Record** before any discussion.

**Sources**: grading-calibration.md §6.2

---

### 3.7 Anti-Bias Checklist

| Bias | Mechanism | Prevention |
|---|---|---|
| Upward bias | Wishful thinking inflates grade 1–2 categories | Grade before checking price; ask "what would CGC grade this?" not "what would I like this to be?" |
| Anchoring | Second grade anchors to first | Reveal grades simultaneously, never sequentially |
| Age/vintage | Loose standards for older comics | No special allowances for era — CGC scale is uniform |
| Key issue | High-value books graded higher | Remove price guides; randomize order; cover title |
| Session fatigue | Accuracy degrades after 90 min | 20–25 comic blocks; break between blocks |
| Contrast effects | Extreme book makes adjacent book look different | Random grading order; never sort before grading |

**Sources**: grading-calibration.md §3.1–3.7

---

### 3.8 ICC Computation

```python
import pingouin as pg
import pandas as pd

data = pd.DataFrame({
    'Subject': list(range(70)) * 2,
    'Rater': ['Sean'] * 70 + ['Marcus'] * 70,
    'Score': sean_grades + marcus_grades
})

result = pg.intraclass_corr(
    data=data, targets='Subject', raters='Rater',
    ratings='Score', nan_policy='omit'
)
icc31 = result[result['Type'] == 'ICC3']
print(icc31[['ICC', 'CI95%', 'pval']])  # Always report the CI, not just the point estimate
```

**Thresholds**: ICC ≥ 0.90 = excellent (proceed); 0.75–0.90 = good (proceed); 0.60–0.74 = moderate (add calibration round); <0.60 = poor (full recalibration required).

If ICC < 0.75: plot Sean vs. Marcus grades. Identify systematic offset vs. fan-shaped scatter vs. range-specific disagreement. The diagnostic, not blanket re-grading, is the correct response.

**Sources**: grading-calibration.md §5.1–5.5

---

## Part 4: Photography Protocol

### 4.1 Four-Shot Protocol (Per Comic)

| Shot | Lighting | Camera | Purpose | Defects Captured |
|---|---|---|---|---|
| 1 — Standard | 2× LED at 45° symmetric | Main (1x), 25–35 cm | Color reference, stains, overall condition | Stains, foxing, tanning, color rubs, ink loss |
| 2 — Raking Left | 1× LED at 10–15° from left edge | Main (1x), same height | Topographic detection | Creases, bends, stress lines, cockling, spine roll, dimples |
| 3 — Raking Top | 1× LED at 10–15° from top edge | Main (1x), same height | Orthogonal topographic detection | Horizontal creases, spine roll, corner folds missed by Shot 2 |
| 4 — Detail | 2× LED at 45° diffuse | Macro (ultra-wide), 8–15 cm | Fine structure of primary defect | Staple damage, spine stress granularity, corner blunting detail |

**Mandatory**: Shots 1, 2, and 3.  
**Strong recommendation**: Shot 4 for any comic with a known or suspected defect.  
**Optional** (time permitting): Shot 5 (spine detail at 45°), Shot 6 (back cover), Shot 7 (interior pages for water damage and tanning).

**Why two raking directions**: Surface features aligned with one light direction cast no shadow and are missed. Left-raking captures vertically-oriented features (creases perpendicular to spine, corner damage on left/right). Top-raking captures horizontally-oriented features (spine roll, reader crease lines, bottom-edge damage). Both directions required for comprehensive topographic detection.

**Sources**: photography-science.md §5.1, §2.1; grading-calibration.md §6.1

---

### 4.2 Defects Only Visible Under Raking Light

The following defects are routinely missed under standard diffuse lighting and will not be captured without a raking shot:

| Defect | Why Raking Reveals It |
|---|---|
| Light bends (non-color-breaking) | Purely topographic — no ink change to detect |
| Spine stress lines | Sub-mm surface undulation |
| Cockling / waviness | Low-amplitude undulation invisible face-on |
| Finger creases | Small crescent deformations, no color break on glossy |
| Reader creases (early stage) | Pre-ink-crack fold |
| Dimples and impressions | Point deformations from storage pressure |
| Cover undulation / roll | Broad low-amplitude warp invisible face-on |
| Subscription crease (pressed) | Fiber memory remains after pressing |

**Implication for dataset labeling**: If a defect is only visible in Shot 2 or Shot 3 (not Shot 1), annotate it as "raking-only visible." This flags potential AI detection challenges.

**Sources**: photography-science.md §2.3

---

### 4.3 Three-Condition Photography Strategy

Each comic should be photographed in all three image conditions. This is the highest-ROI action for statistical coverage given the fixed physical collection:

| Condition | Method | Purpose |
|---|---|---|
| Scan | Flatbed scanner (if available) | Clean, artifact-free reference; no lighting artifacts |
| Table (controlled) | Full 4-shot protocol as above | Primary dataset condition |
| Handheld | iPhone handheld, 45° ambient room light | Simulates real-world AI use |

This creates 70 × 3 = 210 images for the overall accuracy CI.

**Effective CI after clustering correction**: With within-comic ICC_within ≈ 0.70, design effect DEFF = 2.4, effective N = 87.5 → **corrected CI ≈ ±7.5pp** (not ±4.8pp as the unclustered calculation suggests). [Correction 1 from verification/corrections.md]

The three conditions are most valuable for measuring image-source effects (scan vs. controlled vs. handheld accuracy comparison), not for naive N inflation. The within-comic paired design gives full power for the source-effect comparison.

**Sources**: statistical-design.md §4; verification/corrections.md Correction 1

---

## Part 5: Defect Creation and Severity Thresholds

### 5.1 CGC Defect System Overview

CGC identifies 109 distinct defects across 7 categories: Crease, Distortion, Missing Part, Stain, Substance, Tanning, Tear. The three severity tiers (green/yellow/red) map to the penalty system. Every defect creation procedure must target a specific tier, not just "damage this comic."

**The universal dividing line**: The fiber-breakage threshold separates severity tiers for all fold-type defects.
- Bend (no fiber break) → reversible → Green (minor)
- Crease (fiber break, no color loss) → permanent → Yellow (moderate)
- Crease with color break (fiber break + ink loss) → irreversible → Red (major)

**Sources**: severity-spectrum.md §1.2; defect-creation.md §2.1

---

### 5.2 Tear Threshold Discrepancy — Resolved

**The conflict**: severity-spectrum.md states minor tear = ≤1/8" (3mm); defect-creation.md states minor tear = <1/4" (6mm).

**Resolution** (from verification/corrections.md Correction 3): Both are correct in context. The ≤1/8" threshold is the high-grade context boundary (9.0+), where bindery tear allowances define the minimum identifiable minor tear. The 1/4" threshold is appropriate in mid-grade context (FN/VF, 6.0–8.0) where larger minor tears are tolerated.

**Protocol rule**: **severity-spectrum.md is authoritative for specimen creation**. Use ≤1/8" as the minor tear threshold. When creating specimens targeting FN/VF grade range, note that the minor/moderate boundary shifts upward to 1/4". Label specimens with both the tear length measurement and the target grade range.

**Sources**: verification/corrections.md Correction 3; severity-spectrum.md §2.4; defect-creation.md §5.1

---

### 5.3 Crease Severity Thresholds

**Note on the ≤1/4" key threshold**: The "≤1/4" without color break = green" figure in severity-spectrum.md is the Overstreet 8.0 VF boundary criterion, not a universal ceiling on minor crease length. Minor creases can extend up to 2" without color break and remain green tier at grades below 8.0. [Correction 4 from verification/corrections.md]

| Tier | Criteria | Measurement | Grade Equivalent |
|---|---|---|---|
| Minor (green) | No color break | Length ≤2", width <0.5mm | 8.0–9.2 |
| Moderate (yellow) | Short crease with partial color break | ≤2" length, color break along ~50% | 7.0–7.5 |
| Major (red) | Full color-break crease | >2" long OR full color-break line | Below 7.0, often 4.0–6.0 |

**Grade-anchored thresholds from Overstreet**:
- 9.4 NM: 1/16" bend permitted, no color break (bend, not crease)
- 9.0 VF/NM: 1/8" bend allowed, no color break
- 8.0 VF: 1/4" crease acceptable, no color break (green/yellow boundary at this grade)
- Subscription crease full-height color-breaking: 5.5 or lower (definitive major/red)

**Physical creation**:
- Minor: Fold cover 5–10°, no rubbing. One light bone folder pass with minimal pressure. Success rate ~50% (glossy), ~30% (newsprint).
- Moderate: Fold 30–45°, one firm bone folder pass. White line visible along ~50% of crease length. Success rate ~70%.
- Major: Fold near-90°, two hard bone folder passes. Full white line. Success rate ~90%.

**Paper type effect**: Brittle/aged newsprint — do not attempt minor severity creation. Even careful technique produces moderate due to material fragility.

**Sources**: severity-spectrum.md §2.1; defect-creation.md §2.2; severity-spectrum.md §3.1; grading-calibration.md §2.1; verification/corrections.md Correction 4

---

### 5.4 Spine Roll Severity Thresholds

| Tier | Visual Test | Width Measurement | Grade Equivalent |
|---|---|---|---|
| Minor (green) | Spine edge lifts slightly; book nearly lies flat | Roll width <1/4" | 7.0–8.5 |
| Moderate (yellow) | Cover arches noticeably; back cover fanning visible | Roll width 1/4"–1" | 6.0–8.0 |
| Major (red) | Book cannot lie flat; fanning along full left edge | Roll width >1" | Below 6.0, down to 4.0 |

**Visual test for quick classification**: Lay book flat on table. If spine edge lifts >0.5mm: minor. If cover noticeably arches: moderate. If book cannot lie flat without manual pressure: major.

**Physical creation**:
- Minor: Open book fully flat (180°), gently roll spine edge backward 15–20°, release immediately. Repeat 3–5 times. Check: spine edge barely lifts. Success rate ~40%.
- Moderate: Hold comic one-handed, fan pages behind spine, read through 3–4 times with moderate backward curl. Success rate ~75%.
- Major: Press pages into tight curl around spine, hold 30–60 seconds, repeat through full book. Success rate ~90%.

**Warning on brittle paper**: Attempting major spine roll on brittle comics may produce spine split instead. Monitor progression.

**Sources**: severity-spectrum.md §2.2; defect-creation.md §2.2; severity-spectrum.md §3.2

---

### 5.5 Blunted Corner Severity Thresholds

| Tier | Visual Description | Measurement | Grade Equivalent |
|---|---|---|---|
| Minor (green) | Imperceptibly blunted, still nearly sharp | Flat section <1mm at corner tip | 9.4–9.6 |
| Moderate (yellow) | Visible flat section, color break possible | Flat section 1–3mm, corner angle clearly >90° | 8.0–9.2 |
| Major (red) | Substantially blunted, beginning to round, color break | Flat section >3mm OR rounded arc starting | Below 8.0, down to 6.0 |

**Grade-anchored thresholds from Overstreet**:
- 9.6 NM+: "One corner may be almost imperceptibly blunted"
- 9.4 NM: "Corners cut square and sharp with ever-so-slight blunting permitted"
- 8.0 VF: "Minute wear at corners; blunted or abraded corners"
- 3.0 GD/VG: "Corners may be blunted or even rounded"

**Physical creation**: Minor corner blunting is very difficult to create reliably by impact (even a light 2-inch drop produces more than imperceptible blunting). For minor specimens, use naturally worn high-grade comics rather than creating artificially. For moderate: drop corner 4–6 inches onto hard surface, examine. For major: 8–10 inch drop or sandpaper abrasion (40+ passes, 400-grit). Abrasion technique with 400-grit sandpaper is more controllable than impact for all severities.

**Sources**: severity-spectrum.md §2.3; defect-creation.md §2.2; severity-spectrum.md §3.3

---

### 5.6 Tear Severity Thresholds

(Using high-grade thresholds as the protocol standard; adjust labeling for mid-grade context — see §5.2 above)

| Tier | Visual Description | Size | Grade Equivalent |
|---|---|---|---|
| Minor (green) | Small edge tear, not entering image area | Length ≤1/8" (3mm) | 9.0–9.4 |
| Moderate (yellow) | Tear entering cover, visible from front | Length 1/8"–3/4" (3–19mm) | 7.5–8.5 |
| Major (red) | Long tear crossing image, or triangular loss | Length >3/4" OR triangle missing >1/4" | Below 7.5, down to 4.0 |

**Hard-capped tear types**: Detached cover caps grade at 4.0. Fully split spine + detachment caps at 1.8.

**Physical creation**:
- Minor: Needle or fine tweezers at edge, create 1–2mm nick. Stop immediately. Control propagation with both thumbs. Success rate ~60%.
- Moderate: Metal ruler guide, allow propagation to 6–15mm at 45–60° angle. Success rate ~70%.
- Major: Deliberate propagation to ¾"–1"+. For triangular loss: two converging scissors cuts, pull triangle free. Success rate ~95%.

**Most controllable technique**: Scissors-initiated tears of exact length followed by manual opening for natural appearance. This allows exact length control.

**Sources**: severity-spectrum.md §2.4; defect-creation.md §5.2; severity-spectrum.md §3.4

---

### 5.7 Stain Severity Thresholds

| Tier | Visual Description | Size/Coverage | Grade Equivalent |
|---|---|---|---|
| Minor (green) | Light mark, barely noticeable at arm's length, no prominent tide line | Diameter ≤5mm | 8.5–9.4 |
| Moderate (yellow) | Visible discoloration, tide line present, single area | Diameter 5–25mm OR tide line ≤1" perimeter | 7.0–8.5 |
| Major (red) | Dark stain, obvious at arm's length, spread to multiple areas | >25mm OR multiple areas OR foxing cluster | Below 7.0, down to 4.0 |

**Physical creation**:
- Minor: Fine artist brush, barely damp. Touch once to surface. On glossy: faint ring ~3–5mm. Success rate ~65% (glossy), ~35% (newsprint).
- Moderate: Eyedropper, 1–2 drops. Allow to spread naturally. For colored: 10:1 water:coffee dilution. Success rate ~75%.
- Major: 5–10 drops across 25–40mm area. Colored: undiluted coffee or tea. Success rate ~90%.

**Always use distilled water** (not tap). Tap water leaves mineral residue that adds an unintended whitish ring separate from the tide line.

**Paper type effect**: Glossy covers bead liquid; stain is primarily a tide line. Newsprint absorbs immediately — stain spreads beyond target area very quickly. On matte or newsprint, reduce drop size by half versus the glossy target amount.

**Sources**: severity-spectrum.md §2.5; defect-creation.md §4.2; severity-spectrum.md §3.5

---

### 5.8 Spine Stress Severity Thresholds

| Tier | Visual Description | Count/Length | Grade Equivalent |
|---|---|---|---|
| Minor (green) | 1–3 stress lines, no color break, raking-light only | Count ≤3, each <1/4" long | 9.4–9.6 |
| Moderate (yellow) | 4–5 stress lines OR 1–3 with color break | Count 4–5 OR color-breaking; each <1" | 9.0–9.4 |
| Major (red) | Numerous lines, many with color break, OR any >1" (reclassifies as crease) | Count >5 with color break OR length >1" | Below 9.0, down to 8.0 |

**Critical rule**: Stress lines >1" long are reclassified by CGC as creases, not spine stress. Standard stress lines are "usually less than 1/4 inch long perpendicular to spine."

**Physical creation**:
- Minor: Open comic fully flat (180°). Apply 2–3° additional pressure at 2–3 locations, release immediately. Examine under raking light. 1–3 small white ticks visible. Success rate ~70%.
- Moderate: Open 5–7° past flat at multiple points. Repeat 4–5 times. Success rate ~75%.
- Major: Open forcefully past 180°, work through entire book. Many white ticks visible from front. Success rate ~85%.

**Angle control is critical**: 180° = minor bend. 185–190° = likely color break (moderate). Excess opening angle and held pressure jump to major.

**Sources**: severity-spectrum.md §2.6; defect-creation.md §2.2; severity-spectrum.md §3.6

---

### 5.9 Defect Creation Reproducibility Summary

| Defect | Min Target | Med Target | Maj Target | Notes |
|---|---|---|---|---|
| Crease | ~50% (glossy) | ~70% | ~90% | Brittle paper: skip minor; go to moderate |
| Spine roll | ~40% | ~75% | ~90% | Hard to stop at minor |
| Blunted corner | ~35% | ~65% | ~85% | Use sandpaper over impact for control |
| Tear | ~60% | ~70% | ~95% | Scissors initiation is most controllable |
| Stain (water) | ~65% (glossy) | ~75% | ~90% | Halve drop size for newsprint/matte |
| Spine stress | ~70% | ~75% | ~85% | Angle control is the key variable |

**General rule**: Always create specimens on control comics first to calibrate technique before working on the dataset specimen. Plan for 1.5–2× the needed attempts for minor severity specimens.

**Sources**: severity-spectrum.md §3; defect-creation.md §9 (Reproducibility Summary)

---

### 5.10 Paper Type Reference

| Paper Era | Crease Threshold | Tear Risk | Stain Behavior | Implication |
|---|---|---|---|---|
| Golden/Silver Age newsprint (pre-1970) | Very low; any fold = crease | Tear propagates explosively | Immediate full absorption; no tide line | Skip minor creation; use natural specimens |
| Bronze/Copper (~1970–1990) | Moderate | Moderate | Mixed absorption | Can attempt minor with care; test first |
| Modern glossy (post-1990) | Sharp; fold must exceed ~20° to break | Moderate, somewhat controllable | Beads; creates clean tide line | Best for controlled specimens |

**Key implication for dataset**: Controlled severity specimens should be created on modern glossy stock comics unless specifically targeting vintage newsprint defect appearance. For aged paper specimens, manage expectations downward — the same technique that produces minor on modern paper produces moderate on vintage newsprint.

**Sources**: severity-spectrum.md §4; defect-creation.md §10 (Paper Type Considerations)

---

## Part 6: Compound Defect Specimens

### 6.1 Why Compound Specimens Are the Highest-Value Specimens

Compound specimens test the algorithm's interaction logic — cap selection, diminishing returns, area weighting, minor-only cap — simultaneously. Single-defect specimens only verify one code path. A compound specimen generates 4+ distinct test assertions per comic. Under D-optimal design logic, compound specimens yield the highest information per physical specimen when total specimen count is fixed.

**Sources**: statistical-design.md §1; compound-defects.md Executive Summary

---

### 6.2 Algorithm Mechanics Being Tested

Before the specimen list, understand the three compound interaction types:

**Cap interaction (lowest cap wins)**: When multiple defects are present, the effective grade ceiling is the lowest cap across all defects. This is an upper bound, not a target grade — accumulated penalties can push the grade below the cap.

**Diminishing returns**: When the same keyword (defect type) appears multiple times, the 2nd instance carries 50% penalty weight, the 3rd and beyond carry 25%. This only applies to the same keyword — different defect types (e.g., soiling vs. tanning vs. corner wear) each receive full first-instance penalty even when all present simultaneously.

**Minor-only cap**: When all defects are minor severity, total penalty is capped at -0.3 regardless of count. This cap fails (does not apply) the moment any defect is moderate or major.

**Sources**: compound-defects.md §1, §2, §3

---

### 6.3 Six Prioritized Compound Specimens

Listed in priority order by: (1) likelihood of AI error, (2) algorithmic properties tested, (3) feasibility of controlled creation.

---

**Specimen C-1: Storage Degradation Cluster** (Priority 1)

- **Defects**: Minor-to-moderate soiling (cover) + light tanning (pages) + blunted corners (2–3 corners)
- **Expected grade**: 7.0–8.0 depending on severity
- **Algorithm property tested**: Penalty accumulation across different defect types with the same cap (all three cap at 9.0); no diminishing returns apply across different keywords
- **AI failure mode**: Applies diminishing returns incorrectly across soiling/tanning/corner wear; or misidentifies tanning as a more severe stain type
- **Creation**: Expose comic to damp cardboard environment (sealed bag with damp sponge, 48h) for tanning; stack under weight for corners; graphite smear on cover margins for soiling
- **Why it's priority 1**: Most common real-world compound pattern; the AI encounters this frequently in actual grading submissions

---

**Specimen C-2: Minor-Only Cap Test** (Priority 2)

- **Defects**: 5–6 minor defects — 2 minor creases, minor foxing (2–3 spots), minor soiling, minor stress lines (2–3)
- **Expected grade**: 8.5 (model 9.0, minor-only cap → -0.3 → 8.7 → snapped to 8.5)
- **Algorithm property tested**: Minor-only cap (-0.3 total) is the binding constraint, not individual penalties
- **AI failure mode**: Reports one defect as moderate → kills the cap → grade drops to 7.5–8.0 instead of 8.5
- **Creation**: Light spine flexes for stress lines; fine brush water touch for foxing simulation; light graphite smear for soiling; minimal bone folder pass for minor crease
- **Critical**: This is the most algorithmically unusual rule in the system. The counter-intuitive result (10 minor defects grades the same as 3 minor defects) is what this specimen validates.

---

**Specimen C-3: Water Damage + Tape Repair** (Priority 3)

- **Defects**: Moderate water damage (corner or bottom edge) + tape repair applied over the damaged area
- **Expected grade**: 6.0 (water damage cap 6.0 dominates over tape cap 7.0)
- **Algorithm property tested**: Lowest cap wins; CGC functional-tape policy (2013: tape ignored if it serves a repair function, underlying defect fully scored)
- **AI failure mode 1**: Applies tape cap (7.0) instead of water damage cap (6.0) → 1 grade point too high
- **AI failure mode 2**: Double-penalizes tape + water damage when CGC policy would only penalize the water damage (known algorithm deviation — document this as expected difference, not AI error)
- **Creation**: Apply water to a corner, let dry/warp, then apply Scotch tape over the water-damaged area. Easy to create; high reproducibility.

---

**Specimen C-4: Same Defect, Multiple Locations (Diminishing Returns)** (Priority 4)

- **Defects**: Three moderate creases at different zones (top-right corner, cover center, bottom edge) — all described as "crease"
- **Expected grade**: 7.5 (with diminishing returns) vs. 7.0 (without)
- **Algorithm property tested**: Diminishing returns (2nd = 50%, 3rd = 25%) for same keyword across locations
- **AI failure mode 1**: Uses varying vocabulary for the creases ("fold," "bend," "crease") → keyword mismatch → diminishing returns not applied
- **AI failure mode 2**: Reports creases as minor instead of moderate → minor-only cap triggers → masks the diminishing-returns mechanism
- **Creation**: Three controlled diagonal creases using bone folder at specified zones. Moderate difficulty.

---

**Specimen C-5: Minor + Major Mix (Minor-Only Cap Should NOT Apply)** (Priority 5)

- **Defects**: Four minor defects (soiling, tanning, minor foxing, minor corner wear) + one major crease (1-inch diagonal through cover center)
- **Expected grade**: 6.0–6.5 (major crease dominates at -1.5 × 1.0 cover area; minor-only cap must NOT apply)
- **Algorithm property tested**: Minor-only cap correctly skipped when any non-minor defect is present
- **AI failure mode**: Rates major crease as moderate → minor-only cap incorrectly applies → grade inflates to 8.5 when correct answer is 6.0 (2.5 grade point error)
- **Creation**: Single large deliberate crease (bone folder, firm pressure, 1+ inch); age other defects separately with minor techniques

---

**Specimen C-6: Structural Failure — Spine Split + Loose Cover** (Priority 6)

- **Defects**: Major spine split (full length) + partially detached cover at one staple
- **Expected grade**: 3.0–4.0 per algorithm (penalty-dominated, not cap-dominated); CGC's documented maximum for full split + detachment is 1.8
- **Algorithm property tested**: Penalty accumulation dominating over cap; exposes calibration gap between algorithm and CGC practice
- **AI failure mode**: Applies detached cover cap (4.0) as the target grade rather than upper bound; reports 4.0 when actual grade should be 2.0–3.0
- **Creation**: Difficult (destructive, permanent, hard to control). Create full spine split first, then progressively open past range until one staple detachment occurs. Monitor carefully. This is LOW-MEDIUM feasibility.
- **Priority 6 rationale**: Important for algorithm validation but destructive creation risk; schedule last, use most damaged existing comic.

**Sources**: compound-defects.md §4; statistical-design.md §1

---

### 6.4 Non-Obvious Grade Interaction: Many Minor vs. One Major

A comic with one major crease (penalty -1.5) grades lower (7.5) than a comic with 10 minor defects (minor-only cap → 8.5). This counter-intuitive result is verified by the algorithm and confirmed by CGC grade-definition language ("accumulation of minor defects OR one or two moderate defects" as equivalent at FN 6.0 — and the algorithm's cap makes accumulation of all-minor defects less damaging than a single major).

The AI may not grasp this. Specimen C-2 (minor-only) and C-5 (minor + major mix) together validate that the AI correctly handles both sides of this interaction.

**Sources**: compound-defects.md §3.1; grading-calibration.md §2.1

---

### 6.5 Known Algorithm Deviations from CGC (Document, Don't "Fix")

**CGC 2013 functional-tape policy**: CGC ignores tape that serves a repair function; only the underlying defect is graded. The algorithm double-penalizes (tape + underlying defect). Specimen C-3 documents this. Expected deviation: ~0.5 grade point lower than CGC would give.

**Spine split + detachment calibration**: The algorithm predicts 3.0–4.0 for major spine split + detachment. CGC's documented maximum for this combination is 1.8. This is a known calibration gap — the algorithm penalty values may be insufficiently aggressive for extreme structural failure. Document this as an open calibration issue, not a test failure.

**Sources**: compound-defects.md §5.3; compound-defects.md §1.4

---

## Part 7: Statistical Design and Allocation

### 7.1 The 70-Comic Allocation

**Corrected effective CI**: The headline number for Phase 1 is approximately ±7.5pp effective CI (not ±4.8pp) due to within-comic clustering across the three photography conditions. Report this number, not the uncorrected Wilson CI. [Correction 1]

| Category | Count | Role |
|---|---|---|
| Baseline (no controlled damage) | 39 | Grade accuracy evaluation; 3-condition photography; 4 serve as ICC anchors |
| Single-defect controlled | 14 | Defect detection coverage — 7 priority types, 2 per category |
| Severity-spectrum | 9 | 3 severity levels × 3 defect types |
| Compound-defect | 8 | Multi-defect interaction tests (6 priority compounds from §6.3) |
| **Total** | **70** | |

Note: 4 of the 39 baseline comics double as ICC calibration anchors (spanning: near 9.0, near 7.5, near 5.5, near 3.0). They are not a separate physical set. ICC is computed from all 39 double-graded baseline comics.

**Sources**: statistical-design.md §2; verification/corrections.md Correction 1

---

### 7.2 Grade Tier Distribution

| Tier | Grade Range | Comic Count | Images (×3) | Per-Tier CI |
|---|---|---|---|---|
| High | 8.5–10.0 | 15 | 45 | ±10.4pp |
| Mid-High | 7.0–8.4 | 22 | 66 | ±8.6pp |
| Mid-Low | 5.0–6.5 | 18 | 54 | ±9.5pp |
| Low | 2.0–4.5 | 10 | 30 | ±12.7pp |
| Very Low | 0.5–1.8 | 5 | 15 | ±17.6pp |
| **Total** | | **70** | **210** | **±7.5pp effective** |

**Why overweight mid-high (7.0–8.4)**: Neyman optimal allocation assigns more samples to strata with higher within-stratum variance. The 7.0–8.4 range has the highest inter-rater variance — this is where both human and AI graders are most uncertain. Estimated σ_mid-high ≈ 0.50 grade points vs. σ_high ≈ 0.25.

**Very Low (0.5–1.8)**: 5 comics created via controlled severe damage (detached cover, missing pages). Natural very-low acquisition is difficult; controlled creation is practical and documents system behavior on extreme cases.

**Per-tier CIs are wide** (±8–18pp). This is unavoidable at 70 comics. Correct framing: Phase 1 can detect tier-level biases of ≥20pp with reasonable confidence. Biases of 10–15pp are detectable only at the high/mid-high tiers (larger N).

**Sources**: statistical-design.md §3; verification/corrections.md Correction 1

---

### 7.3 Controlled Specimen Allocation by Defect Category

The 23 controlled comics (14 single-defect + 9 severity) concentrate on 4 P0 defect categories:

| Category | Controlled Specimens | Severity Coverage | Specific Types |
|---|---|---|---|
| crease | 6 | 2 minor, 2 moderate, 2 major | Spine roll (3), reader crease (2), subscription crease (1) |
| stain (water) | 5 | 2 minor, 2 moderate, 1 major | Water ring stain (3), soiling (2) |
| tear | 5 | 1 minor, 2 moderate, 2 major | Corner tear (2), spine split (2), detached cover (1) |
| substance (tape) | 4 | 2 minor, 2 moderate | Tape applied (2), tape residue (2) |
| **Total controlled** | **20** | | |

Remaining 3 categories (distortion, missing_part beyond tear, tanning) sourced from natural specimens in the existing worn collection.

**Why these 4 categories**:
- crease: Most common real-world defect; multiple severity levels easy to create
- stain (water): Cap at 6.0; probably undertested; easy to create with eyedropper
- tear (including detached cover): Cap at 4.0; catastrophic grade impact; easily created
- substance (tape): Cap at 7.0; extremely common; easy to create

**Detection power note**: With 5 specimens per category, the CI on recall is ±31pp — statistically indefensible for precision recall claims. The correct goal is catastrophic failure detection (detecting a system that misses 100% of a defect type). With 5 specimens and true recall = 0%, P(detecting the failure) = 1 - 0.95⁵ = 23%. Weak but better than nothing. Phase 1 goal is catastrophic failure ruling-out, not precision recall measurement.

**Sources**: statistical-design.md §5

---

### 7.4 What Phase 1 Can and Cannot Claim

| Claim | Feasible? | Requirement Met? |
|---|---|---|
| Overall accuracy ±7.5pp effective CI | Yes | 70 comics × 3 conditions |
| High vs. low grade tier accuracy bias of ≥20pp | Yes (marginal) | ~15 comics per tier with design effect |
| Defect recall ±15pp CI per category | No | Needs 28 positives per category |
| Detect catastrophic detection failure (0% recall) per category | Yes (~23–30%) | 5–7 specimens per category |
| Severity miscalibration detection | Partial | 3 severity levels × 3 defect types |
| Compound interaction failures | Yes | 6 compound specimens |

**Sources**: statistical-design.md §3, §5, §6a

---

## Part 8: Annotation Protocol

### 8.1 Required Fields Per Comic

Every comic in the dataset requires these fields:

| Field | Format | Notes |
|---|---|---|
| comic_id | String (e.g., COM-001) | Sequential, not title-based (reduces familiarity bias) |
| title | String | For internal reference only; not used in AI input |
| grade_sean | Float (CGC scale: 0.5–10.0) | Before ICC comparison |
| grade_marcus | Float | Before ICC comparison |
| grade_consensus | Float | Post-ICC discussion grade (use for ground truth) |
| grade_confidence | Integer 1–5 | Per grader, per comic |
| grade_borderline | Boolean | Flag for borderline cases |
| defects_noted | Array of defect objects | See below |
| specimen_type | Enum: baseline / single-defect / severity / compound | |
| paper_type | Enum: modern-glossy / bronze-copper / golden-silver-newsprint | |
| photography_conditions | Array: scan / table / handheld | Which conditions completed |
| image_paths | Dict keyed by condition + shot number | |

### 8.2 Defect Object Schema

Per defect:

| Field | Format | Notes |
|---|---|---|
| category | Enum: crease / distortion / missing_part / stain / substance / tanning / tear | CGC 7 categories |
| keyword | String (CGC keyword) | e.g., "spine_roll", "crease", "water_damage", "tape" |
| severity | Enum: minor / moderate / major | green / yellow / red |
| area | Enum: spine / corner_tl / corner_tr / corner_bl / corner_br / edge_top / edge_bottom / edge_right / staple_top / staple_bottom / cover_center / full_cover / pages | 12-zone system |
| measurement | String (e.g., "1.5 inches", "3mm", "0.8cm flat section") | Physical measurement where applicable |
| visible_under | Enum: diffuse / raking / both | Critical for AI photographic analysis |
| created_intentionally | Boolean | True for controlled specimens |
| creation_technique | String | Brief description for controlled specimens |
| notes | String | Edge cases, ambiguities, deviations from expected |

### 8.3 Edge Case Rules

**Borderline severity**: Default to the lower severity tier when borderline. Annotate as borderline in notes. This creates conservative ground truth — better to slightly underpenalize than to overpenalize.

**Tear threshold context**: Label tear measurements in millimeters. Also note whether the specimen is targeting high-grade or mid-grade range, since the minor/moderate boundary shifts from ≤1/8" to ≤1/4" respectively.

**Raking-only defects**: If a defect is visible only in Shot 2 or Shot 3 (not Shot 1), set visible_under = "raking". This is a critical annotation for AI analysis — the model may not detect raking-only defects if only the diffuse shot is provided.

**Compound specimens**: Annotate each defect in the compound independently. Note which cap interaction or algorithm property the compound tests in the specimen-level notes field.

**Tanning source**: For naturally occurring tanning specimens, note the approximate age/era of the comic. Dell comics (1950s–60s) are graded less harshly for inside cover tanning due to known paper composition — annotate this explicitly.

**Sources**: grading-calibration.md §6.4; compound-defects.md §1; defect-creation.md §8.1; verification/corrections.md Correction 3

---

## Part 9: Quality Checkpoints

### 9.1 Pre-Session Checks (Before Each Grading Day)

- [ ] Both graders have completed pre-study materials (Phase 0)
- [ ] Photography station tested with a dummy comic — verify raking shadows appear at 10–15°
- [ ] Color balance verified (white card shot, no warm cast)
- [ ] AE/AF Lock procedure confirmed
- [ ] Grading forms and laminated reference cards printed
- [ ] Comics randomized (not sorted by condition)
- [ ] Equipment: ruler, calipers, loupe, cotton gloves present

---

### 9.2 Per-Specimen Checks (During Defect Creation)

- [ ] Defect type and severity target documented before creation
- [ ] Control comic used for technique test before dataset comic (for any defect type attempted for the first time)
- [ ] Post-creation measurement taken (crease length, tear length, stain diameter, roll width)
- [ ] Compared measurement against severity thresholds in §5.3–5.8
- [ ] If over-severity: flag specimen; do not discard — annotate actual severity achieved
- [ ] Safety protocol for FeSO₄ (if used for foxing): gloves AND safety glasses [Correction 2]

---

### 9.3 Per-Comic Photography Checks

- [ ] Comic lies completely flat on background (no page curl creating shadow)
- [ ] Background material flat — foam board corners taped down
- [ ] No crew shadow visible in frame
- [ ] AE/AF Lock engaged before Shot 2 and 3
- [ ] Shot 1: two symmetric lights, verify no hotspot
- [ ] Shot 2: raking shadow from left visible (quick check before capture)
- [ ] Shot 3: raking shadow from top visible
- [ ] All shot types noted in metadata

---

### 9.4 Post-Grading ICC Verification

- [ ] Both graders have written grades for all 70 comics before any comparison
- [ ] ICC(3,1) computed using pingouin per §3.8
- [ ] 95% CI reported alongside ICC point estimate
- [ ] If ICC ≥ 0.75: proceed
- [ ] If ICC < 0.75: run diagnostic (scatter plot, identify systematic offset vs. range-specific disagreement); do not blanket regrade

---

### 9.5 Dataset Completeness Check

Before declaring the dataset complete:
- [ ] 70 comics graded independently by both graders
- [ ] All 70 photographed in at least Table condition (3 shots minimum)
- [ ] All 70 photographed in all 3 conditions (scan / table / handheld) if feasible
- [ ] 6 compound specimens completed (or documented reason for substitution if C-6 was too destructive)
- [ ] Annotation file has no empty required fields
- [ ] Raking-only defects flagged in annotation
- [ ] Known algorithm deviations documented (functional-tape policy, structural failure calibration gap)

---

## Part 10: Open Questions Requiring Physical Experimentation

These questions cannot be resolved by further desk research. They require physical tests.

1. **UV capture for foxing at AI-detectable severity**: Does UV fluorescence photography add discriminative signal for foxing at the minor-to-moderate severity levels in this dataset, beyond what visible-light raking captures? Test: 3 fox-stained comics, both visible-light diffuse and UV capture, compare AI detection rates. [photography-science.md, Open Q 1]

2. **Optimal raking angle for minor stress lines on modern glossy**: At exactly which angle (10°, 12°, 15°) does a minor stress line first become reliably visible on modern glossy cover stock? The theory says shallower is better for low-relief features, but the practical limit depends on light source distance at tabletop scale. Test: single known-minor-stress comic, photos at 8°, 10°, 12°, 15°, compare AI detection confidence. [photography-science.md, Open Q 4]

3. **Minor corner blunting creation reproducibility**: The 35% success rate estimate for minor corner blunting via impact means significant failure rate. Does the 400-grit sandpaper abrasion technique produce more consistent minor specimens? Test: 10 attempts per technique on identical modern glossy comics, measure flat-section width with calipers after each attempt. [severity-spectrum.md §3.3]

4. **Minor spine roll stopping point**: The ~40% success rate for minor roll creation is problematic for controlled dataset quality. Can the "3–5 very gentle opens to 185°" technique be made more reproducible? Test: 5 attempts per grader, measure roll width after each. May need to accept that minor roll specimens should be sourced naturally rather than created. [severity-spectrum.md §3.2]

5. **Deep Fusion vs. ProRAW for stress line detection**: Does the iPhone Deep Fusion processing help or hurt detection of fine spine stress lines at 1568px resolution? Test: shoot identical raking-light captures in HEIF and ProRAW on a comic with known stress lines, compare AI detection rate. [photography-science.md, Open Q 3]

6. **Oven tanning calibration without climate chamber**: The ISO 5630-3 protocol (80°C, 65% RH) assumes a humidity-controlled chamber. A household oven has poorly calibrated humidity. What duration at 65°C with a cup of water inside the oven produces visible tanning on pre-1980 newsprint? Test: 3 identical newsprint comics, 24h/48h/72h, photograph and compare tanning level. [defect-creation.md §8.2]

7. **Spine split + detachment grade calibration**: The algorithm predicts 3.0–4.0 for major spine split + full detachment; CGC's documented maximum is 1.8. This 1.2–2.0 grade point gap needs real specimen calibration. Test: create Specimen C-6, have both graders grade it, compare result to algorithm output. If gap confirms, flag the structural failure penalty values for future recalibration. [compound-defects.md §1.4]

---

## Cross-Cutting Themes and Integration Points

### Theme 1: Lighting Is the Limiting Variable, Not Resolution

The single most important technical insight from photography-science.md is that **defect visibility is a lighting problem, not a resolution problem**. At 1568px, any remaining resolution is irrelevant — the question is whether the defect casts a detectable shadow or color contrast at all. This has direct implications for the protocol:

- A well-lit image at 1568px detects more defects than a 4K image under wrong lighting.
- The raking shots (Shots 2 and 3) are not optional enhancements — they are the primary detection mechanism for the majority of crease-type defects.
- The 4-shot protocol is not redundancy; each shot captures a non-overlapping defect class.

**Where this intersects with grading**: The grading-calibration.md examination sequence notes that graders "move the book under the lamp at multiple angles" — they are manually performing raking inspection. The photography protocol formalizes this into two fixed raking shots. The AI system must receive both shots to replicate the information available to a human grader.

---

### Theme 2: Severity Thresholds Require Measurement, Not Just Visual Assessment

Every defect type has a physical measurement that anchors the tier boundary. The connection between the grading research and the defect creation research is that **creating a specimen at a target severity tier requires knowing the measurement criterion for that tier**:

- Crease: measure length in mm with ruler; check for color break with loupe
- Tear: measure length in mm before and after each propagation attempt
- Corner blunting: measure flat section width with calipers
- Spine roll: measure roll width by laying book flat and measuring lift height
- Stain: measure diameter; check for tide line visibility
- Spine stress: count lines and measure length with ruler

Without these measurements, a "minor crease" specimen might actually be moderate, contaminating the severity calibration evaluation. Measurement is not optional.

---

### Theme 3: The Algorithm Tests What the Compound Specimens Verify

The compound specimen list in §6.3 was derived directly from analysis of algorithm failure modes in compound-defects.md. The six specimens together test:

- Diminishing returns (C-4)
- Minor-only cap triggering (C-2) and not-triggering (C-5)
- Lowest-cap-wins interaction (C-3)
- Same-type penalty accumulation (C-4)
- Cross-type penalty accumulation (C-1)
- Penalty-dominates-cap scenario (C-6)

Every compound specimen corresponds to a specific algorithm code path. The mapping between specimens and code paths should be documented in the protocol so that when the AI produces an unexpected grade on a compound specimen, the specific algorithm behavior being violated can be identified.

---

### Theme 4: Statistical Limitations Must Be Communicated Clearly

Phase 1 with 70 comics cannot support precision claims. The synthesis of statistical-design.md findings produces three honest framing statements for any publication of Phase 1 results:

1. Overall accuracy is measured to approximately ±7.5pp effective CI (accounting for within-comic clustering across photography conditions).
2. Tier-level accuracy differences smaller than ~20pp cannot be detected with reasonable statistical power.
3. Defect recall is not measurable with precision; Phase 1 results for defect detection can only rule out catastrophic failure (0% recall), not discriminate between 50% and 80% recall.

These limitations do not make Phase 1 valueless — they define the correct scope of its claims.

---

*End of synthesis. All claims traceable to source research files. All corrections from verification/corrections.md applied.*
