#! /usr/bin/env python3 
# Author: Stephen
# Description: This script will demo how to
""" 
    Docstring:
"""


import sys
import os

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print(home_dir)