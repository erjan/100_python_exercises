#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Define a class named Circle which can be
#  constructed by a radius. The Circle class 
# has a method which can compute the area. 
#
# Hints:
# Use def methodName(self) to define a method.
#
################################################################




class Circle():
    def __init__(self,r):
        self.rad = r
    def area(self):
        return self.rad**2*3.14


x = Circle(4)
res = x.area()
print(res)