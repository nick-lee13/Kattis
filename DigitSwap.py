#Kattis problem ID: digitswap
#Nicholas Lee Nov 2021

num = input()
digits = [int(x) for x in str(num)]
print("{}{}".format(digits[1],digits[0]))