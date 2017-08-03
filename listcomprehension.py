#!/usr/bin/python

###### first method
a = [1,4,9,16,25,36,49,64,81,100]
print [i for i in a if i%2 ==0]

####Second Method
import random
y =[]
for x in range(10) :
    y.append(random.randint(1,101))
print [i for i in y if i%2==0]

#####Third Method
a = [1,4,9,16,25,36,49,64,81,100]
print filter(lambda x:x%2==0,a)

####Fourth Method

from random import randint
y =[]
for x in range(10):
    y.append(randint(1,101))
print filter(lambda x:x%2==0,y)

