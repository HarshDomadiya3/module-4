# Write a Python program to count the frequency of words in a file


file=open('example.txt','r')
a=file.read()
file.close()
b=a.lower()
words=b.split()
count={}
for i in words:
    if i in count:
        count[i]+= 1  
    else:
        count[i]=1   
for i in count:
    print("'" + i+"':",count[i])
