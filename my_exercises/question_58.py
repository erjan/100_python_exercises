#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Assuming that we have some email addresses in 
# the "username@companyname.com" format, please write 
# program to print the user name of a given email address.
#  Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# john
# In case of input data being supplied to the question, it 
# should be assumed to be a console input.
#
# Hints:
# Use \w to match letters.
#
################################################################

import re

s = 'llll@google.com'

get_username_pattern = "(\w+)@(\w+).(com)"

q = re.match(get_username_pattern,s).group(1)
print(q)