# Graphene Integration Route Selection for Ferroelectric Photonic Memory

**Paper 4 of 4 — Solbakken Research Initiative**
Nils Haaland · Independent Researcher, Omaha · CC0 1.0 (public domain)

A pre-experimental decision framework that ranks eleven candidate routes for integrating graphene into a ferroelectric photonic memory stack, by the joint probability that each meets five simultaneous material-quality criteria. It ends with five experiments, ordered by decision value, that would collapse the decision space before fabrication begins.

**Current version: v10.12 (draft), September 2026 — loss-closure pass.**

---

## What this is

Photonic matrix-vector multiplication is a strong candidate for energy-efficient AI inference, and its unresolved problem is weight storage: phase weights in thermo-optic or electro-optic shifters are volatile, so every inference cycle reloads them from external memory. A ferroelectric-gated graphene cell would store the weight in remnant polarization and read it out in absorption.

No published prototype does this. The constituent physics exists piecewise — ferroelectric gating of graphene was proposed in 2011, volatile Pauli-blocking waveguide modulators have been mature since 2011, and non-volatile ferroelectric photonic memories are demonstrated in adjacent material systems — but not in this combination.

Before any of that can be built, someone has to choose how to get graphene onto the stack. Eleven routes exist. They differ in substrate physics, growth mechanism, transfer method and process maturity, and no single group can test them in parallel. This paper answers *which to attempt first*, using a Bayesian Monte Carlo simulation anchored to primary literature, and it separates constraints that are irreducible substrate physics from those that are reducible process variables.

**It is not a results paper and not a device prediction.** Every threshold is a theory-derived hypothesis calibrated to an architecture that has never been built. The route rankings are falsifiable predictions; §7 is the protocol for falsifying them.

## Headline findings

**The array size is the binding architectural choice, and it is not 64×64.** Residual absorption in the Pauli-blocked state depends on carrier mobility alone — the Fermi level cancels exactly — which gives a closed-form exchange rate between weight dynamic range and insertion loss, independent of interaction length and layer count. Running a 64×64 tile inside a 0.5 dB per-path budget needs 11,700–30,200 cm²/V·s depending on the weight precision demanded. The theoretical ceiling for graphene on diamond is 8,000–10,000. **64×64 does not close for any route, including Route F at its ideal limit. N ≈ 16 does** — and N ≈ 16 is independently where demonstrated coherent meshes sit.

Route rankings, at the N = 16 baseline:

| | |
|---|---|
| **Route I** (CVD/Pt → hBN) | 38.6% — highest at current demonstrated state; the rational near-term entry point |
| **Route J** (CVD/Pt → bonded SCD(111)) | 21–36% — the development bridge, and the highest-priority unverified hypothesis |
| **Route F** (SCD Ni/Cu graphitization) | ~0% at all three peer-reviewed graphitization anchors; ≈54% at a theoretical ceiling nobody has demonstrated |
| **Routes A–D** (UNCD) | eliminated by substrate physics — nm-scale grains cannot yield 10 µm domains |
| **Route K** (direct PECVD on Al:HfO₂) | ~0%, but by *reducible* nucleation kinetics — deferred, not closed |

The single most valuable measurement in the programme is a Hall mobility measurement on H-terminated SCD(111) graphene. It either opens Route F or closes it — and the closure condition now says what Route F would be *for*: mobility buys array size directly, N ≈ 16 at today's demonstrated transferred-film transport and N ≈ 25–44 at the theoretical ceiling. Route F is the difference between a 16-channel tile and a 32-channel one.

## How to read this document

Read the gaps as content. This is a working draft of a developing research plan, and at every version it will contain open items, flagged marginals, uncomputed cells, and claims at differing verification tiers — by design. Completeness is not the goal and its *appearance* is a hazard: a table with every cell filled and a ledger with every row marked "verified" are the shapes this document is most likely to fail into. Where a value has not been computed or a source has not been read, the document says so in place rather than supplying something plausible.

Three reading rules:

1. **Trust the ordinal ranking, not the cardinal values.** Route I > J > G > H is robust to reasonable perturbation of priors and correlations. "38.6%" is not; read it as "around one-third per cell."
2. **Check the provenance tag before quoting a number.** Priors anchored to peer-reviewed Hall measurements, to a theoretical ceiling, and to nucleation theory are all in the same table and are not the same kind of thing.
3. **Four cells in Table 4 are known to be unsupported.** They are marked. Do not quote them pending the Monte Carlo rerun.

## The verification protocol

The paper has been through eleven revision cycles under a mandatory per-reference DOI-resolution gate. Three fabricated or misattributed citations have been caught and documented (v10.1, v10.4, v10.8), plus one numerical-drift incident caught before entry (v10.9). Removed entries stay in the reference list as tombstones. The cumulative revision log is never silently edited — including entries later found to be wrong, which are annotated rather than deleted.

**Verification tiers.** Every claim sourced since v10.9 carries one, and they are never collapsed:

- **[T1 read]** — the full artifact was retrieved and read
- **[T2 record]** — a publisher or preprint-server record was seen; full text not retrieved
- **[T3 secondary]** — corroborated only through third-party citation lists or another paper's restatement. **Never sufficient for a numerical value** — this is the class that produced the v10.9 drift incident
- **[C correspondence]** — established by direct communication with a named participant, attributed by name and date, used only where that person is positioned to know, and never for a value a published record could supply

Identifier verification and value verification are separate acts. A reference can be T1 for its bibliographic data and T3 for a number attributed to it.

**Clean-room convention.** The instrument that makes a correction does not close its own item. Every cycle's corrections remain open pending a human archive pass, and each revision-log entry records which instrument produced it.

**A gate pass is not a correction.** New in v10.11: entries that resolved cleanly carry a green tag, corrections keep amber. Through v10.10 both rendered identically, which meant a document that logged its errors and not its clean results would drift toward believing itself worse-founded than it is.

## What changed in v10.12

A loss-closure pass. v10.11 had flagged transparent-state insertion loss as the framework's most consequential unknown. It was computed, and it eliminated a baseline the paper had carried since v10.0.

**The computation.** With ωτ ≫ 1 at 1550 nm, `Re σ_intra = e³v_F²/(πℏ²ω²µ)`. The Fermi level cancels, because τ = µm\*/e and m\* = E_F/v_F². Normalising to σ₀ = e²/4ℏ gives dB of weight range per dB of loss — a figure of merit independent of interaction length and layer count. So the 50 µm interaction length assumed throughout was never a free parameter; changing it slides along the exchange rate rather than improving it.

**The result.** Mobility needed to close 0.5 dB per path:

| Required weight range | N = 16 | N = 64 |
|---|---|---|
| 7 dB (with retraining) | 2,930 | 11,700 |
| 10 dB | 4,190 | 16,800 |
| 12 dB (≈4 bits) | 5,030 | 20,100 |
| 18 dB (≈6 bits) | 7,540 | 30,200 |

Against an 8,000–10,000 ceiling: **every N = 64 value is unreachable, every N = 16 value is reachable**, and the low end is met at the mobility threshold the paper has carried since v10.0. The uncertainty in the requirement moves the crossover, not the verdict.

**Consequences.**
- The baseline moves to N = 16. 64×64 is retained as the demonstrated-infeasible case.
- Two of the five thresholds — mobility and n\* uniformity — are not material constants but array-size choices. The fixed 3,000 cm²/V·s threshold is replaced by a closure condition, `N·R/FOM(µ) ≤ B`.
- Table 2 is rebuilt as a feasibility surface and promoted from sensitivity check to central result. Its P(array) column is deleted.
- §6.7 is new: retraining a network against its hardware's actual weight range relaxes the requirement, and is the only non-material lever in the framework.

**A caught error, recorded because it nearly shipped.** The required weight range was first pinned at 12 dB using a one-bit-per-3-dB rule. That rule is a *slope* — bits = ER_dB/3 − constant — and the constant was taken as zero from a source snippet truncated mid-sentence. A second check replaced the point estimate with a 7–12 dB bracket. The verdict proved insensitive to the whole bracket, which is the only reason it wasn't load-bearing. Third instance in four cycles of a number inferred rather than retrieved; the pattern isn't the sources, it's the pull toward converting a bracket into a point estimate.

**Kills.** [5] and [19] deleted as orphans (tombstoned, with the reason recorded as distinct from [18]'s fabrication). [31] demoted from reference to lead after three cycles supporting nothing. "Carbon 2021" withdrawn as a Table 3 anchor, closing defect V4 by re-anchoring Route E to the F1 set rather than by identification. [12] finally cited in §6.4, where edge contact bears directly on the contact-failure pattern — it had sat uncited since v10.0 while that section was written without it.

**What it does not do.** The Drude floor is a floor; measured devices sit ~95× above it, and that gap is precisely what the other four criteria describe. Closure at N = 16 is necessary, not sufficient. No joint probability is recomputed — moving to N = 16 loosens n\* fourfold and raises every route's marginal, and the Monte Carlo rerun is open. And the computation itself is this paper's own arithmetic, checked by no second instrument and no human, which given that it eliminated a baseline is now the most important open item in the document.

## What changed in v10.11

A citation-gate pass, aimed at the legacy reference tier that had been open since v10.8.

**Six gate passes.** [7] Kim 2009, [8] Gao 2012, [9] Banszerus 2015, [10] Pizzocchero 2016, [13] Yazyev & Louie 2010, [14] Tsen 2012 — all resolved live, all correct as attributed. This matters as a *negative* result: v10.8's three-entry sample of this tier returned three errors, and the obvious inference that the tier was systematically bad turns out to be wrong.

**Three banner items closed.**
- *Item 10* — the Table 3 anchor label "JAP 2013" is Tokuda et al., *Jpn. J. Appl. Phys.* 52, 110121 (2013), now promoted to [47].
- *Item 11* — both prior-art leads checked. Neither breaches the novelty claim.
- *Item 18* — IEC TS 62607-6-24:2026 confirmed across two further independent records.
- *Item 5* — closed by **removal**: the uncited "65 fJ per write event" figure is deleted, not re-anchored.

**And four new defects, three of which the closures created.**

- **Verification defect V4.** Identifying "JAP 2013" revealed that it reports TEM structural characterisation with *no transport data*, and it has been carrying Route E's mobility prior since before v10.0. The elimination verdict for Route E stands on independent evidence; the number in Table 3 is sourced to a paper that does not contain it. *An unidentified anchor label cannot be checked for whether it supports the value attached to it — which is why bibliographic housekeeping was concealing a defect.*
- **[36] does not cover this paper's use.** Confirming the standard also supplied its scope: clean CVD films on SiO₂/Si, excluding twisted multilayer structures. Both exclusions apply here. Withdrawn from Experiment 1.
- **[10] is exfoliated, not CVD.** Route I's hBN transfer penalty rests on a three-step analogy, previously stated as two.
- **Title truncation.** Four of six gate-passed entries carried shortened titles. One mattered: dropping "single-crystal" from [8] understated what the Route G/J growth prior rests on.

**Two findings that strengthen existing corrections.** A second independent monolayer counter-anchor ([49], 3–5 layers) now supports the v10.9 correction that rested on a single source; and a fourth published role for graphene in this device class ([48], photoswitchable sp²/sp³ junction) makes the novelty claim stated against four occupied positions rather than three.

**One structural change.** §2.2 now states plainly that the 0.5 dB insertion-loss budget is **per optical path**, not per array — which Table 2's 1/N scaling had implied since it was written but the prose never said. That puts passive mesh loss outside the tolerance chain where it belongs, and exposes the framework's most consequential known gap: transparent-state loss per unit length may bind before any of the five modelled criteria, and it is not one of them. Recorded as a candidate sixth criterion.

## Repository contents

```
paper4-v10.12.html    The paper. Self-contained; no build step.
loss-closure.py       Supplementary: the §2.2a computation. Stdlib + numpy.
README.md             This file.
```

The HTML is a single file with inlined CSS, two webfont links, and one small progress-bar script. It supports light and dark rendering, prints cleanly (the pre-deployment banner is suppressed and link URLs expand), respects `prefers-reduced-motion`, and carries keyboard focus styling and a skip link.

**Before deploying:** delete the red dashed `PRE-DEPLOYMENT DRAFT` block near the top of `<main>`. It lists 36 open items and is for the author, not the reader.

## Status and open work

The largest open items, in rough priority order:

1. **Independent check of the §2.2a computation** — it eliminated a baseline and no second instrument or human has verified it (item 36)
2. Monte Carlo rerun against the N-dependent closure condition; N = 16 loosens n\* fourfold and moves every joint probability (item 33)
3. A better anchor for the required weight dynamic range — currently a 7–12 dB bracket from two sources (item 32)
4. How far above the Drude floor a real device actually lands; without it the feasibility surface is only a bound (item 34)
5. Complete the legacy gate — [4] remains unresolved; identify "Zhang 2012" (items 3, 4)
6. Human archive pass over four cycles of single-instrument corrections (items 6, 12, 30, 36)

## Contributing and falsification

This paper is a call to the field. The author does not have access to the experimental infrastructure required to execute Experiments 1–5, and offers them as a prioritised, decision-branched roadmap for any group with SCD(111) substrates, hBN transfer protocols, Hall measurement infrastructure, and remote-plasma PECVD capability.

The framework's primary falsification target is a working device — a graphene-gated ferroelectric photonic memory cell at any route and any quality level. That result would supply the first experimental anchor for thresholds that are currently all theory.

Corrections to citations, priors, arithmetic or physics are welcome and will be logged rather than silently applied, including the ones that are embarrassing. The revision log's value is that it has never been cleaned up.

**Contact:** nhaaland@yahoo.com

## License

CC0 1.0 Universal — released to the public domain. Simulation code and prior parameter files will be released as supplementary material upon journal submission.
