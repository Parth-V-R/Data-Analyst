import pandas as pd

data={
    "Name":['Arun','Varun','Karun','Narun','Marun'],
    "Age":[38,25,25,28,38],
    "Salary":[10000,4000,6000,16000,12000]
}

df=pd.DataFrame(data)
print(df)

multi_grouped=df.groupby(['Age','Name'])['Salary'].sum()
print(multi_grouped)