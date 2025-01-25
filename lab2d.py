#!/usr/bin/env python3
import sys


if len(sys.argv) != 3:
    print("Usage: ./lab2d.py name age")
    sys.exit()  


name = str(sys.argv[1])
age = int(sys.argv[2])


print("Hi " + name + ", you are " + str(age) + " years old.")
