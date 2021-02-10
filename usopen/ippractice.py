#!/usr/bin/env python3
from ipaddress import ip_address, IPv4Address, IPv6Address 
ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk == '192.168.0.1': # if a match on '192.168.70.1'
   # indented under if
   print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif type(ip_address(ipchk)) == IPv4Address:
    print("its an IPv4 address niceeeeee") # indented under if
elif type(ip_address(ipchk)) == IPv6Address:
    print("this aint no 4 its a 6")
else: # if data is NOT provided
   print('You did not provide input.') # indented under else
