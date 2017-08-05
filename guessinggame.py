#!/usr/bin/python
from random import randint
c =0
while True:
    a = randint(1, 9)
    print(a)
    input_cmd= input("Enter any number from 1 t 9 or exit: ")
    if input_cmd == 'exit':
        break
    else :
        b = int(input_cmd)
        c += 1
        if b >a :
            print ("too high")
        if b <a :
            print("too low")
        if b==a :
            print("exactly right")

print("you have made these many attempts:",c)
