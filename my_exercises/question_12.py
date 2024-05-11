#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 12
# Level 2
#
################################################################
#
# Question:
# Write a program, which will find all such
#  numbers between 1000 and 3000 (both included) such 
# that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated 
# sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################


# s = []

# for i in range(1000,3001):

#     cur = str(i)
#     if all(int(x)%2 == 0 for x in cur):
#         s.append(cur)
# print(','.join(s))


values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))