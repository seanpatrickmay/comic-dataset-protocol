# Research Changelog

## Phase 1: Scope & Plan — 2026-04-07

**Brief:** Definitive protocol for comic book grading dataset construction
**Research axes:** 6 dimensions identified

## Phase 2: Investigate — 2026-04-07

All 6 researchers completed:
- Defect creation science (591 lines, 13 sections)
- Photography science (19 sources, raking light angles, iPhone optimization)
- Grading calibration (500 lines, ICC methodology, calibration exercises)
- Severity spectrum (measurable thresholds per defect type)
- Statistical design (39/14/9/8 allocation, CI analysis)
- Compound defects (6 prioritized specimens, CGC holistic model analysis)

## Phase 3: Verify — 2026-04-07

4 corrections identified:
1. CI width: ±5.9pp → ±7.5pp (clustering correction)
2. FeSO₄ safety: add eye protection
3. Tear threshold discrepancy: resolved (context-dependent)
4. Crease minor threshold: clarified as Overstreet 8.0 VF criterion

## Phase 4: Synthesize — 2026-04-07

Unified synthesis covering equipment → setup → calibration → photography → defect creation → compound specimens → statistics → annotation → checkpoints.

## Phase 5: Adversarial Review — 2026-04-07

5 hard-gate findings:
1. Schedule inflation (65 person-hours ≠ 3-4 days)
2. Tanning technique wrong (damp bag ≠ tanning)
3. ±4pp target unachievable (need ~185 independent comics)
4. Recall power math incorrect
5. Stain severity vs. water damage cap inconsistency

## Phase 6: Iterate — 2026-04-07

All 5 hard-gate fixes applied to deliverable:
- Two explicit schedules (2-day MVP, 5-day full)
- Tanning: natural specimen preferred, oven aging as fallback
- CI: ±7.5pp front-paged, ±4pp explicitly flagged as Phase 2
- Recall: corrected to one-sided exact binomial upper bound
- Stain: water damage cap (6.0) distinguished from general stain table

## Phase 7: Deliver — 2026-04-07

Final deliverable: `output/dataset-construction-protocol.md`
All 10 required sections present. Self-reviewed twice.

## Session Summary: 2026-04-07

**Deliverable:** output/dataset-construction-protocol.md
**Sources used:** 87 (see sources.json)
**Key findings:**
- 70 comics → 210 images → ±7.5pp effective CI (first reportable accuracy)
- Optimal allocation: 39 baseline / 14 single-defect / 9 severity / 8 compound
- Fiber breakage is the universal severity boundary (green vs. red)
- Raking light at 10-15° is required for crease/stress detection
- ICC(3,1) ≥ 0.75 achievable after 2-3 calibration rounds
- Phase 1 is catastrophic-failure detection, not precision measurement
