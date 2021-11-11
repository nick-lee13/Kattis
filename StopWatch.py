#Kattis problem ID: stopwatch
#Nicholas Lee Aug 2021

n = int(input())
onSecond = False
temp = 0
total = 0
for x in range(n):
    if onSecond:
        total +=  (int(input()) - temp)
        onSecond = False
    else:
        temp = int(input())
        onSecond = True
if (n%2) == 0:
    print(total)
else:
    print("still running")