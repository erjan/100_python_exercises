#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Please write a program to generate all 
# sentences where subject is in ["I", "You"] and verb 
# is in ["Play", "Love"] and the object 
# is in ["Hockey","Football"].
#
# Hints:
# Use list[index] notation to get a element from a list.
#
################################################################

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey","Football"]
for subject in subjects:
    for verb in verbs:
        for object in objects:
            print(subject,verb,object, sep = ' ')

