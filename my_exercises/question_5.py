#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 5
# Level 1
#
################################################################
#
# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to 
# test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters
#
################################################################

class yes():
    def __init__(self):
        print()
        print('just created this object, inside init method')
        self.main = None
    
    def getString(self):
        self.main = input()

    def printString(self):
        print(self.main.upper())


strObj = yes()

strObj.getString()
strObj.printString()







# class InputOutString(object):
#     def __init__(self):
#         self.s = ""

#     def getString(self):
#         self.s = raw_input()

#     def printString(self):
#         print self.s.upper()

# strObj = InputOutString()
# strObj.getString()
# strObj.printString()