# ravel and flatten are used to convert MultiDimensional array to 1D Array
# ravel() - original view
# flatten() - copy

import numpy as np
arr=np.array([[1,2,3],
              [4,5,6]])
print(arr.ravel())
print(arr.flatten())
