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
# To define a custom exception, we need to define 
# a class inherited from Exception.
#
################################################################


class MyException(Exception):
    def __init__(self,m):
        self.msg = m


er = MyException("something wrong")