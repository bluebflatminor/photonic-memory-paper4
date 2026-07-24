# Graphene Integration Route Selection for Ferroelectric Photonic Memory

**A Bayesian Quality Assessment Across Eleven Process Scenarios**

Paper 4 of 4 · Solbakken Research Initiative · Nils Haaland (independent researcher, Omaha)

---

## Status

**Version 10.8 (draft) — July 2026 — PRE-DEPLOYMENT.** This version has not cleared its pre-deployment gate. Six banner items are open:

1. **[15b] residuals** — carrier density and sheet-resistivity values from Tables 1–3 of Aitkulova et al. 2026 (publisher blocks automated retrieval; manual extraction from the verified full text or SSRN preprint required).
2. **Monte Carlo companion rerun** of all figures marked ≈, under the scaled-n* convention adopted in v10.5 (the quoted ≈5%/≈24% measured-anchor joints are fixed-n* upper bounds until the rerun reports).
3. **Legacy-tier DOI-gate pass** *(new in v10.8)* — reference entries [4], [5], [7], [8], [9], [10], [12], [13], [14] predate the DOI-gate and have never been individually resolved. Three of three spot-checked legacy entries required correction this cycle.
4. **Table 3 anchor promotion** *(new in v10.8)* — anchor labels "Zhang 2012", "JAP 2013", "Carbon 2021" are not numbered references; identify, gate, and promote.
5. **65 fJ write-energy anchor** *(new in v10.8)* — the §1.1 figure is uncited; locate a verified anchor or remove.
6. **Human archive pass** *(new in v10.8)* — over this cycle's single-instrument corrections. Per the clean-room protocol, the correcting instrument does not close its own items.

## What this paper is

A **pre-experimental decision framework**: a Bayesian Monte Carlo simulation, anchored to primary literature, that ranks eleven graphene integration routes for a proposed graphene-gated ferroelectric photonic memory cell by joint probability of meeting five simultaneous quality criteria; distinguishes irreducible substrate-physics constraints from reducible process-kinetic ones; and specifies five experiments, ordered by decision value, that most efficiently collapse the decision space before fabrication begins.

## What it is not

A results paper or a device-performance prediction. No prototype of the proposed cell exists anywhere; the Goldilocks thresholds are theory-derived hypotheses; route rankings are prioritisation tools for experimental investment. Section 7 is the falsification protocol, and the primary falsification target for the whole framework is any working device at any route.

## Principal results (v10.8)

- All UNCD graphitization routes (A–D) are eliminated by **substrate physics** — sub-micron domains from nm-scale diamond grains — not by any process variable.
- SCD(111) direct graphitization (E) fails within any realistic envelope; Ni-assisted graphitization (F) is ~0% at the only peer-reviewed graphitization anchor (Kanada 2017, 140 cm²/V·s).
- Measured transport for **transferred** CVD graphene on single-crystal diamond (Aitkulova 2026: 1,644 cm²/V·s; Majdi 2023: 2,750 cm²/V·s) implies ≈5–24% joint probability at demonstrated transport; the ceiling-truncated theoretical bound is ≈54% with no experimental confirmation of the ceiling.
- **Route I (CVD/Pt → hBN encapsulation) leads at 38.6%** — the rational near-term entry point, with a structural mobility ceiling set by film grain boundaries.
- Route J (CVD/Pt → bonded SCD(111)) spans 21–36% and is the development bridge toward Route F, pending Experiment 2.
- Route K (direct PECVD on Al:HfO₂) is ~0% at theory-anchored priors, but fails by **reducible nucleation kinetics** — deferred, not eliminated (Experiment 5).

## Verification protocol

This repository documents its own error history rather than hiding it. Conventions in force:

- **DOI-gate:** every reference DOI must resolve live to the claimed title and authors before any deployment. Adopted at v10.4 after a fabricated citation ([18]) survived two earlier verification rounds.
- **Tombstones:** removed or fabricated references are retained in the reference list and revision log, never silently deleted. Three fabricated- or misattributed-citation incidents are documented (v10.1, v10.4, v10.8).
- **Instrument quarantine / clean-room rule:** LLM instruments used for verification are treated as instruments, not authorities. Live retrieval is recorded as such; training-corpus recall is not accepted as verification; concordant recall between two LLMs is treated as **correlated evidence, roughly one opinion**, not independent confirmation; and the instrument that finds or fixes an error never closes its own banner item — a human archive pass does.
- **Documented instrument failure modes:** fabricated citations resolved to unrelated DOIs ([18], v10.4); a retrieval failure promoted to a false nonexistence claim (v10.7); a reviewer recommendation reproducing the mechanism of a known-fabricated reference (v10.5).
- **Cumulative revision log:** every correction cycle is logged in the paper's Appendix, in full, including statements later found to be wrong (annotated, not edited).

## Revision history

| Version | Cycle | Summary |
|---|---|---|
| 10.0 → 10.1 | Reference corrections | DOI and author-attribution fixes (Kanada, Tang→Qian, Hicks→Aitkulova) |
| 10.2 → 10.3 | Internal red team | Route K integrated; ordinal-caveat framing; structural fixes |
| 10.3 → 10.4 | Citation integrity | Fabricated [18] tombstoned; DOI-gate adopted; [15b] added; F2 ceiling truncated; §6.6 array-math corrected |
| 10.4 → 10.5 | Measured re-anchor | [15c] (2,750 cm²/V·s) added; Pauli-blocking constraint corrected (inverted inequality, 10×); Table 2 P(array) corrected; Exp. 5 composition fixed |
| 10.5 → 10.6 | P_r verification | [1] resolved: P_r = 7.43 µC/cm², margin restated ≈3.9×; [24]–[26] added; novelty claim sharpened |
| 10.6 → 10.7 | Archive-pass closures | [1] first author confirmed; [24] verified live, IL corrected; [15b] promoted to VoR; novelty claim sharpened again; second-instrument false-nonexistence failure logged |
| 10.7 → 10.8 | **External red-team pass** | Legacy tier gated: [2] Koike→Taki, [6] Sumant→Berman, [11] Yan→Yu (all live-resolved with DOIs); §2.2 Kubo expression corrected to two-term form; [4b] Shen 2017 added as fJ/MAC anchor with explicit per-token conversion; Table 5 convention column; [24] issue + contact-endurance detail; logs moved to Appendix |

## Contents

- `paper4-v10.8-draft.html` — the paper: self-contained HTML, no build step, dark-mode aware. Open in any browser.
- Simulation code and prior parameter files: to be released as supplementary material.

## License

**CC0 1.0** — released to the public domain. No rights reserved. Use, copy, modify, and redistribute freely, including the experimental protocol.

## AI-collaboration disclosure

This paper was developed in sustained collaboration with large language models under an adversarial multi-instrument review methodology (disclosure level D3): Claude (Anthropic) for simulation design dialogue, prior construction, adversarial red-team review, and citation verification with live web retrieval; additional LLM instruments for editorial and cross-check passes, under the quarantine rules described above. The author retains sole responsibility for all numerical estimates, prior choices, conclusions, and errors. The verification protocol exists because these instruments fail, and it documents each failure it catches.

## Contact

Nils Haaland · nhaaland@yahoo.com

The author does not have access to the experimental infrastructure required to execute Experiments 1–5. This paper is a call to the field: the five experiments are offered as a prioritised, decision-branched roadmap for any group with SCD(111) substrates, hBN transfer protocols, Hall measurement infrastructure, and remote-plasma PECVD capability.
