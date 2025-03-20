import numpy as np


number = np.random.randint(100) # one number int equal to or less than 100
print(number)

print('-------')

array = np.random.randint(100, size=(3, 3))
print(array)
# numbers int equal to or less than 100 in array (3, 3)
print('-------')

array1 = np.random.randint(80, 100, size=(3, 3))
print(array1)
# numbers int between 80 and 100 in array (3, 3)

arr_random = np.random.rand(2, 2)
print(arr_random)

# Random Numbers int
rand_int = np.random.randint(1, 10, (2, 3))
# 1 -> start number generator
# 10 -> which is 10-1 = 9 so the number between 1 to 9
# (2, 3) -> 2*3 matrix
print(rand_int)