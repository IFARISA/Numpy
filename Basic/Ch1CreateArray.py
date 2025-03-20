import numpy as np

print(f'Numpy Version: {np.__version__}')
print(25*"-")

print(f'Numpy path: {np.__path__}')
print(25*"-")

print(f"All Numpy functions and classes: {np.__all__}")
print(25*"-")


my_list = [1, 2, 3, 4, 5]
print('List')
print(my_list)
print(25*"-")

array = np.array([1, 2, 3, 4, 5])
print('1D Numpy Array')
print(array)
print(25*"-")

print(type(my_list))
print(type(array))
print(25*"-")

d0 = np.array([1])
print('0D Numpy Array')
print(d0)
print(f'{d0.ndim} --> Dimension of the array...')
print(25*"-")

d1 = np.array([1, 2, 3, 4, 5])
print('1D Numpy Array')
print(d1)
print(f'{d1.ndim} --> Dimension of the array...')
print(25*"-")

d2 = np.array([ [1, 2, 3], [4, 5, 6] ])
print('2D Numpy Array')
print(d2)
print(f'{d2.ndim} --> Dimension of the array...')
print(25*"-")

d3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('3D Numpy Array')
print(d3)
print(f'{d3.ndim} --> Dimension of the array...')
print(25*"-")

print('-------------------')

Array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(Array[::])
print(Array[1])
print(Array[-1])

Array[0] = 100
print(Array)


a_mul = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(a_mul)
print(a_mul[1, 1]) # [row, col] --> remember start at 0 !!