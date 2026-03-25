# Observer Entropy Bridge — Companion Repository

**Author:** Vladimir Khomyakov — Independent Researcher  
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)  

**Latest release DOI:** [10.5281/zenodo.19202244](https://doi.org/10.5281/zenodo.19202244)  
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

Latest article version: **v2.4.1 — Self-naming removed (editorial correction)**  

Directory: [`v2.4.1_final/`](v2.4.1_final/)  
DOI: [https://doi.org/10.5281/zenodo.19202244](https://doi.org/10.5281/zenodo.19202244)  

Earlier versions are preserved for archival and reproducibility purposes.  

---

## Versions  

| Version | Directory | Zenodo DOI | Key Additions |  
|---------|-----------|------------|---------------|  
| **v2.4.1** | [`v2.4.1_final/`](v2.4.1_final/) | [10.5281/zenodo.19202244](https://doi.org/10.5281/zenodo.19202244) | Self-naming removed (editorial correction) |  
| **v2.4** | [`v2.4_related-work/`](v2.4_related-work/) | [10.5281/zenodo.19080663](https://doi.org/10.5281/zenodo.19080663) | Related Work Section Added; script correction (theorem numbers in console output of `verify_bridge_theorem_v2.py`) |  
| **v2.2** | [`v2.2_readme-correction/`](v2.2_readme-correction/) | [10.5281/zenodo.19026744](https://doi.org/10.5281/zenodo.19026744) | README correction (theorem numbers in companion README.md) |  
| **v2.1** | [`v2.1_izumo-citation/`](v2.1_izumo-citation/) | [10.5281/zenodo.19015730](https://doi.org/10.5281/zenodo.19015730) | Citation of concurrent work (Izumo 2026) |  
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
└── v2.4.1_final/  
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

## Central Result — Bridge Theorem  

A finite observer resolution threshold ε induces a projection of probabilistic descriptions, resulting in measurable KL information loss — observer entropy — that scales quadratically with the threshold, controlled by the Fisher information geometry:  

$$S_{\mathrm{obs}}(p_\theta, \varepsilon) = \tfrac{1}{2}\,\varepsilon^2\, v^\top I(\theta^*)\, v \;+\; O(\varepsilon^3), \qquad \varepsilon \to 0^+$$  

where $I(\theta)$ is the Fisher information matrix and $v$ encodes the direction of information loss in parameter space.  

---

## Quick Start  

To run verification for the latest version (v2.4.1):  

```bash
cd v2.4.1_final  
pip install -r requirements.txt  
python scripts/verify_bridge_theorem_v2.py  
```

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

¹ The article PDF in v2.2 is byte-for-byte identical to v2.1 (confirmed by matching MD5 and SHA-256).
The only change in v2.2 is a correction to the companion README.md.

Full checksums for all files are available in the per-version README files
within each versioned directory.

---

## Citation  

If you use this work, please cite:  

> Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework*, Version 2.4.1 (2026). DOI: [10.5281/zenodo.19202244](https://doi.org/10.5281/zenodo.19202244)  

---

## License  

MIT License. See [LICENSE](LICENSE).  
