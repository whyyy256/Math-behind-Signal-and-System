import matplotlib.pyplot as plt
import numpy as np

# Create two-panel plot
fig, (ax, ax_fr) = plt.subplots(1, 2, figsize=(12, 6))

# Set up the plot limits and labels
ax.axhline(0, color='black', linewidth=1.6)
ax.axvline(0, color='black', linewidth=1.6)
ax.set_xlabel('Re(s)', fontsize=18)
ax.set_ylabel('Im(s)', fontsize=18)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(-4, 2)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')

# Poles and Zeros
# H(s) = s / ((s+1)*(s+3))
# Zero at s = 0
# Poles at s = -1, s = -3

poles_real = [-1, -3]
poles_imag = [0, 0]
zeros = [0]

# Plot Poles
ax.plot(poles_real, poles_imag, 'rx', markersize=10, markeredgewidth=2, label='Pole')

# Plot Zeros
if zeros:
    ax.plot(zeros, [0] * len(zeros), 'bo', markersize=10, fillstyle='none', markeredgewidth=2, label='Zero')

ax.legend(loc='upper right', fontsize=14)
ax.text(0.5, -0.14, '(a)', transform=ax.transAxes, ha='center', va='top', fontsize=18)

# Right panel: magnitude response of H(s) = s / ((s + 1) * (s + 3))
omega = np.linspace(0, 20, 4000)
s = 1j * omega
H = s / ((s + 1) * (s + 3))
H_mag = np.abs(H)

ax_fr.plot(omega, H_mag, color='tab:blue', linewidth=2.2)

ymax = 1.08 * np.max(H_mag)
ax_fr.set_xlim(0, 20)
ax_fr.set_ylim(-0.08 * ymax, ymax)

# Cartesian-style axes without unit ticks
for spine in ax_fr.spines.values():
    spine.set_visible(False)
ax_fr.set_xticks([])
ax_fr.set_yticks([])

xmin, xmax = ax_fr.get_xlim()
ymin, ymax_lim = ax_fr.get_ylim()
axis_arrow = dict(arrowstyle='->', color='black', linewidth=1.6, shrinkA=0, shrinkB=0)
ax_fr.annotate('', xy=(xmax, 0), xytext=(xmin, 0), arrowprops=axis_arrow, clip_on=False)
ax_fr.annotate('', xy=(0, ymax_lim), xytext=(0, ymin), arrowprops=axis_arrow, clip_on=False)

ax_fr.set_xlabel(r'$\omega$', fontsize=18)
ax_fr.set_ylabel(r'$|H(\mathrm{j}\omega)|$', fontsize=18)
ax_fr.text(0.5, -0.14, '(b)', transform=ax_fr.transAxes, ha='center', va='top', fontsize=18)

plt.tight_layout()
# plt.savefig('../Figures/zero_pole_example.pdf')
plt.show()
