# ndim returns the dimension of array
#syntax - array.ndim

import numpy as np
arr_1 = np.array([1,2,3])
arr_2 = np.array([[1,2,3],[4,5,6]])
arr_3 = np.array([[[1,2],[3,4],[5,6],[7,8]]])

print(arr_1.ndim)
print(arr_2.ndim)
print(arr_3.ndim)
