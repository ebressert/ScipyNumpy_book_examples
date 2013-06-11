import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt


# Setting up fake data with artifical noise.
sample = 30
x = np.linspace(1, 10 * np.pi, sample)
y = np.cos(x) + np.log10(x) + np.random.randn(sample) / 10

# Interpolating the data.
f = UnivariateSpline(x, y, s=1)

# x.min and x.max are used to make sure we do not
# go beyond the boundaries of the data for the
# interpolation.
xint = np.linspace(x.min(), x.max(), 1000)
yint = f(xint)
yclean = np.cos(xint) + np.log10(xint)

# Making figure.
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
ax.plot(xint, yint, label='Interpolation')
ax.plot(xint, yclean, label='Original', c='orange')
ax.scatter(x, y, marker='o',
			edgecolor='none', facecolor='black', s=20)
ax.legend(loc='upper left')

ax.set_xlim(1, 10 * np.pi)
fig.savefig('scipy_32_ex2.pdf', bbox_inches='tight')
