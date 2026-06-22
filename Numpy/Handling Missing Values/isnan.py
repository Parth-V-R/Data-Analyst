#isnan checks for nan values in array and return True when finds one
#nan is not a number(nan),it is missing,unidentified,or invalid numerical data
#syntax - np.isnan(array),nan is float datatype

import numpy as np
arr=np.array([10,20,np.nan,40,50,np.nan])
# True returns where nan is present,else false
print(np.isnan(arr))


