#! /usr/bin/env python3 
# Author: Stephen
# Description: This script will simulate a high street bank

""" 
    Docstring: exercise 9
"""

def frange(start,stop=None,step=25):
    if stop is None:
        stop=start
        curr = 0.0
    else:
        curr = float(start)

one = list(frange(0,3.5,0.25))
