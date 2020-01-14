---
marp: true
---

# Reducing Loss

---

## How do we reduce loss

* Hyperparameters are the configuration settings used to tune how the model is trained
* Derivative of $(y - y')^2$ with respect to the weights and biases tells us how oss changes for a given example
  * Simple to compute and convex
* So we repeatedly take samll steps in the direction that minimizes loss
  * We call these **Gradient Septs**
  * This strategy is called **Gradient Descent**

---

## Block Diagram of Gradient Descent

![3-block-diagram-of-gradient-descent](/images/3-block-diagram-of-gradient-descent.png)

---

## Weight Initialization

* For convex problems, wieghts can start anywhere
  * Convex: think of a bowl sahpe
  * Just one minimum
* Foreshadowing: not true for neural nets
  * Non-convexL think of an egg crate
  * More than one minimum
  * Strong dependency on initial values

---

## SGD & Mini-Batch Gradient Descent

* Could compute gradient over entire data set on each step, but this turns out to be unnecessary
* Computing gradient on small data samples works well
  * On every step, get a new random sample
* **Stochastic Gradient Descent**: one example at a time
* **Mini-Batch Gradient Descent**: batches of 10-1000
  * Loss & gradients are averaged over the batch
