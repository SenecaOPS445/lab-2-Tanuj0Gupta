#!/usr/bin/env python3

# Author : Tanuj Gupta
# Author ID: 162349229
# Date Created: 2025/01/25


import sys

if len(sys.argv) > 1: #So here, if user enter argument then the timer = user entered argument"
    timer = int(sys.argv[1])  #I am assigning the enter argumnet here to object named == timer
else:
    timer = 3 #Or else timer == 3


while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')


