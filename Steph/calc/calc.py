#! /usr/bin/env python3 
# Author: Stephen
# Description: This is an ULTRA REALISTIC calculator with tons of features!
""" 
    Docstring:
"""

import sys
import basic
import adv
def main():
    menu = """
            Calculator App
            --------------
            1. Test Basic
            2. Test Adv
    """
    print(menu)
    option = input("Choose 1 or 2: ")
    if option == "1":
        print(f"100 + 50 + 25 + 12.5 = {basic.add(100, 50, 25, 12.5)}")
        print(f"100 + 50 + 25 + 12.5 = {basic.mult(100, 50, 25, 12.5)}")
    elif option == "2":
        print(f"modulus of 100 by 45 = {adv.mod(100, 45)}")
        print(f"Square root of 25 = {adv.sqrt(25)}")
    else:
        print("invalid Option")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0) # exit program with 0 error

