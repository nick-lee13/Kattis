#Kattis problem ID: speeding
#Nicholas Lee Nov 2021

n = int(input())
times = input()
prevT = 0
prevD = 0
topSpeed = 0
for i in range(n-1):
    times = input()
    t,d = times.split()
    t = int(t)
    d = int(d)
    speed = (d-prevD)/(t-prevT)
    if(speed > topSpeed):
        topSpeed = speed
    prevT = t
    prevD = d
print(int(topSpeed))
