# Graphene Integration Route Selection for Ferroelectric Photonic Memory

**Paper 4 of 4 · Solbakken Research Initiative · Nils Haaland**

A pre-experimental decision framework ranking eleven graphene integration routes for a graphene-gated ferroelectric (Al:HfO₂) photonic memory stack. A Bayesian Monte Carlo simulation (N = 200,000, Gaussian copula / Cholesky correlation structure), anchored to primary literature, ranks routes by the joint probability of meeting five simultaneous graphene quality criteria ("Goldilocks window"), distinguishes irreducible substrate-physics constraints from reducible process-kinetic ones, and specifies five experiments — ordered by decision value — that most efficiently collapse the decision space before fabrication begins.

**No experimental prototype combining graphene gating, ferroelectric polarization, and photonic waveguide operation has been demonstrated.** This is a decision tool, not a results paper. Route rankings are falsifiable predictions; Section 7 is the falsification protocol.

## Headline results (v10.5)

| Route | P(all 5 criteria) | Status |
|---|---|---|
| I: CVD/Pt → hBN | **38.6%** | Rational near-term entry point |
| J: CVD/Pt → SCD(111) bonded | 21–36% | Development bridge, pending Exp. 2 |
| F2: SCD(111) Ni+H (theoretical ceiling) | ≈54% | Theory-anchored upper bound, unmeasured |
| F @ demonstrated diamond transport | ≈5–24% | Adjacent-process anchors (Aitkulova 2025; Majdi 2023) |
| F1: SCD(111) Ni graphitized (Kanada 2017) | ~0% | Only demonstrated graphitization state |
| A–D: UNCD graphitization | ~0% | Eliminated — irreducible substrate physics |
| E: SCD(111) direct; K: PECVD on HfO₂ | ~0% | E eliminated; K deferred (reducible kinetics, Exp. 5) |

Percentages are decision-ranking tools, not yield predictions. Trust the ordinal ranking, not the digits.

## Status

**v10.5 — pre-deployment draft.** Do not treat as deployed until the dashed red banner is removed from the HTML. Outstanding:

1. **[15b] residuals** — carrier density and sheet-resistivity values from Tables 1–3 of Aitkulova et al. (*Carbon Trends* 100598, 2025) must be extracted manually from the verified full-text copy (publisher blocks automated retrieval), plus volume/page numbers once the Version of Record replaces the current pre-proof.
2. **Monte Carlo companion rerun** of all figures marked ≈, under the scaled-n\* convention now adopted for Table 5's measured rows. Until the rerun reports, the quoted measured-row joints (≈5% at 1,644 cm²/V·s; ≈24% at 2,750 cm²/V·s) are fixed-n\* **upper bounds**.
3. **Verified citation for the Al:HfO₂ remnant-polarization range** (order 10–20 µC/cm²) quoted in the §2.2 electrostatic feasibility note. Do not deploy with that range uncited.

## What changed in v10.5

- **[15c] added, Table 5 re-anchored.** Majdi et al., *Appl. Phys. Lett.* 123, 012102 (2023), doi:10.1063/5.0156108 (DOI-verified): 2,750 cm²/V·s room-temperature Hall mobility for transferred CVD graphene on electronic-grade (100) single-crystal diamond. The demonstrated graphene-on-diamond transport ceiling now sits within ≈9% of the 3,000 cm²/V·s threshold — for a transferred film on (100), not the graphitization sequence on (111).
- **§2.2 Constraint 1 corrected** — the Pauli-blocking doping constraint had an inverted inequality and a 10× magnitude error (was "n < 1.2×10¹² cm⁻²"; correct is n > 1.2×10¹³ cm⁻² for the transparent state).
- **§2.2 corrected** — insertion loss is governed by the *real* part of the Kubo conductivity, not the imaginary part (the formula was already the real interband term; only the label was wrong).
- **Table 2 P(array) column corrected** — previous independence-model values were overstated by tens to thousands of orders of magnitude (same error class as the §6.6 claim corrected in v10.4).
- **Experiment 5 composition corrected** — "Al₀.₅Hf₀.₅O₂" → Al:HfO₂ at the few-cation-percent ferroelectric doping level.
- **Post-review addenda (adversarial panel):** §2.2 electrostatic feasibility note (σ = ne ≈ 1.9 µC/cm² vs. Al:HfO₂ P_r of order 10–20 µC/cm²; citation pending); Table 5 n\*-convention resolved in favor of scaling n\* with mobility (shared disorder sources), quoted joints re-labeled as fixed-n\* upper bounds; §5.0 threshold-leverage sentence (IL-budget sensitivity); reference-list annotation key.

## Citation-integrity workflow

Per-reference DOI resolution is a mandatory pre-deployment gate for every version of every paper in this series. Three fabricated citations have been caught across this paper's history; each is documented in the Revision Log and, where applicable, retained in the reference list as a tombstone rather than silently deleted. The Revision Log at the top of the paper is the complete, cumulative correction record (v10.1 → v10.5).

Drafts are additionally cycled through a multi-model adversarial review panel treated as **correlated noise, not independent review** — convergent suggestions count as one vote, and reviewer output is screened for regeneration of previously removed content. (The v10.5 log records one rejected recommendation that reproduced the mechanism of fabricated reference [18].)

## Version history

| Version | Summary |
|---|---|
| 10.5 (draft) | Majdi 2023 re-anchor ([15c]); Pauli-constraint, Kubo real-part, Table 2, and Exp. 5 composition corrections |
| 10.4 | Fabricated citation [18] removed; [17] re-scoped (transfer-free ≠ catalyst-free); [15b] measured anchor added; F2 ceiling truncated; §6.6 and Table 2 footnote corrected; Exp. 1 parallel-conduction control |
| 10.3 | Red-team revisions: Route K consistency, ordinal caveat, footnote provenance system |
| 10.1 | Reference corrections (DOIs, author attributions) |
| 10.0 | Route K (11th route) added; F1/F2 split |

## Viewing

The paper is a single self-contained HTML file (`paper4_v10.5_draft.html`) — no build step, no dependencies beyond Google Fonts. Open directly in any browser; supports light and dark mode via `prefers-color-scheme`.

## Related work in this series

- Paper 1 — Ferroelectric grain-boundary polarization as a hidden variability source
- Paper 2 — The weight bottleneck and DRAM energy asymmetry
- Paper 3 — The diamond-integrated FERRO-PCM architecture
- Simulation code and prior parameter files: to be released as supplementary material upon journal submission

## Contact

Nils Haaland · Independent Researcher, Omaha · nhaaland@yahoo.com

License: **CC0 1.0 Universal** — to the extent possible under law, the author has waived all copyright and related rights to this work. Full legal code: https://creativecommons.org/publicdomain/zero/1.0/legalcode
