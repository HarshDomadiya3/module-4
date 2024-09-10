# Write a Python program to read a file line by line store it into a variable

file=open('example.txt','r')
variable= ""
for i in file:
    variable +=i
file.close()
print(variable)

