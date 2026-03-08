import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({"font.size": 20})


# Zero and poles of H(z)
zero = 0.8 + 0j
poles = np.array([-0.5 + 0.3j, -0.5 - 0.3j])


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ---------------- (a) Pole-zero plot ----------------
# Coordinate axes in z-plane
ax1.axhline(0, color="black", linewidth=1.6)
ax1.axvline(0, color="black", linewidth=1.6)

# Unit circle
theta = np.linspace(0, 2 * np.pi, 600)
ax1.plot(np.cos(theta), np.sin(theta), linestyle="--", color="gray", linewidth=1.8, label="Unit circle")

# Plot zero (small circle) and poles (cross markers)
ax1.plot(
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
ax1.plot(
	np.real(poles),
	np.imag(poles),
	linestyle="None",
	marker="x",
	markersize=11,
	markeredgewidth=2.5,
	color="tab:red",
	label="Poles",
)

# Appearance: no unit ticks/values, equal scaling
ax1.set_aspect("equal", adjustable="box")
ax1.set_xlim(-1.4, 1.4)
ax1.set_ylim(-1.4, 1.4)
ax1.set_xticks([])
ax1.set_yticks([])

ax1.set_xlabel("Re(z)")
ax1.set_ylabel("Im(z)")
ax1.legend(loc="upper right", fontsize=14)
ax1.text(0.5, -0.14, "(a)", transform=ax1.transAxes, ha="center", va="top")

# ---------------- (b) Frequency response ----------------
omega = np.linspace(-np.pi, np.pi, 2000)
z = np.exp(1j * omega)
H = (z - zero) / ((z - poles[0]) * (z - poles[1]))
H_mag = np.abs(H)

ax2.plot(omega, H_mag, color="tab:blue", linewidth=2.2)

ymax = 1.08 * np.max(H_mag)
ax2.set_xlim(-np.pi, np.pi)
ax2.set_ylim(-0.08 * ymax, ymax)

for spine in ax2.spines.values():
	spine.set_visible(False)
ax2.set_xticks([])
ax2.set_yticks([])

xmin, xmax = ax2.get_xlim()
ymin, ymax_lim = ax2.get_ylim()

# Draw axis lines with positive direction markers.
ax2.plot([xmin, xmax], [0, 0], color="black", linewidth=1.6)
ax2.plot([0, 0], [ymin, ymax_lim], color="black", linewidth=1.6)
ax2.plot(xmax, 0, marker=">", color="black", markersize=10, clip_on=False)
ax2.plot(0, ymax_lim, marker="^", color="black", markersize=10, clip_on=False)

# Mark Omega = +/- pi with gray vertical dashed lines and labels.
ax2.axvline(-np.pi, color="gray", linestyle="--", linewidth=1.5)
ax2.axvline(np.pi, color="gray", linestyle="--", linewidth=1.5)
ax2.annotate(r"$-\pi$", xy=(-np.pi, 0), xytext=(0, -12), textcoords="offset points", ha="center", va="top")
ax2.annotate(r"$\pi$", xy=(np.pi, 0), xytext=(0, -12), textcoords="offset points", ha="center", va="top")

ax2.set_xlabel(r"$\Omega$")
ax2.annotate(
	r"$|H(\mathrm{e}^{\mathrm{i}\Omega})|$",
	xy=(0, 1.0),
	xycoords=("data", "axes fraction"),
	xytext=(8, -2),
	textcoords="offset points",
	ha="left",
	va="top",
)
ax2.text(0.5, -0.14, "(b)", transform=ax2.transAxes, ha="center", va="top")

plt.tight_layout()
plt.show()
