#! /usr/bin/env python3 
# Author: Stephen
# Description: This script will demo how to repeat a block of commands
# a specific amount of times using a counter loop
""" 
    Docstring:
"""

count = 0 #initialize counter
while count < 10: #test counter
    print (count)
    count += 1

#alternatively, we could use a FOR loop plus the built-in
# range (start, stop, step) function, STEP increment is INTEGER
for num in range(0, 10, 1):
    print(num)

#range (start, stop, step=1) function
for num in range(0, 10):
    print(num)

# range (start =0, stop, step =1) function
for num in range(10):
     print(num)
