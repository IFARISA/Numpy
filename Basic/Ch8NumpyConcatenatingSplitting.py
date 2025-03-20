import numpy as np 

array1 = np.array([ [1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10] ])

array2 = np.array([ [11, 12, 13, 14, 15],
                   [16, 17, 18, 19,20] ])

array = np.concatenate((array1, array2))
print(array)


print('---------------------')

array22 = np.concatenate((array1, array2), axis=0)
print(array22)

print('---------------------')

array3 = np.concatenate((array1, array2), axis=1)
print(array3)

print('---------------------')

array4 = np.vstack((array1, array2))
print(array4)

print('---------------------')

array5 = np.hstack((array1, array2))
print(array5)