from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt

# Defining function to integrate
func = lambda x: np.cos(np.exp(x)) ** 2

# Integrating function with upper and lower
# limits of 0 and 3, respectively
solution = quad(func, 0, 1000)
print solution

# The first element is the desired value
# and the second is the error.

# Plotting output
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
x1 = np.linspace(-1, 4, 10000)
x2 = np.linspace(0, 3, 10000)
ax.plot(x1, func(x1), label='Function')
ax.fill_between(x2, 0, func(x2), alpha=0.2)
ax.set_xlim(-1, 4)
ax.set_ylim(0, 1.05)
fig.savefig('scipy_331_ex1.pdf', bbox_inches='tight')
