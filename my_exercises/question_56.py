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
# Use try/except to catch exceptions.
#
################################################################



def f():
    return 5/0


try:
    f()
except Exception:
    print('bad!')
