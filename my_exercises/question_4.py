#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 4
# Level 1
#
################################################################
#
# Question:
# Write a program which accepts a sequence of 
# comma-separated numbers from console and generate a 
# list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple
#
################################################################



s = input('please enter comma sep numbers: ')

s = s.split(',')
s = list(s)
t = tuple(s)
print(s)
print(t)