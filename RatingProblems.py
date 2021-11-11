#Kattis problem ID: ratingproblems
#Nicholas Lee Aug 2021

line = input()
n,k = line.split()
n = int(n)
k = int(k)
sumOf = 0
for x in range(k):
    sumOf += int(input())
minSum = sumOf
maxSum= sumOf
for y in range(n-k):
    minSum += -3
    maxSum += 3
print(minSum/n,maxSum/n)
