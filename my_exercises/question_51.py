#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Define a class named American and its subclass NewYorker. 
#
# Hints:
# Use class Subclass(ParentClass) to define a subclass.
#
################################################################





class American():
    pass


class NewYorker(American):
    pass

generic_american = American()

typical_nyc_man = NewYorker()

print(generic_american)
print(typical_nyc_man)
