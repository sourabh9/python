#!/usr/bin/python

Num = input("Enter your number :")
check = input("Enter your number :")
if Num % check ==0:
    print check, "divides evenly to", Num
else :
    print check, "doesn't divides evenly to", Num

if Num % 2 ==0:
    print "Number is even", Num
    if Num %4 ==0:
        print "This is 4 multiple ", Num
    else :
        print "Not multiple of 4"
else:
    print "Number is odd",  Num

