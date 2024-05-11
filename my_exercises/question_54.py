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
# To override a method in super class, we can 
# define a method with the same name in the super class.
#
################################################################



class Mysuper():
    def __init__(self,d):
        self.m = d
    
    def my_method(self):
        return self.m*2


class My2(Mysuper):
    def __init__(self,d):
        self.q = d
    def my_method(self):
        return self.q*10
    
x = Mysuper()
print(x.my_method())