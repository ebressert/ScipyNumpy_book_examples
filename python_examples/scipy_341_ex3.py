import numpy as np
from scipy.stats import geom 
	
# Here set up the parameters for the normal distribution. 
# where loc is the mean and scale is the standard deviation.
p = 0.5
dist = geom(p)

# Setup the sample range
x = np.linspace(0, 5, 1000)

# Calling norm's PMF and CDF
pmf = dist.pmf(x)
cdf = dist.cdf(x)

# Here we draw out 500 random values from 
sample = dist.rvs(500)