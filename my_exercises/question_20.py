#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 20
# Level 3
#
################################################################
#
# Question:
# Define a class with a generator
# which can iterate the numbers, which are divisible by 7, 
#between a given range 0 and n.
#
# Hints:
# Consider use yield
#
################################################################

class My():

    def __init__(self,n):
        self.n = n
    
    def mygen(self):

        for i in range(0,self.n+1):
            if i%7==0:
                yield i

z = My(100)

generator = z.mygen()
print(type(generator))
for num in generator:
    print(num)

