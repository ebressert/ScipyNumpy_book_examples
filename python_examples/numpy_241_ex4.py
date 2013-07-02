import numpy as np

# Create an array with randomly valued elements
array = np.random.rand(10000).reshape((100, 100))

# Throw NaNs in random places in an array
rindex = np.random.randint(2, size=(100, 100))
array[rindex] = np.nan

# Creating index of non-NaN values
not_nan = ~np.isnan(array)

# Now using functions that cannot handle NaNs, which
# returns the correct standard deviation value.
print(np.std(array[not_nan]))
# 0.288336362007

