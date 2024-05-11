#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
################################################################
#
#
################################################################
#
# Question:
# Please write a binary search function
# which searches an item in a sorted list.
# The function should return the index of 
#element to be searched in the list.
#
# Hints:
# Use if/elif to deal with conditions.
#
################################################################



def bin_search(nums,val):
    l = 0
    r = len(nums)-1

    while l<=r:
        print('------------------')
        mid = abs((l+r))//2

        if nums[mid]>val:
            r= mid-1
        elif nums[mid]<val:
            l=mid+1
        elif nums[mid] == val:
            return mid
    return -1


li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12000))