#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Please write a program to randomly 
# generate a list with 5 even numbers between 
# 100 and 200 inclusive.
#
# Hints:
# Use random.sample() to generate a list of random values.
#
################################################################


import random

l = [i for i in range(100,201) if i%2 == 0]
x = random.sample(l, 5)

print(x)