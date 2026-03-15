import numpy as np
import matplotlib.pyplot as plt


# Keep math labels and minus signs readable.
plt.rcParams["font.sans-serif"] = ["SimSun", "Microsoft YaHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.size"] = 18


def main() -> None:
	fig = plt.figure(figsize=(8, 7))
	ax = fig.add_subplot(111, projection="3d")

	# Coordinate range: no unit ticks, only key z labels.
	axis_lim = 1.45
	z_min, z_max = -2.6 * np.pi, 2.6 * np.pi

	# Hide default panes/ticks for a clean custom coordinate system.
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	ax.grid(False)
	ax.xaxis.pane.set_alpha(0.0)
	ax.yaxis.pane.set_alpha(0.0)
	ax.zaxis.pane.set_alpha(0.0)

	# Draw custom 3D axes.
	ax.plot([-axis_lim, axis_lim], [0, 0], [0, 0], color="black", linewidth=1.3)
	ax.plot([0, 0], [-axis_lim, axis_lim], [0, 0], color="black", linewidth=1.3)
	ax.plot([0, 0], [0, 0], [z_min, z_max], color="black", linewidth=1.3)

	# Axis labels required by the text.
	ax.text(axis_lim + 0.08, 0, 0, r"$1$", fontsize=18)
	ax.text(0, axis_lim + 0.08, 0, r"$\mathrm{i}$", fontsize=18)
	ax.text(0.20, 0.16, z_max - 0.08 * np.pi, r"$\arg z$", fontsize=18)

	# z-axis marks at ±pi and ±2pi (without unit length ticks).
	z_marks = [
		(-2 * np.pi, r"$-2\pi$"),
		(-np.pi, r"$-\pi$"),
		(np.pi, r"$\pi$"),
		(2 * np.pi, r"$2\pi$"),
	]
	tick_half = 0.06
	for zv, label in z_marks:
		ax.plot([-tick_half, tick_half], [0, 0], [zv, zv], color="black", linewidth=1.0)
		ax.text(0.12, 0.03, zv, label, fontsize=18)

	# Complex plane xOy.
	plane_range = np.linspace(-axis_lim, axis_lim, 2)
	xx, yy = np.meshgrid(plane_range, plane_range)
	zz = np.zeros_like(xx)
	ax.plot_surface(xx, yy, zz, color="#8ecae6", alpha=0.18, edgecolor="none")

	# Horizontal reference planes at key phase levels.
	plane_xy = np.linspace(-axis_lim, axis_lim, 2)
	px, py = np.meshgrid(plane_xy, plane_xy)
	for zv in (-2 * np.pi, -np.pi, np.pi, 2 * np.pi):
		pz = np.full_like(px, zv)
		ax.plot_surface(px, py, pz, color="#adb5bd", alpha=0.08, edgecolor="none")

	# Extended unwrapped branch on r=1 cylinder: z = theta, theta in [-2.4pi, 2.4pi].
	theta = np.linspace(-2.4 * np.pi, 2.4 * np.pi, 1400)
	xh = np.cos(theta)
	yh = np.sin(theta)
	zh = theta
	ax.plot(xh, yh, zh, color="#d62828", linewidth=2.8)

	# Mark the principal value at (1, 0, 0): arg(1)=0.
	ax.scatter([1], [0], [0], color="#d62828", s=36)
	#ax.text(1.07, 0.05, 0.2, r"$\arg(1)=0$", color="#d62828", fontsize=18)

	# Highlight points at z = ±pi, ±2pi on the helix.
	key_t = np.array([-2 * np.pi, -np.pi, np.pi, 2 * np.pi])
	ax.scatter(np.cos(key_t), np.sin(key_t), key_t, color="#d62828", s=24)

	ax.set_xlim(-axis_lim, axis_lim)
	ax.set_ylim(-axis_lim, axis_lim)
	ax.set_zlim(z_min, z_max)
	ax.set_box_aspect((1, 1, 1.75))

	# Oblique top view.
	ax.view_init(elev=13, azim=-70)

	plt.tight_layout()
	plt.show()


if __name__ == "__main__":
	main()
