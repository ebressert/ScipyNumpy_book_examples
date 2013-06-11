import numpy as np

alist = [[1, 2], [3, 4]]

# To return the (0,1) element we must index as shown below.
alist[0][1]

# Converting the list defined above into an array
arr = np.array(alist)

# To return the (0,1) element we use ...
arr[0, 1]

# Now to access the last column, we simply use ...
arr[:, 1]

# Accessing the columns is achieved in the same way,
# which is the bottom row.
arr[1, :]

# Creating an array
arr = np.arange(5)

# Creating the index array
index = np.where(arr > 2)
print(index)

# Creating the desired array
new_arr = arr[index]

# We use the previous array
new_arr = np.delete(arr, index)

index = arr > 2
print(index)
new_arr = arr[index]
