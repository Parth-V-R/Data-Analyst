"""
insert adds a value in array at given index location
syntax - numpy.insert(array,index,value,axis=None)
axis 0 - row wise,axis 1 - column wise
"""

import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr)
# arr is 1D array so axis=1 will not be applicable,by default axis=0 is set
new_arr=np.insert(arr,2,25)
print(new_arr)