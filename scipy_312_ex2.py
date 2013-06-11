import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Defining function to simplify intersection solution
def findIntersection(func1, func2, x0):
    return fsolve(lambda x: func1(x) - func2(x), x0)

# Defining functions that will intersect
funky = lambda x: np.cos(x / 5) * np.sin(x / 2)
line = lambda x: 0.01 * x - 0.5

# Defining range and getting solutions on intersection points
x = np.linspace(0, 45, 10000)
result = findIntersection(funky, line, [15, 20, 30, 35, 40, 45])

# Plotting ouptut
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
ax.plot(x, funky(x), label='Funky func')
ax.plot(x, line(x), label='Line func')
ax.scatter(result, line(result), marker='o',
           edgecolor='red', facecolor='none', s=100)
ax.legend(loc='lower left')
ax.set_xlim(0, 45)
ax.set_ylim(-1, 1)
fig.savefig('scipy_312_ex2.pdf', bbox_inches='tight')
