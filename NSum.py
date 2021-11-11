#Kattis problem ID: nsum
#Nicholas Lee Nov 2021

n = int(input())
line = input()
arr = line.split()
sum = 0
for i in range(n):
    sum = sum + int(arr[i])
print(sum)