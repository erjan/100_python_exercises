#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Define a class Person and its two child classes: 
# Male and Female. All classes have a method "getGender" 
# which can print "Male" for Male class and "Female" for 
# Female class.
#
# Hints:
# Use Subclass(Parentclass) to define a child class.
#
################################################################


class Person():

    def getGender(self):
        print('000')

class Male(Person):
    def getGender(self):
        print('male')

class Female(Person):
    def getGender(self):
        print('female')

s = Male()

tt = Female()

tt.getGender()
s.getGender()