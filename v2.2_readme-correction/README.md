# KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework
**Version 2.2 — README Correction**  

**Author:** Vladimir Khomyakov — Independent Researcher  
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)  

**DOI:** [10.5281/zenodo.19026744](https://doi.org/10.5281/zenodo.19026744)  
**Concept DOI (all versions):** [10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18826258.svg)](https://doi.org/10.5281/zenodo.18826258)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) — Scientific article and associated documentation  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) — Source code and simulation scripts  

---

## Overview  

This directory accompanies Version 2.2 of the article *"KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework"*. The paper constructs a self-contained geometric framework unifying the local information geometry of Kullback–Leibler divergence with an observer-dependent theory of coarse-grained entropy on finite measurable spaces.  

The central result is the **Bridge Theorem (Khomyakov's Bridge)**: a finite observer resolution threshold ε induces a projection of probabilistic descriptions, resulting in measurable KL information loss — observer entropy — that scales quadratically with the threshold, controlled by the Fisher information geometry:  

$$S_{\mathrm{obs}}(p_\theta, \varepsilon) = \tfrac{1}{2}\,\varepsilon^2\, v^\top I(\theta^*)\, v \;+\; O(\varepsilon^3), \qquad \varepsilon \to 0^+$$  

where $I(\theta)$ is the Fisher information matrix and $v$ encodes the direction of information loss in parameter space.  

---

## What's New in Version 2.2  

**One change only:** a correction to the companion README.md file.  

Theorem numbers cited in the "Main Results" section of the README.md (versions v2.0 and v2.1) contained a clerical error: the numbers reflected an earlier internal draft rather than the published article. The theorem numbers in the article itself were correct in all versions and are unchanged. 

**Corrected references (README.md only):**  

| Result | Incorrect (v2.0–v2.1 README) | Correct |  
|---|---|---|  
| Bridge Theorem | Theorem 6.3 | Theorem 6.5 |  
| Sufficient Conditions | Theorem 6.29 | Theorem 6.41 |  
| Coordinate-Invariant Bridge Theorem | Theorem 7.1 | Theorem 7.3 |  
| Observer Entropy as Squared Generator Norm | Corollary 7.3 | Corollary 7.6 |  
| Second-Variation Characterization | Theorem 7.5 | Theorem 7.9 |  
| Bridge Theorem via Dissipation Functional | Corollary 7.7 | Corollary 7.13 |  
| Landauer Bound | Theorem 8.3 | Theorem 8.4 |  

There are **no changes** to the article, proofs, theorems, figures, or verification scripts relative to v2.1.  

**Note on theorem numbering.** The theorem numbers cited in the
"Main Results" section of the README files accompanying versions
v2.0 and v2.1 contained a clerical error: the numbers
(Theorem 7.1, Corollary 7.3, Theorem 7.5, Corollary 7.7)
reflected the numbering of the Riemannian-Geometric Reformulation
section (Section 7) as it appeared in versions v1.0 and v1.2,
and were inadvertently carried over to the v2.0 and v2.1 README
files — presumably from an earlier draft — without being updated
to reflect the renumbering that occurred when additional
environments were introduced in Section 6 (Sufficient Conditions)
in version v2.0. The theorem numbers in the article itself were
correct in all versions and are unchanged. This README corrects
the cited numbers to match the published article (v2.1):
Theorem 7.3, Corollary 7.6, Theorem 7.9, Corollary 7.13.

---

## What's New in Version 2.1  

**One change only:** a citation of independently and concurrently published work has been added to the end of the Introduction.  

The following passage was added at the end of the Introduction (before Section 2):  

> Independently and concurrently, Izumo (2026) introduces a KL-based measure of information loss under discrete partitions, motivated by explainability in machine learning. That framework does not derive a geometric scaling law linking the information loss to Fisher information.  

**Reference added:**
> Takumi Izumo, *Quantifying information loss under coarse-grained partitions: A discrete framework for explainable artificial intelligence*, arXiv:2502.07347 (2026). [doi:10.48550/arXiv.2502.07347](https://doi.org/10.48550/arXiv.2502.07347)  

There are **no mathematical changes** relative to v2.0. All theorems, proofs, figures, and verification scripts are identical to v2.0.  

---

## What's New in Version 2.0  

1. **Sufficient Conditions (Theorem 6.41).** The parametric deformation assumption is proved to be a consequence of three checkable finite-dimensional conditions (within-class neutrality, lift closure, immersion condition) that hold automatically for full exponential families with centered between/within parameterization. This reduces verifiability from an infinite-dimensional functional condition to finite-dimensional linear algebra.  

2. **Second Worked Example (Section 6.2).** Five-point space $\mathcal{X} = \{1,2,3,4,5\}$ with unequal clusters $\mathcal{P} = \{\{1,2,3\},\{4,5\}\}$ (3 distinct Fisher eigenvalues), providing structurally independent verification of the Bridge Theorem.  

3. **Extended Numerical Verification.** Five publication-quality figures covering both examples. All eight verification components pass for both configurations.  

---

## Main Results (Cumulative)  

1. **Bridge Theorem (Theorem 6.5, Khomyakov's Bridge).** Quadratic scaling law for observer entropy with explicit cubic remainder control.  
2. **Sufficient Conditions (Theorem 6.41).** The parametric deformation assumption is proved to be a consequence of three checkable finite-dimensional conditions (within-class neutrality, lift closure, immersion condition) that hold automatically for full exponential families with centered between/within parameterization.  
3. **Riemannian-Geometric Reformulation (Section 7).** The quadratic form $v^\top I\,v$ equals the Fisher–Rao inner product $g_\theta(v,v)$. Observer entropy is one-half the squared Fisher–Rao norm of the coarse-graining generator (Theorem 7.3, Corollary 7.6), and equivalently the second variation of the KL divergence along the coarse-graining orbit (Theorem 7.9). A dissipation functional unifies these perspectives (Corollary 7.13).  
4. **Cognitive Uncertainty Principle (Theorem 8.2).** Resolution–information trade-off relating the observer's finite resolution to minimal energetic cost of distinguishability.  
5. **Landauer Bound (Theorem 8.4).** Thermodynamic lower bound on the energetic cost of finite-resolution observation: $E_{\min} \ge kT \cdot S_{\mathrm{obs}}(p, \varepsilon)$.  
6. **Piecewise Smoothness (Proposition 9.5).** Observer entropy is piecewise-smooth in ε, with partition transitions at critical values given by interpoint distances of the metric space.  

All results are proved from explicitly stated assumptions with complete remainder estimates and hold uniformly over compact parameter subsets.  

---

## Numerical Verification  

The quadratic scaling law is verified by two independent worked examples with structurally distinct configurations:  

**Example 1** — Four-point space $\mathcal{X} = \{1,2,3,4\}$ with equal-size clusters $\mathcal{P} = \{\{1,2\},\{3,4\}\}$ (softmax family, 2 distinct Fisher eigenvalues). Fisher matrix: $I(\theta^*) = \mathrm{diag}(1, \tfrac{1}{2}, \tfrac{1}{2})$.  

**Example 2** — Five-point space $\mathcal{X} = \{1,2,3,4,5\}$ with unequal clusters $\mathcal{P} = \{\{1,2,3\},\{4,5\}\}$ (3 distinct Fisher eigenvalues). Fisher matrix: $I(\theta^*) = \mathrm{diag}(\tfrac{3}{2}, \tfrac{6}{5}, \tfrac{2}{5}, \tfrac{2}{5})$.  

The verification script confirms:  
- Quadratic scaling $S_{\mathrm{obs}} \sim \varepsilon^2$ (log-log slope = 2.000 ± 0.01 in all cases)  
- Bounded $O(\varepsilon^3)$ remainder  
- Fisher matrix agreement between analytic and finite-difference computations  
- Closed-form leading coefficients match Fisher-based predictions  
- Non-negativity of observer entropy (Landauer bound satisfied)  
- Monotone non-decrease $S_{\mathrm{obs}}(\varepsilon)$ (resolution–information trade-off)  

All checks pass: **PASS — ALL BRIDGE THEOREM CHECKS PASSED**.  

---

## Directory Contents  
```
v2.2_readme-correction/  
├── README.md              ← this file  
├── LICENSE  
├── requirements.txt  
├── scripts/  
│   └── verify_bridge_theorem_v2.py  
└── figures/  
    ├── fig1_bridge_theorem_verification.pdf  
    ├── fig2_relative_error.pdf  
    ├── fig3_resolution_information_tradeoff.pdf  
    ├── fig4_bridge_theorem_ex2.pdf  
    └── fig5_relative_error_ex2.pdf  
```

Scripts and figures are identical to v2.0. No new scripts or figures were added in this version.

> **Note on the verification script.** The script `verify_bridge_theorem_v2.py`
> in this directory reflects a minor correction to theorem number references in
> console output (introduced in v2.4); no changes to algorithms, computations,
> or results. The original script as published in the Zenodo archive for this
> version is available at the corresponding Zenodo record.  

---

## Figures  

- **Figure 1** — Bridge Theorem verification (Example 1): exact vs. predicted observer entropy and normalized remainder.  
- **Figure 2** — Relative error of the quadratic approximation (Example 1).  
- **Figure 3** — Resolution–information trade-off: monotone increase of $S_{\mathrm{obs}}(\varepsilon)$.  
- **Figure 4** — Bridge Theorem verification (Example 2): exact vs. predicted observer entropy for unequal clusters.  
- **Figure 5** — Relative error of the quadratic approximation (Example 2).  

---

## Requirements  

Python 3.9+  

Dependencies (specified in `requirements.txt`):  
```
numpy>=1.23  
matplotlib>=3.7  
```

Install with:  
```bash  
pip install -r requirements.txt  
```

---

## Running the Verification  

From this directory:  
```bash  
python scripts/verify_bridge_theorem_v2.py  
```

The script performs the following verifications for both worked examples:  
- Fisher information matrix: analytic vs. finite-difference agreement  
- Exact observer entropy vs. quadratic prediction across ε range  
- Bounded $O(\varepsilon^3)$ remainder  
- Relative error < 5% for ε ≤ 0.03  
- Log-log scaling slope = 2.0 ± 0.01  
- Non-negativity (Landauer bound)  
- Monotone non-decrease (resolution–information trade-off)  

Output figures are written to the `figures/` directory in both PDF and PNG formats.  

---

## Article File Integrity

The article and reproducibility package for this version are archived at two independent
permanent locations. Checksums are provided for independent verification.

**Version 2.2 — README Correction**

> **Note on the article file.** The article PDF (`observer_entropy_bridge_theorem_v2.1.pdf`)
> is identical to the file published in version 2.1. The only change in version 2.2 is a
> correction to the companion README.md (theorem numbers in the "Main Results" section).
> This identity is confirmed by matching checksums across both Zenodo records:
> MD5 `e5e8e09a33c948210972c76a8fb9fc52` (Zenodo v2.1) = MD5 `e5e8e09a33c948210972c76a8fb9fc52`
> (Zenodo v2.2).

> **Note on theorem numbering.** The theorem identifiers listed in this README
> (Theorem 6.5, Theorem 6.41, Theorem 7.3, Corollary 7.6, Theorem 7.9, Corollary 7.13,
> Theorem 8.2, Theorem 8.4, Proposition 9.5) are the corrected numbers matching the
> published article. These supersede the incorrect numbers (Theorem 6.3, Theorem 6.29,
> Theorem 7.1, Corollary 7.3, Theorem 7.5, Corollary 7.7, Theorem 8.3) that appeared
> in the "Main Results" sections of the v2.0 and v2.1 companion README files.

### Canonical record (Zenodo)

| File | Direct URL | MD5 |
|------|-----------|-----|
| `observer_entropy_bridge_theorem_v2.1.pdf` | [download](https://zenodo.org/records/19026744/files/observer_entropy_bridge_theorem_v2.1.pdf) | `e5e8e09a33c948210972c76a8fb9fc52` |
| `observer_entropy_bridge_theorem_v2.2.zip` | [download](https://zenodo.org/records/19026744/files/observer_entropy_bridge_theorem_v2.2.zip) | `81abc2623b488639cc804f122a39633c` |

DOI: [10.5281/zenodo.19026744](https://doi.org/10.5281/zenodo.19026744)

### Mirror (GitHub Releases v2.2)

| File | Permanent URL | SHA-256 |
|------|--------------|---------|
| `observer_entropy_bridge_theorem_v2.1.pdf` | [download](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.2/observer_entropy_bridge_theorem_v2.1.pdf) | `18e9991b1cbd90446af7e3c23f0ce3851f737c0afbd3d0ef99c38a73c6231024` |
| `observer_entropy_bridge_theorem_v2.2.zip` | [download](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.2/observer_entropy_bridge_theorem_v2.2.zip) | `40580e717db175b26d07cb17915e3097541f1b6cce549ea90042b29e4fe93812` |

GitHub Release: [v2.2](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/tag/v2.2)

---

## Version History  

- **Version 1.0** — core framework: see [`../v1.0_core/`](../v1.0_core/)  
- **Version 1.2** — Riemannian-Geometric Reformulation: see [`../v1.2_geometric/`](../v1.2_geometric/)  
- **Version 2.0** — Sufficient Conditions theorem and second worked example: see [`../v2.0_sufficient-conditions/`](../v2.0_sufficient-conditions/)  
- **Version 2.1** — citation of concurrent work (Izumo 2026): see [`../v2.1_izumo-citation/`](../v2.1_izumo-citation/)  
- **Version 2.2** — README correction (theorem numbers): this directory  
- **Version 2.4** — adds Related Work Section and verify_bridge_theorem_v2.py correction (theorem numbers in scripts/verify_bridge_theorem_v2.py): see [`../v2.4_related-work/`](../v2.4_related-work/)  

---

## Keywords  

KL divergence, Fisher information, Fisher–Rao metric, observer entropy, cognitive projection, coarse-graining generator, dissipation functional, information geometry, Landauer's principle, partition-adapted parameterization, sufficient conditions, between/within decomposition.  

**MSC 2020:** 62B10, 94A17, 53B12, 81P45.  

---

## Citation  

> Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework*, Version 2.2 (2026). DOI: [10.5281/zenodo.19026744](https://doi.org/10.5281/zenodo.19026744)  

---

## License  

MIT License. See [LICENSE](LICENSE).  
