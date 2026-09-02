# Graphene Integration Route Selection for Ferroelectric Photonic Memory

**Paper 4 of 4 — Solbakken Research Initiative**
Nils Haaland · Independent Researcher, Omaha · nhaaland@yahoo.com
**Version 10.10 (draft), August 2026** · CC0 1.0 — released to the public domain

A pre-experimental decision framework: a Bayesian Monte Carlo simulation that
ranks eleven candidate routes for integrating graphene into a ferroelectric
photonic memory stack, by joint probability of meeting five simultaneous quality
criteria, and specifies five experiments — ordered by decision value — that most
efficiently collapse the decision space before fabrication begins.

---

## Status: work in progress

**This is a working draft of a developing research plan. It is not, and is not
trying to be, a finished artifact.** Every version will carry open items, flagged
marginals, uncomputed cells, and claims sitting at different verification tiers.
That is the intended state, not a shortfall in it.

The aim is honesty and factual accuracy, not the appearance of completion — and
those pull against each other more often than they sound like they should. A
table with every cell filled and a ledger with every row marked "verified" are
the shapes this work is most likely to fail into, because a plausible number is
easier to produce than a checked one and looks identical on the page. So: where a
value has not been computed, the cell says so and stays empty. Where a source has
not been read, the entry says so and supports nothing. **Read the gaps as
content.** They are the parts that have not been faked.

## What this is, and what it is not

**It is** a prioritisation tool for experimental investment. It answers "which
routes should we attempt first?" before the first wafer is loaded.

**It is not** a prediction of device performance. Every threshold in the
Goldilocks window is a theory-derived hypothesis calibrated to a 64×64 MVM tile
that has never been built. No published prototype uses ferroelectric remnant
polarization to gate graphene as the sole optically modulated medium in a
photonic waveguide, so the framework has **no experimental anchor at the device
level**. Route rankings are falsifiable theoretical predictions; §7 is the
falsification protocol.

**Read the ordinal ranking, not the percentages.** Route I > Route J > Route G >
Route H, with the UNCD routes, SCD direct graphitization, Route F at its
demonstrated state, and Route K at the bottom. Reasonable perturbations to priors
and correlations move individual values by several points without changing that
order. "38.6% for Route I" is more honestly read as "the highest-probability
current path, around one-third per cell."

## Headline results

| | |
|---|---|
| **Rational near-term entry point** | Route I — CVD/Pt graphene, hBN encapsulation. 38.6% per cell. |
| **Highest-priority unverified hypothesis** | Route J — CVD/Pt bonded to SCD(111). 21–36%. Experiment 2 validates or kills it. |
| **Closed by substrate physics** | UNCD routes A–D. 2–5 nm grains cannot yield 10 µm domains. |
| **Closed at every measured anchor** | Route E, and Route F at its demonstrated graphitization state (~0%). |
| **Deferred, not closed** | Route K — direct PECVD on Al:HfO₂. Fails on nucleation kinetics, which are reducible. |
| **Highest-value single measurement** | Hall mobility on H-terminated SCD(111) graphene, with monolayer fraction and a bare-substrate reference arm (Experiment 1). |

## Verification protocol

Every reference in this document must resolve — DOI to claimed title, authors and
venue — before deployment. The gate is mandatory and pre-deployment, not
post-hoc. Corrections are **cumulative and never silently applied**: removed
entries stay in the reference list as tombstones, and the full revision log is
preserved in the Appendix with its original wording, including statements later
found to be wrong.

**Verification tiers (v10.9).** Claims carry one of three provenance levels,
never collapsed into one another:

| | |
|---|---|
| **T1 read** | Full artifact retrieved and read. |
| **T2 record** | Publisher or preprint-server record seen — bibliographic detail and any displayed values confirmed — full text not retrieved. |
| **T3 secondary** | Corroborated only through third-party citation lists or another paper's restatement. **Never sufficient for a numerical value.** |

Tiers are assigned **per value, not per reference.** A reference can be sound at
the identifier level and unsourced at the value level; that combination has
produced two documented failures, and it is the gap the earlier gate did not
cover. Where a reference's bibliographic tier and a value's tier differ, both are
stated.

Caught to date and documented in the log:

- **Three fabricated or misattributed citations** — v10.1 (Hicks→Aitkulova,
  Tang→Qian), v10.4 (reference [18], fabricated, survived two verification
  rounds), v10.8 (Koike→Taki, Sumant→Berman, Yan→Yu).
- **One numerical drift**, v10.9 — an anchor value taken from a *citing* paper's
  restatement rather than from the source, wrong by 1.6× in mobility and 12× in
  carrier density. The gate as previously operated checked names and identifiers,
  not the numbers those references were asked to carry.
- **Four defects inside v10.9's own corrections**, caught by a provenance audit
  before deployment and logged rather than quietly fixed: an unsourced monolayer
  figure written into six locations and withdrawn; an uncomputed probability
  entered into a results table and blanked; a substantive claim built on a survey
  that was never successfully retrieved; and a ledger that reported
  publisher-snippet matching as direct DOI resolution. The tier scheme above
  exists because of the fourth.
- **Two documented instrument failure modes** — a second LLM instrument reporting
  its own retrieval failure as a nonexistence claim (v10.7), and an adversarial
  panel independently regenerating the mechanism of a known-fabricated reference
  (v10.5).

Corollary rules in force: preprints are marked as such and may not anchor a
prior; concordance between two LLM instruments is correlated evidence, not
independent verification; and the correcting instrument does not close its own
items — a human archive pass is the final gate.

## v10.10 — standards pass

A scan of the graphene standards landscape, which v10.9 omitted despite two
sections resting on claims about it.

- **A scope error in our own citation.** ISO/TS 23359:2025 is scoped to powders
  and liquid dispersions, not sheets on substrates. It was cited as a lower tier
  of the needed measurement; it is a different material form. The paper's
  argument is stronger after the correction.
- **Three sheet-scoped standards were omitted**, covering between them layer
  count, coverage, disorder and strain uniformity — four measurements this paper
  treated as unstandardised. One of them, IEC TS 62607-6-24:2026, published in
  June 2026, after the previous scan window. Experiment 3's claim is narrowed to
  what is genuinely uncovered: the strain-from-doping decomposition, the
  substrate-dependent doping offset, and carrier-density uniformity.
- **A reproducibility bound on our own correction.** The interlaboratory study
  behind ISO/TS 21356-2 found up to 200% spread in I(2D)/I(G) between labs
  without relative intensity calibration. The v10.9 monolayer correction survives
  — 19.8% against a >95% criterion is far too wide a gap for that to close — but
  Experiment 1 now specifies the calibration and fitting protocol.
- **A fourth disorder channel, named and deferred.** Nanometre-scale strain
  fluctuation is absent from the correlation structure and is coupled to the
  substrate roughening measured in v10.9. Adding it is deferred, not attempted:
  doing it properly needs fitted correlation coefficients, and the existing ones
  are unfitted.
- **The 64×64 baseline checked against demonstrated scale.** Coherent MZI-mesh
  processors are reported at single- to low-double-digit channel counts. 64×64 is
  a design target, not a scaled version of anything built — and the field's
  answer to mesh scaling is wavelength parallelism rather than larger N, which
  this framework does not model.

Every standards claim this cycle is **T2 or weaker. No standard was read.**

## v10.9

An external literature scan, not a red-team pass. Principal changes:

- **Route F1 expanded from one graphitization anchor to three.** 140 cm²/V·s on
  (111) (Kanada 2017), 79 cm²/V·s on (100) (Suntornwipat 2023), ~670 cm²/V·s on
  (100) with a Cu catalyst (Ueda 2016) — every anchor at n ≥ 10¹³ cm⁻². The ~0%
  result is unchanged and now rests on three independent measurements.
- **The monolayer-coverage marginal is contradicted by measurement.** Modelled at
  0.778; the one anchor that reports it gives ~19.8% against a >95% criterion.
  First Goldilocks criterion in this paper with a measured value contradicting a
  modelled one. F2's ≈54% ceiling inherits the same marginal. (A companion figure
  attributed to the (111) anchor was withdrawn within the cycle as unsourced; the
  correction stands on the single sourced measurement.)
- **Ni graphitization is measured to etch the substrate** — roughness 3 → 7–9 nm,
  step 1.76–12.3 nm. An unpriced constraint for a route premised on an atomically
  flat waveguide interface.
- **The H-plasma-after-graphitization step gains its first citation**, and the
  (111) surface an open metallic-vs-semiconducting dispute. Experiment 1's
  parallel-conduction control now faces three candidate paths, not one.
- **Route I's defect-density marginal flagged** against integration-sequence data.
- **The novelty claim's readout clause demoted to descriptive** — absorption
  readout alone does not distinguish the cell; graphene as sole modulated medium
  does.

One cell in Table 5 is deliberately blank. **Three marginals are currently known
to be unsupported and have no replacement value** (F1 and F2 monolayer coverage; Route I defect density). The ordinal
ranking is unaffected. Those cells should not be quoted until the Monte Carlo
companion rerun reports.

## Open items

Carried in the pre-deployment banner at the top of the document, which is deleted
only when the list is clear. Twenty-one items are open as of v10.10, including
the legacy-tier DOI-gate pass (nine references never individually resolved), the
Monte Carlo companion rerun, three Table 3 anchors that never entered the
numbered reference list, one uncited energy figure, two unchecked prior-art
leads, four items generated by v10.9's own audit of itself, five from the v10.10
standards pass, and the human archive pass. Item 17 closed in v10.10 by
correspondence — the first closure since v10.7; items 7–22 are scope expansion.

Three verification defects also remain open: mobility marginals not regenerating
from priors (V1); defect-density and monolayer-coverage marginals lacking
published priors (V2, partly closed in v10.9); and a correlation matrix that is
only marginally positive definite, with 36% of the perturbation sweep
non-positive-definite (V3).

## Files

| File | |
|---|---|
| `index.html` | The paper. Self-contained; fonts from Google Fonts, no other dependencies. Light and dark modes. |
| `README.md` | This file. |

## A note on the acknowledgement

Simulation design, prior construction, red-team review, and citation verification
were carried out in sustained dialogue with an LLM instrument (Claude, Anthropic).
That instrument's outputs are treated throughout as readings to be scored, not as
authorities — hence the gate, the tombstones, the instrument-record notes, and the
rule that the correcting instrument cannot close its own items. The v10.9 log
documents four defects found in that instrument's own corrections during the same
cycle. They were caught, which is the protocol working; that they were caught by
the same instrument that produced them is not evidence the audit was exhaustive,
which is why the human pass remains the final gate. All numerical
estimates, prior choices, and conclusions remain the author's sole responsibility.

## Citing this work

> Haaland, N. *Graphene Integration Route Selection for Ferroelectric Photonic
> Memory: A Bayesian Quality Assessment Across Eleven Process Scenarios.*
> Solbakken Research Initiative, Paper 4, v10.10 (draft), August 2026. CC0 1.0.

## A call to the field

The author does not have access to the experimental infrastructure required to
execute Experiments 1–5. They are offered as a prioritised, decision-branched
roadmap for any group with SCD(111) substrates, hBN transfer protocols, Hall
measurement infrastructure, and remote-plasma PECVD capability. Simulation code
and prior parameter files will be released as supplementary material on journal
submission.

The primary falsification target for the whole framework is a working device —
any graphene-gated ferroelectric photonic memory cell, at any route, at any
quality level. Corrections, contradicting measurements, and failed replications
are welcome at the address above and will be logged, not quietly absorbed.
