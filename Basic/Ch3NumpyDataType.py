import numpy as np

arr1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(f'Data Type: {arr1.dtype}')

arr2 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9.6]])

print(f'Data Type: {arr2.dtype}')


arr3 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 'FARIS']])

print(f'Data Type: {arr3.dtype}')
print(f'The class: {type(arr3[2, 2])}')

arr4 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], dtype=np.int64)

print(f'Data Type: {arr4.dtype}')

arr5 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], dtype=np.float64)

print(f'Data Type: {arr5.dtype}')

arr6 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]], dtype=np.longdouble) # highest precision available on your system.

print(f'Data Type: {arr6.dtype}')
print(np.finfo(np.longdouble))