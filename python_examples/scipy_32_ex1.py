import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# Setting up fake data.
x = np.linspace(0, 10 * np.pi, 20)
y = np.cos(x)

# Interpolating data
fl = interp1d(x, y, kind='linear')
fq = interp1d(x, y, kind='quadratic')

# x.min and x.max are used to make sure we do not
# go beyond the boundaries of the data for the
# interpolation.
xint = np.linspace(x.min(), x.max(), 1000)
yintl = fl(xint)
yintq = fq(xint)

# Plotting output
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
ax.plot(xint, yintl, label='Linear')
ax.plot(xint, yintq, label='Quadratic')
ax.scatter(x, y, marker='o',
           edgecolor='red', facecolor='none', s=50)
ax.legend(loc='upper left')

ax.set_xlim(0, 10 * np.pi)
ax.set_ylim(-2, 2)
fig.savefig('scipy_32_ex1.pdf', bbox_inches='tight')
