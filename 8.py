# Write a python program to find the longest words.


with open('examplefile.txt', 'r') as file:
    words = file.read().split()

longword = max(words, key=len)

print(longword)

