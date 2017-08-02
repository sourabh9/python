#!/usr/bin/python

####First Method
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

###Second Method
f =0
def pallendrome(str11):
    l=len(str11)-1
    i =0
    global f
    for c in str11:
        if c == str11[l-i] :
            i = i+1
        else :
            f =1
            break
    return f

a = raw_input("Enter the string: ")
result = pallendrome(a)
if result ==1 :
    print "Not pallendrome"
else :
    print "Pallendrome"


#####Third method

x = raw_input("Enter the string: ")
if x[0:]==x [::-1] : print "pallendrome"
else: print "Not pallendrome"

#######Fourth Method

z = lambda s:('Not Pallindrome','Pallindrome')[s[::] == s[::-1]]
print (z(raw_input("Enter the string:")))

