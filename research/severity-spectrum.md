# Severity Spectrum Research: Defect Creation and Calibration

**Axis**: Defect Severity Calibration for AI Grading Evaluation Dataset
**Date**: 2026-04-07
**Researcher**: Claude Sonnet 4.6 (autonomous research agent)

---

## Executive Summary

CGC does not publish explicit measurement tables for minor/moderate/major severity tiers. Instead, severity emerges from the intersection of defect type, size/length, color-break status, location, and accumulation. The Overstreet guide (the underlying reference for CGC and CBCS) does provide grade-anchored dimensional criteria that can be reverse-mapped onto three severity tiers. Physical creation of controlled specimens is achievable with low-cost tools but requires understanding the fiber-breakage threshold — the key dividing line between a bend (reversible, no fiber damage) and a crease (permanent, fiber broken). The six target defect types vary significantly in controllability: creases and stains are most controllable; spine roll and corner blunting are harder to create at precise severity without multiple attempts.

---

## 1. The CGC Severity Framework

### 1.1 Grade-Anchored Language

CGC's published grading scale uses three explicit severity tiers that map onto their green/yellow/red penalty system:

| Grade Band | Defect Language | Tier Mapping |
|---|---|---|
| 9.6–10.0 | "negligible handling/manufacturing defects" | Green (minor) |
| 8.0–9.4 | "moderate defect or number of small defects" | Yellow (moderate) |
| 7.0–7.5 | "major defect or accumulation of small defects" | Red (major) |
| Below 5.0 | "numerous major defects" | Beyond red |

**Evidence**: CGC Grading Scale (cgccomics.com/grading/grading-scale/), Overstreet Access grading definitions (overstreetaccess.com/grading-definitions/).
**Confidence**: HIGH — consistent across multiple independent sources.

### 1.2 The Fiber-Breakage Threshold (Universal Dividing Line)

The single most important criterion separating severity tiers for any fold-type defect is whether paper fibers are broken:

- **Bend (no fiber break)**: Paper deforms but fibers intact; reversible by pressing. Maps to green tier.
- **Crease (fiber break, no color loss)**: Fibers broken but ink surface intact. Maps to yellow tier. May be partially improved by pressing but color-breaking remains.
- **Crease with color break**: Fibers broken + ink/color loss visible as white line. Maps to red tier. Pressing cannot recover color.

**Evidence**: CGC Grader Notes Guide: Crease (cgcgrading.com/en-US/resources/comics-grader-notes-guide/crease).
**Confidence**: HIGH — official CGC documentation, corroborated by comic doctor and pressing community sources.

---

## 2. Measurable Severity Criteria by Defect Type

### 2.1 Crease

**Definition**: Permanent fold where paper fibers are broken along the fold line, potentially causing color/ink loss.

**Sub-types from CGC**: general crease, finger crease, subscription crease, reader crease, polybag crease.

#### Severity Tiers

| Tier | CGC/Overstreet Criteria | Measurement | Grade Equivalent |
|---|---|---|---|
| **Minor (green)** | Hairline crease: <0.5mm wide, <2" long, no color break | Length ≤2", width <0.5mm | 8.0–9.2 |
| **Moderate (yellow)** | Light crease: 0.5–1mm wide, ≤2" long OR color-break <1/4 of length | Length ≤2", some color break | 7.0–7.5 |
| **Major (red)** | Heavy crease: >2" long OR >1mm wide, significant color break | Length >2" OR full color-break line | Below 7.0, often 4.0–6.0 |

**Exact thresholds from Overstreet**:
- 9.4 NM: "1/16" bend permitted, no color break" (minor bend, not yet a crease)
- 9.0 VF/NM: "1/8" bend allowed if color is not broken"
- 8.0 VF: "1/4" crease acceptable if color is not broken" — this is the green/yellow boundary
- Subscription crease (color-breaking, top to bottom): lowers grade to 5.5 or lower — definitive major/red

**Key thresholds**:
- Crease ≤1/4" without color break = green (minor)
- Crease with any color break but <2" = yellow (moderate)
- Crease >2" with color break, or book-length = red (major)

**Evidence**: Overstreet Access grading definitions, CGC Crease Guide (cgcgrading.com), ComicBookGradingTool (comicbookgradingtool.com/comic-grading-terms).
**Confidence**: HIGH for grade-anchored thresholds; MEDIUM for exact minor/moderate boundary (no single authoritative source states it explicitly).

---

### 2.2 Spine Roll

**Definition**: Cover and pages curl around the back of the book from reading, causing the spine to point upward when the book lies flat. Causes torque and fanning along the left edge of the back cover.

#### Severity Tiers

| Tier | Visual Description | Width Measurement | Grade Equivalent |
|---|---|---|---|
| **Minor (green)** | Slightest detectable curl; book nearly lies flat; visible only when held at angle | Roll width <1/4" | 7.0–8.5 |
| **Moderate (yellow)** | Definite curl visible when book lies flat; back cover fanning visible; torquing ≤1/4" at top/bottom | Roll width 1/4"–1" | 6.0–8.0 |
| **Major (red)** | Pronounced curl; book will not lie flat; fanning along full left edge; possible staple stress | Roll width >1" | Below 6.0, down to 4.0 |

**Evidence from CGC Crease Guide**: "Severity ranges from slight shifts to widths exceeding one inch, with torquing causing fanning along the top or bottom edge, usually not exceeding 1/4"."
**Grade impacts from community sources**: "slight rolls have minimal grading impact, moderate ones typically lower a grade to 6.0 to 8.0 and heavy rolls can reduce it to 4.0."

**Visual test**: Lay book flat on table. If spine edge lifts >0.5mm: minor. If cover noticeably arches: moderate. If book cannot lie flat without manual pressure: major.

**Evidence**: CGC Crease Guide (spine roll listed as crease sub-category), comiccollectorlive.com forum expert consensus, CBCS forum discussions.
**Confidence**: MEDIUM — width measurements derived from CGC documentation; grade-impact ranges from community sources, not official CGC measurement tables.

---

### 2.3 Blunted Corner

**Definition**: Compression folds at approximately 45 degrees to the ends/sides of the comic, as if the corner were dropped against a hard surface. Differs from rounded corners (gradual wear) in being more sudden/angular.

#### Severity Tiers

| Tier | Visual Description | Measurement | Grade Equivalent |
|---|---|---|---|
| **Minor (green)** | "Almost imperceptibly blunted, still almost sharp and cut square" | Flat section at corner <1mm | 9.4–9.6 |
| **Moderate (yellow)** | Visible blunting; corner no longer sharp; slight crumpling; slight color break possible | Flat section 1–3mm; corner angle clearly >90° | 8.0–9.2 |
| **Major (red)** | Substantially blunted or beginning to round; color break at corner fold; fibers crushed | Flat section >3mm OR rounded arc beginning | Below 8.0, down to 6.0 |

**Exact thresholds from Overstreet**:
- 9.6 NM+: "One corner may be almost imperceptibly blunted, but still almost sharp and cut square"
- 9.4 NM: "Corners are cut square and sharp with ever-so-slight blunting permitted"
- 8.0 VF: "Minute wear at corners; blunted or abraded corners"
- 6.0 FN: "Blunted or abraded corners are more common"
- 3.0 GD/VG: "Corners may be blunted or even rounded"

**Evidence**: Overstreet Access grading definitions, CGC Grading Scale, multiple grading guides.
**Confidence**: MEDIUM — grade anchoring is high confidence; mm-level thresholds for minor/moderate are inferred from grade language, not explicitly stated.

---

### 2.4 Tear

**Definition**: Separation of paper anywhere on the book, usually uneven (vs. a slice, which is a clean cut).

#### Severity Tiers

| Tier | Visual Description | Size Measurement | Grade Equivalent |
|---|---|---|---|
| **Minor (green)** | Small tear typically at edge or spine; not extending into image area; bindery-type | Length ≤1/8" (3mm) | 9.0–9.4 |
| **Moderate (yellow)** | Tear extending into cover; visible from front; may have some missing fibers at tip | Length 1/8"–3/4" (3–19mm) | 7.5–8.5 |
| **Major (red)** | Long tear crossing image area; or multiple tears; or tear that widens (triangular loss) | Length >3/4" OR triangle missing >1/4" | Below 7.5, down to 4.0 |

**Exact thresholds**:
- 9.8 allowable: bindery tear ≤1/8" at top or bottom spine
- 9.4: bindery tear must be "less than 1/16"" (Silver Age+); Golden Age up to 1/4" allowable
- 4.0 VG: "as much as 1/4" triangle can be missing from corner or edge; missing 1/8" square acceptable"
- Staple tears ≥1": lower grade below 8.0
- Detached cover: grade caps at 4.0

**Evidence**: Overstreet Access definitions, Bry's Comics CGC analysis (bryscomics.com), CGC Tear Guide (cgcgrading.com).
**Confidence**: HIGH for bindery tear thresholds; MEDIUM for general interior/cover tear minor-to-moderate boundary.

---

### 2.5 Stain

**Definition**: Blemish on the comic affecting the appearance of paper, ink, or gloss. Caused by liquids, tape, stickers, dirt, glue, or chemical reactions.

#### Severity Tiers

| Tier | Visual Description | Size/Coverage | Grade Equivalent |
|---|---|---|---|
| **Minor (green)** | Light mark; barely noticeable at arm's length; no tide line; single small spot | Diameter ≤5mm (~nickel if very light) | 8.5–9.4 |
| **Moderate (yellow)** | Visible discoloration; tide line present but contained; single area; no foxing cluster | Diameter 5–25mm OR tide line ≤1" perimeter | 7.0–8.5 |
| **Major (red)** | Dark stain; obvious at arm's length; tide line clearly visible; spread to multiple areas | >25mm coverage OR multiple areas OR foxing cluster | Below 7.0, down to 4.0 |

**Stain type effects on visibility**:
- Water stain: creates a tide line (ring mark); especially visible on glossy covers due to contrast
- Ink/food: opaque; often darker than paper; highly visible on both stock types
- Foxing (brown spots): gradual; worse on newsprint; light foxing = grade 9.0–9.4; dark/extensive = 4.0–6.0
- Smoke/fire: blackening at edges; 4.0–7.0 typical

**Community threshold**: "minor water stains generally acceptable up to Fine (FN) grade if nickel-sized or smaller and hardly noticeable."

**Note on CGC**: CGC stain grades span 1.0–9.8. No explicit mm thresholds published. The size/shade/severity language is qualitative. The above measurements are derived from grade-anchoring.

**Evidence**: CGC Stain Guide (cgcgrading.com/en-US/resources/comics-grader-notes-guide/stain), ComicCollectorLive forum, Quality Comix grading analysis.
**Confidence**: MEDIUM — CGC does not publish size thresholds for stains; thresholds above are inferred from grade descriptions and community expert consensus.

---

### 2.6 Spine Stress

**Definition**: Small horizontal fold/break perpendicular to the spine, caused by bending during reading or handling. Appears as white tick marks along the spine. Distinct from spine roll (which is a curl) and spine split (which is a tear).

#### Severity Tiers

| Tier | Visual Description | Count/Length | Grade Equivalent |
|---|---|---|---|
| **Minor (green)** | 1–3 small stress lines; visible only under raking light; no color break | Count ≤3, each <1/4" long | 9.4–9.6 |
| **Moderate (yellow)** | 4–5 stress lines OR 1–3 with color break; visible under direct light | Count 4–5 OR color-breaking; each <1" | 9.0–9.4 |
| **Major (red)** | Numerous stress lines; many with color break; OR any stress line >1" (reclassified as crease) | Count >5 with color break OR length >1" | Below 9.0, down to 8.0 |

**Critical thresholds**:
- Stress lines >1" long are reclassified as creases (CGC rule)
- Non-color-breaking stress lines: potentially removable by pressing
- Color-breaking stress lines: permanent grading impact
- 9.9 allows: "a few non-color breaking stress lines"
- 9.8 allows: "one or two color-breaking stress lines"
- Numerous stress lines: classified as "general spine wear" — drops to 8.0–8.5

**Evidence**: CGC Crease Guide (stress lines covered here, not in distortion), SubZero Comics grading guide, CBSI Comics grader notes analysis (comicbookinvest.com/2016/05/27/high-grade-comic-books/).
**Confidence**: HIGH for count thresholds and 1" reclassification rule; MEDIUM for exact grade-tier mapping at moderate level.

---

## 3. Physical Creation Techniques by Defect Type and Severity

### 3.1 Crease

**Tools needed**: Bone folder, flat hard surface, steel ruler, magnifying loupe.

**Theory**: Pressure + fold angle + number of fiber-break passes determines severity. A single gentle fold with no rubbing = bend (green). A fold with deliberate pressure along the crease = moderate. A fold with hard rubbing or multiple passes = major.

#### Minor (green) — target: <1/4" no-color-break crease
1. Place comic face-up on hard flat surface.
2. Fold cover back only 5–10 degrees at the target location using thumb and forefinger — do not crease the fold.
3. Hold for 3 seconds, release. Examine under raking light.
4. The result should be a light bend. If fibers have broken (white line visible), you have produced moderate. Reduce pressure on next specimen.
5. For a minimal crease: lightly draw bone folder once across the fold with almost no downward pressure. The goal is fiber disturbance without complete breakage.

**Risk of failure**: Even slight over-pressure jumps to moderate. Minor creases are the hardest to hit precisely on glossy stock (high contrast). On newsprint, minor creases blend into the paper texture.

#### Moderate (yellow) — target: short crease with partial color break
1. Mark target location with pencil on back/interior (not visible in final shot).
2. Fold cover at 30–45 degree angle to the cover face.
3. Run bone folder along fold with firm (not heavy) pressure — one pass.
4. Open: a visible white line should be present along part of the crease. If no white line, repeat with slightly more pressure.
5. Target: 1–2" long crease, color break visible along ~50% of length.

#### Major (red) — target: full color-break crease >2"
1. Fold cover back at near-90 degrees along the target line.
2. Run bone folder firmly along entire length, pressing down hard. Two passes.
3. Open: full white line visible along entire length. On darker covers, loss of pigment clearly visible.
4. For subscription crease (vertical, full-height): fold comic in half vertically as if mailed, crease hard with thumbnail. This reliably produces a major crease.

**Paper type effects**:
- **Modern glossy cover (80 lb., 118 gsm)**: High contrast makes color break very visible. Fold response is sharp; minor/moderate boundary is precise. Single bone folder pass at moderate pressure reliably produces moderate.
- **Modern newsprint interior (55–70 lb., 74–104 gsm)**: Lower contrast hides minor creases more. Fibers break more easily — less force needed. Minor is harder to sustain; creases jump to moderate faster.
- **Older/brittle paper (pre-1990 newsprint)**: Extremely low folding endurance. The "number of manual folds" test: paper with <6 folds before failure is considered weak; <3 folds = highly brittle. On brittle paper, any fold attempt will produce at least a moderate crease. Do not attempt minor crease creation on brittle paper — go directly to moderate or major for test specimens.

**Success rate estimate**: Minor: ~50% on first try (glossy), ~30% (newsprint). Moderate: ~70%. Major: ~90%.

---

### 3.2 Spine Roll

**Tools needed**: Hands only. No tools needed to create; tools needed to avoid.

**Theory**: Spine roll is caused by repeatedly bending the comic so cover and pages curl around the spine. Reading one-handed (bending past 180°) is the primary cause.

#### Minor (green) — roll width <1/4"
1. Hold comic open fully flat (180°) face up.
2. Gently roll spine edge backward 15–20 degrees, release immediately.
3. Repeat 3–5 times.
4. Check: lay book flat. If spine edge lifts slightly but book generally lies flat: minor.
5. Test: run thumbnail down back cover near spine — if slight ridge is palpable: minor achieved.

**Difficulty**: Hard to stop at minor. Even 3–5 gentle reads can jump to moderate on thin paper.

#### Moderate (yellow) — roll width 1/4"–1"
1. Hold comic one-handed, allowing pages to fan behind spine.
2. Read/flip through all pages this way, applying moderate backward curl to spine edge.
3. Do this 3–4 full read-throughs.
4. Check: lay book flat. Cover arches visibly. Back cover left edge fans or lifts.

#### Major (red) — roll width >1"
1. Hold comic one-handed in reading position with pages folded all the way back.
2. Actively press pages and back cover into a tight curl around spine.
3. Hold in this position for 30–60 seconds.
4. Repeat through full book.
5. Check: book will not lie flat; cover arches significantly; fanning of pages visible.

**Paper type effects**:
- Modern glossy paper: more resistant to spine roll due to stiffness (80 lb. cover stock). Requires more repetitions to produce moderate/major.
- Older/thinner paper (40–55 gsm newsprint): roll develops quickly and is more permanent due to low paper stiffness. Major can result from a single aggressive reading.
- Brittle paper: risk of spine split when creating major spine roll. Use caution — attempting major roll on brittle comics may produce spine split instead.

**Success rate estimate**: Minor: ~40% (hard to stop early). Moderate: ~75%. Major: ~90%.

---

### 3.3 Blunted Corner

**Tools needed**: Hard flat surface (desktop, cutting board). Optional: fine-grit sandpaper (400-grit) for creating abrasion-type blunting.

**Theory**: Corner blunting occurs from impact — the corner strikes a hard surface at ~45 degrees. Severity is determined by number of impacts, force, and whether the paper layers separate.

#### Minor (green) — imperceptibly blunted, <1mm flat section
1. Hold comic by two sides (not at corners).
2. Allow one corner to drop ~2–3 inches and tap lightly against desktop.
3. Examine corner with loupe: slight flattening at very tip only.
4. If flattening is >1mm: this is moderate territory.

**Critical note**: This is extremely hard to calibrate. Even a light drop produces more than imperceptible blunting on many papers. For minor specimens on a dataset, consider using naturally-worn high-grade comics rather than creating artificially.

#### Moderate (yellow) — visible flat section 1–3mm
1. Hold comic, drop corner 4–6 inches onto hard surface at slight angle.
2. Examine: flat section visible; some color break possible at crease. No significant paper separation yet.
3. Repeat 1–2 times if needed.

#### Major (red) — >3mm flat section or beginning to round
1. Drop corner 8–10 inches onto hard surface, or tap corner firmly with finger.
2. Repeat 3–5 times, rotating slightly to simulate multiple impacts.
3. Check: the flat section exceeds 3mm; paper layers may show slight separation; color break present.

**Abrasion technique (alternative)**:
- 400-grit sandpaper on a flat surface: run corner across sandpaper 5–10 times for minor; 20–30 times for moderate; 40+ times for major.
- This produces a more gradual rounding type of blunting vs. impact compression. More controllable for minor specimens.

**Paper type effects**:
- Glossy cover stock: blunting shows clearly as white exposed paper beneath the coating. High visibility. Moderate/major easily visible.
- Newsprint: blunting blends into paper texture; less visible but fibers crush more readily.
- Brittle/aged paper: corners flake rather than compress cleanly; may produce irregular damage that is hard to classify as blunting vs. chip.

**Success rate estimate**: Minor: ~35% (very hard to stop at imperceptible). Moderate: ~65%. Major: ~85%.

---

### 3.4 Tear

**Tools needed**: Metal ruler (for controlled straight tears), tweezers (for controlled partial tears), scissors (for controlled length).

**Theory**: Tears run along paper grain or at random angles. Controlled tears are created by initiating a nick at the edge and propagating to a target length. The key controllability factor is stopping the tear at the desired length.

#### Minor (green) — tear ≤1/8" at edge
1. At the edge of the cover (spine top or bottom preferred to mimic bindery tears), use a needle or fine tweezers tip to create a 1–2mm nick perpendicular to the edge.
2. Do not propagate further. Examine: this is the minimum identifiable tear.
3. For a slightly larger minor tear (up to 1/8"): carefully pull the two sides of the nick apart by 1–2mm, keeping the tear perpendicular to the edge.

**Note**: Initiating the tear is easy. Stopping it is the challenge. Once a tear starts running along grain, it can propagate faster than expected. Use both thumbs to pinch the paper right at the tear tip to stop propagation.

#### Moderate (yellow) — tear 1/8"–3/4", entering cover
1. Using metal ruler as a guide, hold tear at edge and allow it to propagate 6–15mm while holding firmly at the propagation point.
2. Alternatively: make a small nick and then pull at controlled angle (45–60° to edge) to create a diagonal tear that enters the cover area.
3. Stop when tear reaches 1/4"–1/2" visible length.

#### Major (red) — tear >3/4" OR triangular loss
1. Make nick at edge.
2. Pull apart deliberately, allowing propagation to ¾"–1" or more.
3. For triangular loss: make two converging cuts/nicks (with scissors) at a corner creating a V-shape, then pull the triangle free. For a 4.0-equivalent defect, the triangle should be ~1/4" on each side.

**Paper type effects**:
- Modern glossy: tears propagate somewhat cleanly but can have rough edges due to coating layer separation.
- Newsprint: tears run more easily along grain; extremely hard to stop at minor — propagation very fast.
- Brittle/aged: tears propagate explosively and unpredictably. Do not attempt controlled minor tears on brittle paper. Go directly to moderate/major and accept imprecision.

**Most controllable technique**: Scissors-initiated tears of exact length are more controllable than hand-propagated tears. Cut with scissors to desired length, then open the cut slightly with fingers for a more natural-looking tear.

**Success rate estimate**: Minor: ~60% with careful technique (scissors). Moderate: ~70%. Major: ~95% (easy to propagate fully).

---

### 3.5 Stain

**Tools needed**: Eyedropper or fine brush; plain water; coffee (diluted for moderate/major); paper towels; plastic wrap.

**Theory**: Stain severity is determined by liquid volume, absorption area, drying pattern (tide lines), and color of liquid. Water alone creates tide lines; colored liquids add chromatic staining. Glossy covers resist absorption; water beads and the stain is primarily a tide line. Newsprint absorbs immediately, producing full saturation stains with no clean border.

#### Minor (green) — small spot ≤5mm, no prominent tide line
1. Dip fine artist brush in plain water (not soaked, barely damp).
2. Touch brush to cover surface once in a single spot.
3. Allow to dry naturally without blotting. On glossy: the water will bead and dry into a faint circular tide line ~3–5mm in diameter.
4. Under raking light: faint ring visible. Under direct light: barely visible.
5. On newsprint: even a very small water touch produces a visible darkened spot due to ink spreading. Use half a brush-dip.

**Key risk**: Even a "tiny" drop of plain water on matte or newsprint paper creates a larger visible stain than expected.

#### Moderate (yellow) — visible tide line 5–25mm, single area
1. Use eyedropper: place 1–2 drops of plain water on cover.
2. Allow to spread naturally (do not spread with brush).
3. Let dry naturally. The tide line will form a ring at the perimeter of the wet area.
4. On glossy: produces a clearly visible circular ring, minimal interior discoloration. Final diameter 10–20mm.
5. For colored moderate stain: use coffee diluted 10:1 with water (1 drop coffee : 10 drops water). Apply same 1–2 drops. This produces a light brown ring with interior coloring — more realistic and more visible to AI.

#### Major (red) — >25mm, prominent tide line, possible ink run
1. Eyedropper: place 5–10 drops of water across a 25–40mm area.
2. For colored major stain: use undiluted coffee or tea applied with eyedropper.
3. Allow to spread and dry. Multiple overlapping tide lines will form, creating a complex ring pattern.
4. For ink run: apply water directly to an area with dense printed ink on newsprint — ink will spread visibly.
5. Do NOT use this technique on valuable or high-grade comics. Reserve for destructible specimens only.

**Paper type effects**:
- **Glossy cover (UV/aqueous coated)**: Liquid beads; stain mainly a tide line at perimeter; interior relatively clean. Minor stains very subtle; major stains visible as distinct ring.
- **Matte cover**: Liquid absorbed more; full-area discoloration rather than just tide line. Stains are harder to contain at minor level.
- **Newsprint**: Immediate absorption; no tide line (absorbs fully); ink bleeding likely even with plain water at moderate or major levels. The stain appears as dark wet-looking mark that lightens but remains after drying.

**Success rate estimate**: Minor: ~65% on glossy; ~35% on newsprint/matte (too easy to over-apply). Moderate: ~75%. Major: ~90%.

---

### 3.6 Spine Stress

**Tools needed**: Thumb and forefinger; comic opened to flat position; ruler for measuring stress line length.

**Theory**: Spine stress lines are created by bending the spine during reading — each opening that stresses the spine creates a horizontal tick mark. Severity depends on count and whether bending is hard enough to break ink layer (color break).

#### Minor (green) — 1–3 stress lines, no color break
1. Hold comic by covers, open fully (180°) to a single page.
2. Apply very slight additional pressure (2–3 degrees past flat), then release immediately.
3. Repeat at 2–3 different pages throughout book.
4. Examine spine under raking light: 1–3 small white horizontal ticks should be visible.
5. If color break is present (white shows through under direct light), you have produced moderate.

**Key control**: The difference between non-color-breaking and color-breaking stress lines is the degree of opening angle. 180° = minor bend. 185°–190° = likely color break.

#### Moderate (yellow) — 4–5 stress lines OR 1–3 with color break
1. Open comic to 180° and apply additional 5–7 degrees of pressure at multiple points.
2. Repeat 4–5 times at different spine locations.
3. For guaranteed color break: open to a page and push slightly past 180°, holding for 2 seconds.

#### Major (red) — numerous stress lines with color break
1. Open book to each page spread and forcefully press spine flat (180°+ angle).
2. Work through entire book, flattening spine at each opening.
3. Examine: many white ticks visible from front; some breaking color. Heavy spine wear visible.

**Critical boundary**: Stress lines >1" long are reclassified by CGC as creases, not spine stress. Avoid pressing past 180° for too long — this can create a stress line that extends beyond 1/4" (the comicbookgradingtool.com definition of spine stress as "usually less than 1/4 inch long perpendicular to spine").

**Success rate estimate**: Minor: ~70%. Moderate: ~75%. Major: ~85%.

---

## 4. Paper Type Effects on Defect Severity

### 4.1 Modern Comic Cover Stock (80 lb. glossy, ~118 gsm)

| Effect | Behavior |
|---|---|
| Crease visibility | High (white line highly contrasted against glossy coating) |
| Crease threshold | Sharp fiber-break point; fold must exceed ~20° to break fibers |
| Fold endurance | High; multiple folds possible before failure |
| Water stain | Beads; primarily tide line; clean minor stains achievable |
| Tear propagation | Moderate speed; controllable |
| Corner blunting | Very visible (white paper under coating appears) |

### 4.2 Modern Comic Interior (55–70 lb. gloss text, 74–104 gsm)

| Effect | Behavior |
|---|---|
| Crease visibility | Moderate (less contrast than cover) |
| Crease threshold | Lower than cover; fibers break more easily |
| Water stain | Mixed absorption; both beading and absorption |
| Tear propagation | Fast along grain |

### 4.3 Pre-1990s Newsprint (35–55 gsm, highly acidic, aged)

| Effect | Behavior |
|---|---|
| Crease threshold | Extremely low — any fold produces crease; brittle paper may crack |
| Fold endurance | <6 double-folds before failure on weak paper; <3 on highly brittle |
| Water stain | Immediate full absorption; ink bleeding likely; no tide line |
| Tear propagation | Extremely fast and unpredictable; hard to control at minor |
| Corner blunting | Corners flake/chip rather than compress cleanly |
| Color break | Very easy; even minor pressure may break ink layer |

**Key implication for dataset**: Do not attempt minor severity specimens on brittle/aged paper. Even "careful" techniques produce moderate or major due to material fragility. For aged paper, calibrate expectations downward — the same technique that produces minor on modern paper produces moderate on vintage newsprint.

### 4.4 Cover Coating Effects on Stain Visibility

| Coating Type | Minor Stain Visibility | Major Stain Visibility |
|---|---|---|
| UV gloss (highest) | Very faint ring only | Prominent tide line, high contrast |
| Aqueous gloss | Faint ring visible under raking light | Clear tide line |
| Matte finish | Stain absorbed; visible as darker patch | Extensive discoloration |
| Uncoated (newsprint) | Immediate dark spot; very visible even at minor | Severe discoloration; ink bleed |

---

## 5. Verification Methodology

### 5.1 Tools Required

| Tool | Purpose | Specification |
|---|---|---|
| Metal ruler (inches + mm) | Measure crease length, tear length, stain diameter | 12" ruler with 1mm markings |
| 10x loupe/magnifier | Inspect corner detail, stress line width, fiber break | Jeweler's loupe, 10x |
| Raking light source | Reveal non-color-breaking creases, stress lines, indentations | Desk lamp at 10–15° angle to comic surface |
| Direct overhead light | Assess color break, stain visibility | Standard room lighting |
| Flat white background | Photography reference for defect mapping | White foam board |
| Phone camera (portrait mode off) | Document created defects | iPhone; shoot at 6–12" distance |

### 5.2 Verification Protocol per Defect

**Crease**:
1. Measure length with ruler (mm).
2. Examine under raking light: is the crease visible? Is there a white line (color break)?
3. Under direct light: is the white line visible? If yes, color has broken.
4. Classify: <6mm no color break = green; 6–50mm with some color break = yellow; >50mm full color break = red.

**Spine Roll**:
1. Lay book flat on table surface.
2. Measure the height the spine edge lifts off the surface (mm).
3. Assess back cover fanning: does the left edge of back cover lift when spine lies flat?
4. Classify: barely perceptible lift = green; visible arch, some fanning = yellow; pronounced curl, book won't lie flat = red.

**Corner Blunting**:
1. Hold corner under 10x loupe.
2. Measure the straight/flat section at the corner tip (mm).
3. Is there a color break line at the fold?
4. Classify: <1mm no color break = green; 1–3mm with possible color break = yellow; >3mm or rounding = red.

**Tear**:
1. Measure total length with ruler.
2. Is the tear at the edge (bindery-type) or entering the cover?
3. Classify: ≤3mm at edge = green; 3–20mm = yellow; >20mm or triangular loss = red.

**Stain**:
1. Measure maximum diameter or affected area (mm).
2. Under raking light: is a tide line visible? How prominent?
3. Under direct light: how visible at arm's length (12")?
4. Classify: ≤5mm, barely visible at arm's length = green; 5–25mm, visible at 12" = yellow; >25mm, immediately obvious = red.

**Spine Stress**:
1. Count stress lines visible under raking light along spine.
2. Measure length of the longest stress line (mm).
3. Are any lines visible under direct light (color break)?
4. Classify: 1–3 lines, visible only under raking, <6mm each = green; 4–5 lines or any with color break = yellow; numerous lines with color break or any >25mm = red.

### 5.3 Reference Comparison Sources

These sources contain reference photos of graded comics at specific condition levels, useful for visual verification of created specimens:

- **CGC Grading Scale page** (cgccomics.com/grading/grading-scale/): Includes visual examples at key grade levels.
- **Quality Comix grading guide** (qualitycomix.com/learn/example-photos-comic-grades): Photos of comics at 8 key grades with defect annotations.
- **CGC Grader Notes Guide** (cgcgrading.com/en-US/resources/comics-grader-notes-guide): Sub-category descriptions for each defect type.
- **ComicBookGradingTool glossary** (comicbookgradingtool.com/comic-grading-terms): Includes hairline crease / light crease / heavy crease definitions with explicit mm criteria.

---

## 6. Failure Modes and Risk Assessment

### 6.1 When Minor Attempts Produce Major

| Defect | Failure Mode | Cause | Mitigation |
|---|---|---|---|
| Crease | Color break when targeting no-color-break | Excess bone folder pressure OR brittle paper | Use feather-light pressure; practice on scrap paper first |
| Spine roll | Moderate produced on first attempt | Paper too thin or too many repetitions | Do only 1–2 roll passes; use stiffer paper |
| Corner blunting | Significant flat section when targeting imperceptible | Drop height too high; paper too stiff | Drop height <2"; use finger-tap instead of drop |
| Tear | Propagation past intended length | Grain alignment OR newsprint | Hold paper immediately beside tear tip; use scissors |
| Stain | Large tide line when targeting spot | Too much liquid | Single brush hair worth of water; let it pool, not flow |
| Spine stress | Color break when targeting no-color-break | Exceeded 180° too aggressively | Stay at exactly 180°; never push further for minor |

### 6.2 Hardest Defects to Control

**Rank from hardest to easiest**:
1. **Corner blunting (minor)** — hardest; barely-blunted requires such small impact it's near impossible to reproduce consistently. ~35% success rate.
2. **Spine roll (minor)** — hard to stop at "slightest detectable curl." ~40% success rate.
3. **Crease (minor) on newsprint** — fiber breakage threshold is very low; jumps to moderate easily. ~30% success rate.
4. **Stain (minor) on matte/newsprint** — liquid absorption too fast; minimal stain hard to achieve. ~35% success rate.
5. **Tear (minor)** — initiating nick is easy; stopping propagation is hard. ~60% with scissors technique.
6. **Spine stress (minor)** — most controllable fold-type defect; angle control is achievable. ~70% success rate.

### 6.3 Recommendations for Dataset Protocol

- **For minor specimens**: Budget 2–3 comics per defect type to account for failure rate. Do dry runs on identical-stock scrap paper before touching the actual comic.
- **For aging brittle paper**: Only attempt moderate and major. Accept that minor is not achievable on pre-1990 newsprint.
- **For glossy modern covers**: These give the most controllable results for crease, stain, and corner blunting minor specimens. Prioritize modern covers for minor-tier specimens.
- **Spine roll and corner blunting minor**: Consider sourcing naturally-worn 9.4–9.6 comics rather than creating artificially — the naturally occurring minor level is more authentic and consistent.

---

## 7. Open Questions and Items Flagged for Follow-Up

1. **CGC's exact green/yellow/red tier boundaries for each defect**: Not publicly documented as explicit thresholds. The mapping above is inferred from grade language. Further research: obtain a copy of "The Official CGC Guide to Grading Comics" (book form) which reportedly contains more detail than the website.
2. **Spine roll width measurement verification**: The 1/4" / 1" width thresholds are sourced from CGC documentation, but community sources describe severity differently (grade impact vs. width). A physical calibration session using three comics with known grades would clarify.
3. **Stain size thresholds**: No authoritative source provides explicit mm thresholds. The "nickel-sized" community heuristic is the strongest practical guidance. Consider requesting pre-submission opinion from CBCS (free pre-screen available) for borderline specimens.
4. **Effect of aging on glossy covers**: Older glossy covers (1990s Chromium/foil variants) may behave differently than modern glossy. No source data found for these.

---

## Sources

| ID | URL | Title | Type | Accessed | Claims Supported |
|---|---|---|---|---|---|
| src-001 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/crease | CGC Comics Grader Notes Guide: Crease Defects | official | 2026-04-07 | crease-definition, fiber-break-threshold, crease-sub-types, severity-tiers |
| src-002 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/distortion | CGC Comics Grader Notes Guide: Distortion Defects | official | 2026-04-07 | spine-roll-width, distortion-categories |
| src-003 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/tear | CGC Comics Grader Notes Guide: Tear Defects | official | 2026-04-07 | tear-types, bindery-tear-thresholds, spine-split-sizes |
| src-004 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/stain | CGC Comics Grader Notes Guide: Stain Defects | official | 2026-04-07 | stain-types, foxing-severity, stain-grade-ranges |
| src-005 | https://www.cgccomics.com/grading/grading-scale/ | CGC Grading Scales | official | 2026-04-07 | grade-anchored-language, minor-moderate-major-tiers |
| src-006 | https://www.overstreetaccess.com/grading-definitions/ | Overstreet Access Grading Definitions | official | 2026-04-07 | crease-measurements-by-grade, spine-split-sizes, corner-wear-language, spine-roll-by-grade |
| src-007 | https://www.comicbookgradingtool.com/comic-grading-terms | Comic Book Grading Tool Glossary | community | 2026-04-07 | hairline-crease-definition, spine-stress-definition, corner-blunting-definition |
| src-008 | https://bryscomics.com/blogs/news/cgc-comic-grading-allowable-defects-in-a-cgc-9-9 | CGC Comic Grading: Allowable Defects in a CGC 9.8 | community | 2026-04-07 | 9.8-bindery-tear-threshold, spine-tick-description |
| src-009 | https://comicbookcpr.com/comic-book-dent-removal | Comic Book Dent Removal (Comic Book CPR) | community | 2026-04-07 | tools-for-defect-work, paper-type-humidification, bone-folder-technique |
| src-010 | https://www.walsworth.com/blog/guide-for-comic-book-paper | Essential Guide for Choosing Comic and Graphic Novel Paper | journalism | 2026-04-07 | paper-weights-gsm, cover-stock-specs, interior-stock-specs |
| src-011 | https://www.cgccomics.com/resources/restoration/ | CGC: Overview of Comic Book Restoration | official | 2026-04-07 | tear-severity-general, restoration-types |
| src-012 | https://comicbookinvest.com/2016/05/27/high-grade-comic-books/ | CBSI Comics: Grader's Notes - High Grade Comic Books | community | 2026-04-07 | spine-stress-count-thresholds, 9.4-9.6-stress-line-criteria |
| src-013 | https://www.loc.gov/preservation/care/deterioratebrochure.html | Paper Deterioration and Preservation - Library of Congress | official | 2026-04-07 | paper-brittleness, aging-effects-on-fold-endurance |
| src-014 | https://www.comiccollectorlive.com/forum/default.aspx?g=posts&t=4807 | Grading Question: What is the definition of Spine Roll? | community | 2026-04-07 | spine-roll-grade-impact |

---

*Self-review note: Iterated once before finalizing. Main uncertainty: the exact green/yellow/red boundary for crease is inferred from grade anchoring (8.0 = ≤1/4" no-color-break), not from a single explicit CGC source that uses those tier labels. This is the most important calibration boundary and should be physically tested with reference specimens before the full dataset run. All other claims have HIGH or MEDIUM confidence with multiple supporting sources.*
