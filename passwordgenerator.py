#!/usr/bin/python
# import random
import string
from random import *

def password_input(help_text):
    return print(help_text)
def password_generator():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(8, 16)))
    return password

password_input("please eneter your password:")
print(password_generator())

