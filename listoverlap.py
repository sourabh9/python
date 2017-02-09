#!/usr/bin/python
x = input ("What is size of first list:")
print "Size1 :", x
y = input ("What is size of second list:")
print "Size2 :", y
list1 = list()
list2 = list()
list3 = list()

for i in range(x):
   num1 = input("enter the number:")
   n1 = list1.append(num1)
print "first list is:", list1
for i in range(y):
   num2 = input("enter the number:")
   n2 = list2.append(num2)
print "second list is:", list2
if x <= y :
    for j in range(x) :
        for k in range(y) : 
           if list1[j] == list2[k] : list3.append(list1[j])
           else : pass
else : pass
print "sorted list:", list3
