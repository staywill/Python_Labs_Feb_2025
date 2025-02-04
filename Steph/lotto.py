#! /usr/bin/env python3
# Author: Stephen
# Description: This script will generate 6 random lottery numbers
"""
    Docstring:
"""
import random

lotto = []

while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("Duplicate number =", num)

print ("Lottery number =", lotto)
