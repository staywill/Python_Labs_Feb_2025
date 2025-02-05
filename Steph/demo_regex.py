#! /usr/bin/env python3 
# Author: Stephen
# Description: This script will simulate a high street bank
# ATM PIN machine
""" 
    Docstring:
"""
import re

fh_in = open(r"c:\labs\words", mode ="rt")

#iterate through file handle one line at a time
for line in fh_in:
    # example of str testing =Good!
    #if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
  # m = re.search("^the", line) #match lines starting with the 'the'
   # m = re.search("ing$", line) # match lines ending with 'ing'
    m = re.search("^ring$", line) # match lines ending with 'ing'
    if m:
        print(line, end="")
