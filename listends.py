
#!/usr/bin/python
# list2 = list()
# list1 = list()
# # x =6 
# for i in range(4) :
#   # print "value of i", i
#   n = input("enter the number:")
#   list1.append(n)
#   if i == 0 or i == 3 : list2.append(n) 
#   else : pass 

# print "the list is ", list1
# print "revised list is", list2

# list2.append()

# a = [5, 10, 15, 20, 25]
list1 = list()
list2 = list()
x = input("enter the length of list:",)
print "length of list is", x
def get_list(n) :
    for i in range (n) :
       n1 = input("Enter List element:", )
       list1.append(n1)  

def firstlast_list(n) :
  for i in range(n) :
    n2 = list1[i]
    if i == 0 or i == n-1: list2.append(n2) 
    else : pass   
get_list(x)
firstlast_list(x)
print "original list is ", list1
print "list with first & last element is", list2