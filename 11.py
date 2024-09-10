# Write a Python program to write a list to a file

list = ['apple','banana']
file = open('example.txt','w')
for i in list:
    file.write(i+'\n')
file.close()
