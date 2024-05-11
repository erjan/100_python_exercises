#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 25
# Level 1
#
################################################################
#
# Question:
#     Define a class, which have a class 
# parameter and have a same instance parameter.
#
# Hints:
#     Define a instance parameter, 
# need add it in __init__ method
#     You can init a object with construct parameter or set the value later
#
################################################################

class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print("class param is %s" % (Person.name))
print('instance param is %s' % (jeffrey.name))
print()

nico = Person()
print("class param is %s" % (Person.name))
print('instance param is %s' % (nico.name))
print()
