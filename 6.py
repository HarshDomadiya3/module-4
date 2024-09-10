# Write a Python program to read a file line by line and store it into a list


file = open('example.txt', 'r')
list = []
for i in file:
    list.append(i)
file.close()
for i in list:
    print(i)