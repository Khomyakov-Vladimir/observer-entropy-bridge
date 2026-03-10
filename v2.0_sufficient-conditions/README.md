# KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework

**Version 2.0 — Sufficient Conditions and Extended Verification**

**Author:** Vladimir Khomyakov — Independent Researcher
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)

**DOI:** [10.5281/zenodo.18932260](https://doi.org/10.5281/zenodo.18932260)

---

## Overview

This directory accompanies Version 2.0 of the article *"KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework"*. The paper constructs a self-contained geometric framework unifying the local information geometry of Kullback–Leibler divergence with an observer-dependent theory of coarse-grained entropy on finite measurable spaces.

The central result is the **Bridge Theorem (Khomyakov's Bridge)**: a finite observer resolution threshold ε induces a projection of probabilistic descriptions, resulting in measurable KL information loss — observer entropy — that scales quadratically with the threshold, controlled by the Fisher information geometry:

$$S_{\mathrm{obs}}(p_\theta, \varepsilon) = \tfrac{1}{2}\,\varepsilon^2\, v^\top I(\theta^*)\, v \;+\; O(\varepsilon^3), \qquad \varepsilon \to 0^+$$

where $I(\theta)$ is the Fisher information matrix and $v$ encodes the direction of information loss in parameter space.

---

## What's New in Version 2.0

1. **Sufficient Conditions (Theorem 6.29).** The parametric deformation assumption is proved to be a consequence of three checkable finite-dimensional conditions (within-class neutrality, lift closure, immersion condition) that hold automatically for full exponential families with centered between/within parameterization. This reduces verifiability from an infinite-dimensional functional condition to finite-dimensional linear algebra.

2. **Second Worked Example (Section 6.2).** Five-point space $\mathcal{X} = \{1,2,3,4,5\}$ with unequal clusters $\mathcal{P} = \{\{1,2,3\},\{4,5\}\}$ (3 distinct Fisher eigenvalues), providing structurally independent verification of the Bridge Theorem.

3. **Extended Numerical Verification.** Five publication-quality figures covering both examples. All eight verification components pass for both configurations.

---

## Main Results (Cumulative)

1. **Bridge Theorem (Theorem 6.3, Khomyakov's Bridge).** Quadratic scaling law for observer entropy with explicit cubic remainder control.

2. **Sufficient Conditions (Theorem 6.29).** The parametric deformation assumption is proved to be a consequence of three checkable finite-dimensional conditions that hold automatically for full exponential families with centered between/within parameterization.

3. **Riemannian-Geometric Reformulation (Section 7).** The quadratic form $v^\top I\,v$ equals the Fisher–Rao inner product $g_\theta(v,v)$. Observer entropy is one-half the squared Fisher–Rao norm of the coarse-graining generator (Theorem 7.1, Corollary 7.3), and equivalently the second variation of the KL divergence along the coarse-graining orbit (Theorem 7.5). A dissipation functional unifies these perspectives (Corollary 7.7).

4. **Cognitive Uncertainty Principle (Theorem 8.2).** Resolution–information trade-off relating the observer's finite resolution to minimal energetic cost of distinguishability.

5. **Landauer Bound (Theorem 8.3).** Thermodynamic lower bound on the energetic cost of finite-resolution observation: $E_{\min} \ge kT \cdot S_{\mathrm{obs}}(p, \varepsilon)$.

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
v2.0_sufficient-conditions/
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

## Version History

- **Version 1.0** — core framework: see [`../v1.0_core/`](../v1.0_core/)
- **Version 1.2** — Riemannian-Geometric Reformulation: see [`../v1.2_geometric/`](../v1.2_geometric/)

---

## Keywords

KL divergence, Fisher information, Fisher–Rao metric, observer entropy, cognitive projection, coarse-graining generator, dissipation functional, information geometry, Landauer's principle, partition-adapted parameterization, sufficient conditions, between/within decomposition.

**MSC 2020:** 62B10, 94A17, 53B12, 81P45.

---

## Citation

> Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework*, Version 2.0 (2026). DOI: [10.5281/zenodo.18932260](https://doi.org/10.5281/zenodo.18932260)

---

## License

MIT License. See [LICENSE](LICENSE).
