#!/usr/bin/env python3
"""
verify_bridge_symbolic_v3.24.12.py

Self-contained symbolic verification (sympy) of the exact identities from
  "KL-Geometric Structure of Observer Entropy", v3.24.12 (V. Khomyakov)

Complements the numerical script verify_bridge_theorem_v3.24.12.py:
  the numerical script checks the asymptotic O(eps^3) expansion, whereas
  the present script verifies the closed-form / exact identities symbolically.

Every printed difference / residual must equal 0.

Coverage:
  (A) Lemma 6.23   : cosh algebraic identity
  (B) Lemma 6.22   : Fisher matrix Ex1 = diag(1, 1/2, 1/2)
  (C) Prop. 6.36   : Fisher matrix Ex2 = diag(3/2, 6/5, 2/5, 2/5)
  (D) Prop. 6.24   : leading coefficient 1/4 (a^2+b^2)              [Ex1]
  (E) Prop. 6.38   : leading coefficient 3/5 a^2 + 1/5 b^2 + 1/5 g^2 [Ex2]
  (F) Theorem 11.9 : closed form  S_obs^fib = log N - H_w   (exact)
  (G) Lemma 6.48 (Vanishing), Steps (a)-(d): difference-Jacobian step
      (G1) contrast matrix  M = I - 1 w^T,  det M = w_1
      (G2) factorization    I_bb = J W J^T,  W = Mhat^T D Mhat >= 0
      (G3) invertibility of J  =>  D_w sigma_b|_0 = 0
      verified symbolically for m = 2, 3.

Author: Vladimir Khomyakov
Independent Researcher
ORCID: https://orcid.org/0009-0006-3074-9145
"""

import os
import sys
import datetime
import atexit
from pathlib import Path

import sympy as sp


# === === === ===
# Reproducibility logging: mirror console output to a log file.
#   This affects only output capture; no computation/identity is modified.
#   Mirrors the convention used in verify_bridge_theorem_v3.24.12.py.
# === === === ===

# Repository paths (same convention as the numerical script).
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent if SCRIPT_DIR.name == "scripts" else SCRIPT_DIR
RESULTS_LOG = REPO_ROOT / "Results_verify_bridge_symbolic_v3.24.12.txt"


class _Tee:
    """Mirror standard output to the console and a log file simultaneously.

    Every character written to the console is recorded verbatim in the log
    file (no rounding or reformatting). Output capture only; the symbolic
    computations and zero-verdicts are unaffected.
    """
    def __init__(self, stream, file_handle):
        self._stream = stream
        self._file = file_handle

    def write(self, data):
        self._stream.write(data)
        self._file.write(data)
        return len(data)

    def flush(self):
        self._stream.flush()
        self._file.flush()


# --- Activate reproducibility logging BEFORE any module-level print, so that
#     blocks (A)-(F) and the (G) banner (all executed at module load) are
#     mirrored to the log file, matching the _Tee docstring and the stated
#     reproducibility goal. ---
_LOG_HANDLE = open(RESULTS_LOG, "w", encoding="utf-8")
_ORIG_STDOUT = sys.stdout
sys.stdout = _Tee(_ORIG_STDOUT, _LOG_HANDLE)


def _restore_stdout():
    """Restore the original stdout and close the log file handle."""
    # Idempotent: safe to call from a main() verdict branch AND from the
    # atexit hook (covers exceptions raised at module load, before main()).
    if sys.stdout is not _ORIG_STDOUT:
        sys.stdout = _ORIG_STDOUT
    if not _LOG_HANDLE.closed:
        _LOG_HANDLE.close()


# Ensure stdout is restored and the log file is flushed/closed even if an
# exception is raised at module load (blocks (A)-(F)/(G) run at import time,
# before main() is entered, so the in-main() restore calls would be skipped).
atexit.register(_restore_stdout)


# Reproducibility header (run timestamp, interpreter, and invocation).
print(f"# Reproducibility run  {datetime.datetime.now().isoformat()}")
print(f"# Python: {sys.version.split()[0]}")
print(f"# SymPy: {sp.__version__}")
print(f"# Script: {Path(__file__).name}")
print(f"# Working directory: {Path.cwd()}")
_argv0 = Path(sys.argv[0])
try:
    _shown = _argv0.resolve().relative_to(Path.cwd())
except ValueError:
    _shown = Path(_argv0.name)
print(f"# Invocation: python {' '.join([str(_shown).replace(os.sep, '/')] + sys.argv[1:])}")
print("# Recommended invocation (from repository root):")
print("# python scripts/verify_bridge_symbolic_v3.24.12.py")
print()


_RESIDUAL_FAILURES = []
_NONDETERMINISTIC_ZEROS = []


def is_identically_zero(e, _label=None):
    """Decide whether `e` is identically zero.

    Verdict policy (in order):
      1. exact rational normal form  num == 0  after expand           -> DETERMINISTIC
      2. exact polynomial test  Poly(num, *syms).is_zero             -> DETERMINISTIC
      3. exact `simplify` collapse to 0                              -> DETERMINISTIC
      4. Schwartz-Zippel probe (50 random rational points)          -> PROBABILISTIC

    Branch 4 is a randomized identity test, NOT a proof.  Any residual
    whose zero-verdict rests on branch 4 is recorded in
    `_NONDETERMINISTIC_ZEROS` so the final report can downgrade the
    overall verdict from "PROVEN" to "PROBABILISTIC".  For the identities
    in this script all residuals are low-degree polynomials/rationals and
    are expected to be settled deterministically by branches 1-3.
    """
    e = sp.together(sp.sympify(e))
    num, _ = sp.fraction(e)
    num = sp.expand(num)
    if num == 0:
        return True
    syms = sorted(num.free_symbols, key=lambda s: s.name)
    if not syms:
        return sp.simplify(num) == 0
    try:
        poly = sp.Poly(num, *syms)
        if poly.is_zero:
            return True
        # Poly with all-zero coefficients but not flagged: still decisive.
        if all(c == 0 for c in poly.all_coeffs()):
            return True
        # A genuine nonzero polynomial: DECISIVELY nonzero, no probing needed.
        return False
    except sp.PolynomialError:
        pass
    # Non-polynomial residual (e.g. surviving log/exp): try an exact collapse.
    if sp.simplify(num) == 0:
        return True
    # Last resort: Schwartz-Zippel.  This is PROBABILISTIC; record it so the
    # final verdict is downgraded rather than silently reported as proven.
    import random
    rng = random.Random(20240613)
    saw_zero_only = True
    for _ in range(50):
        subs = {s: sp.Rational(rng.randint(2, 97), rng.randint(2, 97))
                for s in syms}
        if sp.simplify(num.subs(subs)) != 0:
            return False
    if saw_zero_only:
        _NONDETERMINISTIC_ZEROS.append((_label, sp.srepr(num)))
    return True


# Optional: the 5-point softmax series check in (E) can be computationally slow.
RUN_HEAVY_SERIES = True


def report(label, expr):
    """Reduce a residual that must be 0, avoiding the trigsimp->factor path."""
    e = sp.sympify(expr)
    # Rewrite hyperbolics via exp, then do purely rational simplification.
    e = e.rewrite(sp.exp)
    e = sp.expand(e)
    e = sp.cancel(e)            # rational-function normal form (no factor over QQ<I>)
    e = sp.expand(sp.powsimp(e, force=True))
    # Final logarithm collapse, should any log term survive (block A).
    e = sp.logcombine(sp.expand_log(e, force=True), force=True)
    e = sp.cancel(sp.expand(e))
    val = sp.nsimplify(e) if e.free_symbols == set() else e
    print(f"  {label}: {val}")
    # Automatic verdict: residual lines that must be 0, together with the
    # "# nonzero entries" counters, are checked here. Lines whose value is a
    # symbolic expression (e.g. the explicit nonzero det J) are exempt by label.
    _EXEMPT = ("det J (= r2 - r1)", "det J is a nonzero polynomial")
    if any(tag in label for tag in _EXEMPT):
        return val
    # Zero test handling sympy Matrix and scalar uniformly.
    if isinstance(val, sp.MatrixBase):
        is_zero = all(is_identically_zero(entry, label) for entry in val)
    else:
        is_zero = is_identically_zero(val, label)
    if not is_zero:
        _RESIDUAL_FAILURES.append((label, val))
    return val


# ===================================================================
# (A) Lemma 6.23 (cosh algebraic identity)
#     e^t log(e^t/cosh t) + e^{-t} log(e^{-t}/cosh t)
#       = 2 cosh t [ t tanh t - log cosh t ]
# ===================================================================
print("=== (A) Cosh identity (Lemma 6.23): LHS - RHS ===")
t = sp.Symbol('t', real=True)
lhs = (sp.exp(t)  * sp.log(sp.exp(t)  / sp.cosh(t)) +
       sp.exp(-t) * sp.log(sp.exp(-t) / sp.cosh(t)))
rhs = 2*sp.cosh(t) * (t*sp.tanh(t) - sp.log(sp.cosh(t)))
report("cosh identity", sp.expand_log(lhs - rhs, force=True))


# ===================================================================
# Shared softmax machinery
# ===================================================================
def softmax_p(eta):
    """Symbolic softmax distribution from a list of natural parameters."""
    Z = sum(sp.exp(e) for e in eta)
    return [sp.exp(e)/Z for e in eta]

def fisher_matrix(eta, theta, at=None):
    """
    Fisher = Cov_p[t], t(x)=grad_theta eta_x.
    If `at` (dict theta->value) is given, substitute before simplifying,
    so no exp(symbol) survives into the polynomial engine.
    """
    d = len(theta)
    n = len(eta)
    p = softmax_p(eta)
    if at is not None:
        p = [pi.subs(at) for pi in p]          # numeric probabilities first
    T = [[sp.diff(eta[x], theta[i]) for i in range(d)] for x in range(n)]
    if at is not None:
        T = [[t_xi.subs(at) for t_xi in row] for row in T]
    mean = [sum(p[x] * T[x][i] for x in range(n)) for i in range(d)]
    I = sp.zeros(d, d)
    for i in range(d):
        for j in range(d):
            cov = sum(p[x] * (T[x][i] - mean[i]) * (T[x][j] - mean[j])
                      for x in range(n))
            I[i, j] = sp.nsimplify(sp.cancel(sp.expand(cov)))
    return I


# ===================================================================
# (B) Lemma 6.22 : Fisher matrix for Example 1 at theta* = 0
#     X = {1,2,3,4}, eta = (t1+t2, t1-t2, -t1+t3, -t1-t3)
# ===================================================================
print("\n=== (B) Fisher Ex1 at theta*=0 : I - diag(1,1/2,1/2) ===")
t1, t2, t3 = sp.symbols('t1 t2 t3', real=True)
theta1 = [t1, t2, t3]
eta1 = [t1+t2, t1-t2, -t1+t3, -t1-t3]
I1 = fisher_matrix(eta1, theta1, at={t1: 0, t2: 0, t3: 0})
I1_expected = sp.diag(1, sp.Rational(1, 2), sp.Rational(1, 2))
print("  I1(0) =", I1.tolist())
report("Ex1 Fisher residual", I1 - I1_expected)


# ===================================================================
# (C) Proposition 6.36 : Fisher matrix for Example 2 at theta* = 0
#     X = {1,...,5},
#     eta = (t1+t2+t3, t1+t2-t3, t1-2t2, -3/2 t1 + t4, -3/2 t1 - t4)
# ===================================================================
print("\n=== (C) Fisher Ex2 at theta*=0 : I - diag(3/2,6/5,2/5,2/5) ===")
a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4', real=True)
theta2 = [a1, a2, a3, a4]
eta2 = [a1+a2+a3, a1+a2-a3, a1-2*a2,
        sp.Rational(-3, 2)*a1 + a4, sp.Rational(-3, 2)*a1 - a4]
I2 = fisher_matrix(eta2, theta2, at={a1: 0, a2: 0, a3: 0, a4: 0})
I2_expected = sp.diag(sp.Rational(3, 2), sp.Rational(6, 5),
                      sp.Rational(2, 5), sp.Rational(2, 5))
print("  I2(0) =", I2.tolist())
report("Ex2 Fisher residual", I2 - I2_expected)


# ===================================================================
# (D) Proposition 6.24 : leading coefficient for Ex1
#     1/2 v^T I v with v=(0,-a,-b)  ==  1/4 (a^2 + b^2)
# ===================================================================
print("\n=== (D) Ex1 leading coefficient : 1/2 v^T I v - 1/4(a^2+b^2) ===")
a, b = sp.symbols('a b', real=True)
v1 = sp.Matrix([0, -a, -b])
coeff1 = sp.Rational(1, 2) * (v1.T * I1_expected * v1)[0]
report("Ex1 coeff residual", coeff1 - sp.Rational(1, 4)*(a**2 + b**2))

print("    independent eps^2-coefficient check (Ex1):")
eps = sp.Symbol('eps', positive=True)
f = lambda u: u*sp.tanh(u) - sp.log(sp.cosh(u))
Zc = 2*sp.cosh(eps*a) + 2*sp.cosh(eps*b)
S1 = (2*sp.cosh(eps*a)/Zc)*f(eps*a) + (2*sp.cosh(eps*b)/Zc)*f(eps*b)
ser1 = sp.series(S1, eps, 0, 4).removeO()
c1 = ser1.coeff(eps, 2)
report("Ex1 series eps^2 coeff residual",
       sp.simplify(c1) - sp.Rational(1, 4)*(a**2 + b**2))


# ===================================================================
# (E) Proposition 6.38 : leading coefficient for Ex2
#     1/2 v^T I v with v=(0,-a,-b,-g) == 3/5 a^2 + 1/5 b^2 + 1/5 g^2
# ===================================================================
print("\n=== (E) Ex2 leading coefficient : 1/2 v^T I v - (3/5 a^2+1/5 b^2+1/5 g^2) ===")
g = sp.Symbol('g', real=True)
v2 = sp.Matrix([0, -a, -b, -g])
coeff2 = sp.Rational(1, 2) * (v2.T * I2_expected * v2)[0]
target2 = sp.Rational(3, 5)*a**2 + sp.Rational(1, 5)*b**2 + sp.Rational(1, 5)*g**2
report("Ex2 coeff residual", coeff2 - target2)

if RUN_HEAVY_SERIES:
    print("    independent eps^2-coefficient check (Ex2):")
    subs2 = {a1: 0, a2: eps*a, a3: eps*b, a4: eps*g}
    p2 = [sp.simplify(pi.subs(subs2)) for pi in softmax_p(eta2)]
    pA = sp.simplify(p2[0] + p2[1] + p2[2])
    pB = sp.simplify(p2[3] + p2[4])
    q2 = [pA/3, pA/3, pA/3, pB/2, pB/2]
    S2 = sum(p2[x]*sp.log(p2[x]/q2[x]) for x in range(5))
    ser2 = sp.series(sp.simplify(S2), eps, 0, 3).removeO()
    c2 = sp.simplify(ser2.coeff(eps, 2))
    report("Ex2 series eps^2 coeff residual", sp.simplify(c2 - target2))
else:
    print("    (Ex2 series check skipped: RUN_HEAVY_SERIES = False)")



# ===================================================================
# (F) Theorem 11.9 : closed-form fibre identity (EXACT, symbolic)
#     S_obs^fib(mu) = KL(mu || pi^* pi_* mu) = log N - H_w(mu)
#     verified for symbolic strictly-positive mu on balanced fibres.
# ===================================================================
print("\n=== (F) Theorem 11.9 closed form : direct KL - (log N - H_w) ===")
def fibre_closed_form_residual(n, N):
    m = sp.Matrix(n, N, lambda i, j: sp.Symbol(f'm_{i}_{j}', positive=True))
    total = sum(m[i, j] for i in range(n) for j in range(N))
    mu = sp.Matrix(n, N, lambda i, j: m[i, j]/total)
    p = [sum(mu[i, j] for j in range(N)) for i in range(n)]
    lift = sp.Matrix(n, N, lambda i, j: p[i]/N)
    KL = sum(mu[i, j]*sp.log(mu[i, j]/lift[i, j])
             for i in range(n) for j in range(N))
    Hw = 0
    for i in range(n):
        nu = [mu[i, j]/p[i] for j in range(N)]
        Hw += p[i]*(-sum(nu_j*sp.log(nu_j) for nu_j in nu))
    closed = sp.log(N) - Hw
    return sp.simplify(sp.expand_log(KL - closed, force=True))


for (n, N) in [(2, 2), (3, 2), (2, 3)]:
    report(f"Theorem 11.9 residual (n={n}, N={N})",
           fibre_closed_form_residual(n, N))


# ===================================================================
# (G) Lemma 6.48 (Vanishing), Steps (a)-(d): difference-Jacobian step
#
#     The algebraic core of the proof, verified symbolically
#     for m = 2, 3.  Notation follows the manuscript:
#
#       r_k   = class-average natural-parameter gradients (rows), k=1..m
#       w_k   = |A_k| p_k > 0,  sum_k w_k = 1   (center-of-mass weights)
#       bar_r = sum_k w_k r_k                    (p-weighted mean row)
#       J     = [ r_k - r_1 ]_{k=2}^m            (difference Jacobian)
#       tilde_r_k = r_k - bar_r                  (centered rows)
#
#     Step (b): change of frame from differences J_l to centered rows:
#                 tilde_r_k = sum_l Mhat_{k,l} J_l,
#               with the (m-1)x(m-1) contrast block
#                 M       = I_{m-1} - 1 w^T,   w=(w_2,...,w_m)
#               and rectangular extension Mhat in R^{m x (m-1)}:
#                 Mhat_{1,l}   = -w_{l+1}
#                 Mhat_{k,l}   = delta_{k,l} - w_{l+1}   (k>=2)
#
#     (G1)  det M = w_1                (rank-one determinant identity)
#     (G2)  I_bb = J W J^T,  W = Mhat^T D Mhat,  D = diag(w_1,...,w_m)
#           where  I_bb = sum_k w_k tilde_r_k tilde_r_k^T  (between-Fisher).
#           NOTE the orientation J W J^T (the column vectors are
#           tilde_k = J * Mhat[k,:]^T); for d_b = m-1 the shapes of
#           J W J^T and J^T W J coincide, so the orientation is asserted
#           explicitly and checked entrywise below.
#     (G3)  W > 0  and  (for explicit numeric weights) I_bb > 0  =>  J
#           invertible, hence  D_w sigma_b|_0 = 0.
# ===================================================================
print("\n=== (G) Lemma 6.48 difference-Jacobian step (Steps a-d) ===")


def build_contrast(weights):
    """
    Build the square contrast block M (size (m-1)x(m-1)) and its
    rectangular extension Mhat (size m x (m-1)) from the weight
    vector  w = (w_1, ..., w_m)  with sum w_k = 1.

      w (used in contrast) = (w_2, ..., w_m)
      M_{k,l}    = delta_{k,l} - w_{l+1}        (1<=k,l<=m-1)
      Mhat_{0,l} = -w_{l+1}                     (top row, "class 1")
      Mhat_{k,l} = delta_{k,l} - w_{l+1}        (k=1..m-1)
    """
    m = len(weights)
    wtail = weights[1:]                      # (w_2,...,w_m)
    M = sp.zeros(m - 1, m - 1)
    for k in range(m - 1):
        for l in range(m - 1):
            M[k, l] = (1 if k == l else 0) - wtail[l]
    Mhat = sp.zeros(m, m - 1)
    for l in range(m - 1):
        Mhat[0, l] = -wtail[l]               # row for class 1
    for k in range(1, m):
        for l in range(m - 1):
            Mhat[k, l] = (1 if (k - 1) == l else 0) - wtail[l]
    return M, Mhat


def check_difference_jacobian(m, d_b, seed_rows, weights):
    """
    Symbolic verification of Steps (a)-(d) for given m, with
    symbolic class-gradient rows r_k in R^{d_b} and weights w_k.

    seed_rows : list of m sympy Matrices (column vectors, length d_b)
    weights   : list of m sympy expressions, summing to 1.
    """
    # --- weights sum to 1 (Step (a), normalization) ---
    report(f"(G,m={m}) sum_k w_k - 1", sum(weights) - 1)

    rows = seed_rows                         # r_1, ..., r_m  (column vecs)
    bar_r = sp.zeros(d_b, 1)
    for k in range(m):
        bar_r += weights[k]*rows[k]
    bar_r = sp.simplify(bar_r)

    # Step (a): center-of-mass constraint  sum_k w_k (r_k - bar_r) = 0
    com = sp.zeros(d_b, 1)
    for k in range(m):
        com += weights[k]*(rows[k] - bar_r)
    report(f"(G,m={m}) center-of-mass  sum_k w_k(r_k-bar_r)", sp.simplify(com))

    # difference Jacobian  J = [ r_k - r_1 ]_{k=2}^m   (columns are J_l)
    J = sp.zeros(d_b, m - 1)
    for l in range(m - 1):
        J[:, l] = rows[l + 1] - rows[0]      # J_l = r_{l+1}-r_1 (0-indexed)

    # centered rows  tilde_r_k = r_k - bar_r
    tilde = [sp.simplify(rows[k] - bar_r) for k in range(m)]

    # ---- (G1) contrast determinant  det M = w_1 ----
    M, Mhat = build_contrast(weights)
    detM = sp.simplify(sp.det(M))
    report(f"(G1,m={m}) det M - w_1", sp.simplify(detM - weights[0]))

    # (G1b) Confirm the statement of Lemma 6.48, Step (b):
    # the lower (m-1)x(m-1) block of Mhat (rows k=2..m, i.e. indices
    # 1..m-1 here) equals the invertible contrast matrix M.
    lower_block = Mhat[1:m, :]                 # rows k=2,...,m
    report(f"(G1b,m={m}) lower block of Mhat - M (# nonzero entries)",
           sp.Integer(sum(
               0 if is_identically_zero(lower_block[i, j] - M[i, j]) else 1
               for i in range(m - 1) for j in range(m - 1))))
    # (G1c) ker(Mhat) = {0}: Mhat u = 0 forces u = 0 via the lower block.
    # Symbolically: rank(Mhat) = m-1 (full column rank) <=> det of the
    # lower square block is nonzero (= det M = w_1 > 0).
    report(f"(G1c,m={m}) det(lower block) - w_1",
           sp.simplify(sp.det(lower_block) - weights[0]))

    # ---- Step (b): tilde_r_k = sum_l Mhat_{k,l} J_l ----
    # Entrywise check of the frame-change identity: every entry of
    # tilde_r_k - sum_l Mhat_{k,l} J_l must be identically zero.  We count
    # nonzero canonical-form entries (no Abs wrapper); the count must be 0.
    n_nonzero_frame = 0
    for k in range(m):
        recon = sp.zeros(d_b, 1)
        for l in range(m - 1):
            recon += Mhat[k, l]*J[:, l]
        diff = tilde[k] - recon
        for e in diff:
            if not is_identically_zero(e):
                n_nonzero_frame += 1
    report(f"(G,m={m}) frame change  tilde_r_k - sum_l Mhat J_l "
           f"(# nonzero entries)", sp.Integer(n_nonzero_frame))

    # ---- (G2) factorization  I_bb = J W J^T ----
    # between-Fisher block  I_bb = sum_k w_k tilde_r_k tilde_r_k^T
    I_bb = sp.zeros(d_b, d_b)
    for k in range(m):
        I_bb += weights[k]*(tilde[k]*tilde[k].T)
    I_bb = sp.simplify(I_bb)

    # Frame change gives the COLUMN vector  tilde_k = sum_l Mhat[k,l] J[:,l]
    #                                              = J * Mhat[k,:]^T.
    # Hence  tilde_k tilde_k^T = J * (Mhat[k,:]^T Mhat[k,:]) * J^T, and
    #   I_bb = sum_k w_k tilde_k tilde_k^T
    #        = J * ( sum_k w_k Mhat[k,:]^T Mhat[k,:] ) * J^T
    #        = J * ( Mhat^T D Mhat ) * J^T  =  J * W * J^T.
    # Note the orientation:  I_bb = J W J^T  (not  J^T W J).  For d_b = m-1
    # both have the same shape, so the orientation must be stated explicitly.
    D = sp.diag(*weights)                    # D = diag(w_1,...,w_m)
    # Build W two independent ways and cross-check they agree, so the
    # closed form  W = Mhat^T D Mhat  is itself verified, not assumed.
    W = sp.zeros(m - 1, m - 1)
    for k in range(m):
        mk = Mhat[k, :]                      # 1 x (m-1) contrast row for class k
        W += weights[k] * (mk.T * mk)
    W = sp.simplify(W)
    W_closed = sp.simplify(Mhat.T * D * Mhat)
    report(f"(G2,m={m}) W - Mhat^T D Mhat", sp.simplify(W - W_closed))

    # Entrywise check: each polynomial entry of the residual matrix
    # I_bb - J W J^T must be identically zero.  We expand each entry to
    # canonical polynomial form (no Abs wrapper, which would block
    # cancellation) and count the nonzero entries; the count must be 0.
    # Note: sp.together() over a Matrix does not reliably reduce entries
    # to canonical form in all sympy versions; each entry is reduced
    # separately via expand+cancel so that genuine zeros collapse to 0.
    raw_G2 = I_bb - J * W * J.T
    diff_G2 = sp.Matrix(d_b, d_b,
                        lambda i, j: sp.cancel(sp.expand(raw_G2[i, j])))
    n_nonzero_G2 = 0
    for i in range(d_b):
        for j in range(d_b):
            if not is_identically_zero(diff_G2[i, j]):
                n_nonzero_G2 += 1
    report(f"(G2,m={m}) I_bb - J W J^T (# nonzero entries)",
           sp.Integer(n_nonzero_G2))

    # ---- (G2-orient) guard against the spurious  J^T W J  reading ----
    # The two orientations coincide in SHAPE for d_b = m-1, which is exactly
    # the degenerate case that this script must explicitly distinguish.  We
    # therefore additionally assert that I_bb - J^T W J is NOT generically
    # zero (it would vanish only in non-generic configurations); reported as
    # a count that must be > 0 in general.
    raw_wrong = I_bb - J.T * W * J
    wrong_nonzero = sum(
        0 if is_identically_zero(sp.cancel(sp.expand(raw_wrong[i, j])), None)
        else 1 for i in range(d_b) for j in range(d_b))
    _orient_note = ("(degenerate: 1x1 block is symmetric, so 0 is expected)"
                    if d_b == 1
                    else "(informational, expected > 0 for non-symmetric J)")
    print(f"  (G2-orient,m={m}) I_bb - J^T W J nonzero entries "
          f"{_orient_note}: {wrong_nonzero}")

    return M, Mhat, W, J, I_bb


def main():
    # ==============================================================
    # Run all symbolic blocks (A)-(F) at import time above; the
    # difference-Jacobian step (G) is executed here.
    # ==============================================================

    # --- m = 2 : single difference, d_b = 1 ----------------------------
    print("\n  -- (G) case m = 2 (d_b = 1) --")
    # symbolic scalar rows r_1, r_2 and weight w_1 (w_2 = 1 - w_1)
    r1_2, r2_2 = sp.symbols('r1 r2', real=True)
    w1_2 = sp.Symbol('w1', positive=True)
    weights2 = [w1_2, 1 - w1_2]
    rows2 = [sp.Matrix([r1_2]), sp.Matrix([r2_2])]
    M2, Mhat2, W2, J2, Ibb2 = check_difference_jacobian(
        m=2, d_b=1, seed_rows=rows2, weights=weights2)

    # (G3) invertibility of J for m=2: J = r_2 - r_1 (nonzero generic scalar)
    print("  (G3,m=2) J is the 1x1 block r_2 - r_1; invertible iff nonzero:")
    report("(G3,m=2) det J (= r2 - r1)", sp.simplify(sp.det(J2)))
    # W positive: W2 should be the scalar w_1*w_2 = w_1(1-w_1) > 0
    report("(G3,m=2) W - w_1*w_2", sp.simplify(W2[0, 0] - w1_2*(1 - w1_2)))

    # --- m = 3 : two differences, d_b = 2 ------------------------------
    print("\n  -- (G) case m = 3 (d_b = 2) --")
    # symbolic 2-vectors r_1, r_2, r_3 and weights w_1, w_2 (w_3 = 1-w_1-w_2)
    r1a, r1b, r2a, r2b, r3a, r3b = sp.symbols(
        'r1a r1b r2a r2b r3a r3b', real=True)
    w1_3, w2_3 = sp.symbols('w1 w2', positive=True)
    weights3 = [w1_3, w2_3, 1 - w1_3 - w2_3]
    rows3 = [sp.Matrix([r1a, r1b]),
             sp.Matrix([r2a, r2b]),
             sp.Matrix([r3a, r3b])]
    M3, Mhat3, W3, J3, Ibb3 = check_difference_jacobian(
        m=3, d_b=2, seed_rows=rows3, weights=weights3)

    # (G1) explicit det M = w_1 for m=3 already verified inside the helper.
    # (G3) W positive definite: verify W3 = Mhat3^T D Mhat3 has det = w_1*w_2*w_3
    #      (Cauchy-Binet style identity) and is symmetric.
    print("  (G3,m=3) W symmetric and det W = w_1 w_2 w_3:")
    report("(G3,m=3) W - W^T", sp.simplify(W3 - W3.T))
    report("(G3,m=3) det W - w_1 w_2 w_3",
           sp.simplify(sp.det(W3) - weights3[0]*weights3[1]*weights3[2]))

    # (G3,m=3) invertibility of J: for generic symbolic 2-vectors r_1,r_2,r_3
    # the difference Jacobian J = [r_2-r_1 | r_3-r_1] is invertible iff its
    # determinant is nonzero (generic).  We exhibit det J as a nonzero
    # polynomial in the row entries (it is not identically zero), which is
    # exactly the statement "J invertible for minimal exponential families".
    detJ3 = sp.simplify(sp.det(J3))
    print("  (G3,m=3) det J (must be a nonzero polynomial, not identically 0):")
    print("    det J =", detJ3)
    # Check: det J must not be identically zero.  Report a boolean
    # flag (1 = nonzero polynomial, as required; 0 = degenerate failure).
    detJ3_is_nonzero = sp.Integer(1) if sp.expand(detJ3) != 0 else sp.Integer(0)
    report("(G3,m=3) det J is a nonzero polynomial  (1 = OK, must be 1)",
           detJ3_is_nonzero)

    # Final symbolic confirmation of Step (d): for u != 0,
    #   u^T I_bb u = u^T (J W J^T) u = (J^T u)^T W (J^T u) >= 0,
    # and it is > 0 because W > 0 and J^T u != 0 (J invertible).  We verify the
    # algebraic identity  (J^T u)^T W (J^T u) - u^T (J W J^T) u = 0.
    print("  (G,m=3) Step (d) identity  (J^T u)^T W (J^T u) - u^T(J W J^T)u = 0:")
    u3 = sp.Matrix(sp.symbols('u1 u2', real=True))
    quad_lhs = (J3.T*u3).T * W3 * (J3.T*u3)
    quad_rhs = u3.T * (J3 * W3 * J3.T) * u3
    report("(G,m=3) Step (d) quadratic-form identity",
           sp.simplify((quad_lhs - quad_rhs)[0]))

    # ==============================================================
    # Final verdict
    # ==============================================================
    print("\n" + "=" * 60)
    if _RESIDUAL_FAILURES or detJ3_is_nonzero != 1:
        print(f"  SYMBOLIC FAIL: {len(_RESIDUAL_FAILURES)} nonzero residual(s):")
        for lbl, v in _RESIDUAL_FAILURES:
            print(f"    [FAIL] {lbl}: {v}")
        if detJ3_is_nonzero != 1:
            print("    [FAIL] det J (m=3) is identically zero (J NOT invertible)")
        _restore_stdout()
        sys.exit(1)
    elif _NONDETERMINISTIC_ZEROS:
        # All residuals vanished, but at least one verdict rested on the
        # randomized Schwartz-Zippel branch rather than an exact decision.
        # For a verification artifact this distinction is mandatory: we do
        # NOT claim a proof in this case.
        print("  SYMBOLIC PASS (PROBABILISTIC): all residuals vanished, but the")
        print(f"  zero-verdict for {len(_NONDETERMINISTIC_ZEROS)} residual(s) rested")
        print("  on the randomized Schwartz-Zippel test, NOT on an exact decision:")
        for lbl, _ in _NONDETERMINISTIC_ZEROS:
            print(f"    [PROBABILISTIC] {lbl}")
        print("  These are not certified as identities. Re-run / strengthen the")
        print("  exact branch before citing this as a symbolic proof.")
        _restore_stdout()
        sys.exit(2)
    else:
        print("  SYMBOLIC PASS (PROVEN): every residual was decided exactly")
        print("  (rational/polynomial normal form), with no reliance on the")
        print("  randomized Schwartz-Zippel branch; det J (m=3) is a nonzero")
        print("  polynomial (J invertible). No probabilistic verdicts were used.")
        _restore_stdout()
        sys.exit(0)


if __name__ == "__main__":
    main()
