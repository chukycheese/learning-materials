---
marp: true
---

# Training Neural Nets

---

## Backprop: What You Need to Know

* Gradients are important
  * If it's differentiable, we can probably learn on it
* Gradients can vanish
  * Each additional layer can successively reduce signal vs noise
  * ReLUs are useful here
