#!/usr/bin/python
x = input("Enter the number: ")
b = []
possible_divisor = range(2,x-1)
for i in possible_divisor :
    if x%i ==0:
        b.append(i)
print b

###One line Method
print([i for i in range(2,x-1) if x%i ==0])