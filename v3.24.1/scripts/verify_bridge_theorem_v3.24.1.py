#!/usr/bin/env python3
"""
verify_bridge_theorem_v3.24.1.py

Numerical verification of the Bridge Theorem (Theorem 6.7) and
Section 11 (Fibre-Theoretic Foundation) from the manuscript:

    "KL-Geometric Structure of Observer Entropy:
     A Minimal Information-Theoretic Framework"
    Vladimir Khomyakov, v3.24.1

Manuscript figures (primary outputs):
  fig1_bridge_theorem_verification.pdf   -- Ex1 dual panel
  fig2_relative_error.pdf                -- Ex1 relative error
  fig3_resolution_information_tradeoff.pdf -- Ex1 tradeoff (linear)
  fig4_bridge_theorem_ex2.pdf            -- Ex2 dual panel
  fig5_relative_error_ex2.pdf            -- Ex2 relative error
  fig6_offcenter_ex1.pdf                 -- Ex1 off-center dual panel
  fig7_offcenter_ex2.pdf                 -- Ex2 off-center dual panel

Supplementary diagnostic figures:
  fig_supp_fisher_eigenvalues.pdf
  fig_supp_landauer_budget.pdf
  fig_supp_fibre_identity.pdf

Verification components:
  T1-T8   Bridge Theorem checks (Ex1, Ex2): Fisher, slope, remainder,
          relative-error threshold, Landauer bound, monotonicity.
  T9      Off-center robustness checks (12 random base points total).
  T11.1-T11.6 Fibre-theoretic identity, push-pull idempotence,
          balanced/unbalanced closed-form S_obs^fib = log N - H_w.

Author: Vladimir Khomyakov
"""

import sys
import os
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

# === === === ===
# 0. Global settings & constants
# === === === ===

BOLTZMANN_K = 1.380649e-23   # J / K  (exact, SI 2019)
T_KELVIN    = 300.0           # Kelvin

EPS_GRID   = np.logspace(-4, -1, 200)
EPS_TABLE  = np.array([1e-4, 1e-3, 1e-2, 1e-1])

FD_STEP    = 1e-5

FISHER_ATOL      = 1e-8
SLOPE_TOL        = 0.01
REMAINDER_BOUND  = 10.0
REL_ERR_EPS_MAX  = 0.03

OFFCENTER_SEED   = 42
OFFCENTER_N_EX1  = 6
OFFCENTER_N_EX2  = 6
OFFCENTER_THETA1_RANGE = (-0.8, 0.8)
OFFCENTER_ALPHA_SCALE  = 1.0

# Repository paths
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR
FIG_DIR = REPO_ROOT / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

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

COLORS = ["#2060c0", "#c03020", "#209040", "#9040b0", "#d07010",
          "#008080", "#b05000"]
STYLES = ["-", "--", "-.", ":", (0, (3, 1, 1, 1))]

_FAILURES: list = []


def _pass(msg: str) -> None:
    print(f"  [PASS] {msg}")


def _fail(msg: str) -> None:
    print(f"  [FAIL] {msg}")
    _FAILURES.append(msg)


def section_banner(title: str) -> None:
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def _save_figure(fig, stem: str) -> None:
    for ext in ("pdf", "png"):
        path = FIG_DIR / f"{stem}.{ext}"
        fig.savefig(path, dpi=300, bbox_inches="tight")
    print(f"  [SAVED] figures/{stem}.pdf + .png")
    plt.close(fig)


# === === === ===
# 1. Example 1: 4-point space  X={1,2,3,4}, P={{1,2},{3,4}}
# === === === ===

EX1_CASES = [(1.0, 0.0), (0.0, 1.0), (1.0, 1.0), (3.0, 2.0)]
EX1_CLASSES = [[0, 1], [2, 3]]


def eta_ex1(theta):
    t1, t2, t3 = theta
    return np.array([t1 + t2, t1 - t2, -t1 + t3, -t1 - t3])


def p_ex1(theta):
    eta = eta_ex1(theta)
    eta = eta - eta.max()
    e = np.exp(eta)
    return e / e.sum()


def uniform_lift_ex1(p):
    piA = p[0] + p[1]
    piB = p[2] + p[3]
    return np.array([piA / 2, piA / 2, piB / 2, piB / 2])


def S_obs_ex1(p):
    q = uniform_lift_ex1(p)
    return float(np.sum(p * np.log(p / q)))


def compute_S_obs_ex1(alpha, beta, eps, theta1=0.0):
    theta = np.array([theta1, eps * alpha, eps * beta])
    return S_obs_ex1(p_ex1(theta))


def suff_stat_ex1():
    return np.array([
        [ 1,  1,  0],
        [ 1, -1,  0],
        [-1,  0,  1],
        [-1,  0, -1],
    ], dtype=float)


def fisher_analytic_ex1(theta):
    p = p_ex1(theta)
    T = suff_stat_ex1()
    mu = p @ T
    centered = T - mu[np.newaxis, :]
    return (p[:, np.newaxis] * centered).T @ centered


def fisher_numerical_ex1(theta, h=FD_STEP):
    d = len(theta)
    I = np.zeros((d, d))
    p_th = p_ex1(theta)
    scores = np.zeros((d, len(p_th)))
    for i in range(d):
        ei = np.zeros(d); ei[i] = 1.0
        log_p_plus  = np.log(p_ex1(theta + h * ei) + 1e-300)
        log_p_minus = np.log(p_ex1(theta - h * ei) + 1e-300)
        scores[i] = (log_p_plus - log_p_minus) / (2 * h)
    for i in range(d):
        for j in range(d):
            I[i, j] = np.sum(p_th * scores[i] * scores[j])
    return I


def quadratic_pred_ex1(alpha, beta, eps, theta_star=None):
    if theta_star is None:
        theta_star = np.zeros(3)
    v = np.array([0.0, -alpha, -beta])
    I = fisher_analytic_ex1(theta_star)
    return 0.5 * eps**2 * float(v @ I @ v)


# === === === ===
# 2. Example 2: 5-point space  X={1,2,3,4,5}, P={{1,2,3},{4,5}}
# === === === ===

EX2_CASES = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0),
             (1.0, 1.0, 1.0), (2.0, 1.0, 3.0)]
EX2_CLASSES = [[0, 1, 2], [3, 4]]


def eta_ex2(theta):
    t1, t2, t3, t4 = theta
    return np.array([
        t1 + t2 + t3,
        t1 + t2 - t3,
        t1 - 2.0 * t2,
        -1.5 * t1 + t4,
        -1.5 * t1 - t4,
    ])


def p_ex2(theta):
    eta = eta_ex2(theta)
    eta = eta - eta.max()
    e = np.exp(eta)
    return e / e.sum()


def uniform_lift_ex2(p):
    piA = p[0] + p[1] + p[2]
    piB = p[3] + p[4]
    return np.array([piA / 3, piA / 3, piA / 3, piB / 2, piB / 2])


def S_obs_ex2(p):
    q = uniform_lift_ex2(p)
    return float(np.sum(p * np.log(p / q)))


def compute_S_obs_ex2(alpha, beta, gamma, eps, theta1=0.0):
    theta = np.array([theta1, eps * alpha, eps * beta, eps * gamma])
    return S_obs_ex2(p_ex2(theta))


def suff_stat_ex2():
    return np.array([
        [ 1.0,   1.0,  1.0,  0.0],
        [ 1.0,   1.0, -1.0,  0.0],
        [ 1.0,  -2.0,  0.0,  0.0],
        [-1.5,   0.0,  0.0,  1.0],
        [-1.5,   0.0,  0.0, -1.0],
    ], dtype=float)


def fisher_analytic_ex2(theta):
    p = p_ex2(theta)
    T = suff_stat_ex2()
    mu = p @ T
    centered = T - mu[np.newaxis, :]
    return (p[:, np.newaxis] * centered).T @ centered


def fisher_numerical_ex2(theta, h=FD_STEP):
    d = len(theta)
    I = np.zeros((d, d))
    p_th = p_ex2(theta)
    scores = np.zeros((d, len(p_th)))
    for i in range(d):
        ei = np.zeros(d); ei[i] = 1.0
        log_p_plus  = np.log(p_ex2(theta + h * ei) + 1e-300)
        log_p_minus = np.log(p_ex2(theta - h * ei) + 1e-300)
        scores[i] = (log_p_plus - log_p_minus) / (2 * h)
    for i in range(d):
        for j in range(d):
            I[i, j] = np.sum(p_th * scores[i] * scores[j])
    return I


def quadratic_pred_ex2(alpha, beta, gamma, eps, theta_star=None):
    if theta_star is None:
        theta_star = np.zeros(4)
    v = np.array([0.0, -alpha, -beta, -gamma])
    I = fisher_analytic_ex2(theta_star)
    return 0.5 * eps**2 * float(v @ I @ v)


# === === === ===
# 3. Verification helpers
# === === === ===

def loglog_slope(eps_arr, y_arr):
    """Fit log-log linear regression slope over range ε ∈ [1e-4, 1e-1]."""
    mask = (eps_arr >= 1e-4) & (eps_arr <= 1e-1) & (y_arr > 0)
    log_eps = np.log10(eps_arr[mask])
    log_y = np.log10(y_arr[mask])
    slope, _, _, _, _ = stats.linregress(log_eps, log_y)
    return slope


def check_slope(label, eps_arr, exact_arr):
    slope = loglog_slope(eps_arr, exact_arr)
    err = abs(slope - 2.0)
    if err < SLOPE_TOL:
        _pass(f"{label}: log-log slope = {slope:.6f}  (|slope-2| = {err:.2e} < {SLOPE_TOL})")
    else:
        _fail(f"{label}: log-log slope = {slope:.6f}  (|slope-2| = {err:.2e} >= {SLOPE_TOL})")
    return slope


def check_remainder_bound(label, eps_arr, exact_arr, pred_arr):
    mask = (eps_arr >= 1e-4) & (eps_arr <= 1e-2)
    rem_norm = np.abs(exact_arr[mask] - pred_arr[mask]) / eps_arr[mask]**3
    sup_val = rem_norm.max()
    if sup_val < REMAINDER_BOUND:
        _pass(f"{label}: sup|R|/eps^3 = {sup_val:.6f}  (< {REMAINDER_BOUND})")
    else:
        _fail(f"{label}: sup|R|/eps^3 = {sup_val:.6f}  (>= {REMAINDER_BOUND})")
    return sup_val


def check_rel_error_threshold(label, eps_arr, exact_arr, pred_arr):
    rel_full = np.where(exact_arr > 0,
                        np.abs(exact_arr - pred_arr) / exact_arr, 1e-300)
    C = 0.8
    mask = eps_arr <= REL_ERR_EPS_MAX
    violations = int((rel_full[mask] > C * eps_arr[mask]).sum())
    if violations == 0:
        max_ratio = (rel_full[mask] / np.maximum(eps_arr[mask], 1e-300)).max()
        _pass(f"{label}: rel.err <= {C}*eps verified for eps<={REL_ERR_EPS_MAX}  "
              f"(observed C_* = {max_ratio:.4f} <= {C})")
    else:
        _fail(f"{label}: rel.err > {C}*eps in {violations} points "
              f"for eps<={REL_ERR_EPS_MAX}")

    valid = (eps_arr >= 1e-3) & (eps_arr <= 1e-1) & (rel_full > 1e-20)
    if valid.sum() > 5:
        slope_rel, _, _, _, _ = stats.linregress(
            np.log10(eps_arr[valid]), np.log10(rel_full[valid]))
        if slope_rel >= 0.90:
            _pass(f"{label}: rel.err log-log slope = {slope_rel:.4f}  "
                  f"(O(eps^{slope_rel:.2f}) confirmed)")
        else:
            _fail(f"{label}: rel.err log-log slope = {slope_rel:.4f}  "
                  f"(expected >= 1)")


def check_landauer(label, exact_arr):
    min_val = exact_arr.min()
    if min_val >= -1e-15:
        _pass(f"{label}: Landauer bound satisfied  (min S_obs = {min_val:.3e} >= 0)")
    else:
        _fail(f"{label}: Landauer bound VIOLATED  (min S_obs = {min_val:.3e} < 0)")


def check_monotone(label, eps_arr, s_arr):
    diffs = np.diff(s_arr)
    violations = int((diffs < -1e-15).sum())
    if violations == 0:
        _pass(f"{label}: monotone non-decrease verified (0 violations)")
    else:
        _fail(f"{label}: {violations} monotonicity violations detected")


# === === === ===
# 4. Fisher matrix verification
# === === === ===

def verify_fisher_ex1():
    theta_star = np.zeros(3)
    I_ana = fisher_analytic_ex1(theta_star)
    I_num = fisher_numerical_ex1(theta_star)

    max_diff = np.abs(I_ana - I_num).max()
    if max_diff < FISHER_ATOL:
        _pass(f"Ex1 Fisher: analytic vs. FD agree  (max|dI| = {max_diff:.2e} < {FISHER_ATOL})")
    else:
        _fail(f"Ex1 Fisher: analytic vs. FD MISMATCH  (max|dI| = {max_diff:.2e})")

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


def verify_fisher_ex2():
    theta_star = np.zeros(4)
    I_ana = fisher_analytic_ex2(theta_star)
    I_num = fisher_numerical_ex2(theta_star)

    max_diff = np.abs(I_ana - I_num).max()
    if max_diff < FISHER_ATOL:
        _pass(f"Ex2 Fisher: analytic vs. FD agree  (max|dI| = {max_diff:.2e} < {FISHER_ATOL})")
    else:
        _fail(f"Ex2 Fisher: analytic vs. FD MISMATCH  (max|dI| = {max_diff:.2e})")

    I_expected = np.diag([3/2, 6/5, 2/5, 2/5])
    diff_expected = np.abs(I_ana - I_expected).max()
    if diff_expected < 1e-14:
        _pass(f"Ex2 Fisher: I(theta*) = diag(3/2, 6/5, 2/5, 2/5) confirmed  "
              f"(max|dI| = {diff_expected:.2e})")
    else:
        _fail(f"Ex2 Fisher: I(theta*) != diag(3/2, 6/5, 2/5, 2/5)  "
              f"(max|dI| = {diff_expected:.2e})")

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

    eigvals = np.sort(np.linalg.eigvalsh(I_ana))[::-1]
    print(f"  Analytic I(theta*):\n{I_ana}")
    print(f"  Numerical I(theta*):\n{I_num}")
    print(f"  Eigenvalues: {eigvals}  "
          f"(paper: 3/2={3/2}, 6/5={6/5}, 2/5={2/5}, 2/5={2/5})")


# === === === ===
# 5. Summary table printing
# === === === ===

def print_table_ex1(results):
    hdr = (f"{'a':>5} {'b':>5} {'eps':>10} "
           f"{'S_obs(exact)':>16} {'S_obs(pred)':>16} "
           f"{'rel.error':>12} {'|R|/eps^3':>12} {'E_min(J)':>14} {'STATUS':>6}")
    print("\n" + hdr)
    print("-" * len(hdr))
    for (alpha, beta), r in results.items():
        for eps in EPS_TABLE:
            s_e = compute_S_obs_ex1(alpha, beta, eps)
            s_p = quadratic_pred_ex1(alpha, beta, eps)
            rel = abs(s_e - s_p) / s_e if s_e > 0 else 0.0
            rn = abs(s_e - s_p) / eps**3
            emin = BOLTZMANN_K * T_KELVIN * s_e
            ok = "PASS" if rel < 0.1 or eps > 0.05 else "FAIL"
            print(f"{alpha:5.1f} {beta:5.1f} {eps:10.1e} "
                  f"{s_e:16.8e} {s_p:16.8e} "
                  f"{rel:12.4e} {rn:12.6f} {emin:14.6e} {ok:>6}")


def print_table_ex2(results):
    hdr = (f"{'a':>5} {'b':>5} {'g':>5} {'eps':>10} "
           f"{'S_obs(exact)':>16} {'S_obs(pred)':>16} "
           f"{'rel.error':>12} {'|R|/eps^3':>12} {'E_min(J)':>14} {'STATUS':>6}")
    print("\n" + hdr)
    print("-" * len(hdr))
    for (alpha, beta, gamma), r in results.items():
        for eps in EPS_TABLE:
            s_e = compute_S_obs_ex2(alpha, beta, gamma, eps)
            s_p = quadratic_pred_ex2(alpha, beta, gamma, eps)
            rel = abs(s_e - s_p) / s_e if s_e > 0 else 0.0
            rn = abs(s_e - s_p) / eps**3
            emin = BOLTZMANN_K * T_KELVIN * s_e
            ok = "PASS" if rel < 0.1 or eps > 0.05 else "FAIL"
            print(f"{alpha:5.1f} {beta:5.1f} {gamma:5.1f} {eps:10.1e} "
                  f"{s_e:16.8e} {s_p:16.8e} "
                  f"{rel:12.4e} {rn:12.6f} {emin:14.6e} {ok:>6}")


# === === === ===
# 6. Main verification runners (T1-T8)
# === === === ===

def run_example1():
    section_banner("EXAMPLE 1: 4-POINT SPACE  X={1,2,3,4}, P={{1,2},{3,4}}")

    print("\n[T5] Fisher matrix verification (Example 1)")
    verify_fisher_ex1()

    print("\n  Closed-form consistency check (Proposition 6.24):")
    for alpha, beta in EX1_CASES:
        cf = 0.25 * (alpha**2 + beta**2) * 0.01**2
        fb = quadratic_pred_ex1(alpha, beta, 0.01)
        if abs(cf - fb) < 1e-15:
            _pass(f"Ex1 (a={alpha},b={beta}): closed-form 1/4(a^2+b^2) = Fisher prediction")
        else:
            _fail(f"Ex1 (a={alpha},b={beta}): closed-form != Fisher  ({cf} vs {fb})")

    results = {}
    for alpha, beta in EX1_CASES:
        exact_arr = np.array([compute_S_obs_ex1(alpha, beta, e) for e in EPS_GRID])
        pred_arr = np.array([quadratic_pred_ex1(alpha, beta, e) for e in EPS_GRID])
        rem_arr = np.abs(exact_arr - pred_arr)
        results[(alpha, beta)] = {
            "exact": exact_arr,
            "pred": pred_arr,
            "remainder": rem_arr,
            "remainder_norm": rem_arr / EPS_GRID**3,
            "rel_error": np.where(exact_arr > 0, rem_arr / exact_arr, 0.0),
        }

    print("\n[T1,T2] Exact S_obs and Quadratic Prediction (summary table):")
    print_table_ex1(results)

    print("\n[T3] Remainder bound  |R(eps)|/eps^3  (must be <= 10 for eps in [1e-4, 1e-2]):")
    for alpha, beta in EX1_CASES:
        check_remainder_bound(
            f"Ex1 (a={alpha},b={beta})",
            EPS_GRID, results[(alpha, beta)]["exact"],
            results[(alpha, beta)]["pred"])

    print("\n[T4] Relative error criterion: rel.err(eps) <= 0.8*eps for eps <= 0.03:")
    for alpha, beta in EX1_CASES:
        check_rel_error_threshold(
            f"Ex1 (a={alpha},b={beta})",
            EPS_GRID, results[(alpha, beta)]["exact"],
            results[(alpha, beta)]["pred"])

    print("\n[T6] Log-log scaling slope (must be 2.0 +/- 0.01):")
    for alpha, beta in EX1_CASES:
        check_slope(f"Ex1 (a={alpha},b={beta})",
                    EPS_GRID, results[(alpha, beta)]["exact"])

    print("\n[T7] Landauer bound (S_obs >= 0):")
    for alpha, beta in EX1_CASES:
        check_landauer(f"Ex1 (a={alpha},b={beta})",
                       results[(alpha, beta)]["exact"])

    print(f"\n    Minimum energetic cost at T = {T_KELVIN} K  (eps = 0.01):")
    for alpha, beta in EX1_CASES:
        s = compute_S_obs_ex1(alpha, beta, 0.01)
        e_min = BOLTZMANN_K * T_KELVIN * s
        print(f"    (a,b) = ({alpha},{beta}):  E_min = {e_min:.6e} J")

    print("\n[T8] Resolution-information trade-off: S_obs(eps) monotone increasing:")
    s_mono = np.array([compute_S_obs_ex1(1.0, 1.0, e) for e in EPS_GRID])
    check_monotone("Ex1 (a=1,b=1)", EPS_GRID, s_mono)

    return results


def run_example2():
    section_banner("EXAMPLE 2: 5-POINT SPACE  X={1,2,3,4,5}, P={{1,2,3},{4,5}}")

    print("\n[T5] Fisher matrix verification (Example 2)")
    verify_fisher_ex2()

    print("\n  Closed-form consistency check (Proposition 6.38, eq. (13)):")
    for alpha, beta, gamma in EX2_CASES:
        cf = (3.0/5 * alpha**2 + 1.0/5 * beta**2 + 1.0/5 * gamma**2) * 0.01**2
        fb = quadratic_pred_ex2(alpha, beta, gamma, 0.01)
        if abs(cf - fb) < 1e-15:
            _pass(f"Ex2 (a={alpha},b={beta},g={gamma}): closed-form = Fisher prediction")
        else:
            _fail(f"Ex2 (a={alpha},b={beta},g={gamma}): closed-form != Fisher  "
                  f"({cf:.6e} vs {fb:.6e})")

    results = {}
    for alpha, beta, gamma in EX2_CASES:
        exact_arr = np.array([compute_S_obs_ex2(alpha, beta, gamma, e) for e in EPS_GRID])
        pred_arr = np.array([quadratic_pred_ex2(alpha, beta, gamma, e) for e in EPS_GRID])
        rem_arr = np.abs(exact_arr - pred_arr)
        results[(alpha, beta, gamma)] = {
            "exact": exact_arr,
            "pred": pred_arr,
            "remainder": rem_arr,
            "remainder_norm": rem_arr / EPS_GRID**3,
            "rel_error": np.where(exact_arr > 0, rem_arr / exact_arr, 0.0),
        }

    print("\n[T1,T2] Exact S_obs and Quadratic Prediction (summary table):")
    print_table_ex2(results)

    print("\n[T3] Remainder bound  |R(eps)|/eps^3  (must be <= 10 for eps in [1e-4, 1e-2]):")
    for alpha, beta, gamma in EX2_CASES:
        check_remainder_bound(
            f"Ex2 (a={alpha},b={beta},g={gamma})",
            EPS_GRID, results[(alpha, beta, gamma)]["exact"],
            results[(alpha, beta, gamma)]["pred"])

    print("\n[T4] Relative error criterion: rel.err(eps) <= 0.8*eps for eps <= 0.03:")
    for alpha, beta, gamma in EX2_CASES:
        check_rel_error_threshold(
            f"Ex2 (a={alpha},b={beta},g={gamma})",
            EPS_GRID, results[(alpha, beta, gamma)]["exact"],
            results[(alpha, beta, gamma)]["pred"])

    print("\n[T6] Log-log scaling slope (must be 2.0 +/- 0.01):")
    for alpha, beta, gamma in EX2_CASES:
        check_slope(f"Ex2 (a={alpha},b={beta},g={gamma})",
                    EPS_GRID, results[(alpha, beta, gamma)]["exact"])

    print("\n[T7] Landauer bound (S_obs >= 0):")
    for alpha, beta, gamma in EX2_CASES:
        check_landauer(f"Ex2 (a={alpha},b={beta},g={gamma})",
                       results[(alpha, beta, gamma)]["exact"])

    print(f"\n    Minimum energetic cost at T = {T_KELVIN} K  (eps = 0.01):")
    for alpha, beta, gamma in EX2_CASES:
        s = compute_S_obs_ex2(alpha, beta, gamma, 0.01)
        e_min = BOLTZMANN_K * T_KELVIN * s
        print(f"    (a,b,g) = ({alpha},{beta},{gamma}):  E_min = {e_min:.6e} J")

    print("\n[T8] Resolution-information trade-off: S_obs(eps) monotone increasing:")
    s_mono = np.array([compute_S_obs_ex2(1.0, 1.0, 1.0, e) for e in EPS_GRID])
    check_monotone("Ex2 (a=1,b=1,g=1)", EPS_GRID, s_mono)

    return results


# === === === ===
# 7. Off-center robustness checks (T9)
# === === === ===

def _random_alpha(d_within, rng, scale=OFFCENTER_ALPHA_SCALE):
    v = rng.standard_normal(d_within)
    return scale * v / np.linalg.norm(v)


def run_offcenter_checks():
    section_banner(
        "SECTION 9 (T9): OFF-CENTER BASE POINTS & RANDOM DIRECTIONS\n"
        "  Confirms Theorem 6.7 holds for theta* != 0  (locality check)"
    )

    rng = np.random.default_rng(OFFCENTER_SEED)
    lo, hi = OFFCENTER_THETA1_RANGE

    print(f"\n[T9.1] Example 1: {OFFCENTER_N_EX1} random (theta_1*, alpha, beta) pairs")
    print("       theta(eps) = (theta_1*, eps*alpha, eps*beta),  v = (0, -alpha, -beta)")

    ex1_offcenter_data = []
    for k in range(OFFCENTER_N_EX1):
        theta1_star = float(rng.uniform(lo, hi))
        alpha_raw = _random_alpha(2, rng)
        alpha, beta = float(alpha_raw[0]), float(alpha_raw[1])
        theta_star = np.array([theta1_star, 0.0, 0.0])

        exact_arr = np.array([
            compute_S_obs_ex1(alpha, beta, e, theta1=theta1_star)
            for e in EPS_GRID])
        pred_arr = np.array([
            quadratic_pred_ex1(alpha, beta, e, theta_star=theta_star)
            for e in EPS_GRID])

        label = (f"Ex1-OC#{k+1}  theta_1*={theta1_star:+.3f}  "
                 f"alpha={alpha:+.3f}  beta={beta:+.3f}")
        check_slope(label, EPS_GRID, exact_arr)
        check_remainder_bound(label, EPS_GRID, exact_arr, pred_arr)

        ex1_offcenter_data.append({
            "label": label, "theta1": theta1_star,
            "alpha": alpha, "beta": beta,
            "exact": exact_arr, "pred": pred_arr,
            "rem_norm": np.abs(exact_arr - pred_arr) / EPS_GRID**3,
        })

    print(f"\n[T9.2] Example 2: {OFFCENTER_N_EX2} random (theta_1*, alpha, beta, gamma) pairs")
    print("       theta(eps) = (theta_1*, eps*alpha, eps*beta, eps*gamma)")

    ex2_offcenter_data = []
    for k in range(OFFCENTER_N_EX2):
        theta1_star = float(rng.uniform(lo, hi))
        alpha_raw = _random_alpha(3, rng)
        alpha, beta, gamma = (float(alpha_raw[0]), float(alpha_raw[1]),
                              float(alpha_raw[2]))
        theta_star = np.array([theta1_star, 0.0, 0.0, 0.0])

        exact_arr = np.array([
            compute_S_obs_ex2(alpha, beta, gamma, e, theta1=theta1_star)
            for e in EPS_GRID])
        pred_arr = np.array([
            quadratic_pred_ex2(alpha, beta, gamma, e, theta_star=theta_star)
            for e in EPS_GRID])

        label = (f"Ex2-OC#{k+1}  theta_1*={theta1_star:+.3f}  "
                 f"alpha={alpha:+.3f}  beta={beta:+.3f}  gamma={gamma:+.3f}")
        check_slope(label, EPS_GRID, exact_arr)
        check_remainder_bound(label, EPS_GRID, exact_arr, pred_arr)

        ex2_offcenter_data.append({
            "label": label, "theta1": theta1_star,
            "alpha": alpha, "beta": beta, "gamma": gamma,
            "exact": exact_arr, "pred": pred_arr,
            "rem_norm": np.abs(exact_arr - pred_arr) / EPS_GRID**3,
        })

    return ex1_offcenter_data, ex2_offcenter_data


# === === === ===
# 8. Section 11 — Fibre-Theoretic Foundation
# === === === ===

def shannon_entropy(p):
    """Shannon entropy in nats (with 0*log(0) = 0 convention)."""
    p = np.asarray(p, dtype=float)
    p = p[p > 1e-300]
    return float(-np.sum(p * np.log(p)))


def push_balanced(mu, N, n):
    """Pushforward pi_*: balanced fibres of size N over n classes."""
    mu = np.asarray(mu, dtype=float).reshape(n, N)
    return mu.sum(axis=1)


def pull_balanced(q, N):
    """Uniform pullback pi^*: q (length n) -> mu (length n*N)."""
    q = np.asarray(q, dtype=float)
    return np.repeat(q / N, N)


def push_unbalanced(mu, fibre_sizes):
    """Pushforward for unbalanced fibres."""
    mu = np.asarray(mu, dtype=float)
    n = len(fibre_sizes)
    out = np.zeros(n)
    idx = 0
    for x, Nx in enumerate(fibre_sizes):
        out[x] = mu[idx:idx + Nx].sum()
        idx += Nx
    return out


def pull_unbalanced(q, fibre_sizes):
    """Uniform pullback for unbalanced fibres."""
    q = np.asarray(q, dtype=float)
    parts = [np.full(Nx, q[x] / Nx) for x, Nx in enumerate(fibre_sizes)]
    return np.concatenate(parts)


def Sobs_fib_direct(mu, pi_star_pi_star_mu):
    """Direct KL(mu || pi^* pi_* mu)."""
    mu = np.asarray(mu, dtype=float)
    q = np.asarray(pi_star_pi_star_mu, dtype=float)
    mask = mu > 1e-300
    return float(np.sum(mu[mask] * np.log(mu[mask] / q[mask])))


def Sobs_fib_closed_balanced(mu, N, n):
    """Closed form: log N - H_w(mu) for balanced fibres."""
    mu = np.asarray(mu, dtype=float).reshape(n, N)
    p = mu.sum(axis=1)
    Hw = 0.0
    for x in range(n):
        if p[x] > 1e-300:
            nu_x = mu[x] / p[x]
            Hw += p[x] * shannon_entropy(nu_x)
    return float(np.log(N) - Hw)


def Sobs_fib_closed_unbalanced(mu, fibre_sizes):
    """Closed form for unbalanced fibres: E_x[log N_x - H(nu_x)]."""
    mu = np.asarray(mu, dtype=float)
    n = len(fibre_sizes)
    val = 0.0
    idx = 0
    for x, Nx in enumerate(fibre_sizes):
        block = mu[idx:idx + Nx]
        px = block.sum()
        if px > 1e-300:
            nu_x = block / px
            val += px * (np.log(Nx) - shannon_entropy(nu_x))
        idx += Nx
    return float(val)


def run_section11_fibre():
    section_banner("SECTION 11: FIBRE-THEORETIC FOUNDATION")

    rng = np.random.default_rng(42)
    test_results = []

    # T11.1: Push-pull left inverse pi_* o pi^* = id
    print("\n[T11.1] Push-pull identity:  pi_* o pi^* = id_{P(X)}")
    for n in [3, 4, 5]:
        for N in [2, 3]:
            q = rng.dirichlet(np.ones(n))
            mu = pull_balanced(q, N)
            q_back = push_balanced(mu, N, n)
            max_diff = float(np.abs(q - q_back).max())
            if max_diff < 1e-13:
                _pass(f"T11.1: n={n}, N={N}: max|q - pi_* pi^* q| = {max_diff:.2e}")
            else:
                _fail(f"T11.1: n={n}, N={N}: max|q - pi_* pi^* q| = {max_diff:.2e}")

    # T11.2: Idempotence (pi^* pi_*)^2 = pi^* pi_*
    print("\n[T11.2] Idempotence of pi^* pi_*")
    for n in [3, 4]:
        for N in [2, 3]:
            mu = rng.dirichlet(np.ones(n * N))
            P_mu = pull_balanced(push_balanced(mu, N, n), N)
            P2_mu = pull_balanced(push_balanced(P_mu, N, n), N)
            diff = float(np.abs(P_mu - P2_mu).max())
            if diff < 1e-13:
                _pass(f"T11.2: n={n}, N={N}: max|(P^2-P) mu| = {diff:.2e}")
            else:
                _fail(f"T11.2: n={n}, N={N}: max|(P^2-P) mu| = {diff:.2e}")

    # T11.3: Closed-form identity (balanced)
    print("\n[T11.3] Closed-form identity S_obs^fib = log N - H_w(mu)  (balanced)")
    scatter_data_balanced = []
    for trial in range(8):
        n = int(rng.integers(2, 6))
        N = int(rng.integers(2, 5))
        mu = rng.dirichlet(np.ones(n * N))
        P_mu = pull_balanced(push_balanced(mu, N, n), N)
        s_direct = Sobs_fib_direct(mu, P_mu)
        s_closed = Sobs_fib_closed_balanced(mu, N, n)
        diff = abs(s_direct - s_closed)
        scatter_data_balanced.append((s_direct, s_closed))
        if diff < 1e-12:
            _pass(f"T11.3: trial {trial+1} (n={n}, N={N}): "
                  f"|direct - closed| = {diff:.3e}")
        else:
            _fail(f"T11.3: trial {trial+1} (n={n}, N={N}): "
                  f"|direct - closed| = {diff:.3e}")

    # T11.4: Closed-form identity (unbalanced, including Example 2)
    print("\n[T11.4] Closed-form identity (unbalanced fibres)")
    scatter_data_unbalanced = []
    # Example 2 partition first
    ex2_sizes = [3, 2]
    p_ex2_uniform = np.full(5, 0.2)
    s_direct_ex2 = Sobs_fib_direct(
        p_ex2_uniform, pull_unbalanced(push_unbalanced(p_ex2_uniform, ex2_sizes), ex2_sizes))
    s_closed_ex2 = Sobs_fib_closed_unbalanced(p_ex2_uniform, ex2_sizes)
    diff = abs(s_direct_ex2 - s_closed_ex2)
    scatter_data_unbalanced.append((s_direct_ex2, s_closed_ex2))
    if diff < 1e-12:
        _pass(f"T11.4: Example 2 uniform (|A|=3,|B|=2): "
              f"|direct-closed| = {diff:.3e}")
    else:
        _fail(f"T11.4: Example 2 uniform: |direct-closed| = {diff:.3e}")

    for trial in range(6):
        sizes = [int(rng.integers(1, 5)) for _ in range(int(rng.integers(2, 5)))]
        total = sum(sizes)
        mu = rng.dirichlet(np.ones(total))
        Pmu = pull_unbalanced(push_unbalanced(mu, sizes), sizes)
        s_direct = Sobs_fib_direct(mu, Pmu)
        s_closed = Sobs_fib_closed_unbalanced(mu, sizes)
        diff = abs(s_direct - s_closed)
        scatter_data_unbalanced.append((s_direct, s_closed))
        if diff < 1e-12:
            _pass(f"T11.4: trial {trial+1} (sizes={sizes}): "
                  f"|direct-closed| = {diff:.3e}")
        else:
            _fail(f"T11.4: trial {trial+1} (sizes={sizes}): "
                  f"|direct-closed| = {diff:.3e}")

    # T11.5: Range  0 <= S_obs^fib <= log N
    print("\n[T11.5] Range:  0 <= S_obs^fib <= log N")
    for trial in range(6):
        n = int(rng.integers(2, 5))
        N = int(rng.integers(2, 4))
        mu = rng.dirichlet(np.ones(n * N))
        s = Sobs_fib_closed_balanced(mu, N, n)
        if -1e-13 <= s <= np.log(N) + 1e-13:
            _pass(f"T11.5: trial {trial+1} (n={n}, N={N}): "
                  f"S_obs = {s:.6f} in [0, log({N})={np.log(N):.4f}]")
        else:
            _fail(f"T11.5: trial {trial+1}: S_obs = {s:.6f} out of range")

    # T11.6: Equivalence to partition-threshold definition (host paper)
    print("\n[T11.6] Equivalence: S_obs(p, eps) = S_obs^fib(p)  (Remark 11.11)")
    # Example 1: balanced 4-point, partition {{1,2},{3,4}}
    for alpha, beta in EX1_CASES:
        for eps in [0.01, 0.05]:
            p = p_ex1(np.array([0.0, eps*alpha, eps*beta]))
            s_obs = S_obs_ex1(p)
            s_fib = Sobs_fib_closed_balanced(p, N=2, n=2)
            diff = abs(s_obs - s_fib)
            if diff < 1e-13:
                _pass(f"T11.6 Ex1: (a={alpha},b={beta}), eps={eps}: "
                      f"|S_obs - S_obs^fib| = {diff:.2e}")
            else:
                _fail(f"T11.6 Ex1: (a={alpha},b={beta}), eps={eps}: diff = {diff:.2e}")
    # Example 2: unbalanced 5-point
    for alpha, beta, gamma in EX2_CASES:
        for eps in [0.01, 0.05]:
            p = p_ex2(np.array([0.0, eps*alpha, eps*beta, eps*gamma]))
            s_obs = S_obs_ex2(p)
            s_fib = Sobs_fib_closed_unbalanced(p, [3, 2])
            diff = abs(s_obs - s_fib)
            if diff < 1e-13:
                _pass(f"T11.6 Ex2: (a={alpha},b={beta},g={gamma}), eps={eps}: "
                      f"|S_obs - S_obs^fib| = {diff:.2e}")
            else:
                _fail(f"T11.6 Ex2: diff = {diff:.2e}")

    return {
        "scatter_balanced": scatter_data_balanced,
        "scatter_unbalanced": scatter_data_unbalanced,
    }


# === === === ===
# 10. Figure generation — manuscript figures (1-7)
# === === === ===

def plot_bridge_dual_panel(results, example_label, stem, key_fmt,
                            eps_grid=EPS_GRID,
                            legend_fontsize_top=8,
                            legend_fontsize_bot=9):
    """Dual-panel figure (log-log + normalised remainder) for Bridge Theorem.

    Panel (a): log-log S_obs(exact, solid) vs. S_obs(pred, dashed)
               + eps^2 reference (dotted).
    Panel (b): log-log normalised remainder |S_obs - hat S| / eps^3.
    """
    fig, axes = plt.subplots(2, 1, figsize=(7.5, 10))
    ax1, ax2 = axes

    cases = list(results.keys())
    for idx, key in enumerate(cases):
        r = results[key]
        color = COLORS[idx % len(COLORS)]
        lbl_e = key_fmt(key) + r"  exact"
        lbl_p = key_fmt(key) + r"  pred."
        ax1.loglog(eps_grid, r["exact"], color=color, ls="-",
                   lw=1.8, label=lbl_e)
        ax1.loglog(eps_grid, r["pred"], color=color, ls="--",
                   lw=2.2, alpha=0.7, label=lbl_p)

    ref_y = 0.5 * eps_grid**2
    ax1.loglog(eps_grid, ref_y, "k:", lw=1.2, alpha=0.55,
               label=r"$\propto\varepsilon^2$ reference")
    ax1.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax1.set_ylabel(r"$S_{\mathrm{obs}}$  (nats)")
    ax1.set_title(
        r"(a) $S_{\mathrm{obs}}^{\mathrm{exact}}$ vs. "
        r"$\hat{S} = \frac{1}{2}\varepsilon^2 v^\top I v$"
        "\n[" + example_label + "]")
    ax1.legend(fontsize=legend_fontsize_top, ncol=2, loc="lower right")
    ax1.grid(True, which="both", alpha=0.25)

    for idx, key in enumerate(cases):
        r = results[key]
        color = COLORS[idx % len(COLORS)]
        # Compute remainder normalization on the fly (do not depend on
        # results-dict carrying it; preserves backward compatibility).
        rem = np.abs(r["exact"] - r["pred"]) / np.maximum(eps_grid**3, 1e-300)
        ax2.loglog(eps_grid, rem, color=color, ls="-", lw=1.6,
                   label=key_fmt(key))

    ax2.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax2.set_ylabel(
        r"$\left|S_{\mathrm{obs}} - \hat{S}\right| / \varepsilon^3$")
    ax2.set_title(
        r"(b) Normalised remainder — confirms $O(\varepsilon^3)$"
        "\n[" + example_label + "]")
    ax2.legend(fontsize=legend_fontsize_bot, ncol=2)
    ax2.grid(True, which="both", alpha=0.25)

    fig.tight_layout(pad=2.5)
    _save_figure(fig, stem)


def plot_relerr(results, example_label, stem, key_fmt,
                eps_grid=EPS_GRID, legend_fontsize=9):
    """Relative-error plot for the quadratic approximation."""
    fig, ax = plt.subplots(figsize=(7.5, 5))
    for idx, key in enumerate(results.keys()):
        r = results[key]
        rel = np.where(r["exact"] > 0,
                       np.abs(r["exact"] - r["pred"]) / r["exact"],
                       1e-300)
        color = COLORS[idx % len(COLORS)]
        ax.loglog(eps_grid, rel + 1e-20, color=color, ls="-", lw=1.6,
                  label=key_fmt(key))

    ax.axhline(0.01, color="gray", ls="--", lw=1.4,
               label=r"$1\%$ threshold")
    ax.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax.set_ylabel(
        r"$\left|S_{\mathrm{obs}}^{\mathrm{exact}} - \hat{S}\right|"
        r"\;/\; S_{\mathrm{obs}}^{\mathrm{exact}}$")
    ax.set_title("Relative error of quadratic approximation\n"
                 "[" + example_label + "]")
    ax.legend(fontsize=legend_fontsize)
    ax.grid(True, which="both", alpha=0.25)
    ax.set_ylim(1e-12, 10)
    fig.tight_layout()
    _save_figure(fig, stem)


def plot_tradeoff(results_ex1):
    """Figure 3: resolution-information trade-off (linear scale, Ex1)."""
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
        xy=(0.28, 0.024), xycoords="data",
        xytext=(0.65, 0.85), textcoords="axes fraction",
        fontsize=9, color="dimgray", style="italic", ha="center",
        arrowprops=dict(arrowstyle="->", color="gray"), zorder=10,
    )
    ax.annotate(
        "",
        xy=(0.48, 0.005), xytext=(0.35, 0.005),
        arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
        zorder=10,
    )
    ax.text(0.355, 0.007, r"increasing $\varepsilon$", fontsize=9)

    fig.tight_layout()
    _save_figure(fig, "fig3_resolution_information_tradeoff")


def plot_offcenter_ex1(ex1_offcenter_data, eps_grid=EPS_GRID):
    """Figure 6: off-center robustness for Example 1 (dual panel)."""
    fig, axes = plt.subplots(2, 1, figsize=(7.5, 10))
    ax1, ax2 = axes

    for idx, d in enumerate(ex1_offcenter_data):
        color = COLORS[idx % len(COLORS)]
        lbl = (rf"$\theta_1^*={d['theta1']:+.2f}$, "
               rf"$\alpha={d['alpha']:+.2f}$, $\beta={d['beta']:+.2f}$")
        ax1.loglog(eps_grid, d["exact"], color=color, ls="-", lw=1.6,
                   label=lbl + "  exact")
        ax1.loglog(eps_grid, d["pred"], color=color, ls="--", lw=2.0,
                   alpha=0.65, label=lbl + "  pred.")
        ax2.loglog(eps_grid, d["rem_norm"] + 1e-20, color=color, ls="-",
                   lw=1.6, label=lbl)

    ref_y = 0.5 * eps_grid**2
    ax1.loglog(eps_grid, ref_y, "k:", lw=1.2, alpha=0.5,
               label=r"$\propto\varepsilon^2$")
    ax1.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax1.set_ylabel(r"$S_{\mathrm{obs}}$  (nats)")
    ax1.set_title(
        r"(a) Off-center check: $S_{\mathrm{obs}}^{\mathrm{exact}}$ vs. "
        r"$\hat{S} = \frac{1}{2}\varepsilon^2 v^\top I(\theta^*) v$"
        "\n[Example 1, random $\\theta_1^* \\neq 0$, random "
        "$(\\alpha,\\beta)$]")
    ax1.legend(fontsize=7, ncol=2, loc="lower right")
    ax1.grid(True, which="both", alpha=0.25)

    ax2.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax2.set_ylabel(
        r"$\left|S_{\mathrm{obs}} - \hat{S}\right| / \varepsilon^3$")
    ax2.set_title(
        r"(b) Normalised remainder — $O(\varepsilon^3)$ bound at "
        r"$\theta^* \neq 0$"
        "\n[Example 1]")
    ax2.legend(fontsize=7, ncol=2)
    ax2.grid(True, which="both", alpha=0.25)

    fig.tight_layout(pad=2.5)
    _save_figure(fig, "fig6_offcenter_ex1")


def plot_offcenter_ex2(ex2_offcenter_data, eps_grid=EPS_GRID):
    """Figure 7: off-center robustness for Example 2 (dual panel)."""
    fig, axes = plt.subplots(2, 1, figsize=(7.5, 10))
    ax1, ax2 = axes

    for idx, d in enumerate(ex2_offcenter_data):
        color = COLORS[idx % len(COLORS)]
        lbl = (rf"$\theta_1^*={d['theta1']:+.2f}$, "
               rf"$\alpha={d['alpha']:+.2f}$, $\beta={d['beta']:+.2f}$, "
               rf"$\gamma={d['gamma']:+.2f}$")
        ax1.loglog(eps_grid, d["exact"], color=color, ls="-", lw=1.6,
                   label=lbl + "  exact")
        ax1.loglog(eps_grid, d["pred"], color=color, ls="--", lw=2.0,
                   alpha=0.65, label=lbl + "  pred.")
        ax2.loglog(eps_grid, d["rem_norm"] + 1e-20, color=color, ls="-",
                   lw=1.6, label=lbl)

    ref_y = 0.5 * eps_grid**2
    ax1.loglog(eps_grid, ref_y, "k:", lw=1.2, alpha=0.5,
               label=r"$\propto\varepsilon^2$")
    ax1.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax1.set_ylabel(r"$S_{\mathrm{obs}}$  (nats)")
    ax1.set_title(
        r"(a) Off-center check: $S_{\mathrm{obs}}^{\mathrm{exact}}$ vs. "
        r"$\hat{S} = \frac{1}{2}\varepsilon^2 v^\top I(\theta^*) v$"
        "\n[Example 2, random $\\theta_1^* \\neq 0$, random "
        "$(\\alpha,\\beta,\\gamma)$]")
    ax1.legend(fontsize=6, ncol=2, loc="lower right")
    ax1.grid(True, which="both", alpha=0.25)

    ax2.set_xlabel(r"Resolution threshold $\varepsilon$")
    ax2.set_ylabel(
        r"$\left|S_{\mathrm{obs}} - \hat{S}\right| / \varepsilon^3$")
    ax2.set_title(
        r"(b) Normalised remainder — $O(\varepsilon^3)$ bound at "
        r"$\theta^* \neq 0$"
        "\n[Example 2]")
    ax2.legend(fontsize=6, ncol=2)
    ax2.grid(True, which="both", alpha=0.25)

    fig.tight_layout(pad=2.5)
    _save_figure(fig, "fig7_offcenter_ex2")


# === === === ===
# 11. Supplementary diagnostic figures (Section 11)
# === === === ===

def plot_supp_fisher_eigenvalues():
    """Supplementary: eigenvalue structure of Fisher matrices for Ex1 and Ex2."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    I1 = fisher_analytic_ex1(np.zeros(3))
    eig1 = np.sort(np.linalg.eigvalsh(I1))[::-1]
    axes[0].bar(np.arange(len(eig1)), eig1, color=COLORS[0], alpha=0.8)
    axes[0].set_xticks(np.arange(len(eig1)))
    axes[0].set_xticklabels([f"$\\lambda_{i+1}$" for i in range(len(eig1))])
    axes[0].set_ylabel("Eigenvalue")
    axes[0].set_title("Example 1: $I(\\theta^*)$ eigenvalues\n"
                      r"$\mathrm{diag}(1, 1/2, 1/2)$")
    axes[0].grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(eig1):
        axes[0].text(i, v + 0.02, f"{v:.4f}", ha="center", fontsize=9)

    I2 = fisher_analytic_ex2(np.zeros(4))
    eig2 = np.sort(np.linalg.eigvalsh(I2))[::-1]
    axes[1].bar(np.arange(len(eig2)), eig2, color=COLORS[1], alpha=0.8)
    axes[1].set_xticks(np.arange(len(eig2)))
    axes[1].set_xticklabels([f"$\\lambda_{i+1}$" for i in range(len(eig2))])
    axes[1].set_ylabel("Eigenvalue")
    axes[1].set_title("Example 2: $I(\\theta^*)$ eigenvalues\n"
                      r"$\mathrm{diag}(3/2, 6/5, 2/5, 2/5)$")
    axes[1].grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(eig2):
        axes[1].text(i, v + 0.03, f"{v:.4f}", ha="center", fontsize=9)

    fig.tight_layout()
    _save_figure(fig, "fig_supp_fisher_eigenvalues")


def plot_supp_landauer_budget(results_ex1, results_ex2):
    """Supplementary: Landauer minimum energetic cost at T=300K."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    # Example 1
    eps_subset = np.array([1e-4, 1e-3, 1e-2, 5e-2, 1e-1])
    for idx, (alpha, beta) in enumerate(EX1_CASES):
        s_vals = np.array([compute_S_obs_ex1(alpha, beta, e) for e in eps_subset])
        e_min = BOLTZMANN_K * T_KELVIN * s_vals
        axes[0].loglog(eps_subset, e_min, "o-", color=COLORS[idx],
                       lw=1.6, label=rf"$(\alpha,\beta)=({alpha:.0f},{beta:.0f})$")
    axes[0].axhline(BOLTZMANN_K * T_KELVIN * np.log(2), color="gray",
                    ls="--", lw=1.4,
                    label=r"$kT\log 2$ (1 bit)")
    axes[0].set_xlabel(r"Resolution threshold $\varepsilon$")
    axes[0].set_ylabel(r"$E_{\min}$  (J)  at $T=300$ K")
    axes[0].set_title("Example 1: Landauer energy budget")
    axes[0].legend(fontsize=8)
    axes[0].grid(True, which="both", alpha=0.25)

    # Example 2
    for idx, (alpha, beta, gamma) in enumerate(EX2_CASES):
        s_vals = np.array([compute_S_obs_ex2(alpha, beta, gamma, e)
                           for e in eps_subset])
        e_min = BOLTZMANN_K * T_KELVIN * s_vals
        axes[1].loglog(eps_subset, e_min, "o-", color=COLORS[idx],
                       lw=1.6,
                       label=(rf"$(\alpha,\beta,\gamma)="
                              rf"({alpha:.0f},{beta:.0f},{gamma:.0f})$"))
    axes[1].axhline(BOLTZMANN_K * T_KELVIN * np.log(2), color="gray",
                    ls="--", lw=1.4,
                    label=r"$kT\log 2$ (1 bit)")
    axes[1].set_xlabel(r"Resolution threshold $\varepsilon$")
    axes[1].set_ylabel(r"$E_{\min}$  (J)  at $T=300$ K")
    axes[1].set_title("Example 2: Landauer energy budget")
    axes[1].legend(fontsize=7)
    axes[1].grid(True, which="both", alpha=0.25)

    fig.tight_layout()
    _save_figure(fig, "fig_supp_landauer_budget")


def plot_supp_fibre_identity(fibre_data):
    """Supplementary: direct vs. closed-form S_obs^fib (Section 11)."""
    fig, axes = plt.subplots(1, 2, figsize=(11, 5))

    bal = np.array(fibre_data["scatter_balanced"])
    unb = np.array(fibre_data["scatter_unbalanced"])

    axes[0].scatter(bal[:, 0], bal[:, 1], s=70, color=COLORS[0], alpha=0.7,
                    edgecolor="black", lw=0.6, label="balanced fibres")
    lim_b = (min(bal.min(), 0), bal.max() * 1.05)
    axes[0].plot([lim_b[0], lim_b[1]], [lim_b[0], lim_b[1]], "k:", lw=1)
    axes[0].set_xlabel(r"$S_{\mathrm{obs}}^{\mathrm{fib}}$ direct  "
                       r"($D_{\mathrm{KL}}(\mu \,\|\, \pi^*\pi_*\mu)$)")
    axes[0].set_ylabel(r"$S_{\mathrm{obs}}^{\mathrm{fib}}$ closed-form  "
                       r"($\log N - H_{\mathrm{w}}$)")
    axes[0].set_title("Theorem 11.9 (closed-form identity)\nBalanced fibres")
    axes[0].legend(fontsize=9)
    axes[0].grid(True, alpha=0.3)
    axes[0].set_aspect("equal", adjustable="box")

    axes[1].scatter(unb[:, 0], unb[:, 1], s=70, color=COLORS[1], alpha=0.7,
                    edgecolor="black", lw=0.6, label="unbalanced fibres")
    lim_u = (min(unb.min(), 0), unb.max() * 1.05)
    axes[1].plot([lim_u[0], lim_u[1]], [lim_u[0], lim_u[1]], "k:", lw=1)
    axes[1].set_xlabel(r"$S_{\mathrm{obs}}^{\mathrm{fib}}$ direct")
    axes[1].set_ylabel(r"$S_{\mathrm{obs}}^{\mathrm{fib}}$ closed-form  "
                       r"($\mathbb{E}_x[\log N_x - H(\nu_x)]$)")
    axes[1].set_title("Theorem 11.9 (unbalanced extension)\nUnbalanced fibres")
    axes[1].legend(fontsize=9)
    axes[1].grid(True, alpha=0.3)
    axes[1].set_aspect("equal", adjustable="box")

    fig.tight_layout()
    _save_figure(fig, "fig_supp_fibre_identity")


# === === === ===
# 12. Entry point
# === === === ===

def _key_fmt_ex1(key):
    a, b = key
    return rf"$(\alpha,\beta)=({a:.0f},{b:.0f})$"


def _key_fmt_ex2(key):
    a, b, g = key
    return rf"$(\alpha,\beta,\gamma)=({a:.0f},{b:.0f},{g:.0f})$"


def main():
    print()
    print("=" * 80)
    print("  NUMERICAL VERIFICATION (v3.24.1)")
    print()
    print("  Theorem 6.7 (Bridge Theorem) +")
    print("  Section 11 (Fibre-Theoretic Foundation, Theorem 11.9)")
    print()
    print("  Paper: 'KL-Geometric Structure of Observer Entropy', v3.24.1")
    print("  Author: Vladimir Khomyakov")
    print("=" * 80)

    # ------------------------------------------------------
    # T1-T8: Bridge Theorem checks (Examples 1 & 2)
    # ------------------------------------------------------
    results_ex1 = run_example1()
    results_ex2 = run_example2()

    # ------------------------------------------------------
    # T9: Off-center robustness checks
    # ------------------------------------------------------
    ex1_oc, ex2_oc = run_offcenter_checks()

    # ------------------------------------------------------
    # T11.x: Section 11 (Fibre-Theoretic Foundation)
    # ------------------------------------------------------
    fibre_data = run_section11_fibre()

    # ------------------------------------------------------
    # Figure generation
    # ------------------------------------------------------
    print()
    section_banner("FIGURE GENERATION: MANUSCRIPT FIGURES (v3.24.1)")
    # Example 1: fewer legend entries -> larger fonts (matches v3 originals)
    plot_bridge_dual_panel(
        results_ex1, "Example 1: 4-point space",
        "fig1_bridge_theorem_verification", _key_fmt_ex1,
        legend_fontsize_top=8, legend_fontsize_bot=9)
    plot_relerr(
        results_ex1, "Example 1: 4-point space",
        "fig2_relative_error", _key_fmt_ex1,
        legend_fontsize=9)
    plot_tradeoff(results_ex1)
    # Example 2: more legend entries -> smaller fonts to avoid overflow
    plot_bridge_dual_panel(
        results_ex2, "Example 2: 5-point space",
        "fig4_bridge_theorem_ex2", _key_fmt_ex2,
        legend_fontsize_top=7, legend_fontsize_bot=8)
    plot_relerr(
        results_ex2, "Example 2: 5-point space",
        "fig5_relative_error_ex2", _key_fmt_ex2,
        legend_fontsize=8)
    plot_offcenter_ex1(ex1_oc)
    plot_offcenter_ex2(ex2_oc)

    print()
    section_banner("FIGURE GENERATION: SUPPLEMENTARY DIAGNOSTICS")
    plot_supp_fisher_eigenvalues()
    plot_supp_landauer_budget(results_ex1, results_ex2)
    plot_supp_fibre_identity(fibre_data)

    # ------------------------------------------------------
    # Final verdict
    # ------------------------------------------------------
    print()
    print("=" * 80)
    if not _FAILURES:
        print("  PASS  ALL VERIFICATION CHECKS PASSED")
        print()
        print("  Summary:")
        print("    [T1-T8]  Bridge Theorem 6.7 (Examples 1 & 2):")
        print("       - Fisher matrices match paper exactly:")
        print("           Ex1: I(theta*) = diag(1, 1/2, 1/2)         [Lemma 6.22]")
        print("           Ex2: I(theta*) = diag(3/2, 6/5, 2/5, 2/5)  [Proposition 6.36]")
        print("       - Closed-form leading coefficients verified")
        print("           [Propositions 6.24, 6.38]")
        print("       - Log-log slope = 2.000 +/- 0.01 in all 9 configurations")
        print("       - O(eps^3) remainder confirmed: sup|R|/eps^3 < 10")
        print("       - rel.err(eps) <= 0.8*eps for eps <= 0.03 (Validation criterion)")
        print("       - Landauer bound S_obs >= 0 in all cases")
        print("       - S_obs(eps) monotone non-decreasing in eps")
        print()
        print(f"    [T9]    Off-center robustness ({OFFCENTER_N_EX1}+{OFFCENTER_N_EX2}={OFFCENTER_N_EX1+OFFCENTER_N_EX2} random base points):")
        print("       - Quadratic scaling and O(eps^3) remainder confirmed at theta* != 0")
        print(f"       - theta_1* in [{OFFCENTER_THETA1_RANGE[0]}, {OFFCENTER_THETA1_RANGE[1]}], "
              f"RNG seed = {OFFCENTER_SEED}")
        print()
        print("    [T11.x] Fibre-theoretic foundation (Section 11):")
        print("       - Push-pull left inverse  pi_* o pi^* = id")
        print("       - Idempotence  (pi^* pi_*)^2 = pi^* pi_*")
        print("       - Closed-form identity  S_obs^fib = log N - H_w  (Theorem 11.9)")
        print("       - Unbalanced extension (Example 2 partition |A|=3, |B|=2)")
        print("       - Range  0 <= S_obs^fib <= log N")
        print("       - Equivalence with partition-threshold definition (Remark 11.11)")
        print()
        print("    Figures generated:")
        print("       Manuscript (referenced in v3.24.tex):")
        print("          fig1_bridge_theorem_verification.pdf")
        print("          fig2_relative_error.pdf")
        print("          fig3_resolution_information_tradeoff.pdf")
        print("          fig4_bridge_theorem_ex2.pdf")
        print("          fig5_relative_error_ex2.pdf")
        print("          fig6_offcenter_ex1.pdf")
        print("          fig7_offcenter_ex2.pdf")
        print("       Supplementary diagnostics:")
        print("          fig_supp_fisher_eigenvalues.pdf")
        print("          fig_supp_landauer_budget.pdf")
        print("          fig_supp_fibre_identity.pdf")
        print("=" * 80)
        sys.exit(0)
    else:
        print(f"  FAIL  VERIFICATION FAILED  ({len(_FAILURES)} check(s)):")
        for i, f in enumerate(_FAILURES, 1):
            print(f"    [{i}] {f}")
        print("=" * 80)
        sys.exit(1)


if __name__ == "__main__":
    main()
