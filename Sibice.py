#Kattis problem ID: sibice
#Nicholas Lee Nov 2021
import math
line = input()
n,w,h = line.split()
n = int(n)
w = float(w)
h = float(h)
maxLength = math.sqrt((w**2)+(h**2))
for i in range (n):
    l = float(input())
    if(l <= maxLength):
        print("DA")
    else:
        print("NE")