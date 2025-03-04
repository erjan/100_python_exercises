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
#write a program to print the list after 
#removing delete numbers which are divisible by 5 and 7 in 
#[12,24,35,70,88,120,155].
#
# Hints:
# Use list comprehension to delete a bunch of element from a list.
#
################################################################

s = [12,24,35,70,88,120,155]

s = [num for num in s if num%5 != 0 and num%7 != 0]
print(s)

