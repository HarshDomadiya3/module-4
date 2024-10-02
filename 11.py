# Write a Python program to write a list to a file


list = ['apple', 'banana', 'cherry']

with open('examplefile.txt','w') as file:

    for item in list:
        file.write(item)

