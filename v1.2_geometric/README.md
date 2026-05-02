# KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework

**Version 1.2 — Riemannian-Geometric Reformulation**  

**Author:** Vladimir Khomyakov — Independent Researcher  
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)  

**DOI:** [10.5281/zenodo.18870450](https://doi.org/10.5281/zenodo.18870450)  
**Concept DOI (all versions):** [10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)  

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18826258.svg)](https://doi.org/10.5281/zenodo.18826258)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) — Scientific article and associated documentation  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) — Source code and simulation scripts  
---

## Overview  

This directory accompanies Version 1.2 of the article. Building on the core framework of Version 1.0, this version introduces the **Riemannian-Geometric Reformulation** of the Bridge Theorem and a new section on Discussion and Open Questions.  

---

## What's New in Version 1.2  

**Riemannian-Geometric Reformulation (Section 7)** — five provable extensions of the Bridge Theorem:  

1. **Coordinate-Invariant Reformulation (Theorem 7.1).** The quadratic form $v^\top I\,v$ equals the Fisher–Rao inner product $g_\theta(v,v)$. Observer entropy is one-half the squared Fisher–Rao norm of the coarse-graining generator.  

2. **Coarse-Graining Generator (Definition 7.2, Corollary 7.3).** Vector field characterization of the coarse-graining direction in parameter space.  

3. **Second-Variation Characterization (Theorem 7.5).** Observer entropy as the second variation of KL divergence along the coarse-graining orbit.  

4. **Dissipation Functional (Corollary 7.7).** Unified perspective connecting observer entropy, Fisher–Rao geometry, and information dissipation.  

5. **Fisher–Rao Distance Interpretation (Corollary 7.7).** Observer entropy expressed through the tangent-space Fisher–Rao distance.  

**Discussion and Open Questions (Section 11)** — clearly caveated mentions of unprovable directions: semigroup structure, Onsager principle, Wasserstein geometry, informational second law, α-connections.  

---

## Main Results (Cumulative)  

1. **Bridge Theorem.** Quadratic scaling law for observer entropy with explicit cubic remainder control.  

2. **Riemannian-Geometric Reformulation.** Observer entropy equals one-half the squared Fisher–Rao norm of the coarse-graining generator, and equivalently the second variation of KL divergence along the coarse-graining orbit.  

3. **Cognitive Uncertainty Principle.** Resolution–information trade-off relating the observer's finite resolution to minimal energetic cost of distinguishability.  

4. **Landauer Bound.** Thermodynamic lower bound: $E_{\min} \ge kT \cdot S_{\mathrm{obs}}(p, \varepsilon)$.  

5. **Piecewise Smoothness.** Observer entropy is piecewise-smooth in ε, with partition transitions at critical values.  

---

## Numerical Verification  

The quadratic scaling law is verified by a worked example:  

**Example 1** — Four-point space $\mathcal{X} = \{1,2,3,4\}$ with equal-size clusters $\mathcal{P} = \{\{1,2\},\{3,4\}\}$ (softmax family, 2 distinct Fisher eigenvalues). Fisher matrix: $I(\theta^*) = \mathrm{diag}(1, \tfrac{1}{2}, \tfrac{1}{2})$.  

All verification checks pass (quadratic scaling, bounded remainder, Fisher matrix agreement, non-negativity, monotonicity).  

---

## Directory Contents  

```
v1.2_geometric/  
├── README.md              ← this file  
├── LICENSE  
├── requirements.txt  
├── scripts/  
│   └── verify_bridge_theorem.py  
└── figures/  
    ├── fig1_bridge_theorem_verification.pdf  
    ├── fig2_relative_error.pdf  
    └── fig3_resolution_information_tradeoff.pdf  
```

---

## Figures  

- **Figure 1** — Bridge Theorem verification: exact vs. predicted observer entropy and normalized remainder.  
- **Figure 2** — Relative error of the quadratic approximation.  
- **Figure 3** — Resolution–information trade-off: monotone increase of $S_{\mathrm{obs}}(\varepsilon)$.  

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
python scripts/verify_bridge_theorem.py  
```

Output figures are written to the `figures/` directory in both PDF and PNG formats.  

---

## Article File Integrity

The article and reproducibility package for this version are archived at two independent
permanent locations. Checksums are provided for independent verification.

**Version 1.2 — Riemannian-Geometric Reformulation**

> **Note on theorem numbering.** The theorem identifiers listed in this README
> (Theorem 7.1, Corollary 7.3, Theorem 7.5, Corollary 7.7) reflect the numbering
> as it appeared in the published article at version 1.2. Subsequent versions (v2.0–v2.2)
> introduced additional environments in Section 6 (Sufficient Conditions), which caused
> renumbering of these results in Section 7 to Theorem 7.3, Corollary 7.6, Theorem 7.9,
> and Corollary 7.13 respectively. The numbers cited here are exact and correct
> for this version.

### Canonical record (Zenodo)

| File | Direct URL | MD5 |
|------|-----------|-----|
| `observer_entropy_bridge_theorem_v1.2.pdf` | [download](https://zenodo.org/records/18870450/files/observer_entropy_bridge_theorem_v1.2.pdf) | `0187620c505931540d563dc912fb430c` |
| `observer_entropy_bridge_theorem_v1.2.zip` | [download](https://zenodo.org/records/18870450/files/observer_entropy_bridge_theorem_v1.2.zip) | `2565cd1e6c86e5334b5f2cdfce6961fa` |

DOI: [10.5281/zenodo.18870450](https://doi.org/10.5281/zenodo.18870450)

### Mirror (GitHub Releases v1.2)

| File | Permanent URL | SHA-256 |
|------|--------------|---------|
| `observer_entropy_bridge_theorem_v1.2.pdf` | [download](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v1.2/observer_entropy_bridge_theorem_v1.2.pdf) | `ad158e6352c2459c058ea3a1de378b656e2aa6478e899c9ef24757a7924340c4` |
| `observer_entropy_bridge_theorem_v1.2.zip` | [download](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v1.2/observer_entropy_bridge_theorem_v1.2.zip) | `c92d54d05ef2d20b9f382c440d260c8eadf52743d6f5bf7a1fac42f95cfed41f` |

GitHub Release: [v1.2](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/tag/v1.2)

---

## Version History  

- **Version 1.0** — core framework: see [`../v1.0_core/`](../v1.0_core/)  
- **Version 1.2** — Riemannian-Geometric Reformulation: this directory  
- **Version 2.0** — adds Sufficient Conditions theorem and second worked example: see [`../v2.0_sufficient-conditions/`](../v2.0_sufficient-conditions/)  
- **Version 2.1** — adds citation of concurrent work (Izumo 2026): see [`../v2.1_izumo-citation/`](../v2.1_izumo-citation/)  
- **Version 2.2** — adds README correction (theorem numbers in README.md): see [`../v2.2_readme-correction/`](../v2.2_readme-correction/)  
- **Version 2.4** — adds Related Work Section and verify_bridge_theorem_v2.py correction (theorem numbers in scripts/verify_bridge_theorem_v2.py): see [`../v2.4_related-work/`](../v2.4_related-work/)  
- **Version 2.4.1** — adds self-naming removed (editorial correction): see [`../v2.4.1/`](../v2.4.1/)  
- **Version 2.4.8** — adds Strengthened Assumption 6.1 with (D1)–(D3); extended proof of Theorem 6.41 (Step 3); expanded proof of Lemma 6.42: see [`../v2.4.8/`](../v2.4.8/)  
- **Version 2.4.12** — adds Editorial clarifications; corrected statements; improved notation; no change to mathematical content: see [`../v2.4.12/`](../v2.4.12/)  

---

## Citation  

> Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework*, Version 1.2 (2026). DOI: [10.5281/zenodo.18870450](https://doi.org/10.5281/zenodo.18870450)  

---

## License  

MIT License. See [LICENSE](LICENSE).  
