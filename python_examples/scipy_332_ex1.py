import numpy as np
from scipy.integrate import quad, trapz
import matplotlib.pyplot as plt

# Setting up fake data.
x = np.sort(np.random.randn(150) * 4 + 4).clip(0, 5)
# x = np.clip()
func = lambda x: np.sin(x) * np.cos(x ** 2) + 1
y = func(x)

# Integrating function with upper and lower
# limits of 0 and 5, respectively.
fsolution = quad(func, 0, 5)
dsolution = trapz(y, x=x)
print('fsolution = ' + str(fsolution[0]))
print('dsolution = ' + str(dsolution))
print('The difference is ' + str(np.abs(fsolution[0] - dsolution)))

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
x1 = np.linspace(-1, 6, 10000)
x2 = np.linspace(0, 5, 10000)

ax.plot(x1, func(x1), label='Function')
ax.fill_between(x2, 0, func(x2), alpha=0.2)
ax.scatter(x, y, marker='o', edgecolor='none', facecolor='red',
			s=7, zorder=3, label='Data points')
ax.legend(loc='upper left')
ax.set_xlim(-1, 6)
ax.set_ylim(0, 2.5)
fig.savefig('scipy_332_ex1.pdf', bbox_inches='tight')
