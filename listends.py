
#!/usr/bin/python

#######Method 3

import random
c = []

def length_list():
    return int(input("what is your length of list: "))
def random_list(n1):
    return random.sample(range(0, 201), n1)
def first_last_element_list(y1):
    c.append(y1[0])
    c.append(y1[x-1])

x = length_list()
y = random_list(x)
print(y)
first_last_element_list(y)
print(c)

######Method 4

import random

def length_list():
    return int(input("what is your length of list: "))

def random_list(n1):
    return random.sample(range(0, 201), n1)

def first_last_element_list(y1):
    return [y1[0],y1[x-1]]

def even_element_list(y2):
    return list(filter(lambda z:z%2==0, y2))

def odd_element_list(y2):
    return list(filter(lambda z:z%2!=0, y2))

x = length_list()
y = random_list(x)
c =first_last_element_list(y)
d = even_element_list(random_list(x))
print(d)
e = odd_element_list(random_list(x))
print(e)


###Method 1
list2 = list()
list1 = list()
# x =6
for i in range(4) :
  # print "value of i", i
  n = input("enter the number:")
  list1.append(n)
  if i == 0 or i == 3 : list2.append(n)
  else : pass

print "the list is ", list1
print "revised list is", list2

# list2.append()

#####Method2
a = [5, 10, 15, 20, 25]
list1 = list()
list2 = list()
x = input("enter the length of list:",)
print "length of list is", x
def get_list(n) :
    for i in range (n) :
       n1 = input("Enter List element:", )
       list1.append(n1)

def firstlast_list(n) :
  for i in range(n) :
    n2 = list1[i]
    if i == 0 or i == n-1: list2.append(n2)
    else : pass
get_list(x)
firstlast_list(x)
print "original list is ", list1
print "list with first & last element is", list2


