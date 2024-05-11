#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#[5,6,77,45,22,12,24]
#By using list comprehension, please write a 
# program to print  after deleting even nums from the list
# 7 in [12,24,35,70,88,120,155].
# Hints:
# Use list comprehension to delete a bunch of 
# element from a list.
#
################################################################




s = [5,6,77,45,22,12,24]

s = [num for num in s if num%2 !=0]
print(s)


