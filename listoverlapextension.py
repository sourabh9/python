#!/usr/bin/python

#####First method

import random
x = int(input("Enter number of elements for first list :"))
y = int(input("Enter number of elements for second list :"))
a = random.sample(range(100),x)
b = random.sample(range(200),y)
c =[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)

print(c)

