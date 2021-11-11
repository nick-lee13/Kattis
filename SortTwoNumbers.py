#Kattis problem ID: sorttwonumbers
#Nicholas Lee Aug 2021

line = input()
a, b = line.split()
a = int(a)
b = int(b)
if(a > b):
    print(b,a)
else:
    print(a,b)