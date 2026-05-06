# photonic-memory-paper4

**Graphene Integration Route Selection for Ferroelectric Photonic Memory:
A Bayesian Quality Assessment Across Ten Process Scenarios**

*Nils Haaland — Solbakken Research Initiative, Omaha*
*Version 10.0 — May 2026*

---

## What this is

This repository contains the white paper, simulation framework description, and prior parameter documentation for Paper 4 of the Solbakken Research Initiative's four-paper series on non-volatile photonic weight memory for AI acceleration.

The paper is a **pre-experimental decision framework** — not a results paper. It asks: given ten candidate routes for integrating graphene into a ferroelectric photonic memory stack, which should a laboratory attempt first, and why? It answers that question using a Bayesian Monte Carlo simulation anchored to primary experimental literature, ranking ten routes by joint probability of meeting five simultaneous graphene quality criteria.

**No experimental prototype combining graphene gating, ferroelectric polarization, and photonic waveguide operation has been demonstrated.** The route rankings are falsifiable theoretical predictions. The four experiments in Section 7 of the paper are the falsification protocol, not supplementary work.

---

## Epistemic status — read before citing

The most important correction relative to earlier versions of this work:

**Route F (SCD(111) Ni-assisted graphitization) achieves approximately 0% joint pass probability at the only peer-reviewed experimental anchor for this process family:** Kanada et al. (2017) reports 140 cm²/V·s room-temperature Hall mobility and 5.7×10¹³ cm⁻² carrier density for Ni-assisted graphitization on SCD(111), pre-H-termination.

The 57.2% projected ceiling for Route F under H-termination is a **theoretical upper bound** derived from diamond surface phonon scattering models (Hicks et al. 2024). It has no direct experimental confirmation. The gap between the Kanada anchor (~0%) and the Hicks ceiling (57.2%) is an experimental gap, not a theoretical one. Experiment 1 in Section 7 is the measurement that begins to close it.

**Route I (CVD/Pt → hBN encapsulation, 38.6%)** is the only route with a meaningful demonstrated joint pass probability and remains the rational near-term entry point.

---

## Principal results

| Route | P(all 5) | Status | Binding constraint |
|-------|----------|--------|--------------------|
| A–D: UNCD graphitization | ~0.000 | Eliminated — substrate physics | Domain size |
| E: SCD(111) direct | ~0.000 | Eliminated — device physics | Mobility / n* |
| F1: SCD(111) Ni, demonstrated | ~0.000 | Kanada 2017 anchor | Mobility / n* |
| F2: SCD(111) Ni+H, theoretical | 57.2% | Theoretical upper bound only | n* |
| G: CVD/Pt → SiO₂ | 13.7% | Transfer penalty | n* (next: mobility) |
| H: CVD/Cu → SiO₂ | 8.2% | Transfer penalty | n* (next: mobility) |
| **I: CVD/Pt → hBN** | **38.6%** | **Highest demonstrated** | **Mobility** |
| J: CVD/Pt → SCD(111) | 21–36% | Engineering estimate, unverified | n* (next: mobility) |

N = 200,000 Monte Carlo samples. Sampling error < 0.05 percentage points.

---

## The four experiments — falsification protocol

Ordered by decision value:

1. **Route F Mobility Mapping** — Does H-termination produce any usable improvement over the 140 cm²/V·s Kanada baseline? This determines whether Route F is experimentally accessible at all.

2. **Route J Transfer Penalty** *(highest priority)* — Replace the ~10× order-of-magnitude transfer penalty estimate with a measured value. Determines whether SCD(111) substrate infrastructure investment is justified before Route F process maturity.

3. **Raman Strain–Doping Decomposition** — Build the metrology instrument that separates compressive strain from carrier doping in CVD/Pt graphene. Required for all other experiments to report carrier density with quantified uncertainty.

4. **Spatial Carrier Density Mapping** — Measure the spatial correlation length L_corr of carrier density fluctuations. Determines whether global calibration or cell-by-cell trimming is required at target array sizes.

---

## Repository contents

```
photonic-memory-paper4/
├── index.html          # Full white paper — rendered at GitHub Pages
├── README.md           # This file
├── LICENSE             # CC0 1.0 Universal
```

Simulation code and prior parameter files will be added as supplementary material. The Monte Carlo engine is straightforward: correlated lognormal draws via Cholesky decomposition, 200,000 samples, five independent pass/fail gates. Prior parameters are fully documented in Table 3 of the paper.

---

## Related repositories

| Repository | Contents |
|------------|----------|
| [graphene-photonic-memory-routes](https://github.com/bluebflatminor/graphene-photonic-memory-routes) | Simulation code and priors JSON for route ranking (companion to this paper) |
| [on-slop](https://github.com/bluebflatminor/on-slop) | Field guide to LLM-assisted research quality control |

---

## Key literature

The two results that most directly constrain this framework:

- **Kanada et al.** (2017). Fabrication of graphene on atomically flat diamond (111) surfaces using nickel as a catalyst. *Diamond and Related Materials* 74, 24–28. doi:10.1016/j.diamond.2017.01.011 — *Route F demonstrated mobility anchor: 140 cm²/V·s, pre-H-termination.*

- **Hicks et al.** (2024). Graphene on single-crystal diamond for electronic applications: a review. *physica status solidi (a)* 221, 2400567. — *Route F theoretical H-termination mobility ceiling: 8,000–10,000 cm²/V·s.*

- **Banszerus et al.** (2015). Ultrahigh-mobility graphene devices from CVD on reusable copper. *Science Advances* 1, e1500222. — *Route I carrier density transfer penalty anchor: ~5× for hBN encapsulation.*

Full reference list in the paper (index.html).

---

## Collaboration and contact

This paper is a call to the field. The four experiments in Section 7 are offered as a prioritised, decision-branched experimental roadmap for any group with access to:

- SCD(111) substrates and Ni-assisted graphitization toolsets (Experiment 1)
- CVD/Pt graphene and Hall measurement infrastructure (Experiments 2–4)
- hBN transfer capability (Experiment 2 reference arm)

If your group is working on any of these measurements, the author would welcome contact.

**Nils Haaland** — nhaaland@yahoo.com
Solbakken Research Initiative, Omaha

---

## Acknowledgements

The author thanks Claude (Anthropic) for sustained dialogue partnership throughout the simulation design, prior construction, red-team review, and manuscript development. The author retains sole responsibility for all numerical estimates, prior choices, and conclusions. This work was conducted independently without institutional funding.

---

## License

CC0 1.0 Universal — see LICENSE. This work is dedicated to the public domain. You may copy, modify, and distribute it without asking permission.
