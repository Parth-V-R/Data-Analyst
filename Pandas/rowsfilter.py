import pandas as pd

data={
    "Name":["Ram","Shyam","Ganshyam","Dhanshyam","Amit","Jagdish","Raj","Simran"],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)

#filtering rows - salary > 50000

high_salary=df[df['Salary']>50000]
print(high_salary)

#salary > 50000 and Age > 30

filtered_and=df[(df['Salary']>50000) & (df['Age']>30)]
print("\nSalary greater than 50000 and Age greater than 30")
print(filtered_and)

#age > 35 or performance score greater than 90

filtered_or=df[(df['Age']>35) | (df['Performance Score'] > 90)]
print("\nAge greater than 35 and Performance Score greater than 90")
print(filtered_or)