# KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework  
**Version 2.4.8 — Strengthened Assumption 6.1 with (D1)–(D3); extended proof of Theorem 6.41 (Step 3); expanded proof of Lemma 6.42**  

**Author:** Vladimir Khomyakov — Independent Researcher  
[ORCID: 0009-0006-3074-9145](https://orcid.org/0009-0006-3074-9145)  

**DOI:** [10.5281/zenodo.19645407](https://doi.org/10.5281/zenodo.19645407)  
**Concept DOI (all versions):** [10.5281/zenodo.18826258](https://doi.org/10.5281/zenodo.18826258)  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18826258.svg)](https://doi.org/10.5281/zenodo.18826258)  
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) — Scientific article and associated documentation  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) — Source code and simulation scripts  

---

## Overview  

This directory accompanies Version 2.4.8 of the article *"KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework"*. The paper constructs a self-contained geometric framework unifying the local information geometry of Kullback–Leibler divergence with an observer-dependent theory of coarse-grained entropy on finite measurable spaces.  

The central result is the **Bridge Theorem**: a finite observer resolution threshold ε induces a projection of probabilistic descriptions, resulting in measurable KL information loss — observer entropy — that scales quadratically with the threshold, controlled by the Fisher information geometry:  

$$S_{\mathrm{obs}}(p_\theta, \varepsilon) = \tfrac{1}{2}\,\varepsilon^2\, v^\top I(\theta^*)\, v \;+\; O(\varepsilon^3), \qquad \varepsilon \to 0^+$$  

where $I(\theta)$ is the Fisher information matrix and $v$ encodes the direction of information loss in parameter space.  

---

## What's New in Version 2.4.8  

Version 2.4.8 introduces three substantive mathematical improvements relative to v2.4.1. No changes have been made to the article's figures, verification scripts, or worked examples.  

### 1. Strengthened Parametric Deformation Assumption (Assumption 6.1)  

The Parametric Deformation Assumption has been reformulated with three explicit regularity conditions **(D1)–(D3)**:  

- **(D1)** The displaced parameter remains in Θ for all ε in a compact regime.  
- **(D2)** The remainder satisfies ‖ρ(θ,ε)‖ ≤ L_K ε² uniformly on every compact K ⊂ Θ.  
- **(D3)** The ε-derivative of ρ satisfies ‖∂_ε ρ(θ,ε)‖ ≤ 2L_K ε with ∂_ε ρ(θ,0) = 0, following from C²-regularity of ρ in ε via Taylor's theorem with integral remainder.  

A **fixed-partition regime** requirement — that the partition 𝒫_ε is independent of ε for ε ∈ (0,ε*) — is now incorporated as an explicit part of the assumption rather than stated only as a separate remark. These additions close a gap in earlier versions concerning the precise regularity requirements on the remainder term needed for the Bridge Theorem proof.  

### 2. Extended Proof of the Sufficient Conditions Theorem (Theorem 6.41)  

The proof of the Sufficient Conditions Theorem now contains an explicit **Step 3: Verification of Assumption 6.1**, which systematically checks conditions (D1)–(D3) uniformly on compact subsets of Θ. Specifically:  

- The uniform constant L_K is identified via the second-order Taylor remainder of σ_b, bounded by ½ · M_K · ‖α‖² · ε², where M_K is the supremum of ‖D²_w σ_b‖ over K.  
- (D1) is verified by compactness of K and openness of Θ.  
- (D3) is verified by C²-regularity of the remainder R_b(ε) as a function of ε, with explicit derivative bound.  

This step was implicit in v2.4.1 but is now fully written out, making the logical chain from conditions (A1)–(A3) to Assumption 6.1 complete and self-contained.  

### 3. Strengthened Proof of the Vanishing Lemma (Lemma 6.42)  

The proof of the Vanishing Lemma ($D_\mathrm{w}\sigma_\mathrm{b}|_{\theta_\mathrm{w}=0} = 0$) has been substantially expanded. The new version includes:  

- An **explicit construction** of the decomposition $\eta_x(\theta) = \bar{\eta}_k(\theta_\mathrm{b}) + \phi_x(\theta_\mathrm{w})$ for $x \in A_k$, with $\bar{\eta}_k$ defined canonically via within-class neutrality (A1) and uniqueness verified by local injectivity (A3).  
- A **direct proof** that $\phi_x(0) = 0$ for all $x \in A_k$ and that $\sum_{x \in A_k} \phi_x \equiv 0$, derived from conditions (L1)–(L2) without invoking Assumption 6.1.  
- An explicit **block decomposition** of $D\Phi|_{(\theta_b^*,0)}$ confirming that the Jacobian $\partial\bar{\eta}/\partial\sigma_\mathrm{b}$ is square of full rank $d_\mathrm{b} = m-1$, which is required for the implicit function theorem application.  
- A self-contained independence statement confirming that the argument does not invoke Assumption 6.1 at any point, preserving the logical independence required for the proof of Theorem 6.41.  

---

## What's New in Version 2.4.1  

**One change only:** self-naming of the main theorem removed (editorial correction).  

In versions 2.0–2.4, the Bridge Theorem was referred to as "Khomyakov's Bridge" or "Khomyakov Bridge Theorem" within the article itself. This practice — an author naming their own result after themselves in the same document — is not consistent with academic norms: theorem names are assigned by the scientific community after recognition, not by the author at the time of publication.  

**Affected locations in the `.tex` source (5 occurrences removed):**  

| Location | Change |  
|---|---|  
| Abstract | Removed `(herein referred to as Khomyakov's Bridge)` |  
| Introduction | Removed sentence `We formally designate this result as the Khomyakov Bridge Theorem.` |  
| Section 6 heading | `Bridge Theorem: ... (Khomyakov's Bridge)` → `Bridge Theorem: ...` |  
| Theorem 6.5 label | `[Bridge Theorem (Khomyakov's Bridge)]` → `[Bridge Theorem]` |  
| Conclusion | Removed `Khomyakov's Bridge` from parenthetical |  

There are **no changes** to the article's mathematics, theorems, proofs, figures, or verification scripts relative to v2.4. The term **Bridge Theorem** is fully preserved throughout.  

---

## What's New in Version 2.4  

A **Related Work** section has been added, situating the Bridge Theorem with respect to two concurrent works: Izumo (2026), who introduces a KL-based measure of information loss under discrete partitions without deriving a geometric scaling law, and Kiely et al. (2026), who employ quantum Fisher information in the context of classical objectivity emergence, also without establishing a KL-geometric scaling relation. There are **no changes** to the article's theorems, proofs, figures, or verification scripts relative to v2.2.  

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

1. **Bridge Theorem (Theorem 6.5).** Quadratic scaling law for observer entropy with explicit cubic remainder control, $|S_\mathrm{obs} - \tfrac{1}{2}\varepsilon^2 v^\top Iv| \le C_1 \varepsilon^3$.  

2. **Sufficient Conditions (Theorem 6.41).** The Parametric Deformation Assumption (including conditions (D1)–(D3)) is proved to be a consequence of three checkable finite-dimensional conditions — within-class neutrality (A1), lift closure (A2), immersion condition (A3) — that hold automatically for full exponential families with centered between/within parameterization. Uniform constants are now identified explicitly.  

3. **Riemannian-Geometric Reformulation (Section 7).** The quadratic form $v^\top I\,v$ equals the Fisher–Rao inner product $g_\theta(v,v)$. Observer entropy is one-half the squared Fisher–Rao norm of the coarse-graining generator (Theorem 7.3, Corollary 7.6), and equivalently the second variation of the KL divergence along the coarse-graining orbit (Theorem 7.9). A dissipation functional unifies these perspectives (Corollary 7.13).  

4. **Cognitive Uncertainty Principle (Theorem 8.2).** Resolution–information trade-off: the observer's finite resolution threshold ε must satisfy $\varepsilon \ge \sqrt{2\delta_0/Q}\,(1 - C'\varepsilon)$ for the information loss to exceed the detection threshold $\delta_0$.  

5. **Landauer Bound (Theorem 8.4).** Thermodynamic lower bound: $E_\mathrm{min} \ge kT \cdot S_\mathrm{obs}(p,\varepsilon)$.  

6. **Piecewise Smoothness (Proposition 9.5).** Observer entropy is piecewise-smooth in ε, with partition transitions at critical values given by interpoint distances of the metric space.  

All results are proved from explicitly stated assumptions with complete remainder estimates and hold uniformly over compact parameter subsets.  

---

## Numerical Verification  

The quadratic scaling law is verified by two independent worked examples (unchanged from v2.0):  

**Example 1** — Four-point space $\mathcal{X} = \{1,2,3,4\}$, equal-size clusters $\mathcal{P} = \{\{1,2\},\{3,4\}\}$, softmax family, 2 distinct Fisher eigenvalues.  
Fisher matrix: $I(\theta^*) = \mathrm{diag}(1,\tfrac{1}{2},\tfrac{1}{2})$.  

**Example 2** — Five-point space $\mathcal{X} = \{1,2,3,4,5\}$, unequal clusters $\mathcal{P} = \{\{1,2,3\},\{4,5\}\}$, 3 distinct Fisher eigenvalues.  
Fisher matrix: $I(\theta^*) = \mathrm{diag}(\tfrac{3}{2},\tfrac{6}{5},\tfrac{2}{5},\tfrac{2}{5})$.  

The verification script confirms:  

- Quadratic scaling $S_\mathrm{obs} \sim \varepsilon^2$ (log-log slope = 2.000 ± 0.01 in all cases)  
- Bounded $O(\varepsilon^3)$ remainder  
- Fisher matrix agreement between analytic and finite-difference computations  
- Closed-form leading coefficients match Fisher-based predictions  
- Non-negativity of observer entropy (Landauer bound satisfied)  
- Monotone non-decrease $S_\mathrm{obs}(\varepsilon)$ (resolution–information trade-off)  

All checks pass: **PASS — ALL BRIDGE THEOREM CHECKS PASSED**.  

---

## Directory Contents  

```
v2.4.8/  
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

Figures and the verification script are identical to v2.0.  

---

## Figures  

- **Figure 1** — Bridge Theorem verification (Example 1): exact vs. predicted observer entropy and normalized remainder.  
- **Figure 2** — Relative error of the quadratic approximation (Example 1).  
- **Figure 3** — Resolution–information trade-off: monotone increase of $S_\mathrm{obs}(\varepsilon)$.  
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

The article and reproducibility package for this version are archived at two independent permanent locations. Checksums are provided for independent verification.  

**Version 2.4.8 — Strengthened Assumption 6.1 with (D1)–(D3); extended proof of Theorem 6.41 (Step 3); expanded proof of Lemma 6.42**  

> **Note on theorem numbering.** The theorem identifiers listed in this README  
> (Theorem 6.5, Theorem 6.41, Theorem 7.3, Corollary 7.6, Theorem 7.9, Corollary 7.13,  
> Theorem 8.2, Theorem 8.4, Proposition 9.5) reflect the numbering as it appeared  
> in the published article. These numbers are unchanged relative to v2.0 and remain  
> correct through all subsequent versions including v2.4.8.  

### Canonical record (Zenodo)  

| File | Direct URL | MD5 |  
|------|-----------|-----|  
| `observer_entropy_bridge_theorem_v2.4.8.pdf` | [download](https://zenodo.org/records/19645407/files/observer_entropy_bridge_theorem_v2.4.8.pdf) | `bec0b3e2b92208822c159e1cc9548829` |  
| `observer_entropy_bridge_theorem_v2.4.8.zip` | [download](https://zenodo.org/records/19645407/files/observer_entropy_bridge_theorem_v2.4.8.zip) | `b53e24a5b91d04c82984222ebf3febd6` |  

DOI: [10.5281/zenodo.19645407](https://doi.org/10.5281/zenodo.19645407)  

### Mirror (GitHub Releases v2.4.8)  

| File | Permanent URL | SHA-256 |  
|------|--------------|---------|  
| `observer_entropy_bridge_theorem_v2.4.8.pdf` | [download](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.8/observer_entropy_bridge_theorem_v2.4.8.pdf) | `5d8f86282d3487f76337b8895e499c08c0071d50b622c40ce26a3d91247f5996` |  
| `observer_entropy_bridge_theorem_v2.4.8.zip` | [download](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/download/v2.4.8/observer_entropy_bridge_theorem_v2.4.8.zip) | `b55437f4275a8624d305fd5bd93a71204654f755a4902284ff52d8df4f81fa65` |  

GitHub Release: [v2.4.8](https://github.com/Khomyakov-Vladimir/observer-entropy-bridge/releases/tag/v2.4.8)  

---

## Version History  

- **Version 1.0** — core framework: see [`../v1.0_core/`](../v1.0_core/)  
- **Version 1.2** — Riemannian-Geometric Reformulation: see [`../v1.2_geometric/`](../v1.2_geometric/)  
- **Version 2.0** — Sufficient Conditions theorem and second worked example: see [`../v2.0_sufficient-conditions/`](../v2.0_sufficient-conditions/)  
- **Version 2.1** — citation of concurrent work (Izumo 2026): see [`../v2.1_izumo-citation/`](../v2.1_izumo-citation/)  
- **Version 2.2** — README correction (theorem numbers): see [`../v2.2_readme-correction/`](../v2.2_readme-correction/)  
- **Version 2.4** — Related Work Section and verify_bridge_theorem_v2.py correction (theorem numbers in scripts/verify_bridge_theorem_v2.py): see [`../v2.4_related-work/`](../v2.4_related-work/)  
- **Version 2.4.1** — self-naming removed (editorial correction): see [`../v2.4.1/`](../v2.4.1/)  
- **Version 2.4.8** — Strengthened Assumption 6.1 with (D1)–(D3); extended proof of Theorem 6.41 (Step 3); expanded proof of Lemma 6.42: this directory  
- **Version 2.4.12** — adds Editorial clarifications; corrected statements; improved notation; no change to mathematical content: see [`../v2.4.12/`](../v2.4.12/)  

---

## Keywords  

KL divergence, Fisher information, Fisher–Rao metric, observer entropy, cognitive projection, coarse-graining generator, dissipation functional, information geometry, Landauer's principle, partition-adapted parameterization, sufficient conditions, between/within decomposition.  

**MSC 2020:** 62B10, 94A17, 53B12, 81P45.  

---

## Citation  

> Vladimir Khomyakov, *KL-Geometric Structure of Observer Entropy: A Minimal Information-Theoretic Framework*, Version 2.4.8 (2026). DOI: [10.5281/zenodo.19645407](https://doi.org/10.5281/zenodo.19645407)  

---

## License  

MIT License. See [LICENSE](LICENSE).  
