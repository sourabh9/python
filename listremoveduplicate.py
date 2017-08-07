#!/usr/bin/python
import random


####Method 1
print(list(set(random.sample(range(1,9),5))))

####Method 2
def list_generation():
    return random.sample(range(1, 9), 6)


def new_list_duplicates(y):
    return set(y)


print(new_list_duplicates(list_generation()))

#####Method 3

a = [1, 1, 2,2, 3, 3, 5, 5, 8, 13, 21, 21, 34, 55, 89]
print (list(set(a)))


######Method 4

