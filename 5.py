# Write a Python program to read last n lines of a file. 

file = 'examplefile.txt'
n = 5 

with open(file,'r') as file:
    lines = file.readlines()
  
print(''.join(lines[-n:]))

# file.lines[-n:]
