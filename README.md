# Observer Entropy Bridge — Companion Repository  

**Author:** Vladimir Khomyakov — Independent Researcher  
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)  

**Latest release DOI:** [10.5281/zenodo.20004735](https://doi.org/10.5281/zenodo.20004735)  
**Concept DOI (all versions):** [10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18826258.svg)](https://doi.org/10.5281/zenodo.18826258)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) — Scientific article and associated documentation  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) — Source code and simulation scripts  

---

## About  

This repository contains verification scripts, figures, and supporting materials for the research article series:  

> *"KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework"*  

Each published version of the article has its own self-contained directory with all files needed for full scientific reproducibility.  

### Current Version  

Latest article version: **v3.0 — New Section 9 (off-center robustness checks at twelve random base points); two new figures (Figs. 6–7); empirical C\* table; quantitative validation criterion; extended verification script v3**  

Directory: [`v3.0/`](v3.0/)  
DOI: [https://doi.org/10.5281/zenodo.20004735](https://doi.org/10.5281/zenodo.20004735)  

Earlier versions are preserved for archival and reproducibility purposes.  

---

## Central Result — Bridge Theorem  

A finite observer resolution threshold ε induces a projection of probabilistic descriptions, resulting in measurable KL information loss — **observer entropy** — that scales quadratically with the threshold, controlled by the Fisher information geometry:  

$$S_{\mathrm{obs}}(p_\theta, \varepsilon) = \tfrac{1}{2}\,\varepsilon^2\, v^\top I(\theta^*)\, v \;+\; O(\varepsilon^3), \qquad \varepsilon \to 0^+$$  

where $I(\theta)$ is the Fisher information matrix and $v$ encodes the direction of information loss in parameter space.  

The quadratic scaling law is verified by two independent worked examples:

- **Example 1** — Four-point space $\mathcal{X} = \{1,2,3,4\}$, equal-size clusters $\mathcal{P} = \{\{1,2\},\{3,4\}\}$, 2 distinct Fisher eigenvalues. Fisher matrix: $I(\theta^*) = \mathrm{diag}(1,\tfrac{1}{2},\tfrac{1}{2})$.  
- **Example 2** — Five-point space $\mathcal{X} = \{1,2,3,4,5\}$, unequal clusters $\mathcal{P} = \{\{1,2,3\},\{4,5\}\}$, 3 distinct Fisher eigenvalues. Fisher matrix: $I(\theta^*) = \mathrm{diag}(\tfrac{3}{2},\tfrac{6}{5},\tfrac{2}{5},\tfrac{2}{5})$.  

The scaling law is confirmed numerically not only at the symmetric base point $\theta^*=0$ of each example, but also at **twelve randomly sampled off-center base points** $\theta^*\neq 0$ with random perturbation directions (v3.0, Section 9).

---

## Main Results (Cumulative, v3.0)  

1. **Bridge Theorem (Theorem 6.7).** Quadratic scaling law for observer entropy with explicit cubic remainder control, $|S_\mathrm{obs} - \tfrac{1}{2}\varepsilon^2 v^\top Iv| \le C_1 \varepsilon^3$.  

2. **Sufficient Conditions (Theorem 6.43).** The Parametric Deformation Assumption (including conditions (D1)–(D3)) is proved to be a consequence of three checkable finite-dimensional conditions — within-class neutrality (A1), lift closure (A2), immersion condition (A3) — that hold automatically for full exponential families with centered between/within parameterization. Uniform constants are identified explicitly.  

3. **Riemannian-Geometric Reformulation (Section 7).** The quadratic form $v^\top I\,v$ equals the Fisher–Rao inner product $g_\theta(v,v)$. Observer entropy is one-half the squared Fisher–Rao norm of the coarse-graining generator (Theorem 7.4, Corollary 7.7), and equivalently the second variation of the KL divergence along the coarse-graining orbit (Theorem 7.10). A dissipation functional unifies these perspectives (Corollary 7.14).  

4. **Cognitive Uncertainty Principle (Theorem 8.3).** Resolution–information trade-off: the observer's finite resolution threshold ε must satisfy $\varepsilon \ge \sqrt{2\delta_0/Q}\,(1 - C'\varepsilon)$ for the information loss to exceed the detection threshold $\delta_0$.  

5. **Landauer Bound (Theorem 8.5).** Thermodynamic lower bound: $E_\mathrm{min} \ge kT \cdot S_\mathrm{obs}(p,\varepsilon)$. At $T=300$ K and $\varepsilon=10^{-2}$ the verification script yields $E_\mathrm{min}\sim 10^{-25}$–$10^{-24}$ J depending on the perturbation direction, many orders of magnitude below the thermal noise floor $kT\sim 4\cdot 10^{-21}$ J in the small-ε regime.  

6. **Piecewise Smoothness (Proposition 10.5).** Observer entropy is piecewise-smooth in ε, with partition transitions at critical values given by interpoint distances of the metric space.  

7. **Off-Center Robustness (Section 9, v3.0).** The locality of the Bridge Theorem is numerically confirmed at twelve randomly sampled off-center base points $\theta^*\neq 0$. Measured log-log slopes lie within $|\mathrm{slope}-2|<5\cdot 10^{-3}$, and normalised remainders $|R|/\varepsilon^3$ remain bounded by 0.2 uniformly on $\varepsilon\in[10^{-4},10^{-2}]$.  

All results are proved from explicitly stated assumptions with complete remainder estimates and hold uniformly over compact parameter subsets.  

---

## Versions  

| Version | Directory | Zenodo DOI | Key Additions |  
|---------|-----------|------------|---------------|  
| **v3.0**    | [`v3.0/`](v3.0/)         | [10.5281/zenodo.20004735](https://doi.org/10.5281/zenodo.20004735) | New Section 9 (off-center robustness checks at twelve random base points); two new figures (Figs. 6–7); empirical C\* table; quantitative validation criterion; extended verification script v3 |  
| **v2.4.24** | [`v2.4.24/`](v2.4.24/) | [10.5281/zenodo.19883297](https://doi.org/10.5281/zenodo.19883297) | Resolved scoping inconsistency in `as:deformation` and `thm:bridge`; logically closed version |  
| **v2.4.12** | [`v2.4.12/`](v2.4.12/) | [10.5281/zenodo.19729887](https://doi.org/10.5281/zenodo.19729887) | Editorial clarifications; corrected statements; improved notation; no change to mathematical content |  
| **v2.4.8** | [`v2.4.8/`](v2.4.8/) | [10.5281/zenodo.19645407](https://doi.org/10.5281/zenodo.19645407) | Strengthened Assumption 6.1 with (D1)–(D3); extended proof of Theorem 6.41 (Step 3); expanded proof of Lemma 6.42 |  
| **v2.4.1** | [`v2.4.1/`](v2.4.1/) | [10.5281/zenodo.19202244](https://doi.org/10.5281/zenodo.19202244) | Self-naming removed (editorial correction) |  
| **v2.4** | [`v2.4_related-work/`](v2.4_related-work/) | [10.5281/zenodo.19080663](https://doi.org/10.5281/zenodo.19080663) | Related Work Section added; script correction (theorem numbers in console output of `verify_bridge_theorem_v2.py`) |  
| **v2.2** | [`v2.2_readme-correction/`](v2.2_readme-correction/) | [10.5281/zenodo.19026744](https://doi.org/10.5281/zenodo.19026744) | README correction (theorem numbers in companion README.md) |  
| **v2.1** | [`v2.1_izumo-citation/`](v2.1_izumo-citation/) | [10.5281/zenodo.19015730](https://doi.org/10.5281/zenodo.19015730) | Citation of concurrent work (Izumo 2026) |  
| **v2.0** | [`v2.0_sufficient-conditions/`](v2.0_sufficient-conditions/) | [10.5281/zenodo.18932260](https://doi.org/10.5281/zenodo.18932260) | Sufficient Conditions theorem; second worked example (5-point space); 5 figures |  
| **v1.2** | [`v1.2_geometric/`](v1.2_geometric/) | [10.5281/zenodo.18870450](https://doi.org/10.5281/zenodo.18870450) | Riemannian-Geometric Reformulation; Discussion and Open Questions |  
| **v1.0** | [`v1.0_core/`](v1.0_core/) | [10.5281/zenodo.18826259](https://doi.org/10.5281/zenodo.18826259) | Core framework: Bridge Theorem, Cognitive Uncertainty Principle, Landauer bound |  

> **Note on theorem numbering in the Key Additions column.** Theorem, lemma, and proposition numbers cited in each row reflect the numbering of the article version described by that row, not the numbering of the current version. Numbering shifted across versions as new theorem environments were introduced. The authoritative numbers for each version are given in the per-version README files and in the corresponding Zenodo records.

**Related preprint (observer entropy concept):** [doi:10.5281/zenodo.17407408](https://doi.org/10.5281/zenodo.17407408)  

---

## Quick Start  

To run verification for the latest version (v3.0):  

```bash
cd v3.0  
pip install -r requirements.txt  
python scripts/verify_bridge_theorem_v3.py  
```

All checks pass: **PASS — ALL BRIDGE THEOREM CHECKS PASSED** (including twelve off-center robustness checks at randomly sampled base points $\theta^*\neq 0$).  

---

## Citation  

If you use this work, please cite the latest version:  

Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework*, Version 3.0 (2026). DOI: [10.5281/zenodo.20004735](https://doi.org/10.5281/zenodo.20004735)  

Concept DOI (always resolves to latest version): [10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)  

---

## Code Availability  

The verification script and all figures are available at:  
[https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/)  

---

## Article File Integrity

All versions of the article are archived at two independent permanent locations.
The table below provides direct download links and checksums for independent verification.

| Version | File | Zenodo direct URL | MD5 | GitHub Release URL | SHA-256 |
|---------|------|-------------------|-----|--------------------|---------| 
| **v1.0** | article PDF | [observer_entropy_bridge_theorem.pdf](https://zenodo.org/records/18826259/files/observer_entropy_bridge_theorem.pdf) | `5a35a...4b0` | [v1.0 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v1.0/observer_entropy_bridge_theorem.pdf) | `7cf0f135...9b1` |
| **v1.0** | scripts ZIP | [observer_entropy_bridge_theorem.zip](https://zenodo.org/records/18826259/files/observer_entropy_bridge_theorem.zip) | `c248d...4f8` | [v1.0 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v1.0/observer_entropy_bridge_theorem.zip) | `5fb4a3b3...0d1` |
| **v1.2** | article PDF | [observer_entropy_bridge_theorem_v1.2.pdf](https://zenodo.org/records/18870450/files/observer_entropy_bridge_theorem_v1.2.pdf) | `01876...30c` | [v1.2 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v1.2/observer_entropy_bridge_theorem_v1.2.pdf) | `ad158e63...0c4` |
| **v1.2** | scripts ZIP | [observer_entropy_bridge_theorem_v1.2.zip](https://zenodo.org/records/18870450/files/observer_entropy_bridge_theorem_v1.2.zip) | `2565c...1fa` | [v1.2 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v1.2/observer_entropy_bridge_theorem_v1.2.zip) | `c92d54d0...41f` |
| **v2.0** | article PDF | [observer_entropy_bridge_theorem_v2.0.pdf](https://zenodo.org/records/18932260/files/observer_entropy_bridge_theorem_v2.0.pdf) | `e1d64...4ac` | [v2.0 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.0/observer_entropy_bridge_theorem_v2.0.pdf) | `7c0ea73f...040` |
| **v2.0** | scripts ZIP | [observer_entropy_bridge_theorem_v2.0.zip](https://zenodo.org/records/18932260/files/observer_entropy_bridge_theorem_v2.0.zip) | `87f86...bf7` | [v2.0 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.0/observer_entropy_bridge_theorem_v2.0.zip) | `ba3494e2...500` |
| **v2.1** | article PDF | [observer_entropy_bridge_theorem_v2.1.pdf](https://zenodo.org/records/19015730/files/observer_entropy_bridge_theorem_v2.1.pdf) | `e5e8e...c52` | [v2.1 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.1/observer_entropy_bridge_theorem_v2.1.pdf) | `18e9991b...024` |
| **v2.1** | scripts ZIP | [observer_entropy_bridge_theorem_v2.1.zip](https://zenodo.org/records/19015730/files/observer_entropy_bridge_theorem_v2.1.zip) | `8e9b6...366` | [v2.1 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.1/observer_entropy_bridge_theorem_v2.1.zip) | `39ce2c0c...221` |
| **v2.2** | article PDF ¹ | [observer_entropy_bridge_theorem_v2.1.pdf](https://zenodo.org/records/19026744/files/observer_entropy_bridge_theorem_v2.1.pdf) | `e5e8e...c52` | [v2.2 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.2/observer_entropy_bridge_theorem_v2.1.pdf) | `18e9991b...024` |
| **v2.2** | scripts ZIP | [observer_entropy_bridge_theorem_v2.2.zip](https://zenodo.org/records/19026744/files/observer_entropy_bridge_theorem_v2.2.zip) | `81abc...33c` | [v2.2 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.2/observer_entropy_bridge_theorem_v2.2.zip) | `40580e71...812` |
| **v2.4** | article PDF | [observer_entropy_bridge_theorem_v2.4.pdf](https://zenodo.org/records/19080663/files/observer_entropy_bridge_theorem_v2.4.pdf) | `9fc40...e82` | [v2.4 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4/observer_entropy_bridge_theorem_v2.4.pdf) | `fad1c8f4...9ba` |
| **v2.4** | scripts ZIP | [observer_entropy_bridge_theorem_v2.4.zip](https://zenodo.org/records/19080663/files/observer_entropy_bridge_theorem_v2.4.zip) | `7cddd...377` | [v2.4 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4/observer_entropy_bridge_theorem_v2.4.zip) | `1fab9c29...f5c` |
| **v2.4.1** | article PDF | [observer_entropy_bridge_theorem_v2.4.1.pdf](https://zenodo.org/records/19202244/files/observer_entropy_bridge_theorem_v2.4.1.pdf) | `ec3f6...00d` | [v2.4.1 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.1/observer_entropy_bridge_theorem_v2.4.1.pdf) | `f689fa87...cd6` |
| **v2.4.1** | scripts ZIP | [observer_entropy_bridge_theorem_v2.4.1.zip](https://zenodo.org/records/19202244/files/observer_entropy_bridge_theorem_v2.4.1.zip) | `a52d3...41e` | [v2.4.1 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.1/observer_entropy_bridge_theorem_v2.4.1.zip) | `8fa892e0...bf6` |
| **v2.4.8** | article PDF | [observer_entropy_bridge_theorem_v2.4.8.pdf](https://zenodo.org/records/19645407/files/observer_entropy_bridge_theorem_v2.4.8.pdf) | `bec0b...829` | [v2.4.8 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.8/observer_entropy_bridge_theorem_v2.4.8.pdf) | `5d8f8628...996` |
| **v2.4.8** | scripts ZIP | [observer_entropy_bridge_theorem_v2.4.8.zip](https://zenodo.org/records/19645407/files/observer_entropy_bridge_theorem_v2.4.8.zip) | `b53e2...bd6` | [v2.4.8 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.8/observer_entropy_bridge_theorem_v2.4.8.zip) | `b55437f4...a65` |
| **v2.4.12** | article PDF | [observer_entropy_bridge_theorem_v2.4.12.pdf](https://zenodo.org/records/19729887/files/observer_entropy_bridge_theorem_v2.4.12.pdf) | `31e36...937` | [v2.4.12 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.12/observer_entropy_bridge_theorem_v2.4.12.pdf) | `129cefb6...769` |
| **v2.4.12** | scripts ZIP | [observer_entropy_bridge_theorem_v2.4.12.zip](https://zenodo.org/records/19729887/files/observer_entropy_bridge_theorem_v2.4.12.zip) | `6db46...7a3` | [v2.4.12 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.12/observer_entropy_bridge_theorem_v2.4.12.zip) | `295c046b...a08` |
| **v2.4.24** | article PDF | [observer_entropy_bridge_theorem_v2.4.24.pdf](https://zenodo.org/records/19883297/files/observer_entropy_bridge_theorem_v2.4.24.pdf) | `f80a5...981` | [v2.4.24 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.24/observer_entropy_bridge_theorem_v2.4.24.pdf) | `80e52d30...1c2` |
| **v2.4.24** | scripts ZIP | [observer_entropy_bridge_theorem_v2.4.24.zip](https://zenodo.org/records/19883297/files/observer_entropy_bridge_theorem_v2.4.24.zip) | `e4903...b85` | [v2.4.24 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.24/observer_entropy_bridge_theorem_v2.4.24.zip) | `964aec3c...457` |
| **v3.0** | article PDF | [observer_entropy_bridge_theorem_v3.0.pdf](https://zenodo.org/records/20004735/files/observer_entropy_bridge_theorem_v3.0.pdf) | `b9a7d...d41` | [v3.0 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v3.0/observer_entropy_bridge_theorem_v3.0.pdf) | `077a11f4...5e7` |
| **v3.0** | scripts ZIP | [observer_entropy_bridge_theorem_v3.0.zip](https://zenodo.org/records/20004735/files/observer_entropy_bridge_theorem_v3.0.zip) | `fca37...d30` | [v3.0 release](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v3.0/observer_entropy_bridge_theorem_v3.0.zip) | `36c633ae...45e` |

¹ The article PDF in v2.2 is byte-for-byte identical to v2.1 (confirmed by matching MD5 and SHA-256).
The only change in v2.2 is a correction to the companion README.md.

Full checksums for all files are available in the per-version README files
within each versioned directory.

---

## Repository Structure  

```
observer-entropy-bridge/  
│
├── README.md                          ← this file  
├── LICENSE  
├── requirements.txt  
│
├── v1.0_core/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       └── fig3_resolution_information_tradeoff.pdf  
│
├── v1.2_geometric/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       └── fig3_resolution_information_tradeoff.pdf  
│
├── v2.0_sufficient-conditions/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem_v2.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       ├── fig3_resolution_information_tradeoff.pdf  
│       ├── fig4_bridge_theorem_ex2.pdf  
│       └── fig5_relative_error_ex2.pdf  
│
├── v2.1_izumo-citation/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem_v2.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       ├── fig3_resolution_information_tradeoff.pdf  
│       ├── fig4_bridge_theorem_ex2.pdf  
│       └── fig5_relative_error_ex2.pdf  
│
├── v2.2_readme-correction/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem_v2.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       ├── fig3_resolution_information_tradeoff.pdf  
│       ├── fig4_bridge_theorem_ex2.pdf  
│       └── fig5_relative_error_ex2.pdf  
│
├── v2.4_related-work/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem_v2.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       ├── fig3_resolution_information_tradeoff.pdf  
│       ├── fig4_bridge_theorem_ex2.pdf  
│       └── fig5_relative_error_ex2.pdf  
│
├── v2.4.1/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem_v2.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       ├── fig3_resolution_information_tradeoff.pdf  
│       ├── fig4_bridge_theorem_ex2.pdf  
│       └── fig5_relative_error_ex2.pdf  
│
├── v2.4.8/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem_v2.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       ├── fig3_resolution_information_tradeoff.pdf  
│       ├── fig4_bridge_theorem_ex2.pdf  
│       └── fig5_relative_error_ex2.pdf  
│
├── v2.4.12/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem_v2.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       ├── fig3_resolution_information_tradeoff.pdf  
│       ├── fig4_bridge_theorem_ex2.pdf  
│       └── fig5_relative_error_ex2.pdf  
│
├── v2.4.24/  
│   ├── README.md  
│   ├── LICENSE  
│   ├── requirements.txt  
│   ├── scripts/  
│   │   └── verify_bridge_theorem_v2.py  
│   └── figures/  
│       ├── fig1_bridge_theorem_verification.pdf  
│       ├── fig2_relative_error.pdf  
│       ├── fig3_resolution_information_tradeoff.pdf  
│       ├── fig4_bridge_theorem_ex2.pdf  
│       └── fig5_relative_error_ex2.pdf  
│
└── v3.0/  
    ├── README.md  
    ├── LICENSE  
    ├── requirements.txt  
    ├── scripts/  
    │   └── verify_bridge_theorem_v3.py  
    └── figures/  
        ├── fig1_bridge_theorem_verification.pdf  
        ├── fig2_relative_error.pdf  
        ├── fig3_resolution_information_tradeoff.pdf  
        ├── fig4_bridge_theorem_ex2.pdf  
        ├── fig5_relative_error_ex2.pdf  
        ├── fig6_offcenter_ex1.pdf  
        └── fig7_offcenter_ex2.pdf  
```

---

## License  

MIT License. See [LICENSE](LICENSE).  
