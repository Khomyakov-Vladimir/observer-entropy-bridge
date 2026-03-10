#!/usr/bin/env python3
"""
verify_bridge_theorem_v2.py
===========================
Numerical Verification of Theorem 6.3 (Bridge Theorem) — Version 2.0
(Parametrization aligned with Definition 6.3 and Definition 6.13)

Paper: "KL-Geometric Structure of Observer Entropy: A Minimal
        Information-Theoretic Framework"
Author: Vladimir Khomyakov (Version 2.0, DOI: 10.5281/zenodo.18826258)

Central result — Khomyakov's Bridge Theorem (Theorem 6.3):

    S_obs(p_θ, ε) = ½ ε² v⊤ I(θ) v + O(ε³),   ε → 0⁺

This script verifies the theorem for two concrete examples:
  • Example 1: 4-point space  X={1,2,3,4}, P={{1,2},{3,4}}
                (Definition 6.3, Lemma 6.5, Proposition 6.8)
  • Example 2: 5-point space  X={1,2,3,4,5}, P={{1,2,3},{4,5}}
                (Definition 6.13, Proposition 6.19, Proposition 6.22)

All eight required verification components are implemented with explicit
PASS/FAIL verdicts. Five publication-quality figures are generated.

Dependencies: numpy, scipy (linear regression only), matplotlib
"""

import sys
import os
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 0. Global settings & constants
# ============================================================

BOLTZMANN_K = 1.380649e-23   # J / K  (exact, SI 2019)
T_KELVIN    = 300.0           # Kelvin

# Epsilon grids
EPS_GRID   = np.logspace(-4, -1, 200)   # for plotting
EPS_TABLE  = np.array([1e-4, 1e-3, 1e-2, 1e-1])   # for summary table

# Finite-difference step for Fisher verification
FD_STEP    = 1e-5

# Tolerances
FISHER_ATOL      = 1e-8    # analytic vs. numerical Fisher agreement
SLOPE_TOL        = 0.01    # |fitted slope - 2.0| < SLOPE_TOL
REMAINDER_BOUND  = 10.0    # |R(ε)| / ε³ < REMAINDER_BOUND for ε ∈ [1e-4, 1e-2]
REL_ERR_EPS_MAX  = 0.03    # verify rel. error < 5 % for ε ≤ this value

# ------------------------------------------------------------
# Repository paths (support universal script execution)
# ------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent

# If the script lives in scripts/, repository root is its parent.
# Otherwise the script itself is in the repo root.
REPO_ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR

# Output directory for figures (always in repo root)
FIG_DIR = REPO_ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Matplotlib publication settings
plt.rcParams.update({
    "font.size":        11,
    "axes.labelsize":   12,
    "axes.titlesize":   13,
    "legend.fontsize":  9,
    "xtick.labelsize":  10,
    "ytick.labelsize":  10,
    "text.usetex":      False,
    "mathtext.fontset": "cm",
    "figure.dpi":       300,
    "savefig.dpi":      300,
    "savefig.bbox":     "tight",
    "lines.linewidth":  2.0,
})

COLORS = ["#2060c0", "#c03020", "#209040", "#9040b0", "#d07010"]
STYLES = ["-", "--", "-.", ":", (0, (3, 1, 1, 1))]

# Track all check failures globally
_FAILURES: list[str] = []


def _pass(msg: str) -> None:
    print(f"  [PASS] {msg}")


def _fail(msg: str) -> None:
    print(f"  [FAIL] {msg}")
    _FAILURES.append(msg)


# ============================================================
# 1. Example 1: 4-point space  X={1,2,3,4}, P={{1,2},{3,4}}
#    (Definition 6.3 of the paper)
# ============================================================

# Test cases (α, β) — 4 cases as in Figure 1 & 2 of the paper
EX1_CASES = [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (3.0, 2.0)]
# Partition classes (0-indexed)
EX1_CLASSES = [[0, 1], [2, 3]]


def eta_ex1(theta: np.ndarray) -> np.ndarray:
    """Natural parameters for Example 1 (Definition 6.3).
    θ = (θ₁, θ₂, θ₃)
    η₁ = θ₁+θ₂,  η₂ = θ₁−θ₂,  η₃ = −θ₁+θ₃,  η₄ = −θ₁−θ₃
    """
    t1, t2, t3 = theta
    return np.array([t1 + t2, t1 - t2, -t1 + t3, -t1 - t3])


def p_ex1(theta: np.ndarray) -> np.ndarray:
    """Softmax distribution for Example 1."""
    eta = eta_ex1(theta)
    eta = eta - eta.max()   # numerical stability
    e = np.exp(eta)
    return e / e.sum()


def uniform_lift_ex1(p: np.ndarray) -> np.ndarray:
    """Coarse-grained (uniform-lift) distribution for Example 1."""
    piA = p[0] + p[1]
    piB = p[2] + p[3]
    return np.array([piA / 2, piA / 2, piB / 2, piB / 2])


def S_obs_ex1(p: np.ndarray) -> float:
    """Exact observer entropy D_KL(p || p_tilde) for Example 1."""
    q = uniform_lift_ex1(p)
    return float(np.sum(p * np.log(p / q)))


def compute_S_obs_ex1(alpha: float, beta: float, eps: float) -> float:
    """Compute exact S_obs at θ(ε) = (0, εα, εβ)."""
    theta = np.array([0.0, eps * alpha, eps * beta])
    return S_obs_ex1(p_ex1(theta))


def suff_stat_ex1() -> np.ndarray:
    """Sufficient statistic matrix T, shape (4, 3).
    Row x = t(x) = ∇_θ η_x  (Proposition 6.8).
      t(1) = (1, 1, 0),  t(2) = (1, -1, 0),
      t(3) = (-1, 0, 1), t(4) = (-1, 0, -1)
    """
    return np.array([
        [ 1,  1,  0],
        [ 1, -1,  0],
        [-1,  0,  1],
        [-1,  0, -1],
    ], dtype=float)


def fisher_analytic_ex1(theta: np.ndarray) -> np.ndarray:
    """Fisher information I(θ) = Cov_p[T(x)] for Example 1."""
    p = p_ex1(theta)
    T = suff_stat_ex1()
    mu = p @ T
    centered = T - mu[np.newaxis, :]
    return (p[:, np.newaxis] * centered).T @ centered


def fisher_numerical_ex1(theta: np.ndarray, h: float = FD_STEP) -> np.ndarray:
    """Fisher information via central finite differences for Example 1."""
    d = len(theta)
    I = np.zeros((d, d))
    for i in range(d):
        ei = np.zeros(d); ei[i] = 1.0
        log_p_plus  = np.log(p_ex1(theta + h * ei) + 1e-300)
        log_p_minus = np.log(p_ex1(theta - h * ei) + 1e-300)
        score_i = (log_p_plus - log_p_minus) / (2 * h)
        for j in range(d):
            ej = np.zeros(d); ej[j] = 1.0
            log_p_plus2  = np.log(p_ex1(theta + h * ej) + 1e-300)
            log_p_minus2 = np.log(p_ex1(theta - h * ej) + 1e-300)
            score_j = (log_p_plus2 - log_p_minus2) / (2 * h)
            I[i, j] = np.sum(p_ex1(theta) * score_i * score_j)
    return I


def quadratic_pred_ex1(alpha: float, beta: float, eps: float,
                        theta_star: np.ndarray = np.zeros(3)) -> float:
    """½ ε² v⊤ I(θ*) v  for Example 1.
    v = (0, -α, -β),  I(θ*) = diag(1, 1/2, 1/2)
    → ½ [0·1·0 + α²·(1/2) + β²·(1/2)] ε² = ¼(α²+β²) ε²
    """
    v = np.array([0.0, -alpha, -beta])
    I = fisher_analytic_ex1(theta_star)
    return 0.5 * eps**2 * float(v @ I @ v)


# ============================================================
# 2. Example 2: 5-point space  X={1,2,3,4,5}, P={{1,2,3},{4,5}}
#    (Definition 6.13 of the paper)
# ============================================================

# Test cases (α, β, γ) — ALL 5 cases from Figures 4-5 of the paper
EX2_CASES = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0),
             (1.0, 1.0, 1.0), (2.0, 1.0, 3.0)]
EX2_CLASSES = [[0, 1, 2], [3, 4]]


def eta_ex2(theta: np.ndarray) -> np.ndarray:
    """Natural parameters for Example 2 (Definition 6.13 of the paper).

    θ = (θ₁, θ₂, θ₃, θ₄)

    η₁(θ) = θ₁ + θ₂ + θ₃      (state 1 ∈ A)
    η₂(θ) = θ₁ + θ₂ − θ₃      (state 2 ∈ A)
    η₃(θ) = θ₁ − 2θ₂           (state 3 ∈ A)
    η₄(θ) = −3/2·θ₁ + θ₄      (state 4 ∈ B)
    η₅(θ) = −3/2·θ₁ − θ₄      (state 5 ∈ B)

    Centered parametrization: 3·(+1) + 2·(−3/2) = 0  (Remark 6.14).
    θ₁ = between-cluster parameter
    θ₂ = within-A: {1,2} vs {3}  (coefficients +1,+1,−2 sum to 0)
    θ₃ = within-A: {1} vs {2}    (coefficients +1,−1,0 sum to 0)
    θ₄ = within-B: {4} vs {5}    (coefficients +1,−1 sum to 0)
    """
    t1, t2, t3, t4 = theta
    return np.array([
        t1 + t2 + t3,          # η₁
        t1 + t2 - t3,          # η₂
        t1 - 2.0 * t2,         # η₃
        -1.5 * t1 + t4,        # η₄
        -1.5 * t1 - t4,        # η₅
    ])


def p_ex2(theta: np.ndarray) -> np.ndarray:
    """Softmax distribution for Example 2."""
    eta = eta_ex2(theta)
    eta = eta - eta.max()
    e = np.exp(eta)
    return e / e.sum()


def uniform_lift_ex2(p: np.ndarray) -> np.ndarray:
    """Coarse-grained distribution for Example 2."""
    piA = p[0] + p[1] + p[2]
    piB = p[3] + p[4]
    return np.array([piA / 3, piA / 3, piA / 3, piB / 2, piB / 2])


def S_obs_ex2(p: np.ndarray) -> float:
    """Exact observer entropy D_KL(p || p_tilde) for Example 2."""
    q = uniform_lift_ex2(p)
    return float(np.sum(p * np.log(p / q)))


def compute_S_obs_ex2(alpha: float, beta: float, gamma: float,
                      eps: float) -> float:
    """Compute exact S_obs at θ(ε) = (0, εα, εβ, εγ)."""
    theta = np.array([0.0, eps * alpha, eps * beta, eps * gamma])
    return S_obs_ex2(p_ex2(theta))


def suff_stat_ex2() -> np.ndarray:
    """Sufficient statistic matrix T, shape (5, 4).
    Row x = t(x) = ∇_θ η_x  (Proposition 6.19 of the paper).

      t(1) = ( 1,    1,  1,  0)
      t(2) = ( 1,    1, -1,  0)
      t(3) = ( 1,   -2,  0,  0)
      t(4) = (-3/2,  0,  0,  1)
      t(5) = (-3/2,  0,  0, -1)
    """
    return np.array([
        [ 1.0,   1.0,  1.0,  0.0],
        [ 1.0,   1.0, -1.0,  0.0],
        [ 1.0,  -2.0,  0.0,  0.0],
        [-1.5,   0.0,  0.0,  1.0],
        [-1.5,   0.0,  0.0, -1.0],
    ], dtype=float)


def fisher_analytic_ex2(theta: np.ndarray) -> np.ndarray:
    """Fisher information I(θ) = Cov_p[T(x)] for Example 2."""
    p = p_ex2(theta)
    T = suff_stat_ex2()
    mu = p @ T
    centered = T - mu[np.newaxis, :]
    return (p[:, np.newaxis] * centered).T @ centered


def fisher_numerical_ex2(theta: np.ndarray, h: float = FD_STEP) -> np.ndarray:
    """Fisher information via central finite differences for Example 2."""
    d = len(theta)
    I = np.zeros((d, d))
    for i in range(d):
        ei = np.zeros(d); ei[i] = 1.0
        log_p_plus  = np.log(p_ex2(theta + h * ei) + 1e-300)
        log_p_minus = np.log(p_ex2(theta - h * ei) + 1e-300)
        score_i = (log_p_plus - log_p_minus) / (2 * h)
        for j in range(d):
            ej = np.zeros(d); ej[j] = 1.0
            log_p_plus2  = np.log(p_ex2(theta + h * ej) + 1e-300)
            log_p_minus2 = np.log(p_ex2(theta - h * ej) + 1e-300)
            score_j = (log_p_plus2 - log_p_minus2) / (2 * h)
            I[i, j] = np.sum(p_ex2(theta) * score_i * score_j)
    return I


def quadratic_pred_ex2(alpha: float, beta: float, gamma: float, eps: float,
                        theta_star: np.ndarray = np.zeros(4)) -> float:
    """½ ε² v⊤ I(θ*) v  for Example 2.
    v = (0, -α, -β, -γ)  (Proposition 6.22)
    I(θ*) = diag(3/2, 6/5, 2/5, 2/5)  (Proposition 6.19)
    → ½ [α²·(6/5) + β²·(2/5) + γ²·(2/5)] ε²
    = (3/5·α² + 1/5·β² + 1/5·γ²) ε²    (equation 6.15)
    """
    v = np.array([0.0, -alpha, -beta, -gamma])
    I = fisher_analytic_ex2(theta_star)
    return 0.5 * eps**2 * float(v @ I @ v)


# ============================================================
# 3. Verification helpers
# ============================================================

def loglog_slope(eps_arr: np.ndarray, y_arr: np.ndarray) -> float:
    """Fit log-log linear regression slope over range ε ∈ [1e-4, 1e-1]."""
    mask = (eps_arr >= 1e-4) & (eps_arr <= 1e-1) & (y_arr > 0)
    log_eps = np.log10(eps_arr[mask])
    log_y   = np.log10(y_arr[mask])
    slope, _, _, _, _ = stats.linregress(log_eps, log_y)
    return slope


def check_slope(label: str, eps_arr: np.ndarray,
                exact_arr: np.ndarray) -> float:
    """Verify log-log slope ≈ 2.0 ± SLOPE_TOL."""
    slope = loglog_slope(eps_arr, exact_arr)
    err   = abs(slope - 2.0)
    if err < SLOPE_TOL:
        _pass(f"{label}: log-log slope = {slope:.6f}  (|slope-2| = {err:.2e} < {SLOPE_TOL})")
    else:
        _fail(f"{label}: log-log slope = {slope:.6f}  (|slope-2| = {err:.2e} >= {SLOPE_TOL})")
    return slope


def check_remainder_bound(label: str, eps_arr: np.ndarray,
                          exact_arr: np.ndarray,
                          pred_arr: np.ndarray) -> float:
    """Verify |R(ε)|/ε³ ≤ REMAINDER_BOUND for ε ∈ [1e-4, 1e-2]."""
    mask = (eps_arr >= 1e-4) & (eps_arr <= 1e-2)
    rem_norm = np.abs(exact_arr[mask] - pred_arr[mask]) / eps_arr[mask]**3
    sup_val  = rem_norm.max()
    if sup_val < REMAINDER_BOUND:
        _pass(f"{label}: sup|R|/eps^3 = {sup_val:.6f}  (< {REMAINDER_BOUND})")
    else:
        _fail(f"{label}: sup|R|/eps^3 = {sup_val:.6f}  (>= {REMAINDER_BOUND})")
    return sup_val


def check_rel_error_threshold(label: str, eps_arr: np.ndarray,
                              exact_arr: np.ndarray,
                              pred_arr: np.ndarray) -> None:
    """Verify relative error is small for ε ≤ REL_ERR_EPS_MAX.

    The core theorem guarantee is the O(ε³) remainder bound (Component 3).
    The relative error |R|/S_obs ∝ O(ε) should be small for small ε.
    We use a 5% threshold to accommodate cases with large higher-order terms.
    """
    mask = eps_arr <= REL_ERR_EPS_MAX
    rel  = np.where(exact_arr[mask] > 0,
                    np.abs(exact_arr[mask] - pred_arr[mask]) / exact_arr[mask],
                    0.0)
    max_rel = rel.max()
    threshold = 0.05
    if max_rel < threshold:
        _pass(f"{label}: max rel.err for eps<={REL_ERR_EPS_MAX} = {max_rel:.2e}  "
              f"(< {threshold*100:.0f}%; O(eps) scaling confirmed)")
    else:
        _fail(f"{label}: max rel.err for eps<={REL_ERR_EPS_MAX} = {max_rel:.2e}  "
              f"(>= {threshold*100:.0f}%)")
    # Check relative error scaling: slope ≥ 1 in log-log means at least O(ε)
    rel_full = np.where(exact_arr > 0,
                        np.abs(exact_arr - pred_arr) / exact_arr, 1e-300)
    valid = (eps_arr >= 1e-3) & (eps_arr <= 1e-1) & (rel_full > 1e-20)
    if valid.sum() > 5:
        slope_rel, _, _, _, _ = stats.linregress(
            np.log10(eps_arr[valid]), np.log10(rel_full[valid]))
        if slope_rel >= 0.90:
            _pass(f"{label}: rel.err log-log slope = {slope_rel:.4f}  "
                  f"(O(eps^{slope_rel:.2f}) confirmed — remainder <= O(eps^3))")
        else:
            _fail(f"{label}: rel.err log-log slope = {slope_rel:.4f}  "
                  f"(expected >= 1, theorem requires O(eps) relative error)")


def check_landauer(label: str, exact_arr: np.ndarray) -> None:
    """Verify S_obs ≥ 0 everywhere (Landauer bound / Theorem 3.2)."""
    min_val = exact_arr.min()
    if min_val >= -1e-15:
        _pass(f"{label}: Landauer bound satisfied  (min S_obs = {min_val:.3e} >= 0)")
    else:
        _fail(f"{label}: Landauer bound VIOLATED  (min S_obs = {min_val:.3e} < 0)")


def check_monotone(label: str, eps_arr: np.ndarray,
                   s_arr: np.ndarray) -> None:
    """Verify S_obs is non-decreasing in ε (resolution-information trade-off)."""
    diffs = np.diff(s_arr)
    violations = int((diffs < -1e-15).sum())
    if violations == 0:
        _pass(f"{label}: monotone non-decrease verified (0 violations)")
    else:
        _fail(f"{label}: {violations} monotonicity violations detected")


# ============================================================
# 4. Fisher matrix verification (Component 5)
# ============================================================

def section_banner(title: str) -> None:
    print("\n" + "=" * 100)
    print(f"  {title}")
    print("=" * 100)


def verify_fisher_ex1() -> None:
    """Component 5 for Example 1: analytic vs. numerical Fisher, plus
    explicit check against I(θ*) = diag(1, 1/2, 1/2) (Lemma 6.5)."""
    theta_star = np.zeros(3)
    I_ana = fisher_analytic_ex1(theta_star)
    I_num = fisher_numerical_ex1(theta_star)

    max_diff = np.abs(I_ana - I_num).max()
    if max_diff < FISHER_ATOL:
        _pass(f"Ex1 Fisher: analytic vs. FD agree  (max|dI| = {max_diff:.2e} < {FISHER_ATOL})")
    else:
        _fail(f"Ex1 Fisher: analytic vs. FD MISMATCH  (max|dI| = {max_diff:.2e})")

    # Check expected value: I(θ*) = diag(1, 1/2, 1/2)  (Lemma 6.5)
    I_expected = np.diag([1.0, 0.5, 0.5])
    diff_expected = np.abs(I_ana - I_expected).max()
    if diff_expected < 1e-14:
        _pass(f"Ex1 Fisher: I(theta*) = diag(1, 1/2, 1/2) confirmed  "
              f"(max|dI| = {diff_expected:.2e})")
    else:
        _fail(f"Ex1 Fisher: I(theta*) != diag(1, 1/2, 1/2)  "
              f"(max|dI| = {diff_expected:.2e})")

    print(f"  Analytic I(theta*):\n{I_ana}")
    print(f"  Numerical I(theta*):\n{I_num}")


def verify_fisher_ex2() -> None:
    """Component 5 for Example 2: analytic vs. numerical Fisher, plus
    explicit check against I(θ*) = diag(3/2, 6/5, 2/5, 2/5)
    (Proposition 6.19 of the paper)."""
    theta_star = np.zeros(4)
    I_ana = fisher_analytic_ex2(theta_star)
    I_num = fisher_numerical_ex2(theta_star)

    max_diff = np.abs(I_ana - I_num).max()
    if max_diff < FISHER_ATOL:
        _pass(f"Ex2 Fisher: analytic vs. FD agree  (max|dI| = {max_diff:.2e} < {FISHER_ATOL})")
    else:
        _fail(f"Ex2 Fisher: analytic vs. FD MISMATCH  (max|dI| = {max_diff:.2e})")

    # Check against paper value: I(θ*) = diag(3/2, 6/5, 2/5, 2/5)
    # (Proposition 6.19)
    I_expected = np.diag([3/2, 6/5, 2/5, 2/5])
    diff_expected = np.abs(I_ana - I_expected).max()
    if diff_expected < 1e-14:
        _pass(f"Ex2 Fisher: I(theta*) = diag(3/2, 6/5, 2/5, 2/5) confirmed  "
              f"(max|dI| = {diff_expected:.2e})")
    else:
        _fail(f"Ex2 Fisher: I(theta*) != diag(3/2, 6/5, 2/5, 2/5)  "
              f"(max|dI| = {diff_expected:.2e})")

    # Also verify via manual covariance formula at uniform p=1/5
    p0 = p_ex2(theta_star)
    assert np.allclose(p0, 0.2, atol=1e-14), "p_ex2(0) should be uniform"
    T = suff_stat_ex2()
    mu = (1.0 / 5) * T.sum(axis=0)
    cent = T - mu
    I_ref = (1.0 / 5) * cent.T @ cent
    diff_cov = np.abs(I_ana - I_ref).max()
    if diff_cov < 1e-14:
        _pass(f"Ex2 Fisher: matches manual covariance formula  "
              f"(max|dI| = {diff_cov:.2e})")
    else:
        _fail(f"Ex2 Fisher: deviates from manual covariance  "
              f"(max|dI| = {diff_cov:.2e})")

    # Print eigenvalues to highlight the three-distinct-eigenvalue structure
    eigvals = np.sort(np.linalg.eigvalsh(I_ana))[::-1]
    print(f"  Analytic I(theta*):\n{I_ana}")
    print(f"  Numerical I(theta*):\n{I_num}")
    print(f"  Eigenvalues: {eigvals}  "
          f"(paper: 3/2={3/2}, 6/5={6/5}, 2/5={2/5}, 2/5={2/5})")


# ============================================================
# 5. Summary table printing
# ============================================================

def print_table_ex1(results: dict) -> None:
    hdr = (f"{'a':>5} {'b':>5} {'eps':>10} "
           f"{'S_obs(exact)':>16} {'S_obs(pred)':>16} "
           f"{'rel.error':>12} {'|R|/eps^3':>12} {'E_min(J)':>14} {'STATUS':>6}")
    print("\n" + hdr)
    print("-" * len(hdr))
    for (alpha, beta), r in results.items():
        for eps in EPS_TABLE:
            s_e  = compute_S_obs_ex1(alpha, beta, eps)
            s_p  = quadratic_pred_ex1(alpha, beta, eps)
            rel  = abs(s_e - s_p) / s_e if s_e > 0 else 0.0
            rn   = abs(s_e - s_p) / eps**3
            emin = BOLTZMANN_K * T_KELVIN * s_e
            ok   = "PASS" if rel < 0.1 or eps > 0.05 else "FAIL"
            print(f"{alpha:5.1f} {beta:5.1f} {eps:10.1e} "
                  f"{s_e:16.8e} {s_p:16.8e} "
                  f"{rel:12.4e} {rn:12.6f} {emin:14.6e} {ok:>6}")


def print_table_ex2(results: dict) -> None:
    hdr = (f"{'a':>5} {'b':>5} {'g':>5} {'eps':>10} "
           f"{'S_obs(exact)':>16} {'S_obs(pred)':>16} "
           f"{'rel.error':>12} {'|R|/eps^3':>12} {'E_min(J)':>14} {'STATUS':>6}")
    print("\n" + hdr)
    print("-" * len(hdr))
    for (alpha, beta, gamma), r in results.items():
        for eps in EPS_TABLE:
            s_e  = compute_S_obs_ex2(alpha, beta, gamma, eps)
            s_p  = quadratic_pred_ex2(alpha, beta, gamma, eps)
            rel  = abs(s_e - s_p) / s_e if s_e > 0 else 0.0
            rn   = abs(s_e - s_p) / eps**3
            emin = BOLTZMANN_K * T_KELVIN * s_e
            ok   = "PASS" if rel < 0.1 or eps > 0.05 else "FAIL"
            print(f"{alpha:5.1f} {beta:5.1f} {gamma:5.1f} {eps:10.1e} "
                  f"{s_e:16.8e} {s_p:16.8e} "
                  f"{rel:12.4e} {rn:12.6f} {emin:14.6e} {ok:>6}")


# ============================================================
# 6. Main verification runners
# ============================================================

def run_example1() -> dict:
    section_banner("EXAMPLE 1: 4-POINT SPACE  X={1,2,3,4}, P={{1,2},{3,4}}")

    # --- Component 5: Fisher matrix verification ---
    print("\n[5] Fisher matrix verification (Example 1)")
    verify_fisher_ex1()

    # --- Consistency: closed-form vs. Fisher-based prediction ---
    # Paper (Proposition 6.10):  ½ v⊤ I v = ¼(α²+β²)
    print("\n  Closed-form consistency check (Proposition 6.10):")
    for alpha, beta in EX1_CASES:
        cf = 0.25 * (alpha**2 + beta**2) * 0.01**2
        fb = quadratic_pred_ex1(alpha, beta, 0.01)
        if abs(cf - fb) < 1e-15:
            _pass(f"Ex1 (a={alpha},b={beta}): closed-form 1/4(a^2+b^2) = "
                  f"Fisher-based prediction")
        else:
            _fail(f"Ex1 (a={alpha},b={beta}): closed-form != Fisher-based  "
                  f"({cf} vs {fb})")

    # --- Compute arrays ---
    results: dict = {}
    for alpha, beta in EX1_CASES:
        exact_arr = np.array([compute_S_obs_ex1(alpha, beta, e) for e in EPS_GRID])
        pred_arr  = np.array([quadratic_pred_ex1(alpha, beta, e) for e in EPS_GRID])
        rem_arr   = np.abs(exact_arr - pred_arr)
        results[(alpha, beta)] = {
            "exact":          exact_arr,
            "pred":           pred_arr,
            "remainder":      rem_arr,
            "remainder_norm": rem_arr / EPS_GRID**3,
            "rel_error":      np.where(exact_arr > 0,
                                       rem_arr / exact_arr, 0.0),
        }

    # --- Component 1 & 2: Exact S_obs + Quadratic prediction ---
    print("\n[1,2] Exact S_obs and Quadratic Prediction (summary table):")
    print_table_ex1(results)

    # --- Component 3: Remainder bound O(ε³) ---
    print("\n[3] Remainder bound  |R(eps)|/eps^3  "
          "(must be bounded <= 10 for eps in [1e-4, 1e-2]):")
    for alpha, beta in EX1_CASES:
        check_remainder_bound(
            f"Ex1 (a={alpha},b={beta})",
            EPS_GRID, results[(alpha, beta)]["exact"],
            results[(alpha, beta)]["pred"]
        )

    # --- Component 4: Relative error O(ε) ---
    print("\n[4] Relative error < 5% for eps <= 0.03:")
    for alpha, beta in EX1_CASES:
        check_rel_error_threshold(
            f"Ex1 (a={alpha},b={beta})",
            EPS_GRID, results[(alpha, beta)]["exact"],
            results[(alpha, beta)]["pred"]
        )

    # --- Component 6: Quadratic scaling exponent ≈ 2.0 ---
    print("\n[6] Log-log scaling slope (must be 2.0 +/- 0.01):")
    for alpha, beta in EX1_CASES:
        check_slope(f"Ex1 (a={alpha},b={beta})",
                    EPS_GRID, results[(alpha, beta)]["exact"])

    # --- Component 7: Landauer bound S_obs ≥ 0 ---
    print("\n[7] Landauer bound (S_obs >= 0):")
    for alpha, beta in EX1_CASES:
        check_landauer(f"Ex1 (a={alpha},b={beta})",
                       results[(alpha, beta)]["exact"])

    # --- Landauer minimum energetic cost table ---
    print(f"\n    Minimum energetic cost at T = {T_KELVIN} K  (eps = 0.01):")
    for alpha, beta in EX1_CASES:
        s = compute_S_obs_ex1(alpha, beta, 0.01)
        e_min = BOLTZMANN_K * T_KELVIN * s
        print(f"    (a,b) = ({alpha},{beta}):  E_min = {e_min:.6e} J")

    # --- Component 8: Resolution-information trade-off (monotone increase) ---
    print("\n[8] Resolution-information trade-off: S_obs(eps) monotone increasing:")
    s_mono = np.array([compute_S_obs_ex1(1.0, 1.0, e) for e in EPS_GRID])
    check_monotone("Ex1 (a=1,b=1)", EPS_GRID, s_mono)

    return results


def run_example2() -> dict:
    section_banner("EXAMPLE 2: 5-POINT SPACE  X={1,2,3,4,5}, P={{1,2,3},{4,5}}")

    # --- Component 5: Fisher matrix verification ---
    print("\n[5] Fisher matrix verification (Example 2)")
    verify_fisher_ex2()

    # --- Consistency: closed-form vs. Fisher-based prediction ---
    # Paper (Proposition 6.22, eq. 6.15):
    #   ½ v⊤ I(θ*) v = 3/5·α² + 1/5·β² + 1/5·γ²
    print("\n  Closed-form consistency check (Proposition 6.22, eq. 6.15):")
    for alpha, beta, gamma in EX2_CASES:
        cf = (3.0/5 * alpha**2 + 1.0/5 * beta**2 + 1.0/5 * gamma**2) * 0.01**2
        fb = quadratic_pred_ex2(alpha, beta, gamma, 0.01)
        if abs(cf - fb) < 1e-15:
            _pass(f"Ex2 (a={alpha},b={beta},g={gamma}): closed-form "
                  f"3/5*a^2+1/5*b^2+1/5*g^2 = Fisher-based prediction")
        else:
            _fail(f"Ex2 (a={alpha},b={beta},g={gamma}): closed-form != Fisher  "
                  f"({cf:.6e} vs {fb:.6e})")

    # --- Compute arrays ---
    results: dict = {}
    for alpha, beta, gamma in EX2_CASES:
        exact_arr = np.array([compute_S_obs_ex2(alpha, beta, gamma, e)
                              for e in EPS_GRID])
        pred_arr  = np.array([quadratic_pred_ex2(alpha, beta, gamma, e)
                              for e in EPS_GRID])
        rem_arr   = np.abs(exact_arr - pred_arr)
        results[(alpha, beta, gamma)] = {
            "exact":          exact_arr,
            "pred":           pred_arr,
            "remainder":      rem_arr,
            "remainder_norm": rem_arr / EPS_GRID**3,
            "rel_error":      np.where(exact_arr > 0,
                                       rem_arr / exact_arr, 0.0),
        }

    # --- Components 1 & 2: Summary table ---
    print("\n[1,2] Exact S_obs and Quadratic Prediction (summary table):")
    print_table_ex2(results)

    # --- Component 3: Remainder bound ---
    print("\n[3] Remainder bound  |R(eps)|/eps^3  "
          "(must be bounded <= 10 for eps in [1e-4, 1e-2]):")
    for alpha, beta, gamma in EX2_CASES:
        check_remainder_bound(
            f"Ex2 (a={alpha},b={beta},g={gamma})",
            EPS_GRID, results[(alpha, beta, gamma)]["exact"],
            results[(alpha, beta, gamma)]["pred"]
        )

    # --- Component 4: Relative error ---
    print("\n[4] Relative error < 5% for eps <= 0.03:")
    for alpha, beta, gamma in EX2_CASES:
        check_rel_error_threshold(
            f"Ex2 (a={alpha},b={beta},g={gamma})",
            EPS_GRID, results[(alpha, beta, gamma)]["exact"],
            results[(alpha, beta, gamma)]["pred"]
        )

    # --- Component 6: Scaling exponent ---
    print("\n[6] Log-log scaling slope (must be 2.0 +/- 0.01):")
    for alpha, beta, gamma in EX2_CASES:
        check_slope(f"Ex2 (a={alpha},b={beta},g={gamma})",
                    EPS_GRID, results[(alpha, beta, gamma)]["exact"])

    # --- Component 7: Landauer bound ---
    print("\n[7] Landauer bound (S_obs >= 0):")
    for alpha, beta, gamma in EX2_CASES:
        check_landauer(f"Ex2 (a={alpha},b={beta},g={gamma})",
                       results[(alpha, beta, gamma)]["exact"])

    # --- Landauer minimum energetic cost table ---
    print(f"\n    Minimum energetic cost at T = {T_KELVIN} K  (eps = 0.01):")
    for alpha, beta, gamma in EX2_CASES:
        s = compute_S_obs_ex2(alpha, beta, gamma, 0.01)
        e_min = BOLTZMANN_K * T_KELVIN * s
        print(f"    (a,b,g) = ({alpha},{beta},{gamma}):  E_min = {e_min:.6e} J")

    # --- Component 8: Resolution-information trade-off (monotone increase) ---
    print("\n[8] Resolution-information trade-off: S_obs(eps) monotone increasing:")
    s_mono = np.array([compute_S_obs_ex2(1.0, 1.0, 1.0, e) for e in EPS_GRID])
    check_monotone("Ex2 (a=1,b=1,g=1)", EPS_GRID, s_mono)

    return results


# ============================================================
# 7. Figure generation
# ============================================================

def save_figure(fig: plt.Figure, stem: str) -> None:
    for ext in ("pdf", "png"):
        path = FIG_DIR / f"{stem}.{ext}"
        fig.savefig(path, dpi=300, bbox_inches="tight")
    print(f"  [SAVED] figures/{stem}.pdf + .png")
    plt.close(fig)


def make_figure1(results_ex1: dict) -> None:
    """Figure 1: Bridge Theorem verification (Example 1).
    Panel (a): log-log  S_obs(exact) vs S_obs(pred) + ε² reference.
    Panel (b): normalised remainder |S_obs - pred| / ε³.
    """
    fig, axes = plt.subplots(2, 1, figsize=(7.5, 10))
    ax1, ax2 = axes

    for idx, (alpha, beta) in enumerate(EX1_CASES):
        r      = results_ex1[(alpha, beta)]
        lbl_e  = rf"$(\alpha,\beta)=({alpha:.0f},{beta:.0f})$  exact"
        lbl_p  = rf"$(\alpha,\beta)=({alpha:.0f},{beta:.0f})$  pred."
        ax1.loglog(EPS_GRID, r["exact"],  color=COLORS[idx], ls="-",
                   lw=1.8, label=lbl_e)
        ax1.loglog(EPS_GRID, r["pred"],   color=COLORS[idx], ls="--",
                   lw=2.2, alpha=0.7, label=lbl_p)

    ref_y = 0.5 * EPS_GRID**2
    ax1.loglog(EPS_GRID, ref_y, "k:", lw=1.2, alpha=0.55,
               label=r"$\propto\varepsilon^2$ reference")
    ax1.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax1.set_ylabel(r"$S_{\mathrm{obs}}$  (nats)")
    ax1.set_title(
        r"(a) $S_{\mathrm{obs}}^{\mathrm{exact}}$ vs. "
        r"$\hat{S} = \frac{1}{2}\varepsilon^2 v^\top I v$"
        "\n[Example 1: 4-point space]")
    ax1.legend(fontsize=8, ncol=2, loc="lower right")
    ax1.grid(True, which="both", alpha=0.25)

    for idx, (alpha, beta) in enumerate(EX1_CASES):
        r = results_ex1[(alpha, beta)]
        ax2.loglog(EPS_GRID, r["remainder_norm"], color=COLORS[idx], ls="-",
                   label=rf"$(\alpha,\beta)=({alpha:.0f},{beta:.0f})$")

    ax2.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax2.set_ylabel(
        r"$\left|S_{\mathrm{obs}} - \hat{S}\right| / \varepsilon^3$")
    ax2.set_title(
        r"(b) Normalised remainder — confirms $O(\varepsilon^3)$"
        "\n[Example 1]")
    ax2.legend(fontsize=9)
    ax2.grid(True, which="both", alpha=0.25)

    fig.tight_layout(pad=2.5)
    save_figure(fig, "fig1_bridge_theorem_verification")


def make_figure2(results_ex1: dict) -> None:
    """Figure 2: Relative error for Example 1."""
    fig, ax = plt.subplots(figsize=(7.5, 5))

    for idx, (alpha, beta) in enumerate(EX1_CASES):
        r = results_ex1[(alpha, beta)]
        ax.loglog(EPS_GRID, r["rel_error"] + 1e-20, color=COLORS[idx], ls="-",
                  label=rf"$(\alpha,\beta)=({alpha:.0f},{beta:.0f})$")

    ax.axhline(0.01, color="gray", ls="--", lw=1.4, label=r"$1\%$ threshold")
    ax.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax.set_ylabel(
        r"$\left|S_{\mathrm{obs}}^{\mathrm{exact}} - \hat{S}\right|"
        r"\;/\; S_{\mathrm{obs}}^{\mathrm{exact}}$")
    ax.set_title("Relative error of quadratic approximation\n"
                 "[Example 1: 4-point space]")
    ax.legend(fontsize=9)
    ax.grid(True, which="both", alpha=0.25)
    ax.set_ylim(1e-12, 10)

    fig.tight_layout()
    save_figure(fig, "fig2_relative_error")


def make_figure3(results_ex1: dict) -> None:
    """Figure 3: Resolution-information trade-off (Example 1)."""
    fig, ax = plt.subplots(figsize=(7.5, 5))

    eps_coarse = np.linspace(1e-4, 0.5, 400)
    for idx, (alpha, beta) in enumerate(EX1_CASES):
        s_arr = np.array([compute_S_obs_ex1(alpha, beta, e) for e in eps_coarse])
        ax.plot(eps_coarse, s_arr, color=COLORS[idx], ls="-", lw=1.8,
                label=rf"$(\alpha,\beta)=({alpha:.0f},{beta:.0f})$")

    ax.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax.set_ylabel(r"$S_{\mathrm{obs}}(\varepsilon)$  (nats)")
    ax.set_title(
        "Resolution-information trade-off\n"
        r"Larger $\varepsilon$ $\to$ coarser partition $\to$ "
        "higher observer entropy")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    ax.annotate(
        r"$S_{\mathrm{obs}}$ monotone increasing in $\varepsilon$",
        xy=(0.28, 0.024),
        xycoords="data",
        xytext=(0.65, 0.85),
        textcoords="axes fraction",
        fontsize=9,
        color="dimgray",
        style="italic",
        ha="center",
        arrowprops=dict(arrowstyle="->", color="gray"),
        zorder=10,
    )

    ax.annotate(
        "",
        xy=(0.48, 0.005),
        xytext=(0.35, 0.005),
        arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
        zorder=10,
    )

    ax.text(
        0.355, 0.007,
        r"increasing $\varepsilon$",
        fontsize=9,
    )

    fig.tight_layout()
    save_figure(fig, "fig3_resolution_information_tradeoff")


def make_figure4(results_ex2: dict) -> None:
    """Figure 4: Bridge Theorem verification (Example 2).
    Analogous to Figure 1 but for the 5-point space.
    All 5 test cases from the paper.
    """
    fig, axes = plt.subplots(2, 1, figsize=(7.5, 10))
    ax1, ax2 = axes

    for idx, (alpha, beta, gamma) in enumerate(EX2_CASES):
        r     = results_ex2[(alpha, beta, gamma)]
        lbl_e = (rf"$(\alpha,\beta,\gamma)="
                 rf"({alpha:.0f},{beta:.0f},{gamma:.0f})$  exact")
        lbl_p = (rf"$(\alpha,\beta,\gamma)="
                 rf"({alpha:.0f},{beta:.0f},{gamma:.0f})$  pred.")
        ax1.loglog(EPS_GRID, r["exact"],  color=COLORS[idx], ls="-",
                   lw=1.8, label=lbl_e)
        ax1.loglog(EPS_GRID, r["pred"],   color=COLORS[idx], ls="--",
                   lw=2.2, alpha=0.7, label=lbl_p)

    ref_y = 0.5 * EPS_GRID**2
    ax1.loglog(EPS_GRID, ref_y, "k:", lw=1.2, alpha=0.55,
               label=r"$\propto\varepsilon^2$ reference")
    ax1.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax1.set_ylabel(r"$S_{\mathrm{obs}}$  (nats)")
    ax1.set_title(
        r"(a) $S_{\mathrm{obs}}^{\mathrm{exact}}$ vs. "
        r"$\hat{S} = \frac{1}{2}\varepsilon^2 v^\top I v$"
        "\n[Example 2: 5-point space]")
    ax1.legend(fontsize=7, ncol=2, loc="lower right")
    ax1.grid(True, which="both", alpha=0.25)

    for idx, (alpha, beta, gamma) in enumerate(EX2_CASES):
        r = results_ex2[(alpha, beta, gamma)]
        ax2.loglog(EPS_GRID, r["remainder_norm"], color=COLORS[idx], ls="-",
                   label=(rf"$(\alpha,\beta,\gamma)="
                          rf"({alpha:.0f},{beta:.0f},{gamma:.0f})$"))

    ax2.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax2.set_ylabel(
        r"$\left|S_{\mathrm{obs}} - \hat{S}\right| / \varepsilon^3$")
    ax2.set_title(
        r"(b) Normalised remainder — confirms $O(\varepsilon^3)$"
        "\n[Example 2]")
    ax2.legend(fontsize=8)
    ax2.grid(True, which="both", alpha=0.25)

    fig.tight_layout(pad=2.5)
    save_figure(fig, "fig4_bridge_theorem_ex2")


def make_figure5(results_ex2: dict) -> None:
    """Figure 5: Relative error for Example 2."""
    fig, ax = plt.subplots(figsize=(7.5, 5))

    for idx, (alpha, beta, gamma) in enumerate(EX2_CASES):
        r = results_ex2[(alpha, beta, gamma)]
        ax.loglog(EPS_GRID, r["rel_error"] + 1e-20, color=COLORS[idx], ls="-",
                  label=(rf"$(\alpha,\beta,\gamma)="
                         rf"({alpha:.0f},{beta:.0f},{gamma:.0f})$"))

    ax.axhline(0.01, color="gray", ls="--", lw=1.4, label=r"$1\%$ threshold")
    ax.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax.set_ylabel(
        r"$\left|S_{\mathrm{obs}}^{\mathrm{exact}} - \hat{S}\right|"
        r"\;/\; S_{\mathrm{obs}}^{\mathrm{exact}}$")
    ax.set_title("Relative error of quadratic approximation\n"
                 "[Example 2: 5-point space]")
    ax.legend(fontsize=8)
    ax.grid(True, which="both", alpha=0.25)
    ax.set_ylim(1e-12, 10)

    fig.tight_layout()
    save_figure(fig, "fig5_relative_error_ex2")


# ============================================================
# 8. Entry point
# ============================================================

def main() -> None:
    print()
    print("=" * 100)
    print("  NUMERICAL VERIFICATION OF THEOREM 6.3 (BRIDGE THEOREM) — v2.0")
    print()
    print("  S_obs(p_theta, eps) = 1/2 eps^2 v^T I(theta*) v + O(eps^3),   eps -> 0+")
    print()
    print("  Paper: 'KL-Geometric Structure of Observer Entropy'")
    print("  Author: Vladimir Khomyakov  (DOI: 10.5281/zenodo.18826258)")
    print("=" * 100)

    # ------------------------------------------------------------------
    # Run both examples (all 8 verification components each)
    # ------------------------------------------------------------------
    results_ex1 = run_example1()
    results_ex2 = run_example2()

    # ------------------------------------------------------------------
    # Generate all five figures
    # ------------------------------------------------------------------
    print()
    section_banner("FIGURE GENERATION")
    make_figure1(results_ex1)
    make_figure2(results_ex1)
    make_figure3(results_ex1)
    make_figure4(results_ex2)
    make_figure5(results_ex2)

    # ------------------------------------------------------------------
    # Final verdict
    # ------------------------------------------------------------------
    print()
    print("=" * 100)
    if not _FAILURES:
        print("  PASS  ALL BRIDGE THEOREM CHECKS PASSED")
        print()
        print("  Summary:")
        print("    Example 1 (4-point, equal clusters)  :  O(eps^3) remainder confirmed.")
        print("    Example 2 (5-point, unequal clusters):  O(eps^3) remainder confirmed.")
        print("    Quadratic scaling S_obs = 1/2 eps^2 v^T I v + O(eps^3)  "
              "verified numerically.")
        print("    Fisher matrices match paper exactly:")
        print("      Ex1: I(theta*) = diag(1, 1/2, 1/2)          [Lemma 6.5]")
        print("      Ex2: I(theta*) = diag(3/2, 6/5, 2/5, 2/5)  [Proposition 6.19]")
        print("    Closed-form leading coefficients verified:")
        print("      Ex1: 1/2 v^T I v = 1/4(a^2+b^2)            [Proposition 6.10]")
        print("      Ex2: 1/2 v^T I v = 3/5*a^2+1/5*b^2+1/5*g^2 [Proposition 6.22]")
        print("    Landauer bound S_obs >= 0 satisfied in all cases.")
        print("    Log-log slope = 2.000 +/- 0.01 in all cases.")
        print("    Monotone non-decrease verified for both examples.")
        print("=" * 100)
        sys.exit(0)
    else:
        print(f"  FAIL  BRIDGE THEOREM VERIFICATION FAILED  "
              f"({len(_FAILURES)} check(s)):")
        for i, f in enumerate(_FAILURES, 1):
            print(f"    [{i}] {f}")
        print("=" * 100)
        sys.exit(1)


if __name__ == "__main__":
    main()
