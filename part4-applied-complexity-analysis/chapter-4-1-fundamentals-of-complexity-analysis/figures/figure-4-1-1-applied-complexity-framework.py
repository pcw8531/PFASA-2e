"""
Figure 4.1.1 — Applied Complexity Analysis Framework.

Produces Figure 4.1.1 in Chapter 4.1, "Fundamentals of Complexity Analysis",
of Park, C. (forthcoming 2027), Practical Foundation of Applied Complexity
Analysis: From Basic Statistics to Nonlinear Dynamics, 2nd ed., CRC Press
/ Taylor & Francis.

The figure presents a schematic of the Applied Complexity Analysis framework,
showing the integration of four methodological corners, namely complex
models, simple models, quantitative methods, and qualitative methods, around
a central integration and synthesis node. Mathematical bridge equations,
bidirectional arrows, and emergence indicators illustrate the relations
across the framework.

Dependencies: numpy, matplotlib.

Usage:
    python figure-4-1-1-applied-complexity-framework.py
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle


def main():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=1000)
    ax.set_xlim(0, 12)
    ax.set_ylim(0.2, 8.2)
    ax.axis('off')

    # Clean white background
    ax.add_patch(plt.Rectangle((0, 0.2), 12, 8.2,
                               facecolor='white', alpha=1.0))

    # Systems principles at the top
    ax.text(6, 8.0, 'Systems Principles & Mathematical Foundations',
            ha='center', va='center',
            fontsize=16, fontweight='bold', color='black')
    ax.text(6, 7.6,
            ' • Nonlinear Dynamics • Emergence • Critical Transitions • Bifurcations',
            ha='center', va='center', fontsize=12, color='black')

    # Four corner methodologies

    # Top-left: Complex Models
    ax.text(2.5, 6.5, 'Complex Models', ha='center', va='center',
            fontsize=16, fontweight='bold', color='black')
    ax.text(2.5, 6.0, 'System Dynamics \n Multi-Agent Networks',
            ha='center', va='center', fontsize=11, color='black')
    ax.text(2.5, 5.3, 'dx/dt = f(x,A,t)', ha='center', va='center',
            fontsize=12, fontfamily='monospace', fontweight='bold',
            color='black')

    # Top-right: Simple Models
    ax.text(9.5, 6.5, 'Simple Models', ha='center', va='center',
            fontsize=16, fontweight='bold', color='black')
    ax.text(9.5, 6.0, 'Iterated Maps \n Logistic Equations',
            ha='center', va='center', fontsize=11, color='black')
    ax.text(9.5, 5.3, 'x_{n+1} = f(x_n)', ha='center', va='center',
            fontsize=12, fontfamily='monospace', fontweight='bold',
            color='black')

    # Bottom-left: Quantitative Methods
    ax.text(2.5, 2.5, 'Quantitative Methods', ha='center', va='center',
            fontsize=16, fontweight='bold', color='black')
    ax.text(2.5, 2.0, 'ODEs/PDEs \nAttractors',
            ha='center', va='center', fontsize=11, color='black')
    ax.text(2.5, 1.3, '∂u/∂t = D∇²u', ha='center', va='center',
            fontsize=12, fontfamily='monospace', fontweight='bold',
            color='black')

    # Bottom-right: Qualitative Methods
    ax.text(9.5, 2.5, 'Qualitative Methods', ha='center', va='center',
            fontsize=16, fontweight='bold', color='black')
    ax.text(9.5, 2.0, 'Dynamical Systems \n Stability Assessment',
            ha='center', va='center', fontsize=11, color='black')
    ax.text(9.5, 1.3, 'λ = ∂f/∂x|_{x*}', ha='center', va='center',
            fontsize=12, fontfamily='monospace', fontweight='bold',
            color='black')

    # Center: integration concept
    ax.text(6, 4.7, 'Applied Complexity', ha='center', va='center',
            fontsize=16, fontweight='bold', color='black')
    ax.text(6, 4.3, 'Integration & Synthesis', ha='center', va='center',
            fontsize=14, fontweight='bold', color='black')
    ax.text(6, 3.8, 'Applications \n Practical Implementations',
            ha='center', va='center', fontsize=12, color='black')

    # Mathematical bridge equations around the center

    # Left side
    ax.text(4.2, 4.0, '∫f(x,t)dt', ha='center', va='center',
            fontsize=14, fontfamily='monospace', fontweight='bold',
            color='black')

    # Right side
    ax.text(7.8, 4.0, 'Σᵢwᵢⱼxⱼ', ha='center', va='center',
            fontsize=14, fontfamily='monospace', fontweight='bold',
            color='black')

    # Top
    ax.text(6, 5.5, 'A(t+1) = g(A,S)', ha='center', va='center',
            fontsize=14, fontfamily='monospace', fontweight='bold',
            color='black')

    # Bottom
    ax.text(6, 3.0, '∇²u + R(u,v)', ha='center', va='center',
            fontsize=14, fontfamily='monospace', fontweight='bold',
            color='black')

    # Arrows from center to top (systems principles)
    ax.annotate('', xy=(6, 7.4), xytext=(6, 5.4),
                arrowprops=dict(arrowstyle='->', lw=3,
                                color='black', alpha=0.8))

    # Arrows from corners to center, with different line styles

    # From complex models (top-left)
    ax.annotate('', xy=(4.8, 4.8), xytext=(3.2, 5.8),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='black',
                                alpha=0.7, linestyle='--'))

    # From simple models (top-right)
    ax.annotate('', xy=(7.2, 4.8), xytext=(8.8, 5.8),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='black',
                                alpha=0.7, linestyle='-.'))

    # From quantitative methods (bottom-left)
    ax.annotate('', xy=(4.8, 3.8), xytext=(3.2, 3.0),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='black',
                                alpha=0.7, linestyle=':'))

    # From qualitative methods (bottom-right)
    ax.annotate('', xy=(7.2, 3.8), xytext=(8.8, 3.0),
                arrowprops=dict(arrowstyle='->', lw=2.5, color='black',
                                alpha=0.7, linestyle='-'))

    # Bidirectional interactions between methodologies

    # Horizontal: Complex ↔ Simple Models
    path1 = mpatches.FancyArrowPatch((3.5, 6.2), (8.5, 6.2),
                                     arrowstyle='<->', mutation_scale=20,
                                     color='gray', linewidth=2, alpha=0.6,
                                     linestyle='--')
    ax.add_patch(path1)
    ax.text(6, 6.4, 'Model Complexity Spectrum',
            ha='center', va='center', fontsize=10,
            color='gray', style='italic')

    # Vertical: Quantitative ↔ Qualitative Methods
    path2 = mpatches.FancyArrowPatch((11.0, 2.0), (11.0, 7.0),
                                     arrowstyle='<->', mutation_scale=20,
                                     color='gray', linewidth=2, alpha=0.6,
                                     linestyle=':')
    ax.add_patch(path2)
    ax.text(10.8, 4.5, 'Analytical Approaches',
            ha='center', va='center', fontsize=12,
            color='gray', style='italic', rotation=90)

    # Diagonal: Quantitative-Simple to Qualitative-Complex
    path3 = mpatches.FancyArrowPatch((8.8, 2.8), (3.2, 5.8),
                                     arrowstyle='<->', mutation_scale=20,
                                     color='gray', linewidth=2, alpha=0.6,
                                     linestyle='-.',
                                     connectionstyle='arc3,rad=0.3')
    ax.add_patch(path3)

    # Complexity progression indicators
    complexity_levels = [
        (1, 7.5, 'High\nComplexity', '#808080'),
        (1, 1.5, 'Low\nComplexity', '#808080'),
    ]

    for x, y, text, color in complexity_levels:
        ax.text(x, y, text, ha='center', va='center',
                fontsize=12, fontweight='bold', color=color)

    # Complexity flow arrow
    ax.annotate('', xy=(1, 2.0), xytext=(1, 7.0),
                arrowprops=dict(arrowstyle='<->', lw=2,
                                color='gray', alpha=0.6))

    # Mathematical symbols around the framework
    math_symbols = [
        (0.5, 8.0, '∂'),
        (0.5, 6.0, '∫'),
        (0.5, 4.0, '∇'),
        (0.5, 2.0, 'Σ'),
        (11.5, 8.0, 'λ'),
        (11.5, 6.0, 'μ'),
        (11.5, 4.0, 'ω'),
        (11.5, 2.0, 'α'),
    ]

    for x, y, symbol in math_symbols:
        ax.text(x, y, symbol, ha='center', va='center',
                fontsize=16, fontweight='bold', color='black', alpha=0.5)

    # Emergence indicators
    emergence_points = [(4.5, 5.8), (7.5, 5.8), (4.5, 2.8), (7.5, 2.8)]
    for x, y in emergence_points:
        circle = Circle((x, y), 0.08,
                        facecolor='black', edgecolor='gray',
                        linewidth=1, alpha=0.6)
        ax.add_patch(circle)

    # Bottom caption line
    ax.text(6, 0.6,
            'Comprehensive Framework for Understanding and Modeling Complex Systems',
            ha='center', va='center',
            fontsize=14, color='black', style='italic')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
