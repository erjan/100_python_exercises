#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 18
# Level 3
#
################################################################
#
# Question:
# A website requires the users to input username and password 
# to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated
#  passwords and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################

import re
pwds = input().split(',')
valids = []

def checker(s):
    one_number = bool(re.search(r'\d',s))
    one_upper_letter = bool(re.search(r'[A-Z]',s))
    one_lower_letter = bool(re.search(r'[a-z]',s))
    one_char = bool(re.search(r'[$#@]',s))
    len_check = len(s)>=6 and len(s)<=12

    return one_char and one_upper_letter and one_lower_letter and len_check and one_number

for pwd in pwds:
    if checker(pwd):
        valids.append(pwd)

valids = ','.join(valids)
print(valids)

    
