#! /usr/bin/env python3 
# Author: Stephen
# Description: This module contains a collection off calculator funcions
""" 
    basic calculator functions including add, multiply, and divide
"""

import sys

def add(*args):
    """ Return Sum of all parameters """
    total = 0
    for num in args:
        total += num
    return total

def mult(*args):
    """ Return PRODUCT of all parameters """
    total = 1
    for num in args:
        total += num
    return total

def div(x, z):
    """ Return Quotient of all parameters """
    return round(x/z, 3)

print("Basic Calculator App ")

print (f"4 + 3 = {add(4, 3)}")
print (f"4 + 3 + 2 = {add(4, 3, 2)}")
print (f"4 * 3 = {mult(4, 3)}")
print (f"4 * 3 * 2 = {mult(4, 3, 2)}")
print (f"4 / 3 = {div(4, 3)}")

sys.exit(0) # exit program with 0 errors