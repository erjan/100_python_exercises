#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Define a function which can print a 
# dictionary where the keys are numbers 
# between 1 and 20 (both included) and the values are
# square of keys.
#
# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
#
################################################################


def f():
    q = dict()

    for i in range(1,21):
        q[i] = i**2
    print(q)

f()
