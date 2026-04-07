# Verification: Grading Calibration Research
**Axis**: Human Grading Calibration Protocol  
**Date**: 2026-04-07  
**Verifier**: fact-checker agent

---

## Verdict: PASS — CGC definitions and grade boundaries verified; ICC thresholds correct

The grading-calibration.md file is the most well-sourced of the six files. CGC grade boundary criteria are correctly derived from Overstreet Access. ICC model selection and thresholds are accurately attributed to Koo & Mae 2016. Three minor issues are flagged.

---

## CGC Grade Boundary Claims

### Overstreet 9.4 NM: "1/16" bend permitted, no color break"

**Status: VERIFIED**

This is the canonical Overstreet criterion for 9.4 NM. Source is Overstreet Access grading definitions (src-006), which is the official Overstreet digital publication. Correctly stated.

### Overstreet 9.0 VF/NM: "1/8" bend allowed if color is not broken"

**Status: VERIFIED**

Correctly stated and correctly sourced. The doubling of the bend tolerance from 9.4 to 9.0 (1/16" → 1/8") is a well-established boundary criterion.

### 9.8 allowances: spine ticks ≤1/8", bindery tears ≤1/16"

**Status: VERIFIED (community-sourced but high confidence)**

Source is bryscomics.com (src-009), which is a detailed community analysis of actual 9.8 submissions, not official CGC. The specific allowances cited (spine ticks ≤1/8" not visible looking straight on; bindery tears ≤1/16"; color rubs ≤1" total) are consistent with community consensus and the CGC Grader Notes Guide. Marked HIGH confidence in the file — this is appropriate for community-sourced but well-established criteria.

### Tape grade cap: "4.5 is the highest grade for any tape present"

**Status: VERIFIED — with important exception documented elsewhere**

CGC's 2013 tape policy update (cited in compound-defects.md as src-cd-02) states that functional tape (holding a split spine, reattaching a detached cover) is graded as if the tape is not present. The grading-calibration.md correctly states "4.5 is the highest grade for any tape" in the context of VG/FN general tape. This refers to non-functional decorative or sticker-type tape, not repair tape.

**Consistency risk**: The grading-calibration.md does not cross-reference the 2013 CGC tape policy update. The compound-defects.md correctly documents the exception. A protocol note should link these two files so graders are not confused. Not a factual error, but a cross-reference gap.

### CGC process: "three graders, each enters grade independently, head grader prevails"

**Status: VERIFIED**

Source is the CGC grading process page (src-016). The head grader override is correctly described: "If two graders rate a book at 7.0 and the Head Grader grades it at 7.5, the latter grade prevails." This is correctly cited.

---

## ICC Model Selection

### ICC(3,1) recommendation for Sean and Marcus as fixed raters

**Status: VERIFIED**

The model selection follows Koo & Mae 2016 logic correctly:
- ICC(3,1) = Two-way mixed-effects, absolute agreement, single measures
- Appropriate when raters are the specific subjects of interest (not a random sample)
- Absolute agreement variant is correct when actual grade differences matter

The Python code using `pingouin` (`type='ICC3'`) correctly implements this.

### ICC threshold benchmarks: ≥0.90 = excellent, 0.75–0.90 = good, 0.60–0.74 = moderate, <0.60 = poor

**Status: VERIFIED**

These are the Koo & Mae 2016 thresholds, correctly attributed. Source PMC4913118 is the correct PMC ID for this paper.

### "Minimum 30 samples" for stable ICC (Koo & Mae 2016)

**Status: VERIFIED**

Koo & Mae 2016 recommend "at least 30 heterogeneous samples." The file correctly reports this minimum.

---

## Bias Claims

### "Inexperienced graders routinely grade 1–2 full grade categories higher"

**Status: PLAUSIBLE — sourced from community, not formal study**

Sources are MyComicShop grading guide (src-014) and Covrprice (src-015). Both are community-tier. No controlled experiment was cited. The claim is widely repeated in the community and is plausible, but the specific "1–2 full grade categories" quantification is not from a measured study. Confidence should be MEDIUM, not HIGH as stated.

**Impact on protocol**: None. The upward bias correction protocol (grade before checking market value, lock grade in writing) is sound regardless of the exact magnitude.

### Session fatigue: "45–90 minutes before a break"

**Status: MEDIUM CONFIDENCE — one counterevidence source noted in file**

The file correctly cites both supporting evidence (decision fatigue literature) and contradicting evidence (Nature 2025 paper finding no evidence for decision fatigue in expert practitioners). The MEDIUM confidence rating is appropriate. The 20–25 comics per 90-minute session guidance is conservative and defensible.

---

## No Dangerous Claims Found

No hazardous procedures. The physical grading setup (desk lamp, loupe, cotton gloves optional) is standard practice with no safety concerns.
