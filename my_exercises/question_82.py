#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Please write a program to compress and 
# decompress the 
# string "hello world!hello world!hello world!hello world!".
#
# Hints:
# Use zlib.compress() and zlib.decompress() to compress and decompress a string.
#
################################################################


s = b"hello world!hello world!hello world!hello world!"


import zlib

t = zlib.compress(s)

print(t)

t = zlib.decompress(t)

print(t)
