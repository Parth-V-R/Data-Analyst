"""
concatenate fn is used to concatenate arrays
syntax- numpy.concatenate((array1,array2),axis=0)
"""

import numpy as np
arr1=np.array([10,20,30])
arr2=np.array([40,50,60])
#1D array,axis=0 concatenate adds arrays in one row,axis=1 invalid as 1D array
new_arr=np.concatenate((arr1,arr2),axis=0)
print(new_arr)

arr3=np.array([[1,2],[3,4]])
arr4=np.array([[5,6],[7,8]])
#2D array,axis=0 adds rows,axis=1 adds row-column beside array in column
new_arr2=np.concatenate((arr3,arr4),axis=1)
print(new_arr2)