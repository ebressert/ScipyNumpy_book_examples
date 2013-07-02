import numpy as np

# Loading and existing file
arr = np.loadtxt('somefile.txt')

# Saving a new file
np.savetxt('somenewfile.txt', arr)

# Opening an existing file with the append option
f = open('existingfile.txt', 'a')

# Creating some random data to append to the existing file
data2append = np.random.rand(100)

# With np.savetxt we replace the file name with the file handle.
np.savetxt(f, data2append)

f.close()
