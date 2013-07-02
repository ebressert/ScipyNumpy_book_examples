import numpy as np

# Hyperbolic cotangent
coth = lambda x: 1 / np.tanh(x)

# Hyperbolic secant
sech = lambda x: 2 / (np.exp(x) - np.exp(-x))

# An inverse hyperbolic cosecant
arccsch = lambda x: np.log(1 / x + np.sqrt(1 + x ** 2) / np.abs(x))