#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
# proto.extend('dns')
    #this added 'd', 'n', 's' to the end of the list
proto.append('dns')
    #this will add 'dns' as an object to the list
print(proto)
