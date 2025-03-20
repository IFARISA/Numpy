import numpy as np

# Fill the arrays with dfault values:

# arr = np.full(shape, fill_value, dtype=None, order='C', *, like=None)
arr1 = np.full((2, 3), 7) # First will be the array (row, column), teh number)
print(arr1)

print(23*'-')


# an array with 0s values by default 
arr2 = np.zeros((3, 4), dtype=np.int8)
print(arr2)

print(23*'-')

# an array with 1s values by default 
arr3 = np.ones((3, 4), dtype=np.int8)
print(arr3)

print(23*'-')

# an empty array --> the values from memory RAM
arr4 = np.empty((2, 2))
print(arr4)

print(23*'-')


# Generate sequences --> for plot almost
x = np.arange(0, 25, 5) # (start, end, steps)
print(x)

print(23*'-')

x2 = np.linspace(0, 3, 5) 
print(x2)