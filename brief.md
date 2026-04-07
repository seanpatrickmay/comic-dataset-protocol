# Research Brief: Definitive Protocol for Comic Book Grading Dataset Construction

## Topic

How to construct a gold-standard evaluation dataset for an AI comic book condition grading system using ~70 physical comics (some destructible), two human graders, iPhone cameras, and a budget under $100 for equipment. The output must be a bulletproof, step-by-step protocol that a team can follow with zero ambiguity.

## Scope

### In Scope
- **Controlled defect creation**: Exact physical procedures for creating reproducible, CGC-standard defects on sacrificial comics. Which tools, motions, pressures, and techniques produce defects that match each CGC defect category.
- **Defect severity calibration**: How to create minor/moderate/major versions of the same defect type, and how to verify the severity matches CGC definitions.
- **Photography science**: Exact lighting angles, distances, and camera settings that maximize defect visibility for AI analysis. Raking light angles for different defect types. How to avoid artifacts that create false positives.
- **Human grading calibration**: How two non-professional graders can produce reliable grades. Specific calibration exercises, reference materials, and inter-rater reliability measurement.
- **Annotation precision**: Exact field definitions, controlled vocabularies, and edge-case rules for every annotation field. How to handle ambiguous cases.
- **Statistical design**: Optimal allocation of 70 comics across grade tiers and defect types. Which controlled defects give the most evaluation information per specimen.
- **Compound defect interactions**: How multiple defects on one comic interact in CGC grading. Which combinations are most informative to test.
- **Defect verification**: How to verify that a controlled defect actually matches what CGC would classify it as. Reference photos, measurement criteria.

### Out of Scope
- AI pipeline code changes (already done)
- CGC submission logistics
- Acquiring additional comics
- Building custom photography equipment

## Dimensions

### 1. Controlled Defect Creation Science
How does CGC define each defect type? What physical actions produce defects that match those definitions? What tools are needed? How reproducible is each technique? What are the failure modes (defect too severe, wrong type created)?

### 2. Photography for Defect Detection
What specific lighting setups maximize visibility for each defect category? What's the optimal raking light angle for creases vs. stains vs. corner wear? How does the background color affect defect visibility? What resolution is needed to capture minor vs. major defects?

### 3. Human Grading Calibration Protocol
How do professional graders calibrate? What exercises can non-professionals do to improve consistency? How many comics need to be double-graded before ICC stabilizes? What CGC reference materials are publicly available for calibration?

### 4. Severity Spectrum Engineering
How to reliably create minor/moderate/major versions of the same defect. What physical measurements define each severity level for each defect type? How does paper weight and age affect defect creation?

### 5. Optimal Statistical Design with 70 Comics
Given exactly 70 comics (some high-grade, some worn, some beat-up), what's the optimal allocation between baseline photography, controlled single-defect, severity spectrum, and compound defect specimens? Information-theoretic approach to maximizing evaluation power.

### 6. Compound Defect Testing Strategy
Which combinations of defects produce non-obvious grading interactions? Which test the AI's penalty stacking algorithm most effectively? How many compound specimens are needed?

## Output Format

A single comprehensive protocol document (Markdown) that a team member can print out and follow step-by-step. Sections:

1. **Equipment List** — Exact items with purchase links or descriptions
2. **Setup Guide** — With diagrams/descriptions of the photography station
3. **Sorting Protocol** — How to categorize the 70 comics
4. **Photography Protocol** — Shot-by-shot instructions per comic
5. **Human Grading Guide** — Calibration exercises + grading reference
6. **Defect Creation Catalog** — Per-defect-type physical instructions with severity levels
7. **Compound Defect Recipes** — Specific multi-defect combinations to create
8. **Annotation Guide** — Field-by-field instructions with examples
9. **Quality Checkpoints** — Verification steps at each phase
10. **Allocation Matrix** — Exactly how to distribute 70 comics across all test categories

## Quality Requirements

- Every defect creation instruction must reference CGC's official definitions
- Photography recommendations must be grounded in conservation/archival imaging standards
- Severity calibration must reference measurable criteria (not just "light" vs "heavy")
- The protocol must be executable in 3–4 days by 2 people
- Every ambiguous decision point must have a clear default rule

## User Profile

- **Sean May**: Grad student, strong in ML/Python, has graded comics informally but not professionally trained
- **Marcus Yi**: Collaborator, less experienced with grading, can help with photography and physical defect creation
- **Resources**: ~70 physical comics (mix of conditions, some destructible), iPhones, ~$65–100 for equipment, no professional grading training
- **Goal**: Build a dataset rigorous enough to measure AI grading accuracy at ±4pp and identify systematic biases

## Current System Context

The AI grading pipeline uses:
- **CGC 0.5–10.0 scale** with 25 valid grade points
- **100+ defect types** across 7 categories (crease, distortion, missing_part, stain, substance, tanning, tear)
- **Severity-dependent penalties** (green/yellow/red) with caps per defect type
- **12-zone localization** system (spine, 4 corners, 3 edges, 2 staples, cover center, full cover)
- **Post-processing**: defect floor algorithm with area weighting, diminishing returns, minor-only cap, plausibility gate
