#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Write a program to solve a classic ancient Chinese puzzle: 
# We count 35 heads and 94 legs among the 
#chickens and rabbits in a farm. How many rabbits 
# and how many chickens do we have?
# Hint:
# Use for loop to iterate all possible solutions.
#
#
################################################################

head = 35
leg = 94
res =[]

for i in range(head):
    j = head-i
    if i*4+2*j==leg:
        res.append([i,j])

print(res)


def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)