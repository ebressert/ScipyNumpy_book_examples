# Creating an array of zeros and defining column types
import numpy as np

recarr = np.zeros((2,), dtype=('i4,f4,a10'))
toadd = [(1, 2., "Hello"), (2, 3., "World")]
recarr[:] = toadd

# Creating an array of zeros and defining column types
recarr = np.zeros((2,), dtype=('i4,f4,a10'))

# Now creating the columns we want to put
# in the recarray
col1 = np.arange(2) + 1
col2 = np.arange(2, dtype=np.float32)
col3 = ['Hello', 'World']

# Here we create a list of tuples that is
# identical to the previous toadd list.
toadd = zip(col1, col2, col3)

# Assigning values to recarr
recarr[:] = toadd

# Assigning names to each column, which
# are now by default called 'f0', 'f1', and 'f2'.

recarr.dtype.names = ('Integers', 'Floats', 'Strings')

# If we want to access one of the columns by its name, we
# can do the following.

print recarr['Integers']
#[1, 2]
