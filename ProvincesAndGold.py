#Kattis problem ID: provincesandgold
#Nicholas Lee Nov 2021

line = input()
g,s,c = line.split()
g = int(g)
s = int(s)
c = int(c)
buyPower = (g*3) + (s*2) + (c*1)
if(buyPower >1):
    if(buyPower >2):
        if(buyPower >4):
            if(buyPower >5):
                if(buyPower >= 8):
                    print("Province or Gold")
                else:
                    print("Duchy or Gold")
            else:
                print("Duchy or Silver")
        else:
            print("Estate or Silver")
    else:
        print("Estate or Copper")
else:
    print("Copper")