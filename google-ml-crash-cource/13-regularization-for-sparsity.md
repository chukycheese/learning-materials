---
marp: true
---

# Regularization for Sparsity

---

## Let's Go Back to Feature Crosses

* **Caveat**: Sparse feature crosses may significantly increase feature space
* Possible issues:
  * Model size (RAM) may become huge
  * "Noise" coefficients (causes overfitting)

---

## $L_1$ Regularization

* Would like to penalize $L_0$ norm of weights
  * Non-convex optimization; NP-hard
* Relax to $L_1$ regularization:
  * Penalize sum of `abs(weights)`
  * Convex problem
  * Encourage sparsity unlike $L_2$

---

## $L_1$ vs $L_2$ Regularization

* $L_2$ and $L_1$ penalize weights differently:
  * $L_2$ penalize $weight^2$
  * $L_1$ penalize $|weight|$
* Consequently, $L_2$ and $L_1$ have different derivatives:
  * The derivative of $L_2$ is $2 \times weight$
  * The derivative of $L_1$ is $k$ (a constant, whose value is independent of weight)

---

## Programming Exercise

[Sparsity and $L_1$ Regularization programming exercise](https://colab.research.google.com/notebooks/mlcc/sparsity_and_l1_regularization.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=l1regularization-colab&hl=en)
