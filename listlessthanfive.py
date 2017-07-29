#!/usr/bin/python
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
###First Solution
b = []
l =len(a)
i =0
while i<l-1:
    if a[i] <5:
        b.append(a[i])
    i = i+1
print b

###Second Solution

num = input("Enter your number: ")
for i in range(len(a)):
    if a[i] < num:
        print a[i]

###One line Solution
print([i for i in a if i< 30])

