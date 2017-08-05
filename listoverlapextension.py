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

####Second Method
import random
x = int(input("Enter number of elements for first list :"))
y = int(input("Enter number of elements for second list :"))
a = random.sample(range(100),x)
b = random.sample(range(200),y)
print([i for i in a for j in b if i==j])

#####Third Method
import random
x = int(input("Enter number of elements for first list :"))
y = int(input("Enter number of elements for second list :"))
print([i for i in random.sample(range(100),x) if i in random.sample(range(200),y)])

