# Write a Python program to count the number of lines in a text file.

file=open('example.txt','r')
count=0
for i in file:
    count +=1
file.close()
print("Number of lines :-",count)