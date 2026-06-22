import numpy as np

arr=np.array([10,20,np.inf,40,-np.inf])
print(np.isinf(arr))

cleaned_array=np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(cleaned_array)