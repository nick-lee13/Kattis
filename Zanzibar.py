#Kattis problem ID: zanzibar
#Nicholas Lee Nov 2021

n = int(input())
for i in range(n):
    line = input()
    pop = line.split()
    notBorn = 0
    for j in range(len(pop)-1):
        currPop = int(pop[j])
        maxPop = currPop*2
        if(maxPop < int(pop[j+1])):
            notBorn = notBorn + (int(pop[j+1])-maxPop)
    print(notBorn)

