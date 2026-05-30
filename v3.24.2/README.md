# KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework

**Version 3.24.2**

**Author:** Vladimir Khomyakov — Independent Researcher  
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)

**DOI (this version):** [10.5281/zenodo.20444849](https://doi.org/10.5281/zenodo.20444849)

**Concept DOI (always resolves to latest version):** [10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)

---

## Overview

This repository accompanies the research article *"KL-Geometric
Structure of Observer Entropy: A Minimal Information-Theoretic
Framework"* (version 3.24.2). The paper constructs a self-contained
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

## What Is New in Version 3.24.2

Version 3.24.2 is a **self-contained proof-refinement release**:
it strengthens the rigor and self-containedness of several proofs
**without changing any theorem statement, definition, numerical
result, figure, or verification output**. The changes are confined
to the body of selected proofs and one added bibliographic
reference.

- **Self-contained expansion in Proposition 6.38 (Direct
  Verification of the Bridge Theorem, Example 2).** The
  cluster-$A$ contribution $\Sigma_A$ is now derived by a direct
  Taylor expansion of $h(a,b)=\log 3 - H_q(a,b)$ via the explicit
  expansion of $g(a,b)$ and the vanishing of the first-order term
  of $\mathbb{E}_q[s]$, rather than by invoking Corollary 6.51
  (Softmax Families). The previous coincidence with the within-$A$
  Fisher block $\mathrm{diag}(\tfrac{6}{5},\tfrac{2}{5})$ is
  retained as an independent consistency check. The leading
  coefficient and the $O(\varepsilon^3)$ remainder are unchanged.
- **Clarified key step in Lemma 6.48 (Vanishing of
  $D_\mathrm{w}\sigma_\mathrm{b}$ at zero).** An explanatory
  paragraph makes explicit that the proof rests solely on the
  vanishing of the within-class log-partition gradient
  $\nabla_{\theta_\mathrm{w}}\log h_k|_0 = 0$, which requires only
  $C^1$ regularity of the natural parameters; the affine-case
  interpretation via $\nabla^2 H_q|_0 = -\mathrm{Cov}_{q_0}(s)$ is
  recorded for context but not relied upon. The conclusion
  $D_\mathrm{w}\sigma_\mathrm{b}|_0 = 0$ is unchanged.
- **Strengthened justification of condition (A2) in Corollary 6.51
  (Softmax Families on Finite Metric Spaces).** Lift closure is now
  justified by the standard diffeomorphism of the natural parameter
  space of a minimal exponential family onto the interior of its
  mean-parameter support, with an explicit reference (Brown 1986,
  Thm. 3.6; cf. Amari 2016, Ch. 3). The conclusion is unchanged.
- **Self-contained proof of Proposition 11.12 (Local Expansion of
  $S_\mathrm{obs}^\mathrm{fib}$ along fibre-centered
  deformations).** The within-fibre KL expansion is now computed
  directly from $(1+u)\log(1+u) = u + \tfrac12 u^2 + O(|u|^3)$ with
  $\sum_\omega u_\omega = 0$, rather than by invoking Theorem 3.5
  (Local Quadratic Structure). The leading fibre-Fisher quadratic
  form and the $O(\varepsilon^3)$ remainder are unchanged.
- **Precise scope statement in Theorem 8.3 (Resolution–Information
  Trade-off).** The proof now states explicitly that only the
  necessary lower bound is established from the hypothesis
  $S_\mathrm{obs}\ge\delta_0$; the matching two-sided asymptotic
  equality is no longer claimed. The inequality
  (`eq:tradeoff_explicit`) is unchanged.
- **One added reference** (Brown 1986) supporting the (A2)
  justification in Corollary 6.51.

**No change** to:

- any theorem, lemma, proposition, corollary, definition, or
  assumption statement;
- the Bridge Theorem, the Sufficient Conditions Theorem, the
  Riemannian-geometric formulation, the Cognitive Uncertainty
  Principle, the Landauer bound, or the fibre-theoretic closed-form
  identity (Theorem 11.9);
- numerical results, the empirical $C_*$ table, the validation
  criterion, the off-center robustness checks, or the verification
  script and its output;
- Figures 1–7 or the supplementary diagnostic figures.

---

## What Is New in Version 3.24.1

Version 3.24.1 is a **purely editorial patch release** correcting a
theorem-numbering inconsistency introduced in v3.24. In the published
v3.24 manuscript and README, the closed-form fibre identity
$S_\mathrm{obs}^\mathrm{fib}(\mu) = \log N - H_\mathrm{w}(\mu)$ was
referred to as "Theorem 11.8", whereas in the compiled LaTeX source
the correct internal number is **Theorem 11.9** (the preceding
Lemma 11.8 is the chain rule for disintegration, $H(\mu) = H(p) +
H_\mathrm{w}(\mu)$). All five occurrences of "Theorem 11.8" in this
README and the corresponding occurrences in the manuscript and
verification script have been updated to "Theorem 11.9".

The verification script is renamed
`verify_bridge_theorem_v3.24.py` → `verify_bridge_theorem_v3.24.1.py`
with consistent internal version strings. Numerical content, proofs,
figures, and computed values are unchanged.

**No change** to any mathematical content, theorem statements, proofs,
numerical results, figures, or the empirical $C_*$ analysis.

---

## What Is New in Version 3.24

- **New Section 11 — Fibre-Theoretic Foundation.** The equivalence
  relation $\sim_\varepsilon$ is encoded as a surjection
  $\pi:\Omega\twoheadrightarrow\mathcal{X}$ with fibres
  $\Omega_x=\pi^{-1}(x)$, and the uniform lift
  $\widetilde{\Pi_\varepsilon p}$ becomes the pull–push composition
  $\pi^{*}\pi_{*}$. Observer entropy is recast as the KL divergence
  between a measure $\mu$ on $\Omega$ and its fibre-uniform
  reduction $\pi^{*}\pi_{*}\mu$.
- **Exact closed-form identity (Theorem 11.9):**
  $S_\mathrm{obs}^\mathrm{fib}(\mu) = \log N - H_\mathrm{w}(\mu)$,
  valid for every strictly positive measure $\mu$ on the fibred
  ground space, with $N$ the common fibre cardinality and
  $H_\mathrm{w}$ the within-fibre conditional entropy. This identity
  is non-perturbative and requires neither a parametric family nor
  an asymptotic expansion.
- **Unbalanced fibres extension (§11.6):** the closed-form identity
  generalises to fibres of unequal cardinality, covering the
  structurally distinct configuration of Example 2 (cluster sizes
  $3$ and $2$).
- **Updated verification script (`verify_bridge_theorem_v3.24.py`).**
  Extends v3 with new tests (T11.1–T11.6) verifying the push-pull
  identities, idempotence of $\pi^*\pi_*$, the closed-form identity
  for both balanced and unbalanced fibres, the range
  $0 \le S_\mathrm{obs}^\mathrm{fib} \le \log N$, and the
  equivalence with the partition-threshold definition.
- **Three new supplementary diagnostic figures:**
  `fig_supp_fisher_eigenvalues.pdf`, `fig_supp_landauer_budget.pdf`,
  `fig_supp_fibre_identity.pdf`.
- **Updated abstract, introduction, and conclusion** to reflect the
  new kinematic identity complementing the geometric local expansion.

**No change** to:

- the mathematical content of any theorem, lemma, proposition,
  definition, or proof;
- the Bridge Theorem, the Sufficient Conditions Theorem, the
  Riemannian-geometric formulation of Section 7, the Cognitive
  Uncertainty Principle, or the Landauer bound;
- numerical results for the Bridge Theorem, the empirical $C_*$
  table, or the validation criterion
  $\mathrm{rel.err}(\varepsilon)\le 0.8\,\varepsilon$ for
  $\varepsilon\le 0.03$;
- the off-center robustness checks introduced in v3.0
  (Section 9, twelve random base points, seed
    `OFFCENTER_SEED = 42`);
- Figures 1–7 (manuscript figures).

---

## What Was New in Version 3.12

Version 3.12 was a **purely editorial release**. It added a single
discussion paragraph to the section *Discussion and Open Questions*,
raising — as one of several explicitly open questions — the
possibility that coarse-graining flows on statistical manifolds may
admit nontrivial geometric invariants analogous to the frozen-in
topological structures recently established by Asenjo, Winkler, and
Comisso (2026) in gravitational field dynamics. The added paragraph
was formulated as an open problem and did **not** assert the
existence of such invariants in the Fisher–Rao framework; addressing
the question would require extending the metric formulation to
connection- and curvature-based structures (e.g., the
$\alpha$-connections of information geometry).

The substantive content of v3.0 was reproduced unchanged.

---

## What Was New in Version 3.0

Version 3.0 was a **substantive release** that extended the logically
closed framework of v2.4.24 with new numerical content, a new
section, two new figures, and a quantitative empirical analysis of
the validation criterion. The mathematical core (Bridge Theorem,
Sufficient Conditions Theorem, Riemannian-geometric reformulation,
Cognitive Uncertainty Principle, Landauer bound) was preserved from
v2.4.24 without modification.

The following additions and extensions were implemented in v3.0:

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

7. **Off-Center Robustness (Section 9).** The
   locality of the Bridge Theorem is numerically confirmed at
   twelve randomly sampled off-center base points
   $\theta^*\ne 0$ (six for each worked example), with random
   within-class perturbation directions. Measured log-log slopes
   lie within $|\mathrm{slope}-2|<5\cdot 10^{-3}$, and normalised
   remainders $|R|/\varepsilon^3$ remain bounded by 0.2 uniformly
   on $\varepsilon\in[10^{-4},10^{-2}]$. The verification is
   reproducible with fixed seed `OFFCENTER_SEED = 42`.

8. **Fibre-Theoretic Foundation (Section 11, NEW in v3.24).**
   A partition-free, coordinate-free reformulation of observer
   entropy via the pull-push composition $\pi^*\pi_*$, yielding
   the exact closed-form identity
   $S_\mathrm{obs}^\mathrm{fib}(\mu) = \log N - H_\mathrm{w}(\mu)$
   (Theorem 11.9), valid for every strictly positive measure on
   the fibred ground space. This identity complements the
   asymptotic Bridge Theorem (Theorem 6.7) without superseding it:
   the former is exact and global, the latter is local and
   asymptotic, and both expressions characterise the same
   information-theoretic quantity.

All results are proved from explicitly stated assumptions with
complete remainder estimates and hold uniformly over compact
parameter subsets.

---

## Open Questions (Discussion section of the paper)

The paper closes with a section *Discussion and Open Questions*
collecting six open directions that go beyond the present framework.
None of these are claimed as results; they are listed here for
transparency.

- Semigroup structure of coarse-graining across critical
  $\varepsilon$-values.
- **Frozen-in geometric structures.** Motivated
  by recent results of Asenjo, Winkler, and Comisso (2026) on
  frozen-in topological structures in gravitational field dynamics,
  one may ask whether coarse-graining flows on statistical manifolds
  admit analogous geometric invariants. Answering this question
  would require extending the present Fisher–Rao metric formulation
  to connection- and curvature-based structures (e.g., the
  $\alpha$-connections of information geometry). This is an open
  problem; no such invariants are claimed or established here.
- Minimum dissipation principle as a variational characterization
  of the coarse-graining generator $v(\theta)$.
- Connection to Wasserstein geometry and the Benamou–Brenier
  formula.
- "Informational second law" as an interpretive label for the
  already-proved non-negativity $S_\mathrm{obs}\ge 0$.
- Role of $\alpha$-connections and Amari duality.

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
  $\theta^*\ne 0$ (Section 9 of the paper)
- **Empirical $C_*$ distribution** across all nine worked-example
  configurations, separating balanced ($O(\varepsilon^2)$ relative
  error, $C_*\ll 1$) from unbalanced ($O(\varepsilon)$ relative
  error, $C_*\sim 0.7$) regimes, with all nine configurations
  satisfying the conservative criterion
  $\mathrm{rel.err}(\varepsilon)\le 0.8\,\varepsilon$ for
  $\varepsilon\le 0.03$
- **Fibre-theoretic identities (NEW in v3.24):**
  push-pull left inverse $\pi_* \circ \pi^* = \mathrm{id}$,
  idempotence $(\pi^* \pi_*)^2 = \pi^* \pi_*$,
  closed-form identity $S_\mathrm{obs}^\mathrm{fib} = \log N - H_\mathrm{w}$
  (Theorem 11.9) for both balanced and unbalanced fibres,
  range $0 \le S_\mathrm{obs}^\mathrm{fib} \le \log N$, and
  equivalence with the partition-threshold definition (Remark 11.11).

All checks pass: **PASS — ALL BRIDGE THEOREM CHECKS PASSED**
(including the twelve off-center robustness checks at
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
| 2.4.24 | [10.5281/zenodo.19883297](https://doi.org/10.5281/zenodo.19883297) | Resolved scoping inconsistency in `as:deformation` and `thm:bridge`; logically closed version |
| 3.0 | [10.5281/zenodo.20004735](https://doi.org/10.5281/zenodo.20004735) | New Section 9 (off-center robustness checks at twelve random base points); two new figures (Figs. 6–7); empirical $C_*$ table across nine configurations; quantitative validation criterion $\mathrm{rel.err}(\varepsilon)\le 0.8\,\varepsilon$; extended verification script v3 with Landauer energetic cost tables at $T=300$ K |
| 3.12 | [10.5281/zenodo.20034127](https://doi.org/10.5281/zenodo.20034127) | Editorial release. Added one discussion paragraph in *Discussion and Open Questions* raising — as an open problem — whether coarse-graining flows on statistical manifolds admit geometric invariants analogous to the frozen-in topological structures of Asenjo, Winkler, and Comisso (2026). No change to theorems, definitions, proofs, numerical results, verification scripts, figures, or the empirical $C_*$ analysis. |
| 3.24 | [10.5281/zenodo.20258280](https://doi.org/10.5281/zenodo.20258280) | Substantive release. New Section 11 (Fibre-Theoretic Foundation) introducing the partition-free, coordinate-free reformulation of observer entropy via the pull-push composition $\pi^*\pi_*$, with exact closed-form identity $S_\mathrm{obs}^\mathrm{fib}(\mu) = \log N - H_\mathrm{w}(\mu)$ (Theorem 11.8) and unbalanced-fibres extension. Updated verification script `verify_bridge_theorem_v3.24.py` with new tests (T11.1–T11.6). Three new supplementary diagnostic figures. |
| 3.24.1 | [10.5281/zenodo.20304959](https://doi.org/10.5281/zenodo.20304959) | Editorial patch. Corrected theorem-numbering inconsistency: the closed-form fibre identity $S_\mathrm{obs}^\mathrm{fib}(\mu) = \log N - H_\mathrm{w}(\mu)$ is Theorem 11.9 (not 11.8); Lemma 11.8 is the disintegration chain rule. Five occurrences updated in README and corresponding occurrences in manuscript and verification script. Script renamed to `verify_bridge_theorem_v3.24.1.py`. No change to mathematical content, proofs, numerical results, figures, or empirical $C_*$ analysis. |
| **3.24.2** | **[10.5281/zenodo.20444849](https://doi.org/10.5281/zenodo.20444849)** | **Self-contained proof-refinement release. Strengthened self-containedness of selected proofs without changing any theorem statement, definition, numerical result, figure, or verification output: direct Taylor expansion in Prop. 6.38 (Example 2) replacing the appeal to Cor. 6.51; clarified key step in Lemma 6.48; strengthened (A2) justification in Cor. 6.51 via the minimal-exponential-family diffeomorphism (Brown 1986); self-contained within-fibre KL expansion in Prop. 11.12 replacing the appeal to Thm. 3.5; precise scope statement in Thm. 8.3 (necessary lower bound only). One added reference (Brown 1986).** |

---

## Repository Structure

```
observer_entropy_bridge_theorem_v3.24.2/
├── README.md
├── LICENSE
├── requirements.txt
├── scripts/
│   └── verify_bridge_theorem_v3.24.2.py
└── figures/
    ├── fig1_bridge_theorem_verification.pdf
    ├── fig2_relative_error.pdf
    ├── fig3_resolution_information_tradeoff.pdf
    ├── fig4_bridge_theorem_ex2.pdf
    ├── fig5_relative_error_ex2.pdf
    ├── fig6_offcenter_ex1.pdf
    ├── fig7_offcenter_ex2.pdf
    ├── fig_supp_fisher_eigenvalues.pdf
    ├── fig_supp_landauer_budget.pdf
    └── fig_supp_fibre_identity.pdf
```

Figures 1–5 are unchanged from v2.0 (up to extended captions in
Figures 2 and 5 documenting the empirical log-log slopes of the
relative-error curves). Figures 6 and 7 (introduced in v3.0)
display the off-center robustness checks at twelve randomly
sampled base points $\theta^*\ne 0$ (Section 9 of the paper).
Three supplementary diagnostic figures (introduced in v3.24)
visualise the Fisher eigenvalue structure, the Landauer energy
budget at $T=300$ K, and the closed-form fibre identity of
Theorem 11.9. The verification script
`verify_bridge_theorem_v3.24.2.py` includes all checks from v3 plus
new tests (T11.1–T11.6) verifying the fibre-theoretic identities
of Section 11. All checks pass deterministically with fixed RNG
seed `OFFCENTER_SEED = 42`.

---

## Figures

- **Figure 1** — Bridge Theorem verification (Example 1):
  exact vs. predicted observer entropy and normalized remainder.
- **Figure 2** — Relative error of the quadratic approximation
  (Example 1). Caption documents empirical log-log slopes
  ($2.0000\pm 10^{-4}$, balanced regime).
- **Figure 3** — Resolution–information trade-off: monotone
  increase of $S_\mathrm{obs}(\varepsilon)$.
- **Figure 4** — Bridge Theorem verification (Example 2):
  exact vs. predicted observer entropy for unequal clusters.
- **Figure 5** — Relative error of the quadratic approximation
  (Example 2). Caption documents empirical log-log slopes
  ($1.0193$ and $1.1013$ for unbalanced configurations;
  $2.0000\pm 10^{-4}$ for balanced ones).
- **Figure 6** — Off-center robustness check for Example 1:
  six independent random base points
  $\theta_1^*\in[-0.8,0.8]$ with random unit perturbation
  directions $(\alpha,\beta)$. Panel (a): log-log $S_\mathrm{obs}$
  vs. quadratic prediction. Panel (b): normalised remainder
  confirming the $O(\varepsilon^3)$ bound at $\theta^*\ne 0$.
- **Figure 7** — Off-center robustness check for Example 2:
  analogous structure for six random base points with random
  directions $(\alpha,\beta,\gamma)$.
- **Supplementary Figure (Fisher eigenvalues)** — bar plots of
  the eigenvalues of $I(\theta^*)$ for Examples 1 and 2.
- **Supplementary Figure (Landauer budget)** — minimum energetic
  cost $E_\mathrm{min} = kT \cdot S_\mathrm{obs}$ at $T=300$ K
  versus resolution threshold $\varepsilon$.
- **Supplementary Figure (Fibre identity)** — scatter plot of
  direct vs. closed-form $S_\mathrm{obs}^\mathrm{fib}$ verifying
  Theorem 11.9 for balanced and unbalanced fibres.

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
python scripts/verify_bridge_theorem_v3.24.2.py
```

---

## Keywords

KL divergence, Fisher information, Fisher–Rao metric, observer
entropy, cognitive projection, coarse-graining generator,
dissipation functional, information geometry, Landauer's principle,
partition-adapted parameterization, sufficient conditions,
between/within decomposition, fibre bundle, disintegration,
closed-form entropy identity.

**MSC 2020:** 62B10, 94A17, 53B12, 81P45.

---

## Citation

If you use this work, please cite:

Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy:
A Minimal Information-Theoretic Framework*, Version 3.24.2 (2026).
DOI: [10.5281/zenodo.20444849](https://doi.org/10.5281/zenodo.20444849)

Concept DOI (always resolves to latest version):
[10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)

---

## Code Availability

The verification script and all figures are available at:
[https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/)

---

## License

See `LICENSE` file.
