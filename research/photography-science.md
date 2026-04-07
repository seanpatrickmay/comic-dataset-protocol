# Photography Science for Comic Book Defect Capture

**Axis**: Photography for Defect Detection  
**Date**: 2026-04-07  
**Researcher**: agent/photography-science  

---

## Summary

This document synthesizes photography technique research for capturing comic book defects for AI analysis. The core finding: defect visibility is almost entirely a lighting problem, not a resolution problem. Different defect types require fundamentally different lighting geometries — there is no single "best" setup. A minimum two-shot protocol (45° diffuse + 10–15° raking from the left) captures the majority of informative defects. A four-shot protocol adds coverage for glossy and missed-axis defects. Beyond four shots, information gain diminishes sharply.

**Key open questions**: Whether cross-polarization setup cost is justified for our glossy-cover subset, and whether UV adds discriminative signal for foxing beyond what visible-light raking captures.

---

## 1. Lighting Angles for Each Defect Type

### Claim 1.1 — Creases and stress lines are only reliably detected under raking light

**Claim**: Creases, bends, stress lines, and spine roll are frequently invisible under standard 45° diffuse lighting and become visible only when light is raked across the surface at a shallow angle (5–15°). CGC's own grading guides note that some bends are "only visible in a raking light."

**Evidence**:
- CGC's Grader Notes guide for creases states certain defects are "only visible in a raking light." Non-color-breaking stress lines are hard to spot head-on but visible under raking light. Cockling "viewed best under a raking light." [src-001]
- Conservation science: raking light "can amplify the appearance of indentations, undulations... cracks, blisters, pits, tears, scratches, cockles and other types of damages or distortions." [src-002]
- Industrial surface defect research: dent and inclusion defects (analogous to creases and impressions) show up to 18.7% increase in detection precision when illuminant angle is varied — they are "greatly affected by illuminant angles." [src-005]

**Sources**: [src-001], [src-002], [src-005]  
**Confidence**: HIGH — 3 concordant sources across grading practice, conservation science, and machine vision research

---

### Claim 1.2 — Optimal raking angle for paper/cover surface defects is 10–15°

**Claim**: The museum/conservation standard for raking light on flat objects (paintings, paper, prints) is 5–15° from the plane of the surface (i.e., 75–85° from vertical). For paper with moderate texture like comic covers, 10–15° produces better shadow contrast than 5° while avoiding the washout that occurs at 20°+.

**Evidence**:
- Conservation Wiki (AIC): "one light source positioned at a shallow angle to the object's surface, typically between 5 and 15 degrees." [src-002]
- Industrial paper web inspection: a 10° illumination angle with a 90° camera viewing angle "can detect elevated defects and other surface defects on standard paper and board machines." [src-004]
- For impasto paintings (raised paint, analogous to heavy embossing or warped covers): 15–20° from vertical is recommended. The same principle scales down — the shallower the angle, the more low-relief detail is cast in shadow. [src-003]
- Hamilton Kerr Institute guidance: raking light "documents surface irregularities" including "craquelure, cupping or tenting" — direct analog to comic spine roll and cover warping. [src-007]

**Practical note**: At 5°, the light source must be positioned very far from the subject to avoid severe fall-off. 10° is the practical floor for consumer LED panels at tabletop distances. 15° is the preferred starting point.

**Sources**: [src-002], [src-004], [src-003], [src-007]  
**Confidence**: HIGH

---

### Claim 1.3 — Stains, foxing, and tanning are best detected under diffuse front lighting, not raking

**Claim**: Stains, foxing, age tanning, and water damage are surface chemistry defects with negligible topographic relief. Raking light does not improve their visibility and may actually reduce it by creating competing shadows. Standard 45° two-light diffuse setup (cultural heritage standard for color imaging) is optimal.

**Evidence**:
- Conservation science: UV fluorescence is the gold standard for foxing not yet visible to the naked eye — "UVF is effective in mapping adhesives and revealing foxing and molds... particularly valuable for detecting mold and foxing that are not yet visible to the naked eye." [src-008]
- Tidelines (water damage rings) "generally exhibit UV fluorescence, sometimes even those that are not yet visible to naked eye." [src-008]
- FADGI standard: "most Cultural Heritage imaging is done with very flat proscriptive lighting, typically two lights mounted 45° from the subject" — this is the baseline for color-accurate stain documentation. [src-006]
- Industrial machine vision: diffuse lighting "spreads light evenly, reducing glare on shiny or curved surfaces" and is preferred when color discrimination (not topography) is the goal. [src-010]

**Practical note for AI dataset**: Visible-light diffuse shots capture stains that have already developed color contrast. UV requires a separate setup ($30–80 UV LED panel, dark room) and post-processing. For an initial dataset, visible-light diffuse is sufficient for moderate-to-major stains. Minor staining may be underdetected without UV.

**Sources**: [src-006], [src-008], [src-010]  
**Confidence**: HIGH for diffuse-light stain capture; MEDIUM for UV necessity at AI-detectable severity thresholds

---

### Claim 1.4 — Corner wear and spine stress require a combination: 45° diffuse for color breaks, raking for indentation

**Claim**: Corner wear presents as both color-break (ink abraded away — visible under diffuse light) and paper fiber deformation (visible under raking). Spine stress lines are primarily topographic and require raking. A two-shot protocol (diffuse + raking) captures both aspects.

**Evidence**:
- CGC grading guides: spine stress lines are "small horizontal breaks resulting from spine bending" — the break is topographic (fiber deformation), not necessarily a color break. Visible under raking. [src-001]
- Corner wear that has broken color (ink rubbed off) will appear as a pale spot under any frontal lighting — no special technique needed. Sub-surface fiber damage at corners requires raking. [src-001]
- Conservation practice: "multiple raking light images are usually obtained during an examination with each using light angled from a different direction" — single-axis raking can miss defects aligned with the light direction. [src-002]

**Sources**: [src-001], [src-002]  
**Confidence**: HIGH

---

### Claim 1.5 — Minor defects require shallower angles than major defects

**Claim**: Low-relief defects (light bends, fine stress lines) require shallower raking angles (5–10°) to cast shadow. Major defects (hard creases, spine rolls, heavy warping) are visible at steeper angles and are reliably detected even at 45°.

**Evidence**:
- Industrial paper inspection: "low-angle reflection uses typically a 15–20 degree camera angle and 15–20 degree illumination angle to provide a mirror reflection from the paper surface, enabling detection of very small coating defects." [src-004]
- Forensic evidence photography: oblique lighting (low-angle) "is usually used to show detail by creating shadows on the surface of the evidence" — used for "impressions, tool marks, fingerprints, dusty footwear impressions" (all low-relief). [src-009]
- Conservation: 5° is used when "paint rises from canvas" (very subtle height variation). 15° is used for more visible surface undulation. The angle scales with relief height. [src-003]

**Practical implication for dataset**: If you need to capture light bends reliably, shoot at 10° from two axes (left, top). If you only need major-defect detection, 15° single-axis is sufficient and faster.

**Sources**: [src-003], [src-004], [src-009]  
**Confidence**: HIGH

---

## 2. Raking Light Technique Deep Dive

### Claim 2.1 — Museum/conservation standard is 5–15° from the object surface, with two directions

**Claim**: Professional conservation raking is executed at 5–15° from the plane of the object (not from vertical), using at minimum two directions — "from the top and from the left" — because surface features aligned with a single light direction will not cast shadow and will be missed.

**Evidence**:
- Conservation Wiki: "documenting the object with the light orientation both from the top and from the left is ideal because surface features may align with a single light direction." [src-002]
- Raking light specifically "positions the light source as far from the object as possible to minimize drastic light fall-off." [src-002]
- AIC Media Wiki confirms angle range: typically 5–15° from the surface. [src-002]

**Workflow for comics**:
1. Comic flat on black surface, camera directly overhead (90°)
2. Shot A: single LED panel at left edge, angled to 10–15° from surface — light travels right across cover
3. Shot B: single LED panel at top edge, angled to 10–15° from surface — light travels down across cover
4. Both shots at same exposure settings

**Sources**: [src-002]  
**Confidence**: HIGH — from primary conservation science source [Verified: 2026-04-07]

---

### Claim 2.2 — Single-sided raking is standard; double-sided kills shadow contrast

**Claim**: Raking light must come from one side only. Adding a second light source on the opposite side (to reduce harsh shadows) destroys the topographic shadow contrast that makes the technique work. Fill cards can be used at 90° to the light axis if needed.

**Evidence**:
- Conservation technique: requires "one light source positioned at a shallow angle." [src-002]
- The entire mechanism depends on shadow formation — adding an opposing source fills in the shadows that reveal surface relief. This is the opposite of what you want.
- Cross-polarization technique (different goal): DOES use two-sided lighting, but that technique is for eliminating specular reflections from glossy surfaces, not for topographic detection. The two techniques serve orthogonal purposes. [src-011]

**Sources**: [src-002], [src-011]  
**Confidence**: HIGH

---

### Claim 2.3 — Defects visible ONLY under raking light (not visible at 45° diffuse)

The following defect types are routinely missed by standard diffuse lighting and require raking:

| Defect Type | Why Raking Reveals It |
|---|---|
| Light bends (non-color-breaking) | No ink loss — purely topographic deformation |
| Spine stress lines | Sub-mm surface undulation from fiber stress |
| Cockling / waviness | Low-amplitude undulation invisible without shadows |
| Finger creases | Small crescent deformations, no color break on glossy covers |
| Reader creases (early) | Early-stage fold before ink cracks |
| Subscription crease (pressed) | May be partially pressed but retains fiber memory |
| Dimples and impressions | Point deformations from storage pressure |
| Cover undulation / roll | Broad low-amplitude warp invisible face-on |

**Sources**: [src-001], [src-002], [src-007]  
**Confidence**: HIGH

---

### Claim 2.4 — Consumer LED panel setup for raking light

**Equipment needed**:
- One LED panel with barn doors or a focused beam (a "LED lightline" or a shop LED strip taped to cardboard to narrow the light width works) — the narrower the light source, the harder the shadow edges
- Light stand or stack of books to position light at tabletop edge, angled downward at 10–15° from horizontal
- Camera overhead on tripod (or propped steady), looking straight down

**Alternative (no tripod)**: Mount iPhone on a copy-stand arm or use a stack of books to keep it steady directly overhead. Use the 2-second timer or volume button shutter to avoid camera shake during capture.

**Practical test**: Hold a flashlight 30–40 cm from a comic at tabletop level (roughly 10° elevation) and watch the cover surface. Creases and rolls will become immediately visible as you move the light.

**Confidence**: HIGH (direct derivation from conservation setup principles)

---

## 3. iPhone-Specific Optimization

### Claim 3.1 — Use the main (1x) camera at ≥25 cm, not the ultra-wide, for whole-cover shots

**Claim**: The iPhone main camera (26–28mm equivalent) produces the sharpest, least-distorted result for full-cover shots when positioned 25–40 cm from the comic. The ultra-wide (macro) camera has severe barrel distortion and should only be used for close-up defect detail shots within 10 cm.

**Evidence**:
- iPhone 16 Pro main camera minimum focus distance is approximately 25 cm (10 inches), increasing ~1.5 inches per year since iPhone 13 Pro. [src-012]
- Ultra-wide (macro): minimum focus distance is ~2 cm, but "barrel distortion is a lens defect that causes straight lines to bow out toward the edges of the image" — problematic for accurate comic shape documentation. [src-013]
- iPhone lens correction (Settings > Camera > Lens Correction) applies automatic barrel distortion correction to the ultra-wide, but it cannot fully compensate at close distances where warping is severe. [src-013]
- 2x telephoto: uses center crop of main sensor on iPhone 15+, producing optical-quality results but requires ≥50 cm working distance for full comic framing. [src-012]

**Recommended distances**:
- Whole cover: 25–35 cm using main (1x) camera
- Defect detail crop: 8–15 cm using macro (ultra-wide) camera, with Lens Correction on
- 2x telephoto: optional for full-cover shots that benefit from slightly more compression at 45–55 cm working distance

**Sources**: [src-012], [src-013]  
**Confidence**: HIGH

---

### Claim 3.2 — ProRAW does not meaningfully improve AI defect detection; HEIF Max (48MP) is the optimal format

**Claim**: For AI processing through Claude's vision API at 1568px max long edge, ProRAW files offer no practical advantage over HEIF Max. The extra latitude is only useful if you plan to edit the files significantly before feeding them to the model. HEIF at 48MP provides sufficient resolution (any remaining detail beyond what fits at 1568px is irrelevant) and keeps file sizes manageable for batch processing.

**Evidence**:
- ProRAW "records raw sensor information with minimal processing applied" and is 10–12× larger than HEIF. [src-014]
- "HEIF Max (48MP) is great quality and editable, while RAW should only be used for special shots you plan to heavily edit." [src-014]
- Deep Fusion bakes in pixel-level processing that cannot be reversed on HEIF/JPEG. ProRAW bypasses this. However, for defect detection under controlled lighting, Deep Fusion's texture enhancement is not problematic — it sharpens fine surface detail. [src-015]
- For AI analysis at fixed output resolution (1568px), the bit-depth advantage of RAW is irrelevant — the vision API does not use raw 14-bit luminance values.

**Format recommendation**: HEIF Max (48MP) with Smart HDR ON (helps with dynamic range on covers with dark and light areas). OR ProRAW 48MP if shooting for a dataset you will revisit with improved models — the files preserve re-grading flexibility.

**Sources**: [src-014], [src-015]  
**Confidence**: HIGH for HEIF Max sufficiency; MEDIUM for ProRAW advantage specifically for re-use

---

### Claim 3.3 — Deep Fusion helps defect visibility; Smart HDR is neutral to slightly helpful

**Claim**: Deep Fusion's pixel-level texture sharpening enhances fine surface texture (stress lines, cockling) at the cost of slight noise suppression — a net positive for defect capture. Smart HDR helps with dynamic range on covers with both black and glossy white areas, but does not affect defect topography.

**Evidence**:
- Deep Fusion "goes pixel by pixel and selects the best elements" to optimize "texture, details, and noise throughout a photograph." Hair, fabric, and textured surfaces show most benefit. Comic surface texture is analogous. [src-015]
- Deep Fusion activates in "medium light" — exactly the 45° desk-lamp diffuse setups we'll use. [src-015]
- Deep Fusion CANNOT be disabled in the Camera app on iPhone 12+. Shooting ProRAW bypasses it. [src-016]
- Smart HDR: "best for bright/high-contrast scenes." For comics with black covers and white backgrounds, the dynamic range assist is helpful. For uniform color covers, neutral effect. [src-015]

**Recommendation**: Leave Deep Fusion and Smart HDR active (default). Only shoot ProRAW if you want to compare Deep Fusion vs. unprocessed captures for a given defect type.

**Sources**: [src-015], [src-016]  
**Confidence**: MEDIUM — no direct study of Deep Fusion on comic cover texture; inference from mechanism

---

### Claim 3.4 — Lock AE/AF for consistent multi-shot sequences

**Claim**: For any multi-shot sequence of the same comic under different lighting angles, AE/AF Lock is essential. Without it, the iPhone will re-expose and re-focus between shots, making defect comparison unreliable and potentially causing the raking-light shadow to disappear due to automatic exposure compensation.

**Evidence**:
- AE/AF Lock "locks the focus and exposure, which will help prevent blurry shots and keep the focus on one part of the image without requiring you to refocus between each shot." [src-017]
- Automatic exposure is the primary enemy of raking-light capture: the iPhone will try to brighten the dark (shadow-heavy) raking-light image, reducing shadow contrast — exactly the opposite of what is needed.

**How to engage**: Tap and hold the comic surface in the Camera app until "AE/AF LOCK" banner appears. Then do not move the iPhone between raking shots. Unlock before moving to next comic.

**Sources**: [src-017]  
**Confidence**: HIGH

---

## 4. Background Science

### Claim 4.1 — Black background maximizes edge contrast and eliminates bleed-in from background light

**Claim**: A matte black background maximizes contrast between the comic's edges and surroundings, suppresses any ambient light bouncing back onto the cover, and prevents background color from contaminating AI analysis of edge defects. It is the correct choice for condition documentation photography.

**Evidence**:
- Evidence photography: "a full black screen/background eliminates all visual distractions and creates the ideal environment for spotting... even the smallest imperfections immediately visible." [src-018]
- Dental photography analogy (directly applicable to flat subject isolation): "black background eliminates irrelevant distractions and reflections, making the subject stand out more clearly... increases the brightness of the teeth, creating a starker contrast." [src-018]
- If background is positioned too close, it picks up light from main source and does not appear fully black — maintain at least 20 cm separation between comic edge and background edges. [src-019]

**What not to use**:
- **White background**: Reflects light back onto the cover, fills in raking-light shadows, and competes with pale stains/foxing
- **Gray background**: Reduces edge contrast; gray midtones can appear identical to age-tanned paper in AI analysis
- **Glossy black**: Produces specular reflections that the model may misidentify

**Recommended material**: Matte black foam board or black velvet cloth. Velvet produces the blackest (most light-absorbent) surface, ideal for raking-light shots.

**Sources**: [src-018], [src-019]  
**Confidence**: HIGH

---

### Claim 4.2 — Background color affects AI stain detection accuracy

**Claim**: For AI vision models processing RGB images, the background color creates an implicit luminance baseline. A white background adjacent to a cream-colored or tanned comic creates a contrast signal that makes age tanning obvious. A black background can cause the model to underestimate tanning on dark covers. The choice depends on defect type priority.

**Evidence**:
- Machine vision research: "RGB images produce the best result" vs. grayscale alternatives. Background color establishes the color space reference for the model. [src-010]
- Azure Vision color scheme detection: systems detect dominant and accent colors relative to the background frame — a non-neutral background contaminates dominant color detection. [src-010]
- Practical implication: black background is optimal for edge/topographic defects; a light gray background may be superior for tanning/stain color detection where you want the model to see contrast between paper color and ideal-white baseline.

**Recommendation for dataset**: Use black background as the standard. If stain/tanning is a specific evaluation target for a particular comic, shoot an optional second set on mid-gray (18% gray card) background.

**Sources**: [src-010]  
**Confidence**: MEDIUM — inference from machine vision principles, no direct study of background effect on comic AI grading

---

### Claim 4.3 — Glossy covers require cross-polarization OR steep angle management to suppress glare

**Claim**: Modern glossy comic covers produce specular reflections that create large bright hotspots under any single-source lighting. These hotspots saturate the camera sensor, obscure sub-surface defects, and can be mistaken by AI for stains, spots, or cover damage. Cross-polarization eliminates this entirely but requires equipment. Angle management (keeping light sources outside the specular reflection cone) is the equipment-free alternative.

**Evidence**:
- Cross-polarization: "by placing a second perpendicularly oriented polarizer in front of the camera, all that reflected but still polarized light gets blocked." Eliminates specular highlights entirely. [src-011]
- Cross-polarization requires: polarizing gel sheets on light sources + circular CPL filter on camera lens. Cost: ~$20–40 total. [src-011]
- Key trade-off: cross-polarization "can flatten textured surfaces like impasto brushwork, reducing apparent three-dimensionality" — i.e., it reduces the raking-light shadow effect. Use cross-polarization for stain/color shots, not raking-light topographic shots. [src-011]
- Angle management: specular reflection angle equals angle of incidence. Light at 45° produces specular reflection at 45° on the other side. Keep camera at 90° (overhead) and light at 45° — the specular cone goes away from the camera, not toward it.

**Sources**: [src-011]  
**Confidence**: HIGH

---

## 5. Multi-Shot Strategy

### Claim 5.1 — Four-shot protocol is optimal for information-per-time for condition assessment

**Claim**: A four-shot protocol captures all major defect types with minimum redundancy. Two shots are required (45° diffuse + raking left), and two additional shots (raking top + close-up detail) are high-value. Beyond four shots per comic, marginal information gain is low for AI-processed data at 1568px.

**Recommended four-shot protocol**:

| Shot | Lighting | Purpose |
|---|---|---|
| 1 — Standard | 2× LED panels at 45° from left and right | Color accuracy, stains, overall condition reference |
| 2 — Raking Left | Single LED panel at 10–15° from left edge | Creases, stress lines, cockling, dimples |
| 3 — Raking Top | Single LED panel at 10–15° from top edge | Horizontal creases, spine roll, corner fold |
| 4 — Detail | Macro (ultra-wide) camera, 45° diffuse, close-up of primary defect area | Fine detail on spine, corners, staples |

**Evidence**:
- Conservation standard: "multiple raking light images are usually obtained during an examination with each using light angled from a different direction" — two directions (left + top) is the standard two-direction protocol. [src-002]
- Conservation Wiki: "documenting the object with the light orientation both from the top and from the left is ideal" specifically because "surface features may align with a single light direction" and would be missed. [src-002]
- Industrial photometric stereo research uses 3–18 directional lights for maximum coverage of unknown defect orientations. For known-orientation defects (comics are always rectangular, defects tend to be axis-aligned), two raking directions provide adequate coverage. [src-005]
- CGC graders visually "tilt the cover and watch the light roll across the surface" — this is manual raking from multiple directions simultaneously. Two fixed-angle shots approximate this. [src-001]

**Optional shots** (add if time allows):
- Shot 5: Spine detail at 45° — spine stress, staple damage
- Shot 6: Back cover — back damage if relevant
- Shot 7: Interior pages — for water damage detection, tanning

**Sources**: [src-001], [src-002], [src-005]  
**Confidence**: HIGH for 4-shot minimum; MEDIUM for marginal returns beyond 4

---

### Claim 5.2 — Redundant vs. complementary shot pairs

| Shot pair | Relationship | Verdict |
|---|---|---|
| Raking left + Raking right | Mostly redundant — both cast shadows of same features from opposite directions. Right-facing features missed by left shot are usually minor | Skip raking right unless suspect asymmetric defect |
| Raking left + Raking top | Complementary — catches orthogonally-oriented defects | Keep both |
| 45° diffuse + overhead direct | Partially redundant for stains; overhead direct kills topographic shadow | Use only one ambient reference shot |
| Full cover + detail crop | Complementary — full cover provides location context; detail provides fine structure | Keep both |
| Raking + cross-polarized | Complementary for glossy covers — raking for topography, cross-pol for stain color under glare | Conditionally add for glossy cover subset |

**Confidence**: HIGH

---

## 6. Common Photography Errors that Create False Defects

### Error Type 1 — Glare patterns that mimic stains

**Mechanism**: Single off-axis light source on glossy cover creates a bright oval hotspot. The light falls off to dark at hotspot edges. The luminance gradient can be interpreted by AI as a stain or discoloration.

**Prevention**:
- Use two lights at equal 45° angles (left and right) — hotspots cancel each other
- OR use cross-polarization to eliminate specular entirely
- OR position lights slightly behind the plane of the comic (light traveling toward the camera, not reflecting into it)
- Never use a single bare LED panel as the only light source for standard (non-raking) shots

**Detection in post**: Glare artifacts are perfectly smooth luminance gradients with a highlight core; stains have irregular edges and color shift. An AI may not reliably distinguish them.

**Confidence**: HIGH

---

### Error Type 2 — Shadow edge artifacts that mimic creases

**Mechanism**: During raking-light shots, any slight curvature of the background surface (foam board that is not perfectly flat) casts a shadow line that can appear as a crease on the adjacent cover.

**Prevention**:
- Use a rigid, flat background material (foam board, not fabric)
- Ensure the comic lies completely flat — any page curl creates its own shadow that mimics a crease elsewhere
- Keep the black background material from curling up at the edges (tape down corners)

**Mechanism 2**: Hand shadow or light stand shadow falling across the cover edge creates a dark line that exactly mimics a spine crease.

**Prevention**: Position yourself and all equipment so no shadow falls on the comic during capture. Use the 2-second timer.

**Confidence**: HIGH

---

### Error Type 3 — Barrel distortion that mimics warping

**Mechanism**: The iPhone ultra-wide (macro) camera has significant barrel distortion. Straight comic edges appear to curve outward in the image. AI analyzing the cover shape may flag this as warping, bowing, or spine roll when no physical defect exists.

**Prevention**:
- Enable Lens Correction in Settings > Camera
- Do not use the ultra-wide lens for full-cover shots — only for close-up detail crops
- For detail crops, position the defect in the image center (distortion is minimal at center, maximal at corners)

**Confidence**: HIGH

---

### Error Type 4 — Motion blur that mimics foxing or fine scratches

**Mechanism**: Handheld iPhone during macro or raking-light shots introduces micro-vibration. At high ISO with long exposure, motion blur creates directional smearing of surface grain that can appear as fine parallel scratches or scattered foxing-like noise.

**Prevention**:
- Always use a tripod or rigid copy-stand setup
- Use 2-second shutter timer
- Ensure adequate lighting so the camera does not need long exposure
- Keep ISO below 400 where possible — higher ISO creates grain artifacts that are indistinguishable from paper foxing at low AI resolution

**Confidence**: HIGH

---

### Error Type 5 — Ambient color cast that mimics tanning or staining

**Mechanism**: Tungsten light bulbs or warm LED panels produce an orange color cast on the cover. This causes white paper to appear cream or yellowish, which AI may interpret as age tanning or acidic discoloration.

**Prevention**:
- Use daylight-balanced LED panels (5500–6500K color temperature)
- OR set custom white balance in the iPhone Camera app (requires third-party app like Halide or ProCamera)
- At minimum, shoot a white card at the same exposure settings and use it to verify color balance post-shoot

**Confidence**: HIGH

---

### Error Type 6 — Raking-light gradient that mimics cover darkening/fading

**Mechanism**: In a raking-light shot, the side of the cover facing the light source is substantially brighter than the opposite side. This is a lighting artifact, not cover damage. AI interpreting raking-light images as condition reference images may flag the dark side as "cover darkening" or "fading."

**Prevention**: Label raking-light shots explicitly in metadata. The AI pipeline must know these are topographic-detection shots, not color-reference shots. Never use a raking-light shot as the primary color/grade input.

**Confidence**: HIGH

---

## Sources

All sources were live-verified 2026-04-07.

| ID | URL | Title | Type | Claims Supported |
|---|---|---|---|---|
| src-001 | https://www.cgcgrading.com/en-US/resources/comics-grader-notes-guide/crease | CGC Comics Grader Notes Guide: Crease Defects | official | 1.1, 1.4, 2.3, 5.1 |
| src-002 | https://www.conservation-wiki.com/wiki/Raking_light | Raking light — AIC MediaWiki | official | 1.1, 1.2, 1.4, 2.1, 2.2, 2.3, 5.1 |
| src-003 | https://cameo.mfa.org/wiki/Raking_light | Raking light — MFA CAMEO | official | 1.2, 1.5 |
| src-004 | https://www.procemex.com/web-inspection/measurement-geometries/ | Web Inspection Measurement Geometries — Procemex | community | 1.2, 1.5 |
| src-005 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11830798/ | Dataset for surface defect detection using photometric stereo — PMC/Scientific Data | academic | 1.1, 5.1 |
| src-006 | https://www.digitizationguidelines.gov/guidelines/digitize-technical.html | FADGI Technical Guidelines for Digitizing Cultural Heritage Materials | official | 1.3 |
| src-007 | https://www.hki.fitzmuseum.cam.ac.uk/about/services/photographicservices/lightingtechniques | Lighting Techniques — Hamilton Kerr Institute | official | 1.2, 2.3 |
| src-008 | https://chsopensource.org/ultraviolet-fluorescence-photography-uvf/ | Ultraviolet Fluorescence Photography for Art Analysis — CHSOS | official | 1.3 |
| src-009 | https://www.crime-scene-investigator.net/closeup.html | Lighting Methods for Copy and Evidence Close-up Photography | community | 1.5 |
| src-010 | https://www.unitxlabs.com/resources/image-contrast-machine-vision-system-importance-inspection/ | Why Image Contrast Matters in Machine Vision Applications | journalism | 4.2 |
| src-011 | https://chsopensource.org/polarized-light-photography-for-art-documentation/ | Polarized Light Photography for Art Documentation — CHSOS | official | 2.2, 4.3 |
| src-012 | https://discussions.apple.com/thread/255496554 | What is the shortest focus distance of iPhone 15 Camera — Apple Community | community | 3.1 |
| src-013 | https://tomsguide.com/how-to/how-to-enable-lens-correction-on-iphone | How to enable lens correction on iPhone — Tom's Guide | journalism | 3.1 |
| src-014 | https://www.diyphotography.net/proraw-vs-heif-vs-jpeg/ | ProRAW vs HEIF vs JPEG — DIY Photography | journalism | 3.2 |
| src-015 | https://appleinsider.com/articles/19/10/02/inside-apples-deep-fusion-the-iphone-11-and-pros-computational-photography-feature | Inside Apple's Deep Fusion — AppleInsider | journalism | 3.3 |
| src-016 | https://www.macworld.com/article/233656/how-to-enable-or-disable-deep-fusion-and-smart-hdr-on-the-iphone-11.html | How to enable or disable Deep Fusion and Smart HDR — Macworld | journalism | 3.3 |
| src-017 | https://iphonephotographyschool.com/ae-af-lock/ | How To Use iPhone AE/AF Lock — iPhone Photography School | community | 3.4 |
| src-018 | https://intelgic.com/How-to-get-Defects-Visible-on-Plastic-Surfaces-and-Transparent-Sheets-in-Machine-Vision-Imaging | How to get Defects Visible on Plastic Surfaces — Intelgic | journalism | 4.1 |
| src-019 | https://www.dpreview.com/forums/thread/3575966 | Good lighting setup for black backdrop — DPReview | community | 4.1 |

---

## Open Questions (Flagged for Follow-Up)

1. **UV for foxing**: Does UV capture add discriminative signal for foxing at the severity levels our dataset will contain (minor-to-moderate)? UV setup cost is low (~$30 UV LED bar). Recommend: run a test on 3 fox-stained comics with both visible-light diffuse and UV captures, feed both to the AI, compare detection rates. [UNVERIFIED for our specific use case]

2. **Cross-polarization ROI**: Given the time cost of cross-polarization setup (~10 minutes to configure per session, not per comic), is it worth it for the glossy-cover subset? Recommend: only use for comics where glare was visible in Shot 1 review. [UNVERIFIED for our dataset composition]

3. **Deep Fusion texture sharpening effect**: Does Deep Fusion improve or degrade CGC-relevant defect detection accuracy at 1568px? Hypothesis: neutral-to-positive, as the AI sees the HEIF output not raw sensor data. Test: shoot identical raking-light captures in HEIF and ProRAW on a comic with known stress lines, compare AI detection rate. [UNVERIFIED]

4. **Optimal height for overhead camera**: 25 cm vs. 35 cm vs. 45 cm — does a tighter crop with the main camera provide more useful defect detail than a wider frame (which requires cropping in post)? [UNVERIFIED]
