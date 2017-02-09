#!/usr/bin/python
def get_integer (help_text):
    return int(input(help_text))
num1 = get_integer("what is your number :")
b = [ i for i in range(2,num1) if num1 % i == 0]
def prime_check(n) :
	if n > 1 :
		if len(b) == 0 : print "Number is Prime"
		else : print "Number is not Prime"
	else : print "Number is not prime"  	

prime_check(num1)