'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	A program that lets you enter degrees in celsius and converts in Fahrenheit 
Author:	Fabroa.E
Created: 0/12/2020
------------------------------------------------------------------------------
'''

# Gets celsius from the user
celsius = float(input("Enter a temperature in celsius, and my program will convert it to fahrenheit: "))

# Stores its value in fahrenheit inside of this variable
fahrenheit = (9/5)*celsius + 32

# Prints out the variable (result)
print("Your temperature in fahrenheit is: {} degrees".format(fahrenheit))

