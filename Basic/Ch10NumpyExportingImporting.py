import numpy as np


# store the file into csv file

array = np.array([ [1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10] ], dtype=np.int8)

np.savetxt('numpy_to_csv.csv', array, delimiter=',')

#np.save('numpy_array.npy', array)
#new = np.load('numpy_array.npy')
