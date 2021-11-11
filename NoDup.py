#Kattis problem ID: nodup
#Nicholas Lee Aug 2021

line = input()
words = line.split()
wordSet = set(words)
if(len(words) != len(wordSet)):
    print("no")
else:
    print("yes")