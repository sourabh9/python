#!/usr/bin/python
import random

rand_num = str(random.randint(1001, 9999))
print(rand_num)

def cowandbull(y1):
    c = 0
    b = 0
    for i in range(4):
        for j in range(4):
            if (i == j) & (rand_num[i] == user_num[j]):
                c = c + 1
            if (i != j) & (rand_num[i] == user_num[j]):
                b = b + 1
    print(c, "cow")
    print(b, "bull")


if __name__ == "__main__":
    user_num = str(input("Give me a 4 digit number: "))
    cowandbull(user_num)
