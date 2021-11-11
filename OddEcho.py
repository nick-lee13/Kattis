#Kattis problem ID: oddecho
#Nicholas Lee Nov 2021

N = int(input())
for i in range(N):
    word = input()
    if (i % 2) == 0:
        print(word)