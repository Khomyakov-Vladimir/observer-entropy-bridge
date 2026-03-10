# Observer Entropy Bridge — Companion Repository

**Author:** Vladimir Khomyakov — Independent Researcher
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)

**Concept DOI (all versions):** [10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18826258.svg)](https://doi.org/10.5281/zenodo.18826258)   
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) **— Scientific article and associated documentation**  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) **— Source code and simulation scripts**  
---

## About

This repository contains verification scripts, figures, and supporting materials for the research article series:

> *"KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework"*

Each published version of the article has its own self-contained directory with all files needed for full scientific reproducibility.

---

## Versions

| Version | Directory | Zenodo DOI | Key Additions |
|---------|-----------|------------|---------------|
| **v2.0** | [`v2.0_sufficient-conditions/`](v2.0_sufficient-conditions/) | [10.5281/zenodo.18932260](https://doi.org/10.5281/zenodo.18932260) | Sufficient Conditions theorem; second worked example (5-point space); 5 figures |
| **v1.2** | [`v1.2_geometric/`](v1.2_geometric/) | [10.5281/zenodo.18870450](https://doi.org/10.5281/zenodo.18870450) | Riemannian-Geometric Reformulation; Discussion and Open Questions |
| **v1.0** | [`v1.0_core/`](v1.0_core/) | [10.5281/zenodo.18826259](https://doi.org/10.5281/zenodo.18826259) | Core framework: Bridge Theorem, Cognitive Uncertainty Principle, Landauer bound |

**Related preprint (observer entropy concept):** [doi:10.5281/zenodo.17407408](https://doi.org/10.5281/zenodo.17407408)

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
└── v2.0_sufficient-conditions/
    ├── README.md
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

---

## Central Result — Khomyakov's Bridge Theorem

A finite observer resolution threshold ε induces a projection of probabilistic descriptions, resulting in measurable KL information loss — observer entropy — that scales quadratically with the threshold, controlled by the Fisher information geometry:

$$S_{\mathrm{obs}}(p_\theta, \varepsilon) = \tfrac{1}{2}\,\varepsilon^2\, v^\top I(\theta^*)\, v \;+\; O(\varepsilon^3), \qquad \varepsilon \to 0^+$$

where $I(\theta)$ is the Fisher information matrix and $v$ encodes the direction of information loss in parameter space.

---

## Quick Start

To run verification for the latest version (v2.0):

```bash
cd v2.0_sufficient-conditions
pip install -r requirements.txt
python scripts/verify_bridge_theorem_v2.py
```

---

## Citation

If you use this work, please cite:

> Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework*, Version 2.0 (2026). DOI: [10.5281/zenodo.18932260](https://doi.org/10.5281/zenodo.18932260)

---

## License

MIT License. See [LICENSE](LICENSE).
