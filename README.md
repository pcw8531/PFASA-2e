# Practical Foundation of Applied Complexity Analysis (Second Edition)

Companion code and supplementary materials for:

**Park, C. (forthcoming 2027). *Practical Foundation of Applied Complexity Analysis: From Basic Statistics to Nonlinear Dynamics*, Second Edition. CRC Press / Taylor & Francis.**

This repository supports the second edition of the book, which extends the first edition (Seoul National University Press, 2024) with a new Part 4 on Applied Complexity Analysis and expanded coverage throughout.

---

## About the book

The book provides a practical, quantitatively grounded treatment of complexity science for graduate students and researchers across interdisciplinary fields. It builds systematically from basic statistics through linear models and systems analysis to the mathematical foundations of complex behavior, including nonlinear dynamics, iterated maps, phase portraits, attractors, bifurcations, network topology, complex adaptive systems, evolutionary game theory, and system dynamics.

Every chapter pairs conceptual explanation with runnable Python code, so readers can reproduce the figures, extend the models, and adapt them to their own work.

---

## Repository structure

| Part | Topic | Status |
|------|-------|--------|
| Part 1 | Basic Statistics | ⏳ planned |
| Part 2 | Linear Models | ⏳ planned |
| Part 3 | Applied Systems Analysis | ⏳ planned |
| Part 4 | Applied Complexity Analysis | 🔄 in progress |
| Supplementary | Programming, notation, modeling, algorithms, and more | ⏳ planned |

---

## Quick start

```bash
# Clone the repository
git clone https://github.com/pcw8531/PFASA-2e.git
cd PFASA-2e

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run a chapter example, for instance Chapter 4.1
cd part4-applied-complexity-analysis/chapter-4-1-fundamentals-of-complexity-analysis
python figures/figure-4-1-2-fixed-points-stability.py
```

---

## How to cite

If this code has been useful in your research or teaching, please cite the book:

```
Park, C. (forthcoming 2027). Practical Foundation of Applied Complexity 
Analysis: From Basic Statistics to Nonlinear Dynamics, Second Edition. 
CRC Press / Taylor & Francis.
```

A machine-readable citation entry is available in `CITATION.cff`.

---

## First edition

The first edition of this book was published by Seoul National University Press in 2024, with companion code available at [github.com/pcw8531/PFASA](https://github.com/pcw8531/PFASA). The first edition remains in print and continues to serve its original audience. The present repository accompanies the second edition, which substantially expands the material with a new Part 4 and extended coverage across all parts.

---

## License

The code in this repository is released under the MIT License (see `LICENSE`).

The book text is copyright © Chulwook Park and is published by CRC Press / Taylor & Francis. Nothing in this repository reproduces book prose beyond brief technical comments required for code documentation.

---

## Contact

**Chulwook Park**  
Associate Professor, Seoul National University  
Email: pcw8531@snu.ac.kr

Issues and pull requests are welcome.
