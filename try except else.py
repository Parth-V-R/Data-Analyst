try:
    f=open('Samplefile1.txt','r')

except FileNotFoundError:
    print("File Not Found")

except Exception:
    print("Error")

#When error not exists,else part is executed,if error found then except part is executed    
else:
    print(f.read())