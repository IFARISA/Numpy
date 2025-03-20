import numpy as np

arr1 = np.array([1, 2, 3, 4, 5], dtype=np.longdouble)
arr2 = np.array([6, 7, 8, 9, 10], dtype=np.longdouble)

print(f'Sum: {arr1+arr2}')
print(f'Sub: {arr1-arr2}')
print(f'Mul: {arr1*arr2}')
print(f'Div: {arr1/arr2}')


print('----------------------------------------------')

arr3 = np.array([ [1, 2, 3],
                  [4, 5, 6] ])

print(f'sqrt: {np.sqrt(arr3)}')
print('----------------------------------------------')
print(np.sin(arr3))
print('----------------------------------------------')
print(np.cos(arr3))
print('----------------------------------------------')
print(np.tan(arr3))
print('----------------------------------------------')
print(np.exp(arr3))
print('----------------------------------------------')
print(np.log(arr3))
print('----------------------------------------------')
print(np.log2(arr3))
print('----------------------------------------------')
print(np.log10(arr3))

Array = np.array([ [1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10] ])

print(Array.transpose()) # make the row column and the column row 
print('----------------')
print(Array.T)

print('-----------')

print(f'Max: {Array.max()}')
print(f'Min: {Array.min()}')
print(f'Mean: {Array.mean()}')
print(f'STD: {Array.std()}')
print(f'Sum: {Array.sum()}')
print(f'Medain: {np.median(Array)}')

# Identity matrix

iden = np.eye(3)
print(iden)