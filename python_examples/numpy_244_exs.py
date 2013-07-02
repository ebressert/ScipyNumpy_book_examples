import numpy as np
from numpy.polynomial import polynomial as P
import matplotlib.pyplot as plt

x = np.linspace(0, 8 * np.pi, 50)
y1 = np.cos(x)
y2 = np.sin(x - np.pi)

# Fitting data
coeff, stats = P.polyfit(x, y1, 20, full=True)
roots = np.real(P.polyroots(coeff))
fit = P.Polynomial(coeff)
yf1 = fit(x)

# Differentiating fitted polynomial
new_coeff = P.polyder(coeff)
dfit = P.Polynomial(new_coeff)
yf2 = dfit(x)

# Plotting results for illustration
fig = plt.figure(figsize=(8,6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.set_title('Data and fitting')
ax2.set_title('Differentiation')

ax1.set_xlim(0, x.max())
ax2.set_xlim(0, x.max())
ax1.set_ylim(-1.25, 1.25)
ax2.set_ylim(-1.25, 1.25)

ax1.plot(x, yf1, label='Fitted', color='gray')
ax1.scatter(x, y1, label='Original', edgecolor='none', facecolor='red')
ax1.scatter(roots, np.zeros(roots.shape), facecolor='none', edgecolor='black', s=50)

ax2.plot(x, yf2, label='Differentiated', color='gray')
ax2.scatter(x, y2, label='Original', edgecolor='none', facecolor='red')

fig.savefig('polynomials.png')
