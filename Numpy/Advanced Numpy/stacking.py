# vertical stacking - row wise - vstack()
# horizontal stacking - column wise - hstack()

import numpy as np
arr1=np.array([10,20,30])
arr2=np.array([40,50,60])

new_arr1=np.vstack((arr1,arr2))
print(new_arr1)
new_arr2=np.hstack((arr1,arr2))
print(new_arr2)

