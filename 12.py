# Write a Python program to copy the contents of a file to another file


file=open('example.txt','r')
secound_file=open('example.txt','w')

content=file.read()
secound_file.write(content)

file.close()

secound_file.close()
