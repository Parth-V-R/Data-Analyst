import pandas as pd

data={
    "Name":['Arun','Varun','Karun'],
    "Age":[38,21,25],
    "Salary":[10000,4000,6000]
}

df=pd.DataFrame(data)
print(df)

#Used sort_values to sort a column in ascending format
df.sort_values(by="Age",ascending=True,inplace=True)
print('After Sorting')
print(df)