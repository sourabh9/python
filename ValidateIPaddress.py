#!/usr/bin/python

#####Method 1

import re
hostIP =input('Enter the ip:')
pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
test = pat.match(hostIP)
if test:
   print ("Acceptable ip address")
else:
   print ("Unacceptable ip address")

#####Method 2

import socket
def valid_ip(address):
    try:
        socket.inet_aton(address)
        return print("Valid IP")
    except:
        return print("Invalid IP")
valid_ip(input("Enter IP address to validate : "))

####Method 3

def valid_ip(address):
    try:
        host_bytes = address.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b >= 0 and b<=255]
        return print("Valid IP")
    except:
        return print("Invalid IP")

valid_ip(input("Enter Your IP address: "))
