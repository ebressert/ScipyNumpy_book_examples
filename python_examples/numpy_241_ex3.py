import numpy as np

array = np.random.rand(100)
array[5] = np.nan

# Returns inccorrect result
print(np.max(array))
# nan

# Returns correct result
print(np.nanmax(array))
# 0.992949280963
