import matplotlib.pyplot as plt
import numpy as np

# Define points
zeros = [1+0j]           # zero at 1
poles = [-2+0j, -3+0j]   # poles at -2 and -3
endpoint = 0+5j          # vector endpoint at 5i

# Create two-panel plot
fig, (ax, ax_fr) = plt.subplots(1, 2, figsize=(12, 6))

# Plot axes
ax.axhline(0, color='black', linewidth=1.6)
ax.axvline(0, color='black', linewidth=1.6)

# Plot zeros and poles
ax.plot([z.real for z in zeros], [z.imag for z in zeros], 'bo', markersize=10, markeredgewidth=2, fillstyle='none', label='Zero')
ax.plot([p.real for p in poles], [p.imag for p in poles], 'rx', markersize=10, markeredgewidth=2, label='Pole')

# Plot endpoint (no legend entry)
ax.plot(endpoint.real, endpoint.imag, 'k^', markersize=8)

# Draw vectors from each zero/pole to endpoint
for z in zeros:
    # zero vectors in blue
    ax.annotate('', xy=(endpoint.real, endpoint.imag), xytext=(z.real, z.imag),
                arrowprops=dict(arrowstyle='->', color='blue', linewidth=1.8))
for p in poles:
    # pole vectors in red
    ax.annotate('', xy=(endpoint.real, endpoint.imag), xytext=(p.real, p.imag),
                arrowprops=dict(arrowstyle='->', color='red', linewidth=1.8))

# Labels and appearance
# increase axis label font size
ax.set_xlabel('Re(s)', fontsize=18)
ax.set_ylabel('Im(s)', fontsize=18)
# hide numeric ticks but keep axis lines
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

# Set limits to include all points comfortably
all_re = [z.real for z in zeros] + [p.real for p in poles] + [endpoint.real]
all_im = [z.imag for z in zeros] + [p.imag for p in poles] + [endpoint.imag]
pad_re = (max(all_re) - min(all_re)) * 0.5 + 1
pad_im = (max(all_im) - min(all_im)) * 0.2 + 1
ax.set_xlim(min(all_re)-pad_re, max(all_re)+pad_re)
ax.set_ylim(min(all_im)-pad_im, max(all_im)+pad_im)

ax.legend(loc='upper right', fontsize=14)
ax.text(0.5, -0.14, '(a)', transform=ax.transAxes, ha='center', va='top', fontsize=18)

# Right panel: frequency response magnitude of H(s) = (s-1)/((s+2)(s+3))
omega = np.linspace(0, 20, 4000)
s = 1j * omega
H = (s - 1) / ((s + 2) * (s + 3))
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
plt.show()
