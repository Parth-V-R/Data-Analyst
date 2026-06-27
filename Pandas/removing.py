#drop() removes column from df
import pandas as pd

data={
    "Name":["Ram","Shyam","Ganshyam","Dhanshyam","Amit","Jagdish","Raj","Simran"],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print(df)

#removing column "Performance Score"
#syntax- df.drop(columns=['Column_Name'],inplace=True)
#inplace -> True-modifies original DF,False- returns new DF

df.drop(columns=['Performance Score','Age'],inplace=True)
print("Removed Column - Performance Score ")
print(df)