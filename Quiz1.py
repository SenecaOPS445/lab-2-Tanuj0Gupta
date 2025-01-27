#! /usr/bin/env python3

# Author: Tanuj Gupta
# Author Id: 162349229
# Date Created: 2025-01-27



#Giving user option to either inches --> cm or cm --> inches.
print("1. Convert inches -> cm")
print("2. Convert cm -> inches")

#Prompting user to make a selection.
select = int(input("Make your selection (1,2): "))

#Checking users input and performing conversion.
if select == 1:
    inches = int(input("Enter inches: "))
    cm = inches * 2.54
    print("Number of cm:",cm)
elif select == 2:
    cm = int(input("Enter cm: "))
    inches = cm / 2.54
    print("Number of inches:", inches)
else:
    print("Invalid entry") #If a user enters number other than 1 or 2.