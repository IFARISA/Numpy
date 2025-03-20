import numpy as np


arr = np.array([1, 2, 3])

new_arr = np.append(arr, [4, 5, 6])
print(new_arr)
print(arr)
print('--------------------')
arr = np.append(arr, [7, 8, 9])
print(arr)

print('------------')

arr2 = np.array([77, 88, 99, 100])

arr2=np.insert(arr2, 0, [11, 22, 33, 44, 55, 66])
print(arr2)