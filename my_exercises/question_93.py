#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# With two given lists [1,3,6,78,35,55] and 
# [12,24,35,24,88,120,155], write a program to 
# make a list whose elements are intersection of 
# the above given lists.
#
# Hints:
# Use set() and "&=" to do set intersection operation.
#
################################################################



s1=[1,3,6,78,35,55]

s2 = [12,24,35,24,88,120,155]

s1 = set(s1)
s2 = set(s2)

res = list(s1.intersection(s2))

print(res)