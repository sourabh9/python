#!/usr/bin/python

abc = raw_input("Enter your string: ")
l=len(abc)-1
i =0
f=0
for c in abc:
    if c == abc[l-i] :
        i = i+1
    else :
        f =1
        break

if f ==0 :
    print "string is pallendrome"
if f==1 :
    print "string is not pallendrome"


