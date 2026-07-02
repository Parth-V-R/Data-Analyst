import numpy as np
import pandas as pd

#loading the dataset

df=pd.read_csv("Numpy/Indian Employee Dataset/Indian_Employee_Data.csv")
print(df.head())

#checking the missing values

print("Missing Values in each Column")
print(df.isnull().sum())
"""df.isnull().sum(),returns null values in each column"""



