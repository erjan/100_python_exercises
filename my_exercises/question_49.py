#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Write a program which can map() to make a list
#  whose elements are square of numbers
#  between 1 and 20 (both included).
#
# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.
#
################################################################

l = [i for i in range(1,21)]
res = list(map(lambda x: x**2, l))
print(res)

