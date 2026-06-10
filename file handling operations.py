# 'w' means write operation,in new file it writes and in existing file it replaces
f=open('Samplefile1.txt','w')
f.write("Hello")
f.close()
# a - append,It adds input at the end of existing String
f=open('Samplefile1.txt','a')
f.write(" World")
f.close()