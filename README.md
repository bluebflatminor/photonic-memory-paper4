# Graphene Integration Route Selection for Ferroelectric Photonic Memory

**A Bayesian Quality Assessment Across Eleven Process Scenarios**
Paper 4 of 4 · Solbakken Research Initiative · Nils Haaland, Independent Researcher, Omaha

**Read the paper:** https://bluebflatminor.github.io/photonic-memory-paper4/

---

**Current version: v10.4 (June 2026) — citation-integrity & measured-anchor revisions.**
The canonical changelog is the Revision Log section of the paper itself; this README does not duplicate it. Headline changes: one fabricated reference removed and tombstoned ([18]); one reference re-scoped (transfer-free is not catalyst-free); the first published Hall comparison of graphene on H- vs O-terminated single-crystal diamond (Aitkulova et al., *Carbon Trends* 2025) incorporated as a measured anchor; Route F2 ceiling-truncated (57.2% → ≈54%).

## What this is

A pre-experimental decision framework. No experimental prototype combining graphene gating, ferroelectric polarization, and photonic waveguide operation has been demonstrated — by anyone. Eleven candidate routes exist for integrating graphene into a ferroelectric photonic memory stack, and no single group can test them all. This paper ranks the routes by joint probability of meeting five simultaneous graphene quality criteria, separates substrate-physics constraints (irreducible) from process-kinetic constraints (reducible), and specifies five experiments — ordered by decision value, each with explicit decision branches — that most efficiently collapse the route space before anyone loads a wafer.

The route rankings are falsifiable theoretical predictions. Section 7 of the paper is the falsification protocol. The author does not have access to the experimental infrastructure required to run it; the paper is a call to the field.

## Key findings (v10.4)

- **Route I (CVD/Pt → hBN encapsulation): 38.6%** — the highest joint pass probability at demonstrated state, and the rational near-term entry point. Its ceiling is structural: polycrystalline grain boundaries in the CVD film, which no transfer optimisation removes.
- **Route F (SCD(111) Ni-assisted graphitization + H-termination) splits into numbers that must not be conflated:** ~0% at the only peer-reviewed graphitization anchor (Kanada 2017, 140 cm²/V·s); ≈5% at the newly measured transferred-film anchor (Aitkulova 2025, 1,644 cm²/V·s on H-terminated (100) diamond, film-limited); ≈54% at the ceiling-truncated theoretical bound, which no experiment has approached.
- **The Aitkulova measurement confirms the mechanism, not the magnitude:** H-termination raises the remote-phonon energy barrier (114 vs 60 meV) — the physics behind Route F's ceiling — while the configuration this framework actually needs, H-terminated (111) with a graphitized film, remains unmeasured. Experiment 1 specifies that measurement.
- **All UNCD routes and Route K fail today, but for categorically different reasons:** UNCD by irreducible substrate physics (closed); Route K (direct PECVD on the ferroelectric oxide) by reducible nucleation kinetics (deferred, pending Experiment 5).
- **Every route lands in the calibration-dependent regime** — the regime CMOS entered in the 1990s. Single-crystal substrates are eventually a requirement, not a preference; the framework puts a number on the crossover (3,500–4,500 cm²/V·s).

## Repository contents

- `index.html` — the paper, self-contained, auto dark mode (GitHub Pages)
- Monte Carlo companion tool — reproduces all Table 4/5 figures from the Table 3 priors and §4.2 correlation structure
- This README

## Methodology

Every paper in this program follows the same workflow: physics-problem framing → structured multi-AI adversarial review (multiple independent models, each pass triaged into fold-in / reframe / discard) → public deployment with the full revision history visible. Corrections are made in place and tombstoned, never silently rewritten. All versions of this paper, including its errors, are documented in the Revision Log.

### Reference verification (added v10.4)

Per-reference DOI resolution is a mandatory pre-deployment step for every paper and note in this program: each DOI must resolve to the claimed title, authors, and venue before anything ships. The rule exists because this paper failed without it. Three fabricated citations entered published versions — two caught at v10.1, a third at v10.4 — despite structured multi-AI adversarial review. All three are documented in the Revision Log, and the third ([18]) is retained in the reference list as a tombstone. The protocol's failures are part of its record.

The general lesson is worth stating plainly: AI-assisted literature work generates plausible, well-formatted, nonexistent references, and no amount of reviewing the *text* catches them. Only resolving the identifiers does. Review checks arguments; verification checks objects.

## For experimental groups

The five experiments in §7 are offered as a prioritised, decision-branched roadmap for any group with access to SCD(111) substrates, hBN transfer protocols, Hall measurement infrastructure, or remote-plasma PECVD capability. Each experiment names the prior it updates and the decision each branch triggers. Experiment 1 (Hall mobility of graphitized graphene on H-terminated SCD(111), with parallel-conduction control) is the highest-decision-value measurement in the framework — and as of v10.4 it has a published adjacent-process benchmark to beat.

Questions, corrections, and collaboration inquiries: nhaaland@yahoo.com. Corrections are especially welcome; they get tombstoned, credited, and folded into the next version.

## How to cite

Haaland, N. (2026). *Graphene Integration Route Selection for Ferroelectric Photonic Memory: A Bayesian Quality Assessment Across Eleven Process Scenarios* (v10.4). Solbakken Research Initiative. DOI: **[Zenodo concept DOI — fill on first release]**

## License

CC0 1.0 Universal — public domain. No attribution is required; citation is appreciated for traceability.
