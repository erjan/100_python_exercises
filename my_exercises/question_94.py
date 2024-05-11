#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#----------------------------------------#
'''
With a given list [12,24,35,24,88,120,155,88,120,155], write 
a program to print this list 
after removing all duplicate values 
with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

Solution:

def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print removeDuplicate(li)

'''
#----------------------------------------#

s = [12,24,35,24,88,120,155,88,120,155]

def rem(l):

    seen = set()
    res = []
    for num in l:
        if num not in seen:
            seen.add(num)
            res.append(num)
    return res

print(rem(s))
