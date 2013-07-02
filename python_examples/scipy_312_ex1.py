import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Defining line function
line = lambda x: x + 3

# Solving for solution
solution = fsolve(line, -2)
print solution

# Plotting output
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
x = np.linspace(-5, 5, 1000)
y = line(x)
ax.hlines(0, -5, 0, color='black', alpha=0.15, linestyle='--')
ax.plot(x, y, label='Function')
ax.scatter(solution[0], 0, marker='o',\
           edgecolor='red', facecolor='none', s=100, label='Root')
ax.legend(loc='upper left')
ax.set_xlim(-4.5, -1.5)
ax.set_ylim(-1.5, 1.5)
fig.savefig('scipy_312_ex1.pdf', bbox_inches='tight')
