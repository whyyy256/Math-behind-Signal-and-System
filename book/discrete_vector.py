import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({"font.size": 20})

# Same pole-zero setting as the left subplot in discrete_zero.py
zero = 0.8 + 0j
poles = np.array([-0.5 + 0.3j, -0.5 - 0.3j])

# Choose a point on the upper unit circle
theta0 = np.pi / 4
endpoint = np.exp(1j * theta0)

fig, ax = plt.subplots(figsize=(7, 7))

# Coordinate axes
ax.axhline(0, color="black", linewidth=1.6)
ax.axvline(0, color="black", linewidth=1.6)

# Unit circle
theta = np.linspace(0, 2 * np.pi, 600)
ax.plot(np.cos(theta), np.sin(theta), linestyle="--", color="gray", linewidth=1.8, label="Unit circle")

# Zero and poles
ax.plot(
    np.real(zero),
    np.imag(zero),
    marker="o",
    markersize=10,
    markerfacecolor="none",
    markeredgewidth=2.2,
    color="tab:blue",
    linestyle="None",
    label="Zero",
)
ax.plot(
    np.real(poles),
    np.imag(poles),
    linestyle="None",
    marker="x",
    markersize=11,
    markeredgewidth=2.5,
    color="tab:red",
    label="Poles",
)

# Mark selected endpoint on unit circle
ax.plot(np.real(endpoint), np.imag(endpoint), "k^", markersize=8)

# Vector from zero to endpoint (blue)
ax.annotate(
    "",
    xy=(np.real(endpoint), np.imag(endpoint)),
    xytext=(np.real(zero), np.imag(zero)),
    arrowprops=dict(arrowstyle="->", color="tab:blue", linewidth=1.8),
)

# Vectors from poles to endpoint (red)
for p in poles:
    ax.annotate(
        "",
        xy=(np.real(endpoint), np.imag(endpoint)),
        xytext=(np.real(p), np.imag(p)),
        arrowprops=dict(arrowstyle="->", color="tab:red", linewidth=1.8),
    )

# Appearance
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-1.4, 1.4)
ax.set_ylim(-1.4, 1.4)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel("Re(z)")
ax.set_ylabel("Im(z)")
ax.legend(loc="upper right", fontsize=14)

plt.tight_layout()
plt.show()
