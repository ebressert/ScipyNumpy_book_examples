import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Let's create a function to model and create data
def func(x, a0, b0, c0, a1, b1, c1):
    return a0 * np.exp(-(x - b0) ** 2 / (2 * c0 ** 2))\
    + a1 * np.exp(-(x - b1) ** 2 / (2 * c1 ** 2))

# Generating clean data
x = np.linspace(0, 20, 200)
y = func(x, 1, 3, 1, -2, 15, 0.5)
# y2 = func(x[np.where(x > 10)], 0, 1, 1, -2, 15,0.5)

# Adding noise to the data
yn = y + 0.2 * np.random.normal(size=len(x))

# Plot out the current state of the data and model
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, c='k', label='Function')
ax.scatter(x, yn)

# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn, p0=[1, 3, 1, 1, 15, 1])

#popt returns the best fit values for parameters of the given model (func)
print popt

ym = func(x, popt[0], popt[1], popt[2], popt[3], popt[4], popt[5])
ax.plot(x, ym, c='r', label='Best fit')
ax.legend()
fig.savefig('scipy_311_ex3.pdf', bbox_inches='tight')
