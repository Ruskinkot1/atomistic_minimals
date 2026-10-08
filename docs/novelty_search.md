# Novelty search (stage 0) — 2026-10-08, quick pass (not exhaustive)

## Closest prior work
- Deng et al., *Systematic softening in uMLIPs*, npj Comput. Mater. 2025 (arXiv:2405.07105). Defines softening scale = slope of pred vs ref; M3GNet/CHGNet/MACE-MP-0; crystals; one-point fine-tuning fix. **No uncertainty analysis, no molecules.**
- Heterogeneous ensemble uncertainty metric for foundation models (arXiv:2507.21297). UQ vs true error; **not tied to softening** (to verify from primary text).
- Wong & Yang, *Bias in uMLIPs and its effects on fine-tuning* (arXiv:2603.10159, 2026). Q-residual in PCA space as epistemic-uncertainty proxy for MD extrapolation; **does not test softening detection** (abstract only read). Closest 2026 neighbour — read in full.
- Fine-tuning tutorial (arXiv:2506.21935), fine-tuning study (arXiv:2506.07401): bias fixed by high-energy fine-tuning data.
- MACE-MP-0 JCP paper: phonon benchmarks on crystals; MLIPAudit (arXiv:2511.20487): molecular benchmark, **no Hessian/frequency test**.
- Hessian distillation (arXiv:2501.09009), AD Hessians for MACE (PMC12080109): tooling.

## Gaps (candidate contributions)
1. No gas-phase molecular harmonic-frequency benchmark of uMLIPs found -> softening on molecules untested.
2. No work found testing whether ensembles / latent distance detect *softening* (curvature bias) vs. large errors.
3. No cross-domain / cross-functional (GGA, r2SCAN, wB97) softening transfer study found.

## Still to do
- Read 2603.10159, 2507.21297 in full; search arXiv 2026 and NeurIPS 2026 accepted lists with: "softening" + "uncertainty", "curvature", "Hessian calibration".
- Check MACE-OFF / OMol25-model (UMA, eSEN) papers for frequency benchmarks (OMol25 may already cover vibrations).
