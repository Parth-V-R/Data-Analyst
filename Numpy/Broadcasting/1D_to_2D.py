#2d array gets added to 1D array one by one,
#it is called expanding single elements
#this works only with same shapes
import numpy as np

matrix=np.array([[1,2,3],[4,5,6]]) # 2*3 matrix,2D

vector=np.array([10,20,30]) #1D array

result=matrix + vector
print(result)