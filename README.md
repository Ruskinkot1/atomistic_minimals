# Softness ≠ noise: PES softening in universal MLIPs

Research repo: systematic under-estimation of PES curvature in universal atomistic models
(M3GNet, CHGNet, MACE-MP-0, …) on crystals and molecules, and whether uncertainty can detect it.

## Plan
0. **Novelty check** — arXiv/OpenReview 2026: "PES softening" + "uncertainty", "Hessian", "phonons", "curvature fidelity".
1. **Curvature diagnostics** — Hessian / vibrational frequencies vs DFT: crystals (phonons), molecules (vib. spectra); transfer across domains and DFT functionals (GGA → r²SCAN, ωB97).
2. **Uncertainty test** — do ensembles / latent-space distances flag *softening* specifically, not just large errors?
3. **Method** — cheap curvature correction: Hessian calibration on few points; curvature-regularised fine-tuning; baseline = single-point fine-tuning.
4. **Benchmark** — "curvature-fidelity" metric and unified protocol.

Everything is local: inference + small fine-tuning of open models.

## Layout
- `src/curvature_fidelity/` — Hessian, frequencies, softening metrics
- `scripts/` — experiment drivers
- `data/` — datasets (git-ignored)
- `results/` — outputs (git-ignored)
- `docs/` — notes, novelty search log
