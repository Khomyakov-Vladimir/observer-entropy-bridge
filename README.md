# Observer Entropy — Bridge Theorem (Numerical Verification)

This repository provides numerical verification of the Bridge Theorem:

S_obs = 1/2 eps^2 v^T I(theta*) v + O(eps^3)

where I(theta) denotes the Fisher information matrix.

The verification is performed for a softmax family on a 4-point discrete space with a fixed partition structure. The results confirm quadratic Fisher scaling and bounded O(eps^3) remainder.

---

## Repository Structure

```
observer-entropy-bridge/
│
├── LICENSE
├── README.md
├── requirements.txt
├── scripts/
│      └── verify_bridge_theorem.py
└── figures/
       ├── fig1_bridge_theorem_verification.pdf
       ├── fig2_relative_error.pdf
       └── fig3_resolution_information_tradeoff.pdf
```

---

## Requirements

Python 3.9+

Dependencies are specified in `requirements.txt`.

Install with:

```
pip install -r requirements.txt
```

---

## Running the Verification

From the repository root:

```
python scripts/verify_bridge_theorem.py
```

The script:

- verifies the Fisher information at the reference point,
- checks agreement between analytic and Fisher-based predictions,
- computes relative errors,
- confirms bounded O(eps^3) remainder,
- evaluates the associated Landauer bound,
- generates figures in `figures/`.

Output figures are written to:

```
figures/
```

The script is independent of the current working directory and may also be executed from within the `scripts/` directory.

---

## Generated Figures

- **Figure 1** — Exact vs predicted scaling and normalized remainder.
- **Figure 2** — Relative error of the quadratic approximation.
- **Figure 3** — Resolution–information trade-off.

---

## Scientific Context

The Bridge Theorem establishes a local Fisher-geometric expansion of observer entropy:

S_obs(p_theta, eps) = 1/2 eps^2 v^T I(theta*) v + O(eps^3)

This repository contains only numerical verification and supporting figures.
The full theoretical development appears in the associated research article.

---

## License

See `LICENSE` file.
