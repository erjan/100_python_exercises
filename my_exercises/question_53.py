#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
#
# Hints:
# Use def methodName(self) to define a method.
#
################################################################


class Rectangle():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def area(self):
        return self.a*self.b
    

x = Rectangle(2,10)
res = x.area()
print(res)