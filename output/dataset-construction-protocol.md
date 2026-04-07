# Comic Book Grading Dataset Construction Protocol

**Version**: 1.0  
**Date**: 2026-04-07  
**Team**: Sean May, Marcus Yi  
**Purpose**: Build a 70-comic evaluation dataset for the AI comic book condition grading system

---

## Brief Compliance Summary

| Brief Requirement | What Phase 1 Achieves | Gap / Action |
|---|---|---|
| ±4pp accuracy CI | **±7.5pp effective CI** (achievable) | ±4pp requires ~185 independent comics — not achievable in Phase 1. See §10. |
| 3–4 day execution | **5 working days full / 2 days minimum viable** | 3-condition photography alone is ~28 hours. Full schedule: 5 days. Minimum viable: 2 days. |
| $65–100 equipment budget | **$125–224 all-in; $65–100 minimum viable** | Tiered cut list in §1. Minimum viable omits cross-pol and scanner. |
| Defect recall measurement | **Catastrophic-failure detection only** | 5 specimens/category: if 0/5 detected, rules out recall >45% at 95% confidence. Not precision recall. |

**Phase 1 honest framing**: This is a catastrophic-failure detection and directional-accuracy study, not a precision measurement. It establishes the ±7.5pp baseline and identifies algorithm failures that block production deployment. Precision recall measurement requires Phase 2 (185+ independent comics).

**CGC standards caveat**: All severity thresholds in this protocol are derived from Overstreet Guide descriptions and CGC Grader Notes educational materials — the closest publicly available proxy for CGC practice. CGC does not publish a quantitative grading specification. Ground truth is CGC submission, which is out of scope for Phase 1. Treat all grade-equivalent ranges as approximate (±0.5 grade points).

---

## Schedules

### Minimum Viable Path — 2 Days

Achieves: Grade accuracy CI on 70 baseline comics (table photography only, front cover only). Five key controlled defects. Basic harness run.

Drops: Severity spectrum, compound defects, raking light, 3-condition photography.

| Day | Tasks | Hours |
|---|---|---|
| Day 1 AM | Station setup, color calibration, anchor calibration session (Phases 1–2) | 4 hrs |
| Day 1 PM | Photograph 70 comics, Shot 1 only (standard diffuse, 5 min/comic) | 6 hrs |
| Day 2 AM | Blind grading — both graders independently (70 × 2.5 min, two runs) | 3.5 hrs each |
| Day 2 Mid | ICC computation + disagreement discussion | 1.5 hrs |
| Day 2 PM | Create 5 controlled defects (crease, stain, tear, tape, spine roll — one each) + photograph + annotate | 5 hrs |
| Day 2 EOD | Run harness; review results | 1 hr |

**Total**: ~21 person-hours across 2 days (2 people working simultaneously on joint tasks).

---

### Full Protocol — 5 Days

Achieves: All 70 comics × 3 photography conditions; complete grading calibration; 23 controlled specimens; 6 compound specimens; severity spectrum; full annotation.

**Pre-session dependency (start before Day 1)**: If creating Specimen C-1 (storage degradation cluster), the oven-aging tanning component requires 24–72 hours — start it at least 3 days before Day 3. See §6 Specimen C-1.

| Day | Tasks | Est. Person-Hours |
|---|---|---|
| **Day 1** | Station setup (2 hrs); pre-study materials check; anchor calibration Phase 1–2 (3+2 hrs both together); progressive calibration (2 hrs) | ~9 |
| **Day 2** | 3-condition photography: all 70 comics — table condition (9–10 hrs at practiced pace) | ~9–10 |
| **Day 3** | 3-condition photography: handheld condition (70 × 5 min) + scan condition if scanner available (4 hrs); blind grading 70 comics both independently (3.5 hrs each) | ~11 |
| **Day 4** | ICC computation + discussion (1.5 hrs); controlled defect creation for single-defect and severity specimens (23 specimens, 8–12 hrs including re-attempts and photography) | ~10 |
| **Day 5** | Compound defect specimens C-2 through C-6 (C-1 already aging); annotation for all 70 + 23 + up to 8 compounds (5–8 hrs); quality checkpoint review; harness run | ~8 |

**Total**: ~47–50 person-hours, 5 working days at 8–10 hrs/day between two people.

**Phase 0 (independent, before Day 1)**: Each grader completes pre-study materials (~4–6 hrs, done separately).

---

## Section 1: Equipment List

### Tier 1 — Minimum Viable ($65–80 estimated)

Items you likely already own or can source cheaply. This tier supports the 2-day minimum viable path.

| Item | Purpose | Estimated Cost |
|---|---|---|
| Two LED desk lamps with flexible gooseneck, daylight bulb (5500–6500K) | Standard diffuse + raking lighting | $15–30 each = $30–60 |
| Matte black foam board (30×40 cm or larger, rigid) | Photo background | $5–10 |
| Phone tripod or stable book stack for overhead mounting | Overhead camera position | $0–15 (books = free) |
| Steel ruler, metric, 30 cm, 1mm graduations | Crease/tear measurement; fold guide | $5–8 |
| Cotton gloves (archival) | No fingerprint transfer during handling | $5–8 |
| Fine-grit sandpaper (220-grit and 400-grit sheets) | Corner wear creation | $3–5 |
| Eyedropper + fine artist brush | Stain creation | $3–5 |
| Distilled water (1 liter) | Stains — never tap water | $1–2 |
| Coffee or tea (diluted 10:1 for moderate; undiluted for major) | Stain creation | $0 (kitchen) |
| Scotch tape 3M Magic | Tape/substance defects | $3 |
| Bone folder | Crease creation | $5–10 |
| Safety glasses | Required for FeSO₄ foxing simulation | $3–5 |

**Tier 1 total estimate: $63–121**. If over budget, drop the phone tripod (use books) and skip sandpaper (use impact corner wear instead).

---

### Tier 2 — Enhanced ($100–130 estimated)

Adds precision measurement and improved photography. Recommended.

Everything in Tier 1, plus:

| Item | Purpose | Estimated Cost |
|---|---|---|
| Digital calipers, 0.1mm resolution | Corner blunting measurement | $10–20 |
| 10x–12x loupe or magnifying glass | Close defect inspection, color break verification | $10–20 |
| Black velvet cloth (approx. 40×50 cm) | Raking shot background — superior light absorption | $8–15 |
| UV/black light, 365nm LED | Restoration detection | $10–20 |
| Laminated defect reference card | Quick threshold lookup during grading | $2 (print + laminate) |
| FeSO₄ (ferrous sulfate, small quantity) | Option A foxing simulation (optional) | ~$8 |
| Metal tweezers, scissors, scalpel or craft knife | Controlled tear initiation | $5–10 |

**Tier 2 total estimate: $116–204**.

---

### Tier 3 — Full Featured ($140–224 estimated)

Everything in Tier 2, plus:

| Item | Purpose | Estimated Cost |
|---|---|---|
| Polarizing gel sheets + circular CPL filter for iPhone | Cross-polarization for glossy cover glare elimination | $20–40 |

**Note on flatbed scanner**: A legal-size flatbed (required to capture full comic covers) costs $80–180 new. This blows the entire equipment budget on a single item. **The scan photography condition is classified as optional** — complete it only if you have free access to a legal-size scanner (many university libraries have them). Do not purchase one. The statistical design for CI calculation assumes table condition only; scan condition is a bonus if available.

---

### Safety Equipment — Required

Before any defect creation session:

- [ ] Safety glasses on for any FeSO₄ (foxing simulation Option A) work — gloves AND glasses required per Correction 2
- [ ] Nitrile or latex gloves when opening any damp-bag specimens — mold spore risk; wear gloves + mask
- [ ] For oven aging: use a dedicated non-food oven if possible; place a calibrated oven thermometer inside (do not trust the dial); do not leave unattended during multi-hour cycles; paper ignition is at ~233°C but malfunctioning thermostats are a real hazard at 65–80°C long-duration runs
- [ ] Older newsprint can off-gas acidic compounds when heated — ensure kitchen ventilation; use oven range hood

---

## Section 2: Setup Guide

### Photography Station Layout

The station handles three shot types (standard diffuse, raking left, raking top) with a fixed overhead camera. Allow approximately 90 minutes for initial setup and calibration before the first photography session.

```
Top view — standard diffuse (Shot 1):

        [LED left, 45°]         [LED right, 45°]
              \                       /
               \                     /
                [    COMIC COVER    ]
                [  foam board flat  ]
                        |
                   [iPhone overhead,
                    25–35 cm height,
                    perpendicular to cover]
```

**Step-by-step station build:**

- [ ] Place matte black foam board flat on desk. Tape all four corners down — a lifted corner casts a shadow line that mimics a crease in raking shots.
- [ ] Mount iPhone directly overhead using tripod, copy stand, or stable stack of books. Working height: 25–35 cm above the comic surface. The comic should fill approximately 80% of the frame.
- [ ] Verify perpendicularity: all four comic corners should be equidistant from the frame edges. Adjust mount until this is true.
- [ ] For Shot 1 (standard diffuse): place two LED panels at 45° from the left and right edges, equidistant, at the same height as the comic surface (not angled downward). Both lights at equal distance.
- [ ] **Color temperature verification (do once per session)**: Shoot a white card under the LED setup. Review on iPhone: if paper looks warm/orange, switch to a cooler LED or set a custom white balance. Warm cast mimics tanning.
- [ ] For Shot 2 (raking left): remove right LED. Move left LED to the table edge, aimed horizontally across the comic at 10–15° above the surface plane. Light travels right across the cover.
- [ ] For Shot 3 (raking top): move LED to top edge, aimed downward across the comic at 10–15° above the surface plane. Light travels downward across the cover.
- [ ] For Shot 4 (macro detail): switch to iPhone ultra-wide camera. Hold or mount 8–15 cm above the primary defect. Use the Shot 1 two-light diffuse setup.

**Raking angle calibration (test before first session):**  
Hold a flashlight 30–40 cm from the comic at roughly table level (~10° elevation), scan across the cover. Creases and rolls become immediately visible as dark shadows. Adjust until you can reliably see known defects. Too steep (>20°) washes out subtle defects; too shallow (<5°) requires impractically long light source distance.

### Grading Station Layout

Set up separately from the photography station, or clear the photography station between sessions.

- [ ] Desk lamp with flexible neck (daylight bulb, 600+ lm) for defect inspection at multiple angles
- [ ] Ruler, calipers, loupe at hand
- [ ] Laminated grade boundary reference card and defect threshold card printed and accessible
- [ ] Grading forms for each grader (paper forms; do not share a single form)
- [ ] Comics in randomized order — do not sort by condition before grading

---

## Section 3: Sorting Protocol

### Before You Begin: Comic Inventory

- [ ] Count all comics. Confirm total is ≥70.
- [ ] Separate into: (A) non-destructible archive comics, (B) destructible/low-value comics.
- [ ] Identify any extremely brittle/aged newsprint comics (Golden/Silver Age pre-1970) — these cannot be used for controlled defect creation.

### Sorting Step 1: Condition Triage (30 minutes)

Sort all comics into five rough condition bins by visual inspection only. Do not grade precisely at this stage.

| Bin | Visual Appearance | Target Count |
|---|---|---|
| High (8.5–10.0) | Looks like it came off the newsstand — sharp corners, bright cover, no visible defects | 15 |
| Mid-High (7.0–8.4) | Minor wear visible but overall presentable — some corner blunting, possible minor crease | 22 |
| Mid-Low (5.0–6.5) | Clearly used — moderate creases, some spine stress, minor stains possible | 18 |
| Low (2.0–4.5) | Significant wear — multiple defects, possible spine damage, tears | 10 |
| Very Low (0.5–1.8) | Severe damage — detached covers, missing pages, structural failure | 5 |

- [ ] If a bin is short, create Very Low specimens from the most damaged comics via controlled severe damage (detached cover, missing pages).
- [ ] If a bin is over-represented, set excess aside — they become practice comics for technique calibration.

### Sorting Step 2: Controlled Specimen Designation (20 minutes)

From the destructible/low-value comics, designate the following. Write the specimen ID directly on a sticky note attached to each comic — do not write on the comic itself.

| Slot | Specimen Type | Required Paper Type | Count |
|---|---|---|---|
| SD-01 through SD-14 | Single-defect controlled | Modern glossy preferred; bronze/copper acceptable | 14 |
| SS-01 through SS-09 | Severity spectrum | Modern glossy strongly preferred | 9 |
| C-2 through C-6 | Compound specimens | Modern glossy; see §6 per specimen | 5 |
| C-1 | Storage degradation cluster (tanning) | Pre-1980 newsprint required for natural tanning | 1 |
| Practice | Technique calibration — always test here first | Any | 5–10 |

**Paper type guidance**:
- Modern glossy (post-1990): Best for controlled specimens — sharp thresholds, controllable defect creation.
- Bronze/Copper (~1970–1990): Acceptable with care; test technique on practice comic first.
- Golden/Silver Age newsprint (pre-1970): Skip minor severity creation entirely. Any fold produces a crease. Use only for severe-end or natural specimens.

### Sorting Step 3: Allocation Confirmation

- [ ] Count baseline (non-controlled) comics: must be ≥39
- [ ] Confirm 4 baseline comics span the anchor grade range (near 9.0, near 7.5, near 5.5, near 3.0) — these double as ICC calibration anchors
- [ ] All comics have a unique ID (COM-001 through COM-070; specimens continue from COM-071)
- [ ] Sticky-note IDs verified before proceeding

---

## Section 4: Photography Protocol

### Camera Settings (set once per session)

- [ ] Format: HEIF Max (48MP) — Settings → Camera → Formats
- [ ] Deep Fusion: leave active (default)
- [ ] Smart HDR: leave active
- [ ] AE/AF Lock: tap and hold the comic surface until "AE/AF LOCK" banner appears before every raking shot — the iPhone will otherwise auto-brighten and destroy shadow contrast
- [ ] Timer: set to 2-second delay to eliminate camera shake (especially at macro distances)
- [ ] Do NOT use ultra-wide (macro) for full-cover shots — barrel distortion mimics warping defects

### Four-Shot Protocol (per comic)

| Shot | Lighting Setup | Camera | Purpose | Time |
|---|---|---|---|---|
| Shot 1 — Standard | 2× LED at 45° symmetric | Main (1x), 25–35 cm | Color reference, stains, overall condition | ~90 sec |
| Shot 2 — Raking Left | 1× LED at 10–15° from left edge, right LED removed | Main (1x), same height | Topographic detection — vertical features | ~2 min (lighting change) |
| Shot 3 — Raking Top | 1× LED at 10–15° from top edge | Main (1x), same height | Topographic detection — horizontal features | ~90 sec |
| Shot 4 — Macro | 2× LED at 45° diffuse (restore Shot 1 setup) | Ultra-wide, 8–15 cm | Fine defect detail — staple damage, corner blunting, crease granularity | ~90 sec |

**Shots 1, 2, and 3 are mandatory.**  
**Shot 4 is required** for any comic with a known or suspected defect (i.e., any controlled specimen and any comic graded below 9.0).  
Shots 5–7 (spine detail, back cover, interior pages) are optional if time permits.

**Per-comic time at practiced pace**: 6–8 minutes (Shots 1–3 only); 10–12 minutes with Shot 4.  
**Per-comic time at learning-curve pace (first session)**: 12–20 minutes.  
**Photography of all 70 comics — table condition only, Shots 1–3**: approximately 7–10 hours.

### Photography Order

- [ ] Photograph all 70 baseline + controlled specimen comics in table condition before adding the handheld or scan conditions
- [ ] Keep randomized order — do not photograph by condition group
- [ ] Mark Shot 4 (macro) as optional during the first photography pass; add it in a second pass if time permits
- [ ] For raking shots: verify the raking shadow is visible in the frame before capturing — if no shadow is visible, the defect will not be detected

### Common Errors — Prevent These

| Error | What It Looks Like | Prevention |
|---|---|---|
| Single-source glare | Bright oval hotspot mimics stain | Always two symmetric 45° lights for Shot 1 |
| Shadow edge artifact | Background warp casts fake crease line | Tape foam board corners flat |
| Barrel distortion | Edges curve, mimics warping | Ultra-wide for detail only; never full-cover |
| Motion blur | Smear mimics foxing | AE/AF Lock + 2-second timer; ISO <400 |
| Warm color cast | White paper looks tanned | Daylight (5500–6500K) LEDs only |
| Raking gradient | Bright/dark sides look like fading | Label raking shots in metadata; never use as color reference |

### Glossy Cover Management

Post-1990 glossy covers produce specular hotspots. First, try angle management: with camera overhead at 90° and lights at 45°, reflection goes at 45° away from camera and does not enter the lens. If hotspots persist in the Shot 1 review:

- [ ] Use cross-polarization (Tier 3 equipment): polarizing gel on both LED panels + CPL filter on iPhone lens — eliminates specular reflection entirely
- [ ] Do NOT use cross-polarization for raking shots (Shots 2/3) — it reduces shadow contrast and defeats topographic detection

### Defects Requiring Raking Light (Shots 2 and 3 Are Not Optional for These)

The following defects are routinely missed in Shot 1 and will NOT be captured without a raking shot:

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

If a defect is visible only in Shot 2 or Shot 3 (not Shot 1), annotate `visible_under: "raking"` — this is a critical flag for AI photographic analysis.

### Three-Condition Photography (Full Protocol Only)

If executing the full 5-day protocol, photograph each comic in all three conditions:

| Condition | Method | Notes |
|---|---|---|
| Table (controlled) | Full 4-shot protocol above | Primary dataset condition — do this first |
| Handheld | iPhone handheld, 45° ambient room light, no tripod | Simulates real-world use — add after table condition |
| Scan | Flatbed scanner if available — legal-size required | Optional bonus; requires free scanner access |

**Statistical note on three conditions**: This creates 70 × 3 = 210 images, but due to within-comic clustering the effective N for CI purposes is approximately 87.5, not 210. The three-condition design is most valuable for measuring image-source effects (scan vs. controlled vs. handheld accuracy comparison), not for inflating the sample size.

---

## Section 5: Human Grading Guide

### Phase 0: Pre-Study (Independent, Before Day 1)

Each grader completes these independently, before the joint calibration session. Estimated 4–6 hours each.

- [ ] **CGC Grader Notes Guide** — free at cgcgrading.com. Study all 109 defect types across 7 categories and the photographs. This is the canonical vocabulary.
- [ ] **Udemy course "Learn to Grade Comic Books"** — ~$15–20 on sale, ~8 hours. 27 CGC-graded comics at every grade level 0.1–10.0. Watch at 1.5x speed.
- [ ] **Overstreet grade boundary definitions** — overstreetaccess.com/grading-definitions/. Memorize the 9.4 vs. 9.0 boundary (most commercially important) and the 8.0 vs. 7.5 boundary.
- [ ] **Build your laminated reference card**: print the grade boundary table and the defect threshold table from this section. Laminate it or put in a protective sleeve.

### Grade Boundary Reference Card

| Grade | Name | Key Criteria |
|---|---|---|
| 9.8 | NM/M | No creases; bend ≤1/8" invisible straight-on; sharp corners; ≤2 minor stress ticks |
| 9.4 | NM | No creases; bend ≤1/16" no color break; corners sharp with ever-so-slight blunting |
| 9.0 | VF/NM | No creases; bend ≤1/8" no color break; ~9.4 corner level |
| 8.5 | VF+ | Minor creases ≤3" no color break; slight corner blunting ok; slight spine roll ok |
| 8.0 | VF | Color-break crease ≤1/4"; minute corner wear; moderate spine stress |
| 7.5 | VF– | Moderate crease, some color break; blunted corners; stress lines |
| 7.0 | FN/VF | Moderate color-break creases; slight corner blunting; possible 1/4" spine split |
| 6.0 | FN | 1/4" spine split; more corner blunting; visible spine roll |
| 5.0 | VG/FN | Multiple moderate defects; significant wear |
| 4.0 | VG | Multiple moderate defects; small missing piece possible; 1 staple detachment possible |
| 2.0 | GD | Major defects throughout; significant structural damage |
| 0.5 | Poor | Severe structural damage; possible missing pages |

**Water damage hard cap: 6.0** — Any water damage stain that creates a tide line and structural warping caps the grade at 6.0 regardless of any other condition. This is a ceiling, not a target.

**Detached cover hard cap: 4.0** — Any detached cover caps at 4.0.

**Major spine split + detachment cap: 1.8** — Full spine split with cover detachment caps at 1.8.

### Phase 1: Anchor Calibration Session (3 hours, both graders together)

- [ ] Select 10–15 anchor comics spanning the full range: one each near NM, VF, FN, VG, GD, Poor. Use the most visually clear examples — no borderline cases in Phase 1.
- [ ] Grade each independently. Write grade on paper. **Reveal simultaneously** — never sequentially (prevents anchoring bias).
- [ ] For every comic with ≥0.5 point disagreement: identify specific defects, compare defect lists, measure dimensions with ruler/calipers, reach consensus, write a decision rule for that defect class.
- [ ] Anti-bias rule: grade before looking up any price information. Cover the comic title during calibration (reduces familiarity bias).

### Phase 2: Progressive Calibration (2 hours, both graders together)

- [ ] Round A: 10 extreme-case comics (obvious 9.8 vs. obvious 2.0). Builds shared vocabulary.
- [ ] Round B: 10 moderate-case comics in VF range (7.5–8.5). This is where most disagreement surfaces.
- [ ] Round C: 10 deliberate boundary pairs — a 9.4 vs. 9.0 pair, 8.5 vs. 8.0 pair, 7.0 vs. 6.5 pair.
- [ ] After each round: compute percent agreement (within 0.5 = agreement). If <80%, revisit decision rules before proceeding.

### Phase 3: Blind Production Grading (both graders independently, ~3.5 hrs each)

- [ ] Work in blocks of 20–25 comics per 90-minute session. Take a 15-minute break between blocks.
- [ ] Grade in random order. Do not sort by condition — contrast effects bias ordinal ratings.
- [ ] Grade high-value or ambiguous comics early in each session, not late (session fatigue = grade inflation).
- [ ] **Never announce a grade verbally during a session before the other person has written theirs.**
- [ ] After all 70 are complete: reveal grades, compute ICC.

### Per-Comic Examination Sequence

1. **First impression** (5 seconds, book closed): Set preliminary grade range.
2. **Cover examination** (30–60 sec): Front cover at multiple angles — gloss, stains, creases, tears. Spine: ticks, stress lines, roll, color breaks at staples. Corners: sharp (NM) vs. rounded (VG range). Back cover: same.
3. **Spine and staple inspection** (15–30 sec): Measure any splits. Check staple rust, tears, detachment.
4. **Interior examination** (30–60 sec): Page color (white → cream → off-white → tan → brown = NM → VF → FN/VG → low). Brittleness (any = ≤1.8). Centerfold attachment. Writing, stamps, water damage.
5. **Grade assignment**: Start from the ceiling (first glance), then work down by defect. Worst single defect determines the ceiling. Accumulation of smaller defects can push grade further below the ceiling.
6. **Record** grade, defects noted, confidence (1–5), borderline flag — before any discussion.

### Recording Form (per comic)

```
Comic ID: ___________
First impression range: _____ to _____
Defects noted:
  1. [Category] [Location] [Measurement] [Severity]
  2.
  3.
Final grade: _____
Confidence (1–5): _____
Borderline? Y / N
```

### Anti-Bias Checklist

| Bias | Prevention |
|---|---|
| Upward bias (most common) | Grade before checking price; ask "what would CGC grade this?" not "what would I like it to be?" |
| Anchoring | Reveal grades simultaneously, never sequentially |
| Age/vintage bias | No special allowances for era — CGC scale is uniform across publication years |
| Key issue bias | Remove price guides; randomize order; cover title |
| Session fatigue | 20–25 comic blocks; 15-min break between blocks; never marathon |
| Contrast effects | Random grading order; never sort before grading |

### ICC Computation

Run after all 70 comics are graded by both graders.

```python
import pingouin as pg
import pandas as pd

data = pd.DataFrame({
    'Subject': list(range(70)) * 2,
    'Rater': ['Sean'] * 70 + ['Marcus'] * 70,
    'Score': sean_grades + marcus_grades
})

# Validate: no duplicate subject-rater pairs (catches mis-keyed IDs)
assert data.groupby(['Subject', 'Rater']).size().max() == 1, \
    "Duplicate Subject-Rater pair found — check for mis-keyed comic IDs"

result = pg.intraclass_corr(
    data=data, targets='Subject', raters='Rater',
    ratings='Score', nan_policy='omit'
)
icc31 = result[result['Type'] == 'ICC3']  # ICC(3,1) Two-Way Mixed-Effects, Single Measures
print(icc31[['ICC', 'CI95%', 'pval']])    # Always report CI, not just point estimate
```

**Interpretation**:

| ICC | Interpretation | Action |
|---|---|---|
| ≥0.90 | Excellent | Proceed to annotation |
| 0.75–0.89 | Good | Proceed to annotation |
| 0.60–0.74 | Moderate | Run one additional targeted calibration round for the disagreement range |
| <0.60 | Poor | Full recalibration required — plot Sean vs. Marcus grades, identify systematic offset vs. fan-scatter vs. range-specific disagreement |

**Sensitivity note on CI**: The ICC_within = 0.70 assumption for DEFF calculation is a prior estimate. Actual DEFF will be computable from the Phase 1 dataset itself. Sensitivity range: if ICC_within = 0.50, DEFF = 2.0, CI ≈ ±6.9pp; if ICC_within = 0.85, DEFF = 2.70, CI ≈ ±7.8pp.

---

## Section 6: Defect Creation Catalog

### Before Any Defect Creation

**Universal rules:**

- [ ] Always practice the technique on a designated practice comic first before touching a dataset specimen
- [ ] Document the target defect type, target severity, and target measurement before creation — not after
- [ ] Take a "before" photo of the specimen comic
- [ ] Wear cotton gloves during handling; switch to nitrile gloves when using chemicals
- [ ] Measure defect after creation; compare against the threshold tables below
- [ ] If over-severity achieved: flag the specimen but do not discard — annotate the actual severity achieved. If natural-specimen fallback is needed, see §6.8.

**The universal severity dividing line for fold-type defects:**
- Bend (no fiber break) → reversible → Minor (green)
- Crease (fiber break, no color loss) → permanent → Moderate (yellow)
- Crease with color break (fiber break + ink loss) → irreversible → Major (red)

**Severity table disclaimer**: These thresholds are derived from Overstreet Guide descriptions and assume typical defect placement. Cover-center placement elevates effective severity one tier; margin placement may reduce impact. CGC does not publish numerical severity tables; these represent the research team's interpretation of publicly available proxy materials.

---

### 6.1 Crease

**Tools**: Bone folder, steel ruler for fold guide

| Tier | Criteria | Measurement | Grade Equivalent |
|---|---|---|---|
| Minor (green) | No color break | Length ≤2", width <0.5mm | 8.0–9.2 |
| Moderate (yellow) | Short crease, partial color break | ≤2" length, color break along ~50% | 7.0–7.5 |
| Major (red) | Full color-break crease | >2" long OR full color-break line | Below 7.0, often 4.0–6.0 |

**Grade-anchored thresholds (Overstreet)**:
- 9.4 NM: 1/16" bend permitted, no color break (bend, not crease)
- 9.0 VF/NM: 1/8" bend allowed, no color break
- 8.0 VF: 1/4" crease acceptable, no color break
- Subscription crease full-height color-breaking: 5.5 or lower

**Physical creation**:
- Minor: Fold cover 5–10°, no rubbing. One light bone folder pass with minimal pressure. Verify no color break with loupe. Success rate ~50% (glossy), ~30% (newsprint).
- Moderate: Fold 30–45°, one firm bone folder pass. White line visible along ~50% of length. Success rate ~70%.
- Major: Fold near-90°, two hard bone folder passes. Full white line. Success rate ~90%.

**Paper type note**: Brittle/aged newsprint — skip minor severity creation. Any careful technique still produces moderate due to material fragility. Use modern glossy for controlled minor crease specimens.

**Attempt budget**: Minor on modern glossy has ~50% success rate. For 2 minor specimens, budget 6–8 attempts at 50% success for 95% probability. If after 6 attempts you have not achieved minor severity, switch to natural-specimen fallback (§6.8).

---

### 6.2 Spine Roll

**Tools**: Hands only

| Tier | Visual Test | Width Measurement | Grade Equivalent |
|---|---|---|---|
| Minor (green) | Spine edge barely lifts; book nearly flat | Roll width <1/4" | 7.0–8.5 |
| Moderate (yellow) | Cover arches noticeably; back cover fanning visible | Roll width 1/4"–1" | 6.0–8.0 |
| Major (red) | Book cannot lie flat without manual pressure | Roll width >1" | Below 6.0, down to 4.0 |

**Visual test**: Lay book flat on table. If spine edge lifts >0.5mm: minor. If cover noticeably arches: moderate. If book cannot lie flat: major.

**Physical creation**:
- Minor: Open book fully flat (180°), gently roll spine edge backward 15–20°, release immediately. Repeat 3–5 times. Success rate ~40%.
- Moderate: Hold comic one-handed, fan pages behind spine, read through 3–4 times with moderate backward curl. Success rate ~75%.
- Major: Press pages into tight curl around spine, hold 30–60 seconds, repeat through full book. Success rate ~90%.

**Warning**: Attempting major spine roll on brittle comics may produce spine split instead. Monitor progression carefully.

**Attempt budget**: Minor roll has ~40% success rate. For 1 specimen, budget 5–7 attempts. If not achieved after 7 attempts, use natural-specimen fallback (§6.8).

---

### 6.3 Blunted Corner

**Tools**: 400-grit sandpaper (preferred); or impact technique (drop)

| Tier | Description | Measurement | Grade Equivalent |
|---|---|---|---|
| Minor (green) | Imperceptibly blunted, still nearly sharp | Flat section <1mm at corner tip | 9.4–9.6 |
| Moderate (yellow) | Visible flat section, color break possible | Flat section 1–3mm, corner angle clearly >90° | 8.0–9.2 |
| Major (red) | Substantially blunted, beginning to round | Flat section >3mm OR rounded arc starting | Below 8.0, down to 6.0 |

**Overstreet anchors**:
- 9.6 NM+: "One corner may be almost imperceptibly blunted"
- 9.4 NM: "Corners cut square and sharp with ever-so-slight blunting permitted"
- 8.0 VF: "Minute wear at corners; blunted or abraded corners"

**Physical creation**:
- Minor: Very difficult to create reliably by impact. **Prefer naturally worn high-grade comics.** Success rate by impact: ~35%.
- Moderate: Drop corner 4–6 inches onto hard surface, examine. Or: 15–20 passes with 400-grit sandpaper at the corner tip. Success rate ~65%.
- Major: 8–10 inch drop OR 40+ passes with 400-grit sandpaper. Success rate ~85%.

**Preferred technique**: 400-grit sandpaper abrasion is more controllable than impact for all severities — allows incremental progress and measurement after each pass. Check with calipers after every 10 passes.

---

### 6.4 Tear

**Tools**: Metal tweezers (initiation), scissors (controlled length), steel ruler (guide)

| Tier | Description | Size | Grade Equivalent |
|---|---|---|---|
| Minor (green) | Small edge tear, not entering image area | Length ≤1/8" (3mm) [high-grade context] | 9.0–9.4 |
| Moderate (yellow) | Tear entering cover, visible from front | Length 1/8"–3/4" (3–19mm) | 7.5–8.5 |
| Major (red) | Long tear crossing image, or triangular loss | Length >3/4" OR triangle missing >1/4" | Below 7.5, down to 4.0 |

**Threshold context**: The ≤1/8" minor threshold applies at high grades (9.0+). In mid-grade context (FN/VF, 6.0–8.0), the minor/moderate boundary shifts to 1/4". Label specimens with the tear length measurement AND the target grade range.

**Hard-cap types**: Detached cover → caps at 4.0. Fully split spine + detachment → caps at 1.8.

**Physical creation**:
- Minor: Needle or fine tweezers at edge, create 1–2mm nick. Stop immediately. Control propagation with both thumbs pressed near the tear tip. Success rate ~60%.
- Moderate: Metal ruler guide; allow propagation to 6–15mm at 45–60° angle. Success rate ~70%.
- Major: Deliberate propagation to 3/4"+. For triangular loss: two converging scissors cuts, pull triangle free. Success rate ~95%.

**Most controllable technique**: Scissors-initiated tears of exact length, then manual opening for natural appearance. This gives exact length control.

---

### 6.5 Stain (Water/Soiling)

**Tools**: Eyedropper, fine artist brush, distilled water, diluted coffee or tea

**ALWAYS use distilled water** — tap water leaves mineral residue that adds an unintended whitish ring.

| Tier | Description | Size/Coverage | Grade Equivalent |
|---|---|---|---|
| Minor (green) | Light mark, barely noticeable at arm's length, no prominent tide line | Diameter ≤5mm | 8.5–9.4 |
| Moderate (yellow) | Visible discoloration, tide line present, single area | Diameter 5–25mm OR tide line ≤1" perimeter | 7.0–8.5* |
| Major (red) | Dark stain, obvious at arm's length, spread or multiple areas | >25mm OR multiple areas OR foxing cluster | Below 7.0, down to 4.0 |

**Water damage vs. non-water stains — critical distinction**:

The grade equivalents above apply to **non-water stains** (soiling, foxing, graphite). Water damage (tide lines with structural warping/cockling) carries a hard cap of 6.0 that overrides the general stain severity table. A "moderate" stain that qualifies as water damage grades at ≤6.0, not 7.0–8.5. When in doubt, treat any stain with a tide line on coated paper as water damage.

**Physical creation**:
- Minor: Fine artist brush, barely damp. Touch once to surface. Faint ring ~3–5mm. Success rate ~65% (glossy), ~35% (newsprint).
- Moderate: Eyedropper, 1–2 drops. Allow to spread naturally. For colored stain: 10:1 water:coffee dilution. Success rate ~75%.
- Major: 5–10 drops across 25–40mm area. Colored: undiluted coffee or tea. Success rate ~90%.

**Paper type effect**: Glossy covers bead liquid; stain is primarily a tide line. Newsprint absorbs immediately — stain spreads beyond target area very quickly. On matte or newsprint, reduce drop size by half versus the glossy target.

---

### 6.6 Spine Stress

**Tools**: Hands (careful angle control)

| Tier | Description | Count/Length | Grade Equivalent |
|---|---|---|---|
| Minor (green) | 1–3 stress lines, no color break, raking-light only | Count ≤3, each <1/4" long | 9.4–9.6 |
| Moderate (yellow) | 4–5 stress lines OR 1–3 with color break | Count 4–5 OR color-breaking; each <1" | 9.0–9.4 |
| Major (red) | Numerous lines, many with color break | Count >5 with color break | Below 9.0, down to 8.0 |

**Critical rule**: Stress lines >1" long are reclassified by CGC as creases, not spine stress. Do not annotate a >1" line as "spine stress" — it belongs in the crease category. Major spine stress specimens should be defined purely by count of color-breaking lines <1" in length.

**Physical creation**:
- Minor: Open comic fully flat (180°). Apply 2–3° additional pressure at 2–3 locations, release immediately. Examine under raking light. 1–3 small white ticks visible. Success rate ~70%.
- Moderate: Open 5–7° past flat at multiple points. Repeat 4–5 times. Success rate ~75%.
- Major: Open forcefully past 180°, work through entire book. Many white ticks visible from front. Success rate ~85%.

**Angle control**: 180° = minor bend. 185–190° = likely color break (moderate). Excess opening angle and held pressure jump to major.

---

### 6.7 Foxing (FeSO₄ Simulation — Option A)

**Safety required**: Nitrile gloves + safety glasses for all FeSO₄ work.

**Option A (FeSO₄)**: Prepare a very dilute solution (0.1–0.5 g FeSO₄ per 100ml distilled water). Apply with fine artist brush at specific points on newsprint paper — cover back or inside cover. Allow to dry 24 hours. Brown-orange spots should develop. Adjust concentration for target severity.

**Option B (natural specimens)**: If naturally foxed comics are available in the collection, use them. Natural specimens are preferable — no chemical handling risk, and the foxing appearance is authentic.

---

### 6.8 Natural-Specimen Fallback

If after the specified attempt budget a controlled defect cannot be achieved at the target severity, do not continue destroying comics. Switch to natural-specimen sourcing:

- [ ] Search the existing worn collection for a naturally occurring specimen of equivalent severity
- [ ] Annotate `created_intentionally: false` and note the naturally occurring specimen
- [ ] Record that the controlled attempt was abandoned and the reason (usually: paper type too brittle, or minor severity not achievable)
- [ ] This does not invalidate the specimen for the dataset — natural specimens are valid

**Trigger conditions** (abandon controlled creation after N attempts):
- Minor crease: abandon after 8 attempts with no success
- Minor spine roll: abandon after 7 attempts
- Minor corner blunting: prefer natural specimens from the start; abandon after 5 attempts
- Any severity on Golden/Silver Age newsprint: abandon immediately; use natural specimens only

---

## Section 7: Compound Defect Recipes

### Before You Begin

Compound specimens test the algorithm's interaction logic — cap selection, diminishing returns, area weighting, minor-only cap. Each specimen generates 4+ distinct test assertions per comic. These are the highest-value specimens per physical unit.

**Important**: C-2, C-4, and other algorithm-interaction specimens test AI vs. algorithm consistency, not AI vs. CGC. The minor-only cap (-0.3 ceiling) is a design rule in the AI system, not a documented CGC policy. A CGC grader encountering 10 minor defects might grade differently. Document this distinction in annotation notes.

**Start C-1 before anything else** if executing the oven-tanning variant — it requires 24–72 hours.

---

**Specimen C-1: Storage Degradation Cluster** — Priority 1

- **Defects**: Minor-to-moderate soiling (cover margins) + light tanning (pages) + blunted corners (2–3 corners)
- **Expected grade**: 7.0–8.0 (depending on severity)
- **Algorithm property tested**: Penalty accumulation across different defect types sharing the same cap (all three cap at 9.0); no diminishing returns apply across different defect keywords
- **AI failure mode**: Applies diminishing returns incorrectly across soiling/tanning/corner wear; or misidentifies tanning as a more severe stain type

**Tanning creation — validated method only**:

The room-temperature damp-bag technique (48h sealed bag with damp sponge) does **NOT** produce tanning. It produces surface moisture damage, tide lines, and potential foxing initiation — different defects than what C-1 tests. This technique has been removed from the protocol.

**Two valid approaches for tanning in C-1:**

Option A — Natural specimen (preferred): Use a pre-1970 or pre-1980 newsprint comic from the collection that already shows page tanning (yellowing/browning). Natural specimens are preferable; no chemical or thermal process required. Annotate `created_intentionally: false`.

Option B — Oven accelerated aging (if natural specimen not available):
- [ ] Use a dedicated non-food oven if possible; if not, ensure good kitchen ventilation
- [ ] Place an **oven thermometer** inside — do not rely on the dial
- [ ] Set oven to 65°C (149°F). Place a small oven-safe cup of water in the oven to add humidity
- [ ] Place the comic (open to interior pages) on a rack — do not seal in a bag
- [ ] Start with 24 hours and photograph interior pages to assess tanning level
- [ ] If insufficient tanning after 24h, continue to 48h. Check at 48h. Maximum: 72h
- [ ] **Do not leave unattended for multi-hour cycles** — check oven thermometer every 2–3 hours
- [ ] This process requires 24–72 hours — **start at least 3 days before the session where C-1 will be graded and photographed**
- [ ] Safety: newsprint off-gasses acidic compounds when heated; run oven hood ventilation

**Soiling**: Light graphite smear on cover margins (a soft pencil pressed lightly across the edge, then partially erased — leaves gray residue without the cover appearing vandalized).

**Corner blunting**: See §6.3. Drop corners 4–6 inches for moderate; or use natural blunting from the existing condition.

---

**Specimen C-2: Minor-Only Cap Test** — Priority 2

- **Defects**: 5–6 minor defects — 2 minor creases + minor foxing (2–3 spots) + minor soiling + minor stress lines (2–3)
- **Expected grade**: 8.5 (model: 9.0 ceiling, minor-only cap → -0.3 → 8.7 → snapped to 8.5)
- **Algorithm property tested**: Minor-only cap (-0.3 total) is the binding constraint; counter-intuitive result (many minor defects grades same as few minor defects)
- **AI failure mode**: Reports any one defect as moderate → kills the cap → grade drops to 7.5–8.0 instead of 8.5

**Creation**:
- [ ] Light spine flexes for stress lines (open to 182° at 2–3 locations, release immediately)
- [ ] Fine brush water touch for foxing simulation (2–3 spots, <5mm each, distilled water only)
- [ ] Light graphite smear for soiling (margins only)
- [ ] Minimal bone folder pass for 2 minor creases (5–10° fold, single light pass)
- [ ] Verify all defects measure within minor thresholds before finalizing

---

**Specimen C-3: Water Damage + Tape Repair** — Priority 3

- **Defects**: Moderate water damage (corner or bottom edge) + tape repair applied over the damaged area
- **Expected grade**: 6.0 (water damage cap 6.0 dominates over tape cap 7.0)
- **Algorithm property tested**: Lowest cap wins; CGC functional-tape policy (tape ignored if repair function; only underlying defect scored)
- **AI failure mode 1**: Applies tape cap (7.0) instead of water damage cap (6.0) → 1 grade point too high
- **AI failure mode 2**: Double-penalizes tape + water damage — this is a known algorithm deviation from CGC policy; document as expected difference in annotation, not an AI error

**Creation**:
- [ ] Apply 1–2 drops distilled water to a corner; allow to dry completely (2–3 hours) — tide line and minor cockling should be visible
- [ ] Apply strip of Scotch 3M Magic tape over the water-damaged area
- [ ] High reproducibility — straightforward creation

---

**Specimen C-4: Same Defect Multiple Locations (Diminishing Returns)** — Priority 4

- **Defects**: Three moderate creases at different zones — top-right corner, cover center, bottom edge — all annotated as "crease"
- **Expected grade**: 7.5 (with diminishing returns applied) vs. 7.0 (if diminishing returns not applied)
- **Algorithm property tested**: Diminishing returns (2nd instance = 50% penalty weight, 3rd = 25%) for same keyword across locations
- **AI failure mode 1**: Uses varying vocabulary ("fold," "bend," "crease") → keyword mismatch → diminishing returns not applied
- **AI failure mode 2**: Reports creases as minor instead of moderate → minor-only cap triggers → masks the diminishing-returns mechanism

**Creation**: Three controlled diagonal creases using bone folder at specified zones. Fold 30–45°, firm single pass. Verify each crease shows partial color break (moderate tier). Moderate difficulty.

---

**Specimen C-5: Minor + Major Mix (Minor-Only Cap Must NOT Apply)** — Priority 5

- **Defects**: Four minor defects (soiling, light tanning, minor foxing, minor corner wear) + one major crease (1-inch diagonal through cover center)
- **Expected grade**: 6.0–6.5 (major crease dominates; minor-only cap must NOT apply)
- **Algorithm property tested**: Minor-only cap correctly skipped when any non-minor defect is present
- **AI failure mode**: Rates major crease as moderate → minor-only cap incorrectly applies → grade inflates to 8.5 when correct answer is 6.0 (2.5 grade point error)

**Creation**: Single large deliberate crease (bone folder, firm pressure, 1+ inch diagonal through center). Create minor defects separately using techniques from §6.1–6.7.

---

**Specimen C-6: Structural Failure — Spine Split + Loose Cover** — Priority 6

- **Defects**: Major spine split (full length) + partially detached cover at one staple
- **Expected grade per algorithm**: 3.0–4.0 (penalty-dominated). CGC documented maximum for this combination: 1.8. This is a known calibration gap — the algorithm penalty values may be insufficiently aggressive for extreme structural failure.
- **Algorithm property tested**: Penalty accumulation dominating cap; calibration gap between algorithm and CGC practice
- **AI failure mode**: Applies detached cover cap (4.0) as the target grade rather than an upper bound; reports 4.0 when actual grade should be 2.0–3.0

**Creation**: Difficult, destructive, permanent. Create full spine split first by working a folded ruler down the spine; then progressively open staple attachment until one staple detaches. Monitor carefully. **Schedule this last. Use the most damaged existing comic.**

---

## Section 8: Annotation Guide

### Tooling and Time Estimate

**Tooling**: Use a Google Sheet with column headers matching the schema below. Export to JSON after completion. Do not annotate directly in JSON — manual JSON editing at scale introduces transcription errors.

**Time estimate**: 70 comics × average 2 defects × ~39 field-fill operations = ~2,100 field operations. At 2–3 min/comic: approximately 2.5–3.5 hours for baseline comics; 5–7 hours total including controlled specimens.

**Annotation should happen immediately after photography and grading for each comic** — do not batch all annotation to the end of the project. Memory decays; annotate while the comic is in hand.

### Required Fields Per Comic

| Field | Format | Notes |
|---|---|---|
| comic_id | String (e.g., COM-001) | Sequential, not title-based — reduces familiarity bias |
| title | String | Internal reference only; not used as AI input |
| grade_sean | Float (CGC scale: 0.5–10.0) | Grader A's independent grade before ICC comparison |
| grade_marcus | Float | Grader B's independent grade |
| grade_consensus | Float | Post-ICC discussion grade — use this as ground truth |
| grade_confidence | Integer 1–5 | Per grader, per comic |
| grade_borderline | Boolean | Flag for borderline cases where ±0.5 was genuinely ambiguous |
| defects_noted | Array of defect objects | See defect object schema below |
| specimen_type | Enum: `baseline` / `single-defect` / `severity` / `compound` | |
| paper_type | Enum: `modern-glossy` / `bronze-copper` / `golden-silver-newsprint` | |
| photography_conditions | Array: `scan` / `table` / `handheld` | Only list conditions actually completed |
| image_paths | Dict keyed by condition + shot number | e.g., `{"table_shot1": "COM-001_table_s1.heic"}` |

### Defect Object Schema

For each defect on a comic:

| Field | Format | Notes |
|---|---|---|
| category | Enum: `crease` / `distortion` / `missing_part` / `stain` / `substance` / `tanning` / `tear` | CGC 7 categories |
| keyword | String (CGC keyword) | e.g., `"spine_roll"`, `"crease"`, `"water_damage"`, `"tape"` |
| severity | Enum: `minor` / `moderate` / `major` | green / yellow / red |
| area | Enum: `spine` / `corner_tl` / `corner_tr` / `corner_bl` / `corner_br` / `edge_top` / `edge_bottom` / `edge_right` / `staple_top` / `staple_bottom` / `cover_center` / `full_cover` / `pages` | 12-zone + pages |
| measurement | String | e.g., `"1.5 inches"`, `"3mm"`, `"0.8cm flat section"` — physical measurement where applicable |
| visible_under | Enum: `diffuse` / `raking` / `both` | Critical for AI photographic analysis |
| created_intentionally | Boolean | `true` for controlled specimens |
| creation_technique | String | Brief description for controlled specimens only |
| notes | String | Edge cases, ambiguities, deviations from expected |

### Example JSON Record

```json
{
  "comic_id": "COM-047",
  "title": "Internal Reference Only",
  "grade_sean": 8.0,
  "grade_marcus": 7.5,
  "grade_consensus": 8.0,
  "grade_confidence": 3,
  "grade_borderline": true,
  "specimen_type": "single-defect",
  "paper_type": "modern-glossy",
  "photography_conditions": ["table"],
  "image_paths": {
    "table_shot1": "COM-047_table_s1.heic",
    "table_shot2": "COM-047_table_s2.heic",
    "table_shot3": "COM-047_table_s3.heic",
    "table_shot4": "COM-047_table_s4.heic"
  },
  "defects_noted": [
    {
      "category": "crease",
      "keyword": "crease",
      "severity": "moderate",
      "area": "cover_center",
      "measurement": "1.75 inches, ~60% color break",
      "visible_under": "both",
      "created_intentionally": true,
      "creation_technique": "Bone folder, 40° fold, single firm pass",
      "notes": "Targeted moderate tier; color break along ~60% of length; cover-center placement elevates effective severity one tier vs. edge placement"
    }
  ]
}
```

### Edge Case Rules

**Borderline severity**: Default to the lower severity tier when borderline. Annotate as borderline in notes. Conservative ground truth is preferable — slightly underpenalizing is better than overpenalizing.

**Tear threshold context**: Label tear measurements in millimeters. Note whether the specimen targets high-grade (minor ≤1/8") or mid-grade (minor ≤1/4") context.

**Raking-only defects**: If a defect is visible only in Shot 2 or Shot 3 (not Shot 1), set `visible_under: "raking"`. This is a critical annotation for AI analysis.

**Compound specimens**: Annotate each defect in the compound independently. Note which cap interaction or algorithm property the compound tests in the specimen-level notes field. Explicitly state whether the expected grade reflects CGC practice or algorithm behavior.

**Tanning source**: For naturally occurring tanning specimens, note the approximate era of the comic. Dell comics (1950s–60s) are graded less harshly for inside cover tanning due to known paper composition — annotate this explicitly.

**Stain type**: Distinguish water damage stains (tide line + structural warping → 6.0 hard cap) from non-water stains (soiling, foxing, graphite → use general stain severity table).

**Algorithm deviations**: Document known deviations from CGC practice — functional-tape policy (algorithm double-penalizes; CGC ignores repair tape), structural failure calibration gap (algorithm predicts 3.0–4.0; CGC cap is 1.8 for full split + detachment). These are labeled "expected deviations — not AI errors" in notes.

---

## Section 9: Quality Checkpoints

### Pre-Session Checks (before each grading or photography day)

- [ ] Both graders have completed pre-study materials (Phase 0)
- [ ] Photography station tested with a dummy comic — raking shadows visible at 10–15°
- [ ] Color balance verified: white card shot shows no warm cast
- [ ] AE/AF Lock procedure confirmed working
- [ ] Grading forms and laminated reference cards printed
- [ ] Comics in randomized order
- [ ] Equipment at hand: ruler, calipers, loupe, cotton gloves

### Per-Specimen Checks (during defect creation)

- [ ] Target defect type and severity documented BEFORE creation begins
- [ ] Practice comic used for technique test before touching dataset comic (required for any defect type attempted for the first time)
- [ ] Post-creation measurement taken: crease length, tear length, stain diameter, roll width, flat section width
- [ ] Measurement compared against severity thresholds in §6
- [ ] If over-severity achieved: flag specimen; annotate actual severity; do not discard
- [ ] If natural-specimen fallback triggered: note in annotation; continue
- [ ] Safety: gloves + glasses for FeSO₄ work; gloves + mask when opening any damp-aged specimens; oven thermometer in use for thermal aging

### Per-Comic Photography Checks

- [ ] Comic lies completely flat on background — no page curl creating shadow
- [ ] Background foam board corners taped down
- [ ] No crew shadow visible in frame
- [ ] Shot 1: two symmetric lights confirmed, no hotspot visible
- [ ] AE/AF Lock engaged before Shots 2 and 3
- [ ] Shot 2: raking shadow from left visible in frame — if not, adjust angle
- [ ] Shot 3: raking shadow from top visible in frame — if not, adjust angle
- [ ] All shot types noted in image metadata / filename convention

### Post-Grading ICC Verification

- [ ] Both graders have written grades for all 70 comics before any comparison
- [ ] ICC(3,1) computed using pingouin per §5
- [ ] Input validation assertion passed (no duplicate subject-rater pairs)
- [ ] 95% CI reported alongside ICC point estimate — always report CI, not just the point estimate
- [ ] If ICC ≥ 0.75: proceed
- [ ] If 0.60–0.74: run one targeted calibration round for the specific disagreement range; proceed
- [ ] If ICC <0.60: full recalibration — run diagnostic plot (Sean vs. Marcus grades) before deciding on action

### Dataset Completeness Check (before declaring Phase 1 done)

- [ ] 70 comics graded independently by both graders with recorded consensus grade
- [ ] All 70 photographed in table condition, at minimum Shots 1–3
- [ ] Shot 4 completed for all controlled specimens and all comics graded below 9.0
- [ ] All 70 photographed in all 3 conditions (scan/table/handheld) if feasible — not required for minimum viable
- [ ] C-1 tanning specimen completed (oven method if no natural specimen; 72h lead time honored)
- [ ] C-2 through C-6 specimens completed, or C-6 documented as abandoned with reason
- [ ] Annotation Google Sheet has no empty required fields
- [ ] Raking-only defects flagged in annotation (`visible_under: "raking"`)
- [ ] Known algorithm deviations documented (functional-tape policy, structural failure calibration gap)
- [ ] ICC ≥ 0.75 confirmed
- [ ] Final effective CI acknowledged as ±7.5pp (not ±4pp) in any report

---

## Section 10: Allocation Matrix

### 70-Comic Distribution

| Category | Count | Role |
|---|---|---|
| Baseline (no controlled damage) | 39 | Grade accuracy evaluation; 3-condition photography; 4 double as ICC calibration anchors |
| Single-defect controlled | 14 | Defect detection coverage — priority defect types |
| Severity-spectrum controlled | 9 | 3 severity levels × 3 defect types |
| Compound-defect | 8 | Multi-defect interaction tests (6 priority compounds; 2 spares) |
| **Total** | **70** | |

**Design rationale per bin**:
- 39 baseline: Driven by the overall accuracy CI requirement (even though ±7.5pp is the achievable CI, not ±4pp). Neyman optimal allocation overweights high-variance tiers. This is the floor to produce any meaningful accuracy estimate.
- 14 + 9 controlled: Driven by defect detection coverage across 4 priority defect categories (crease, stain, tear, substance).
- 8 compound: Limited by destructible-comic count and creation difficulty, not by information value. Under D-optimal design logic, compounds are the highest-information specimens — but the limiting constraint is physical availability of suitable destructible comics, not theory. If more destructibles are available, increase this bin before any other.

### Grade Tier Distribution

| Tier | Grade Range | Comic Count | Images (×3 conds) | Per-Tier Effective CI | Adequacy |
|---|---|---|---|---|---|
| High | 8.5–10.0 | 15 | 45 | ±10.4pp | Can detect ~20pp bias; ±10pp bias is noise |
| Mid-High | 7.0–8.4 | 22 | 66 | ±8.6pp | Best-powered tier; detect ~17pp bias |
| Mid-Low | 5.0–6.5 | 18 | 54 | ±9.5pp | Can detect ~19pp bias |
| Low | 2.0–4.5 | 10 | 30 | ±12.7pp | Can only detect catastrophic failures (>25pp) |
| Very Low | 0.5–1.8 | 5 | 15 | ±17.6pp | **Effectively unmeasured** — catastrophic failures only |
| **Total** | | **70** | **210** | **±7.5pp effective** | Feasibility + directional accuracy |

**Per-tier adequacy verdict**: Very Low (n=5) and Low (n=10) tiers produce CIs too wide for any tier-level accuracy claim at a practically important effect size. They are included for catastrophic failure detection, not precision measurement. Mid-High is the only tier where meaningful tier-level claims can be made.

**To achieve ±4pp overall CI**: Approximately 185 independent comics are required (556 clustered images with DEFF = 2.4, or 185 comics × 1 table condition with no clustering inflation). This is Phase 2.

### Controlled Specimen Allocation by Defect Category

The 23 controlled comics (14 single-defect + 9 severity) concentrate on 4 priority defect categories:

| Category | Controlled Specimens | Severity Coverage | Specific Types |
|---|---|---|---|
| crease | 6 | 2 minor, 2 moderate, 2 major | Spine roll (3), reader crease (2), subscription crease (1) |
| stain (water) | 5 | 2 minor, 2 moderate, 1 major | Water ring stain (3), soiling (2) |
| tear | 5 | 1 minor, 2 moderate, 2 major | Corner tear (2), spine split (2), detached cover (1) |
| substance (tape) | 4 | 2 minor, 2 moderate | Tape applied (2), tape residue (2) |
| **Total controlled** | **20** | | |

Remaining 3 defect categories (distortion, missing_part beyond tear, tanning) sourced from natural specimens in the existing worn collection.

**Why these 4 categories**: crease is the most common real-world defect. stain (water) has a grade cap (6.0) and is likely undertested. tear carries a catastrophic cap (4.0) with major grade impact. substance (tape) is extremely common and easy to create.

### Detection Power Summary

**Recall CI**: With 5 specimens per defect category, the CI on recall is ±31pp — not appropriate for any precision recall claim.

**Catastrophic failure detection**: If 0/5 specimens of a given defect category are detected, we can exclude recall > 45% at 95% confidence (one-sided exact binomial upper bound). This is the correct framing: Phase 1 rules out catastrophic recall failures (recall ≤ 45%), it does not measure recall precisely.

**What Phase 1 Can Claim**:

| Claim | Feasible? |
|---|---|
| Overall accuracy ±7.5pp effective CI | Yes |
| High vs. low tier accuracy bias of ≥20pp | Yes (marginal) |
| Defect recall ±15pp CI per category | No (needs 28 positives per category) |
| Catastrophic detection failure (recall ≤45%) per category | Yes (if 0/5 detected) |
| Severity miscalibration detection | Partial (3 levels × 3 defect types) |
| Compound interaction failures | Yes (6 compound specimens) |
| CI matches brief target of ±4pp | **No — Phase 2 required** |

---

*End of Protocol — Version 1.0*
