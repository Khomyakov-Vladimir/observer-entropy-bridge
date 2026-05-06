# KL-Geometric Structure of Observer Entropy:
# A Minimal Information-Theoretic Framework

**Version 2.4.24**

**Author:** Vladimir Khomyakov — Independent Researcher
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)

**DOI (this version):** [10.5281/zenodo.19883297](
https://doi.org/10.5281/zenodo.19883297)

**Concept DOI (always resolves to latest version):**
[10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)

---

## Overview

This repository accompanies the research article *"KL-Geometric
Structure of Observer Entropy: A Minimal Information-Theoretic
Framework"* (version 2.4.24). The paper constructs a self-contained
geometric framework unifying the local information geometry of
Kullback–Leibler divergence with an observer-dependent theory of
coarse-grained entropy on finite measurable spaces.

The central result is the **Bridge Theorem**: a finite observer
resolution threshold ε induces a projection of probabilistic
descriptions, resulting in measurable KL information loss —
*observer entropy* — that scales quadratically with the threshold,
controlled by the Fisher information geometry:

$$
S_{\mathrm{obs}}(p_\theta,\varepsilon)
= \tfrac{1}{2}\,\varepsilon^2\,v^\top I(\theta^*)\,v
\;+\; O(\varepsilon^3),
\qquad \varepsilon \to 0^+,
$$

where $I(\theta)$ is the Fisher information matrix and $v$ encodes
the direction of information loss in parameter space.

---

## What Is New in Version 2.4.24

Version 2.4.24 resolves the two structural FAIL items identified in
the formal audit of version 2.4.12 (blocks A4 and C2). This is the
**first logically closed version** of the manuscript: all formal
audit blocks pass with no Critical Failures triggered.

The following changes are implemented:

- **Resolved FAIL A4 / FAIL C2 (structural):** Assumption `as:deformation`
  and Theorem `thm:bridge` (Bridge Theorem) are restated to make
  explicit that the asymptotic is taken along a one-parameter family
  $\theta(\varepsilon) = (\theta_\mathrm{b}^*, \varepsilon\alpha)$
  in which the base parameter co-varies with ε. The previous wording
  fixed θ and varied ε, which was internally inconsistent with the
  fixed-partition regime for nondegenerate $v(\theta) \ne 0$.
  The restatement aligns the formal hypothesis with its usage in
  `thm:sufficient_conditions`, `cor:bridge_adapted`, and both
  worked examples.
- **Added `def:balanced`** — formal definition of a
  $\mathcal{P}$-balanced exponential family (conditions L1–L2),
  previously stated only inline within `lem:vanishing`.
- **Added `rem:balanced_verification`** — explicit cross-reference
  confirming that both worked examples satisfy the balanced condition,
  and that `cor:softmax` covers the centered parameterization
  automatically.
- **Expanded `rem:fixed_partition`** — clarifies the dual role of ε
  (metric threshold vs. parametric perturbation amplitude) with an
  explicit note on the scoping convention used in
  Section `sec:riemannian` versus the worked examples.
- **Refined `rem:D3_redundancy`** — proof of redundancy of condition
  (D3) relative to (D2) is now derived via the second-order Taylor
  expansion with integral remainder, removing the previous appeal to
  the mean value theorem (which gave only $\partial_\varepsilon\rho(\theta,0)=0$
  but not the linear bound on $\partial_\varepsilon\rho$).

All modifications in version 2.4.24 address formal logical closure.
No new mathematical results are introduced beyond those already
present in version 2.4.12.

---

## Formal Audit Status

| Version | Audit result | Blocking items |
|---------|-------------|----------------|
| 2.4.12  | NOT PUBLISHABLE | FAIL A4 (hidden assumption / scoping inconsistency in `as:deformation`); FAIL C2 (theorem statement omits required condition in `thm:bridge`) |
| **2.4.24** | **PUBLISHABLE** | **None — all blocks PASS, no CF triggered** |

The audit was conducted under UFAS v1.0 (Unified Formal Audit
Standard), covering blocks S (structural integrity), D (dependency
correctness), R (regularity), A (assumption integrity), E (asymptotic
consistency), L (labeling), and C (conclusion vs. premise).

---

## Main Results

1. **Bridge Theorem (Theorem 6.7).** Quadratic scaling law for
   observer entropy with explicit cubic remainder control,
   $|S_\mathrm{obs} - \tfrac{1}{2}\varepsilon^2 v^\top Iv|
   \le C_1 \varepsilon^3$.

2. **Sufficient Conditions Theorem (Theorem 6.43).** The
   Parametric Deformation Assumption (including conditions
   (D1)–(D3)) is proved to be a consequence of three checkable
   finite-dimensional conditions — within-class neutrality (A1),
   lift closure (A2), immersion condition (A3) — that hold
   automatically for full exponential families with centered
   between/within parameterization. Uniform constants are
   identified explicitly.

3. **Riemannian-Geometric Reformulation (Section 7).**
   The quadratic form $v^\top I\,v$ equals the Fisher–Rao inner
   product $g_\theta(v,v)$. Observer entropy is one-half the
   squared Fisher–Rao norm of the coarse-graining generator
   (Theorem 7.4, Corollary 7.7), and equivalently the second
   variation of the KL divergence along the coarse-graining orbit
   (Theorem 7.10). A dissipation functional unifies these
   perspectives (Corollary 7.14).

4. **Cognitive Uncertainty Principle (Theorem 8.3).**
   Resolution–information trade-off: the observer's finite
   resolution threshold ε must satisfy
   $\varepsilon \ge \sqrt{2\delta_0/Q}\,(1 - C'\varepsilon)$
   for the information loss to exceed the detection threshold
   $\delta_0$.

5. **Landauer Bound (Theorem 8.5).** Thermodynamic lower bound:
   $E_\mathrm{min} \ge kT \cdot S_\mathrm{obs}(p,\varepsilon)$.

6. **Piecewise Smoothness (Proposition 9.5).** Observer entropy
   is piecewise-smooth in ε, with partition transitions at
   critical values given by interpoint distances of the metric
   space.

All results are proved from explicitly stated assumptions with
complete remainder estimates and hold uniformly over compact
parameter subsets.

---

## Numerical Verification

The quadratic scaling law is verified by two independent worked
examples (unchanged from v2.0):

**Example 1** — Four-point space $\mathcal{X} = \{1,2,3,4\}$,
equal-size clusters $\mathcal{P} = \{\{1,2\},\{3,4\}\}$,
softmax family, 2 distinct Fisher eigenvalues.
Fisher matrix: $I(\theta^*) = \mathrm{diag}(1,\tfrac{1}{2},
\tfrac{1}{2})$.

**Example 2** — Five-point space $\mathcal{X} = \{1,2,3,4,5\}$,
unequal clusters $\mathcal{P} = \{\{1,2,3\},\{4,5\}\}$,
3 distinct Fisher eigenvalues.
Fisher matrix: $I(\theta^*) = \mathrm{diag}(\tfrac{3}{2},
\tfrac{6}{5},\tfrac{2}{5},\tfrac{2}{5})$.

The verification script confirms:

- Quadratic scaling $S_\mathrm{obs} \sim \varepsilon^2$
  (log-log slope = 2.000 ± 0.01 in all cases)
- Bounded $O(\varepsilon^3)$ remainder
- Fisher matrix agreement between analytic and finite-difference
  computations
- Closed-form leading coefficients match Fisher-based predictions
- Non-negativity of observer entropy (Landauer bound satisfied)
- Monotone non-decrease $S_\mathrm{obs}(\varepsilon)$
  (resolution–information trade-off)

All checks pass: **PASS — ALL BRIDGE THEOREM CHECKS PASSED**.

---

## Version History

| Version | DOI | Key change |
|---------|-----|------------|
| 1.0 | [10.5281/zenodo.18826259](https://doi.org/10.5281/zenodo.18826259) | Initial release |
| 1.2 | [10.5281/zenodo.18870450](https://doi.org/10.5281/zenodo.18870450) | Minor corrections |
| 2.0 | [10.5281/zenodo.18932260](https://doi.org/10.5281/zenodo.18932260) | Sufficient conditions theorem; Riemannian-geometric reformulation; two worked examples |
| 2.1 | [10.5281/zenodo.19015730](https://doi.org/10.5281/zenodo.19015730) | Citation of Izumo (2026) added |
| 2.2 | [10.5281/zenodo.19026744](https://doi.org/10.5281/zenodo.19026744) | README theorem-number correction |
| 2.4 | [10.5281/zenodo.19080663](https://doi.org/10.5281/zenodo.19080663) | Related Work section added |
| 2.4.1 | [10.5281/zenodo.19202244](https://doi.org/10.5281/zenodo.19202244) | Editorial: uniform terminology (Bridge Theorem) |
| 2.4.8 | [10.5281/zenodo.19645407](https://doi.org/10.5281/zenodo.19645407) | Strengthened Assumption 6.1 with (D1)–(D3); extended proof of Theorem 6.41 (Step 3); expanded proof of Lemma 6.42 |
| 2.4.12 | [10.5281/zenodo.19729887](https://doi.org/10.5281/zenodo.19729887) | Editorial clarifications; corrected statements; improved notation; no change to mathematical content |
| **2.4.24** | **[10.5281/zenodo.19883297](https://doi.org/10.5281/zenodo.19883297)** | **Resolved FAIL A4 and FAIL C2 from formal audit; first logically closed version (all audit blocks PASS)** |

---

## Repository Structure

```
observer_entropy_bridge_theorem_v2.4.24/
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

Figures and the verification script are identical to v2.0.

---

## Figures

- **Figure 1** — Bridge Theorem verification (Example 1):
  exact vs. predicted observer entropy and normalized remainder.
- **Figure 2** — Relative error of the quadratic approximation
  (Example 1).
- **Figure 3** — Resolution–information trade-off: monotone
  increase of $S_\mathrm{obs}(\varepsilon)$.
- **Figure 4** — Bridge Theorem verification (Example 2):
  exact vs. predicted observer entropy for unequal clusters.
- **Figure 5** — Relative error of the quadratic approximation
  (Example 2).

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

From the repository root:

```bash
python scripts/verify_bridge_theorem_v2.py
```

---

## Keywords

KL divergence, Fisher information, Fisher–Rao metric, observer
entropy, cognitive projection, coarse-graining generator,
dissipation functional, information geometry, Landauer's principle,
partition-adapted parameterization, sufficient conditions,
between/within decomposition.

**MSC 2020:** 62B10, 94A17, 53B12, 81P45.

---

## Citation

If you use this work, please cite:

> Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy:
> A Minimal Information-Theoretic Framework*, Version 2.4.24 (2026).
> DOI: [10.5281/zenodo.19883297](
> https://doi.org/10.5281/zenodo.19883297)
>
> Concept DOI (always resolves to latest version):
> [10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)

---

## Code Availability

The verification script and all figures are available at:
[https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/](
https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/)

---

## License

See `LICENSE` file.
