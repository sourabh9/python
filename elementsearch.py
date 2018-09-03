#!/usr/bin/python
import random
c = sorted([i for i in random.sample(range(200),7)])
print(c)
num = input("Enter the number: ")
while True:
    num1= int(len(c)/2)
    b=[]
    if (c[num1] > int(num)):
        for i in range(num1):
            b.append(c[i])
        print(b)
    elif (c[num1] == int(num)) :
        print ("Equality testing done and number found", int(num))
    else:
        for i in range(num1,len(c)):
            b.append(c[i])
        print(b)
    break



