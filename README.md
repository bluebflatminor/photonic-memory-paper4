# Graphene Integration Route Selection for Ferroelectric Photonic Memory

**A Bayesian Quality Assessment Across Eleven Process Scenarios**

Paper 4 of 4 · Solbakken Research Initiative
Nils Haaland · Independent Researcher, Omaha · nhaaland@yahoo.com
**Current version: 10.7 (draft) — July 2026** · License: CC0 1.0 (public domain)

---

## What this paper is

A pre-experimental decision framework for a proposed non-volatile photonic weight-storage architecture: graphene gated by the remnant polarization of an Al:HfO₂ ferroelectric film, operating as an absorption weight in an integrated waveguide. No published prototype uses ferroelectric remnant polarization to gate graphene as the *sole* optically modulated medium in a photonic waveguide, with absorption readout — the constituent physics is demonstrated piecewise (Strikha & Vasko 2011 proposal; Liu et al. 2011 volatile modulator; Singh et al. 2026 as the closest photonic analog with the roles primarily inverted), but never in this combination.

The paper ranks **eleven graphene integration routes** — UNCD graphitization, SCD(111) graphitization, CVD metal-substrate transfer, and direct low-temperature PECVD on the ferroelectric oxide itself — by joint probability of simultaneously meeting five quality criteria (defect density, domain size, mobility, carrier-density uniformity, monolayer coverage), using a Bayesian Monte Carlo simulation (N = 200,000) anchored to primary literature. It distinguishes constraints that are **substrate physics (irreducible)** from those that are **process kinetics (reducible)**, and specifies **five experiments, ordered by decision value**, that most efficiently collapse the decision space before fabrication begins.

## Principal results

- **UNCD routes (A–D): eliminated by substrate physics.** The 2–5 nm grain structure irreducibly caps graphene domain size orders of magnitude below the 10 µm threshold.
- **SCD(111) direct graphitization (E): ~0%** within any realistic envelope.
- **Route F (SCD(111) Ni-assisted graphitization): ~0% at the only peer-reviewed graphitization anchor** (Kanada 2017, 140 cm²/V·s). Measured transferred-film transport on single-crystal diamond — 1,644 cm²/V·s (Aitkulova et al. 2026) and 2,750 cm²/V·s (Majdi et al. 2023) — implies ≈5–24% at demonstrated graphene-on-diamond transport; the ceiling-truncated theoretical upper bound is ≈54%, undemonstrated.
- **Route I (CVD/Pt → hBN): 38.6%**, the highest of any route at current demonstrated state; mobility-bound by the film's own grain boundaries.
- **Route J (CVD/Pt → bonded SCD(111)): 21–36%**, the development bridge; transfer penalty unmeasured (Experiment 2).
- **Route K (direct PECVD on Al:HfO₂): ~0%, but reducible** — kinetic nucleation, not substrate physics; deferred pending Experiment 5, not eliminated.

Percentages are decision-ranking tools, not yield predictions; trust the ordinal ranking. Route rankings are falsifiable theoretical predictions and §7 is the falsification protocol.

## Verification protocol

This paper series operates under a falsification-first discipline, documented in the in-paper Revision Log:

- **DOI-gate:** every reference DOI is independently resolved against claimed title and authors before any deployment. This gate has caught **three fabricated citations** in this paper's history (all tombstoned in the reference list, never silently removed — see [18]).
- **Correlated-instrument discipline:** agreement between LLM instruments on recalled (rather than retrieved) bibliographic detail is treated as correlated evidence, roughly one opinion, never independent confirmation.
- **Documented instrument failure modes:** fabricated citations ("does not exist" cited as real) and the inverse — retrieval failure promoted to a nonexistence claim ("cannot resolve" reported as "does not exist," logged v10.7). Both are corrosive; both are recorded.
- **Cumulative corrections:** revision-log entries are never edited after the fact; corrections to prior log entries are made in new entries with cross-notes.

## Version history (10.0 → 10.7 highlights)

| Version | Focus |
|---|---|
| 10.1 | Reference corrections (DOIs, author attributions) |
| 10.3 | Red-team revisions; Route K added as eleventh route; ordinal-caveat framing |
| 10.4 | Fabricated citation [18] caught and tombstoned; DOI-gate made mandatory; [15b] added; F2 ceiling truncated |
| 10.5 | [15c] re-anchor (2,750 cm²/V·s); §2.2 inequality/magnitude corrections; Table 2 P(array) corrected |
| 10.6 | P_r verified at 7.43 µC/cm² (margin restated ≈3.9×); [24] Singh added as closest photonic analog; prior-art lineage [25][26] |
| 10.7 | Archive-pass closures: [1] first author resolved; [24] publisher-verified (insertion loss 0.2 dB; role-inversion softened); [15b] promoted to Version of Record (*Carbon Trends* 22, 100598, 2026); novelty claim sharpened to "sole optically modulated medium"; Experiment 1 substrate-cleaning sequencing note; "cannot resolve → does not exist" instrument failure mode logged |

## Status — remaining pre-deployment items

1. **[15b] residuals:** carrier density & sheet-resistivity values from Tables 1–3 of the full text (manual extraction; publisher blocks automated retrieval; SSRN preprint doi:10.2139/ssrn.5623754 available).
2. **Monte Carlo companion rerun** of all ≈-marked figures under the scaled-n* convention; the quoted ≈5%/≈24% measured-anchor joints are fixed-n* upper bounds until then.

## Author's note

The author does not have access to the experimental infrastructure required to execute Experiments 1–5. This paper is a call to the field: the five experiments are offered as a prioritised, decision-branched roadmap for any group with SCD(111) substrates, hBN transfer protocols, Hall measurement infrastructure, and remote-plasma PECVD capability.

GitHub: [bluebflatminor](https://github.com/bluebflatminor) · Released CC0 1.0 — no rights reserved.
