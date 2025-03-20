import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


print(arr)
print('---------------------')
print(f'Array Shape (row, column): {arr.shape}')
print(f'Array Dimensions (number of rows): {arr.ndim}')
print(f'Size (number of elements): {arr.size}')
print(f'Data Type: {arr.dtype}')
