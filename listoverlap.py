#!/usr/bin/python

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

### First Method
# c = []
# for i in a:
#     for j in b:
#         if i==j:
#             c.append(i)
# print c

### Second Method
# print([i for i in a for j in b if i==j])

###Third Method

# c = []
# for i in a:
#     for j in b:
#         if i==j:
#             if i in c:
#                 continue
#             else:
#                 c.append(i)
# print c

###Fourth Method

# import random
# x = random.sample(range (100),10)
# y = random.sample(range (20),15)
# z = []
# for i in x:
#     if i in y:
#         z.append(i)
# print z

###One line Method
import random
# x = random.sample(range (100),10)
# y = random.sample(range (20),15)
# c = []
# c = [i for i in x if i in y and i not in c]
# print c

###Another Method

x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# c = [i for i in x if i in y and i not in c]
c = [i for i in x if i in y]
print c
