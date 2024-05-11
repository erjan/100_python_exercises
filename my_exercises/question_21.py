#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
# Question 21
# Level 3
# Question£º
# A robot moves in a plane starting from the original
#  point (0,0). The robot can move toward UP, DOWN, 
# LEFT and RIGHT with a given steps. The trace of robot movement 
#is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a 
#program to compute the distance from current position after a 
# sequence of movement and original point. If the distance is a
#  float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
#
################################################################
#
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
#
################################################################


res = [0,0]

while True:
    s = input()
    if not s:
        break
    else:
        d,move = s.split()
        move = int(move)
        if d == 'DOWN':
            res[0]-=move
        elif d =='UP':
            res[0]+=move
        elif d =='LEFT':
            res[1]-=move
        elif d == 'RIGHT':
            res[1]+=move
    

distance = (res[0]**2 + res[1]**2)**0.5
print(round(distance))
        
