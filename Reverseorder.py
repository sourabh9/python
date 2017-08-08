#!/usr/bin/python
c = []


def string_input(help_text):
    return input(help_text)

##### Method 1
def reverse_order(y):
    z = y.split(" ")
    l = len(z)
    while l > 0:
        c.append(z[l - 1])
        l = l - 1
    return c

#####Method 2
def reverse_order(y):
    z = y.split(" ")
    z = z[::-1]
    return z

######method 3
def reverse_order(y):
    return y.split(" ")[::-1]

result = reverse_order(string_input("enter sentence: "))
print(result)
