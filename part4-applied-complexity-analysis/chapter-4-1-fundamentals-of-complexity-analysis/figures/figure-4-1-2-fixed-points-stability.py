"""
Figure 4.1.2 — Fixed points and stability analysis.

Produces Figure 4.1.2 in Chapter 4.1, "Fundamentals of Complexity Analysis",
of Park, C. (forthcoming 2027), *Practical Foundation of Applied Complexity
Analysis: From Basic Statistics to Nonlinear Dynamics*, 2nd ed., CRC Press
/ Taylor & Francis.

The figure illustrates the nonlinear system dx/dt = x - x^3. Stable fixed
points at x = +/- 1 are shown as filled circles; the unstable fixed point
at x = 0 is shown as an open circle. Flow arrows indicate the direction of
local dynamics.

Dependencies: numpy, matplotlib.

Usage:
    python figure-4-1-2-fixed-points-stability.py

Output:
    figure-4-1-2.png saved in the same directory as this script.
"""

import os
import numpy as np
import matplotlib.pyplot as plt


def apply_custom_style(ax, xdata, ydata, xlabel, ylabel):
    """Apply the book's standard figure style.

    Parameters
    ----------
    ax : matplotlib Axes
        The axes object to style.
    xdata, ydata : array-like
        Data used to set tick ranges.
    xlabel, ylabel : str
        Axis labels (LaTeX math allowed).
    """
    ax.set_xlabel(xlabel, fontsize=18, color='black')
    ax.set_ylabel(ylabel, fontsize=18, color='black')

    min_x, max_x = xdata.min(), xdata.max()
    ax.set_xticks([min_x, 0, max_x])

    min_y, max_y = ydata.min(), ydata.max()
    ax.set_yticks([min_y, 0, max_y])

    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.grid(True, linestyle='--', alpha=0.5, color='black')
    ax.tick_params(axis='both', which='major', labelsize=12, colors='black')

    tick_formatter = lambda val, _: f'{val:.1f}'
    ax.xaxis.set_major_formatter(plt.FuncFormatter(tick_formatter))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(tick_formatter))


def main():
    # Define the nonlinear system: dx/dt = x - x^3
    x = np.linspace(-2, 2, 500)
    dx_dt = x - x**3

    # Fixed points where dx/dt = 0, with their stability
    fixed_points = [-1, 0, 1]
    stability = ['stable', 'unstable', 'stable']

    # Create the figure
    fig, ax = plt.subplots(figsize=(5, 4), dpi=1000)

    # Plot the dynamics
    ax.plot(x, dx_dt, 'k', linewidth=2.5)
    ax.axhline(0, color='gray', linestyle='-', alpha=0.3)

    # Mark and label fixed points
    for fp, stab in zip(fixed_points, stability):
        # Derivative at fixed point (linearization): f'(x) = 1 - 3x^2
        df_dx = 1 - 3 * fp**2

        if stab == 'stable':
            ax.plot(fp, 0, 'o', color='black', markersize=10,
                    markerfacecolor='grey')
            ax.text(fp, -1.4, f'stable\n$f\'({fp})={df_dx}$',
                    ha='center', fontsize=10)
        else:
            ax.plot(fp, 0, 'o', color='black', markersize=10,
                    markerfacecolor='white', markeredgewidth=2)
            ax.text(fp, 0.6, f'unstable\n$f\'({fp})={df_dx}$',
                    ha='center', fontsize=10)

    # Add flow arrows
    arrow_x = [-1.5, -0.5, 0.5, 1.5]
    for ax_pos in arrow_x:
        if ax_pos - ax_pos**3 > 0:
            ax.annotate('', xy=(ax_pos + 0.15, -0.15), xytext=(ax_pos, -0.15),
                        arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        else:
            ax.annotate('', xy=(ax_pos - 0.15, -0.15), xytext=(ax_pos, -0.15),
                        arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

    # Apply standard book style
    apply_custom_style(ax, x, dx_dt, xlabel='$x$', ylabel='$dx/dt$')

    # Add equation annotation
    ax.text(0.4, 0.25, r'$\frac{dx}{dt} = x - x^3$',
            transform=ax.transAxes, fontsize=14,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))

    plt.tight_layout()

    # Save the figure next to the script
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'figure-4-1-2.png')
    plt.savefig(output_path, dpi=1000, bbox_inches='tight')
    print(f'Figure saved to: {output_path}')

    plt.show()


if __name__ == '__main__':
    main()
