#Kattis problem ID: smil
#Nicholas Lee Nov 2021

line = input()
for i in range(len(line)):
    if(line[i:i+2] == ":)" or line[i:i+2] == ";)" or line[i:i+3] == ":-)" or line[i:i+3] == ";-)"):
        print(i)