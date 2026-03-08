import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update(
	{
		"font.size": 20,
		"axes.titlesize": 20,
		"font.sans-serif": ["Microsoft YaHei", "SimHei", "Noto Sans CJK SC", "DejaVu Sans"],
		"axes.unicode_minus": False,
	}
)


def draw_arrow_axes(ax, xlim, ylim, y_axis_x=0.0):
	"""Draw Cartesian axes with arrowheads and hide the default frame."""
	for spine in ax.spines.values():
		spine.set_visible(False)
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_xlim(xlim)
	ax.set_ylim(ylim)

	ax.annotate(
		"",
		xy=(xlim[1], 0),
		xytext=(xlim[0], 0),
		arrowprops=dict(arrowstyle="->", lw=1.6, color="black"),
		clip_on=False,
	)
	ax.annotate(
		"",
		xy=(y_axis_x, ylim[1]),
		xytext=(y_axis_x, ylim[0]),
		arrowprops=dict(arrowstyle="->", lw=1.6, color="black"),
		clip_on=False,
	)


def place_axis_labels(ax, ylabel_text, xlabel_text=r"$\Omega$", y_axis_x=0.0):
	"""Place x/y labels near axis arrowheads to mimic textbook style."""
	xlim = ax.get_xlim()
	ax.annotate(
		xlabel_text,
		xy=(xlim[1], 0),
		xytext=(-8, -10),
		textcoords="offset points",
		ha="right",
		va="top",
	)
	ax.annotate(
		ylabel_text,
		xy=(y_axis_x, 1.0),
		xycoords=("data", "axes fraction"),
		xytext=(8, -2),
		textcoords="offset points",
		ha="left",
		va="top",
	)


def place_k_labels(ax, x_positions, k_labels):
	"""Write discrete index labels below x-axis without using default ticks."""
	for x_pos, kv in zip(x_positions, k_labels):
		ax.annotate(
			f"{kv}",
			xy=(x_pos, 0),
			xytext=(0, -12),
			textcoords="offset points",
			ha="center",
			va="top",
			fontsize=16,
		)


# x[n] length N=8; choose an arbitrary nontrivial sequence.
N = 8
x = np.array([1.0, 0.7, -0.3, 1.2, 0.5, -0.8, 0.9, 0.2])

# y[n] is zero-padded to length 2N.
y = np.concatenate([x, np.zeros(N)])

n = np.arange(N)
omega = np.linspace(-np.pi, np.pi, 2000)
X_dtft = np.exp(-1j * np.outer(omega, n)) @ x
abs_X_dtft = np.abs(X_dtft)

# DFT samples indexed by k = 0, 1, ..., N-1 (or 2N-1).
Xk = np.fft.fft(x, n=N)
k_x = np.arange(N)
x_plot_x = -np.pi + (2 * np.pi / N) * k_x

Yk = np.fft.fft(y, n=2 * N)
k_y = np.arange(2 * N)
x_plot_y = -np.pi + (2 * np.pi / (2 * N)) * k_y

# Dashed DTFT references projected onto k-axis.
k_dense_x = np.linspace(0, N, 1400)
omega_dense_x = 2 * np.pi * k_dense_x / N
X_dtft_on_kx = np.abs(np.exp(-1j * np.outer(omega_dense_x, n)) @ x)
x_dense_plot_x = -np.pi + (2 * np.pi / N) * k_dense_x

k_dense_y = np.linspace(0, 2 * N, 2000)
omega_dense_y = 2 * np.pi * k_dense_y / (2 * N)
X_dtft_on_ky = np.abs(np.exp(-1j * np.outer(omega_dense_y, n)) @ x)
x_dense_plot_y = -np.pi + (2 * np.pi / (2 * N)) * k_dense_y

fig, axes = plt.subplots(3, 1, figsize=(10, 12), constrained_layout=True)

xlim = (-1.08 * np.pi, 1.08 * np.pi)

# 1) DTFT magnitude
ax = axes[0]
ymax1 = 1.15 * np.max(abs_X_dtft)
draw_arrow_axes(ax, xlim=xlim, ylim=(-0.08 * ymax1, ymax1))
ax.plot(omega, abs_X_dtft, color="black", lw=2.0)
ax.axvline(np.pi, color="gray", ls="--", lw=1.5)
ax.axvline(-np.pi, color="gray", ls="--", lw=1.5)
ax.annotate(r"$-\pi$", xy=(-np.pi, 0), xytext=(0, -12), textcoords="offset points", ha="center", va="top")
ax.annotate(r"$\pi$", xy=(np.pi, 0), xytext=(0, -12), textcoords="offset points", ha="center", va="top")
place_axis_labels(ax, r"$|X(e^{i\Omega})|$", xlabel_text=r"$\Omega$", y_axis_x=0.0)

# 2) DFT of x[n] with DTFT dashed reference
ax = axes[1]
ymax2 = 1.15 * max(np.max(np.abs(Xk)), np.max(abs_X_dtft))
xlim2 = (-1.08 * np.pi, 1.08 * np.pi)
draw_arrow_axes(ax, xlim=xlim2, ylim=(-0.08 * ymax2, ymax2), y_axis_x=-np.pi)
ax.plot(x_dense_plot_x, X_dtft_on_kx, color="gray", ls="--", lw=1.8)
ax.axvline(0, color="gray", ls="--", lw=1.5)
ax.axvline(np.pi, color="gray", ls="--", lw=1.5)
markerline, stemlines, _ = ax.stem(
	x_plot_x,
	np.abs(Xk),
	linefmt="C0-",
	markerfmt="C0o",
	basefmt=" ",
)
plt.setp(stemlines, linewidth=2.0)
plt.setp(markerline, markersize=7)
place_axis_labels(ax, r"$|X[k]|$", xlabel_text=r"$k$", y_axis_x=-np.pi)
place_k_labels(ax, x_plot_x, k_x)

# 3) DFT of y[n] with DTFT dashed reference
ax = axes[2]
ymax3 = 1.15 * max(np.max(np.abs(Yk)), np.max(abs_X_dtft))
xlim3 = (-1.08 * np.pi, 1.08 * np.pi)
draw_arrow_axes(ax, xlim=xlim3, ylim=(-0.08 * ymax3, ymax3), y_axis_x=-np.pi)
ax.plot(x_dense_plot_y, X_dtft_on_ky, color="gray", ls="--", lw=1.8)
ax.axvline(0, color="gray", ls="--", lw=1.5)
ax.axvline(np.pi, color="gray", ls="--", lw=1.5)
markerline, stemlines, _ = ax.stem(
	x_plot_y,
	np.abs(Yk),
	linefmt="C1-",
	markerfmt="C1o",
	basefmt=" ",
)
plt.setp(stemlines, linewidth=1.8)
plt.setp(markerline, markersize=5.5)
place_axis_labels(ax, r"$|Y[k]|$", xlabel_text=r"$k$", y_axis_x=-np.pi)
place_k_labels(ax, x_plot_y, k_y)

plt.show()
