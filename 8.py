# Write a python program to find the longest words.


file=open('example.txt','r')
words = []

for i in file:
    words.extend(i.split())
file.close()
length=0
words=[]
for word in words:
    if len(word) >length:
        length=len(word)
        words=[word]
    elif len(word)==length:
        words.append(word)  
print("Longest word :-")
for i in words:
    print(i)
