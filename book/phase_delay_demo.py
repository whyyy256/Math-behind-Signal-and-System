import numpy as np
import matplotlib.pyplot as plt


plt.rcParams["font.sans-serif"] = ["SimSun"]
plt.rcParams["axes.unicode_minus"] = False


# Single-tone input and system phase-delay parameters
Omega = 0.20 * np.pi
A = 1.0
tau_p = 2.3  # phase delay in samples (can be non-integer)

n = np.arange(0, 25)
n_cont = np.linspace(n.min(), n.max(), 1000)

# Input: x[n] = cos(Omega n)
x = np.cos(Omega * n)
x_cont = np.cos(Omega * n_cont)

# Steady-state response: y_ss[n] = A cos(Omega (n - tau_p))
y = A * np.cos(Omega * (n - tau_p))
y_cont = A * np.cos(Omega * (n_cont - tau_p))

fig, axes = plt.subplots(2, 1, figsize=(10, 6), sharey=True)

# Top panel: input signal
axes[0].plot(n_cont, x_cont, color="0.55", linewidth=1.2)
markerline, stemlines, baseline = axes[0].stem(n, x, linefmt="C0-", markerfmt="C0o", basefmt="k-")
plt.setp(stemlines, linewidth=1.3)
plt.setp(markerline, markersize=4)
axes[0].set_xlim(n.min() - 1, n.max() + 1)
axes[0].set_ylim(-1.2, 1.2)
axes[0].set_title("输入单频离散信号", fontsize=20)
axes[0].set_xticks([])
axes[0].set_yticks([])
axes[0].grid(False)

# Bottom panel: steady-state response with envelope reference curves
# Draw the same envelope curve from subplot 1 and the response envelope as dashed gray.
axes[1].plot(n_cont, x_cont, color="0.55", linewidth=1.2)
axes[1].plot(n_cont, y_cont, color="0.55", linestyle="--", linewidth=1.2)
markerline, stemlines, baseline = axes[1].stem(n, y, linefmt="C1-", markerfmt="C1o", basefmt="k-")
plt.setp(stemlines, linewidth=1.3)
plt.setp(markerline, markersize=4)
axes[1].set_xlim(n.min() - 1, n.max() + 1)
axes[1].set_ylim(-1.2, 1.2)
axes[1].set_title(rf"稳态响应", fontsize=20)
axes[1].set_xticks([])
axes[1].set_yticks([])
axes[1].grid(False)

fig.tight_layout()

plt.show()
