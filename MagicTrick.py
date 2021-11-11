#Kattis problem ID: magictrick
#Nicholas Lee Aug 2021

line = input()
lst = list(line)
lstSet = set(lst)
if(len(lst) != len(lstSet)):
    print("0")
else:
    print("1")
