# Chapter 4.1 — Fundamentals of Complexity Analysis

Companion code for Chapter 4.1 of *Practical Foundation of Applied Complexity Analysis* (2nd ed.).

---

## Chapter summary

This chapter introduces the foundations of Applied Complexity Analysis, bridging traditional systems analysis and the quantitative study of complex behavior. It covers the core mathematical objects used throughout Part 4: differential equations, iterated maps, phase portraits, attractors, bifurcations, network couplings, and system dynamics. A concrete illustration, the nonlinear system dx/dt = x − x³, demonstrates the analysis of fixed points and stability.

---

## Files in this folder

| File | Description |
|------|-------------|
| `figures/figure-4-1-1-applied-complexity-framework.py` | Produces Figure 4.1.1 (applied complexity analysis framework) |
| `figures/figure-4-1-2-fixed-points-stability.py` | Produces Figure 4.1.2 (fixed points and stability flow diagram) |
| `data/` | Any data files used in the chapter (none required for 4.1) |

---

## How to run

From the repository root:

```bash
cd part4-applied-complexity-analysis/chapter-4-1-fundamentals-of-complexity-analysis

# Figure 4.1.1
python figures/figure-4-1-1-applied-complexity-framework.py

# Figure 4.1.2
python figures/figure-4-1-2-fixed-points-stability.py
```

Each script opens the figure in a matplotlib window.

---

## Key concepts

- **Linear and nonlinear systems**: the superposition principle and its violation
- **Fixed points**: equilibrium states where dx/dt = 0
- **Linearization**: stability analysis via the Jacobian matrix
- **Phase portraits**: geometric representation of system dynamics

---

## Dependencies

Requires `numpy` and `matplotlib`. See the root `requirements.txt`.

---

## Related chapters

- Chapter 4.8 develops dynamical systems in depth
- Chapter 4.9 covers phase diagrams
- Chapter 4.10 covers attractors in detail
- Chapter 4.12 develops bifurcation analysis (referenced in footnote 3 of this chapter)
