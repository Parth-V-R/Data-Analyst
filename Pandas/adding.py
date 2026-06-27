import pandas as pd

data={
    "Name":["Ram","Shyam","Ganshyam","Dhanshyam","Amit","Jagdish","Raj","Simran"],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)

#inserting data using assignment(not used,for basic understanding)
df['Bonus']=df['Salary']*0.1
print(df)

#inserting data using insert - RECOMMENDED
#syntax- insert(loc,"column_name",data)
df.insert(0,"Emp ID",[1,2,3,4,5,6,7,8])
print(df)