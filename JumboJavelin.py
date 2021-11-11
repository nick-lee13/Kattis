#Kattis problem ID: jumbojavelin
#Nicholas Lee Aug 2021

N = int(input())
sum = 0
for x in range(N):
    sum+= int(input())
print(sum-(N-1))