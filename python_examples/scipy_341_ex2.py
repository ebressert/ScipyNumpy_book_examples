import numpy as np
from scipy.stats import norm

# Setup the sample range
x = np.linspace(-5, 5, 1000)

# Here set up the parameters for the normal distribution.
# where loc is the mean and scale is the standard deviation.
dist = norm(loc=0, scale=1)

# Calling norm's PDF and CDF
pdf = dist.pdf(x)
cdf = dist.cdf(x)

# Here we draw out 500 random values from
sample = dist.rvs(500)
