# KL-Geometric Structure of Observer Entropy:
# A Minimal Information-Theoretic Framework

**Version 3.0**

**Author:** Vladimir Khomyakov — Independent Researcher
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)

**DOI (this version):** [10.5281/zenodo.20004735](
https://doi.org/10.5281/zenodo.20004735)

**Concept DOI (always resolves to latest version):**
[10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)

---

## Overview

This repository accompanies the research article *"KL-Geometric
Structure of Observer Entropy: A Minimal Information-Theoretic
Framework"* (version 3.0). The paper constructs a self-contained
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

## What Is New in Version 3.0

Version 3.0 is a **substantive release** that extends the logically
closed framework of v2.4.24 with new numerical content, a new
section, two new figures, and a quantitative empirical analysis of
the validation criterion. The mathematical core (Bridge Theorem,
Sufficient Conditions Theorem, Riemannian-geometric reformulation,
Cognitive Uncertainty Principle, Landauer bound) is preserved from
v2.4.24 without modification.

The following additions and extensions are implemented:

- **New Section 9 — Off-Center Robustness Checks
  (`sec:offcenter`).** Numerical verification that the Bridge
  Theorem holds not only at the symmetric base point $\theta^*=0$
  of each worked example, but also at **twelve randomly sampled
  off-center base points** $\theta^*\ne 0$ (six for Example 1, six
  for Example 2) with random within-class perturbation directions
  $\alpha$, drawn with fixed seed `OFFCENTER_SEED = 42` for full
  reproducibility. All twelve checks satisfy both the quadratic-scaling
  diagnostic ($|\mathrm{slope}-2|<10^{-2}$) and the
  $O(\varepsilon^3)$ remainder bound.
- **Two new figures (Figures 6 and 7)** showing $S_\mathrm{obs}$
  versus $\varepsilon$ and the normalised remainder for all
  twelve random off-center base points, one figure per worked
  example.
- **New Table 1 (`tab:C_star_distribution`)** summarising the
  empirical distribution of the relative-error constant
  $C_* := \sup_{\varepsilon\le 0.03}
  \mathrm{rel.err}(\varepsilon)/\varepsilon$ across all nine
  configurations of the two worked examples. The data cleanly
  separate into two regimes predicted by the asymptotic expansion:
  balanced configurations exhibit the sharper scaling
  $\mathrm{rel.err}=O(\varepsilon^2)$ (slope $\approx 2$,
  $C_*\ll 1$); unbalanced configurations exhibit the generic
  $O(\varepsilon)$ scaling (slope $\approx 1$, $C_*\sim 0.7$).
  All nine configurations satisfy the conservative criterion
  $\mathrm{rel.err}(\varepsilon)\le 0.8\,\varepsilon$ for
  $\varepsilon\le 0.03$.
- **New validation criterion.** A quantitative boxed criterion
  (derived from the $O(\varepsilon^3)$ absolute remainder of the
  Bridge Theorem) is introduced:
  $\mathrm{PASS} \iff \mathrm{rel.err}(\varepsilon)
  \le 0.8\,\varepsilon$ for $\varepsilon \le 0.03$.
  The constant $C=0.8$ is a conservative upper bound determined
  empirically from the numerical verification.
- **Extended verification script (`verify_bridge_theorem_v3.py`).**
  Extends v2 with: (i) explicit numerical/analytic Fisher-matrix
  agreement checks; (ii) closed-form consistency checks against
  Propositions `prop:ex_verify` and `prop:ex2_verify`;
  (iii) minimum energetic cost tables at $T=300$ K via the
  Landauer bound (`thm:landauer`); (iv) the off-center robustness
  checks of Section 9.
- **Updated abstract and conclusion** to reflect the new
  off-center numerical evidence for the **locality** of the Bridge
  Theorem away from the symmetric reference $\theta^*=0$.
- **Expanded figure captions** for Figures 2 and 5 documenting
  the empirical log-log slopes of the relative-error curves
  (slopes $2.0000\pm 10^{-4}$ for balanced cases; slopes $1.0193$
  and $1.1013$ for the two unbalanced cases of Example 2).
- **Landauer bound — numerical illustration.** The verification
  script reports $E_\mathrm{min}\sim 10^{-25}$–$10^{-24}$ J at
  $T=300$ K and $\varepsilon=10^{-2}$, confirming that the
  bound is numerically meaningful but many orders of magnitude
  below the thermal noise floor $kT\sim 4\cdot 10^{-21}$ J in the
  small-$\varepsilon$ regime.

No change to the mathematical content of the manuscript's theorems,
definitions, or proofs. All additions are extensions of the
numerical verification layer and its interpretive scaffolding.

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

6. **Piecewise Smoothness (Proposition 10.5).** Observer entropy
   is piecewise-smooth in ε, with partition transitions at
   critical values given by interpoint distances of the metric
   space.

7. **Off-Center Robustness (Section 9, new in v3.0).** The
   locality of the Bridge Theorem is numerically confirmed at
   twelve randomly sampled off-center base points
   $\theta^*\ne 0$ (six for each worked example), with random
   within-class perturbation directions. Measured log-log slopes
   lie within $|\mathrm{slope}-2|<5\cdot 10^{-3}$, and normalised
   remainders $|R|/\varepsilon^3$ remain bounded by 0.2 uniformly
   on $\varepsilon\in[10^{-4},10^{-2}]$. The verification is
   reproducible with fixed seed `OFFCENTER_SEED = 42`.

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
- **Off-center robustness at twelve random base points**
  $\theta^*\ne 0$ (new in v3.0, Section 9 of the paper)
- **Empirical $C_*$ distribution** across all nine worked-example
  configurations, separating balanced ($O(\varepsilon^2)$ relative
  error, $C_*\ll 1$) from unbalanced ($O(\varepsilon)$ relative
  error, $C_*\sim 0.7$) regimes, with all nine configurations
  satisfying the conservative criterion
  $\mathrm{rel.err}(\varepsilon)\le 0.8\,\varepsilon$ for
  $\varepsilon\le 0.03$

All checks pass: **PASS — ALL BRIDGE THEOREM CHECKS PASSED**
(including the twelve new off-center robustness checks at
randomly sampled base points $\theta^*\ne 0$).

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
| 2.4.24 | [10.5281/zenodo.19883297](https://doi.org/10.5281/zenodo.19883297) | Editorial clarifications resolving scoping inconsistencies in Assumption `as:deformation` and Theorem `thm:bridge` |
| **3.0** | **[10.5281/zenodo.20004735](https://doi.org/10.5281/zenodo.20004735)** | **New Section 10 (off-center robustness checks at twelve random base points); two new figures (Figs. 6–7); empirical $C_*$ table across nine configurations; quantitative validation criterion $\mathrm{rel.err}(\varepsilon)\le 0.8\,\varepsilon$; extended verification script v3 with Landauer energetic cost tables at $T=300$ K** |

---

## Repository Structure

```
observer_entropy_bridge_theorem_v3.0/
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

Figures 1–5 are unchanged from v2.0 (up to extended captions in
Figures 2 and 5 documenting the empirical log-log slopes of the
relative-error curves). Figures 6 and 7 are **new in v3.0** and
display the off-center robustness checks at twelve randomly
sampled base points $\theta^*\ne 0$ (Section 9 of the paper).
The verification script is extended from v2 to v3 and includes
explicit numerical/analytic Fisher-matrix agreement checks,
closed-form consistency checks against Propositions `prop:ex_verify`
and `prop:ex2_verify`, minimum energetic cost tables at $T=300$ K
via the Landauer bound, and the off-center robustness checks of
Section 9 (with fixed RNG seed `OFFCENTER_SEED = 42` for
reproducibility).

---

## Figures

- **Figure 1** — Bridge Theorem verification (Example 1):
  exact vs. predicted observer entropy and normalized remainder.
- **Figure 2** — Relative error of the quadratic approximation
  (Example 1). Caption expanded in v3.0 to document empirical
  log-log slopes ($2.0000\pm 10^{-4}$, balanced regime).
- **Figure 3** — Resolution–information trade-off: monotone
  increase of $S_\mathrm{obs}(\varepsilon)$.
- **Figure 4** — Bridge Theorem verification (Example 2):
  exact vs. predicted observer entropy for unequal clusters.
- **Figure 5** — Relative error of the quadratic approximation
  (Example 2). Caption expanded in v3.0 to document empirical
  log-log slopes ($1.0193$ and $1.1013$ for unbalanced
  configurations; $2.0000\pm 10^{-4}$ for balanced ones).
- **Figure 6** *(new in v3.0)* — Off-center robustness check for
  Example 1: six independent random base points
  $\theta_1^*\in[-0.8,0.8]$ with random unit perturbation
  directions $(\alpha,\beta)$. Panel (a): log-log $S_\mathrm{obs}$
  vs. quadratic prediction. Panel (b): normalised remainder
  confirming the $O(\varepsilon^3)$ bound at $\theta^*\ne 0$.
- **Figure 7** *(new in v3.0)* — Off-center robustness check for
  Example 2: analogous structure for six random base points with
  random directions $(\alpha,\beta,\gamma)$.

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
python scripts/verify_bridge_theorem_v3.py
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
> A Minimal Information-Theoretic Framework*, Version 3.0 (2026).
> DOI: [10.5281/zenodo.20004735](
> https://doi.org/10.5281/zenodo.20004735)
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
