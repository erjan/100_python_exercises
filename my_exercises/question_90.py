#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# By using list comprehension, please
# write a program generate a 3*5*8 3D 
#array whose each element is 0.
#
# Hints:
# Use list comprehension to make an array.
#
################################################################


s = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]

print(s)