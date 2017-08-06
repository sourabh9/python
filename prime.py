#!/usr/bin/python
#####Method 1
def get_integer (help_text):
      return int(input(help_text))
def prime_check(n) :
    if n > 1 :
        if len(b) == 0 : print ("Number is Prime")
        else : print ("Number is not Prime")
    else : print ("Number is not prime")

num1 = get_integer("what is your number :")
b = [ i for i in range(2,num1) if num1 % i == 0]
prime_check(num1)

#####Second method
def get_number():
    return int(input("Give me a  number: "))

def prime(n1):
    b=[i for i in range(2,n1) if n1%i ==0]
    print(b)
    if len(b) >0 : print ("not prime")
    else: print("prime number")
number = get_number()
prime(number)
