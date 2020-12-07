'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	A program that distrubutes chicken wings evenly among students, then sets aside the rest for teacher
Author:	Fabroa.E
Created: 07/12/2020
------------------------------------------------------------------------------
'''

# Gets number of students and number of chicken wings from user
number_of_students = int(input("Enter the number of students in Mr.Fabroa's class: "))
number_of_chicken_wings = int(input("Enter the number of chicken wings to be distributed: "))

# This part distributes the chicken wings the way described in the question
chicken_wings_per_student = number_of_chicken_wings // number_of_students
left_over = number_of_chicken_wings % number_of_students

# prints out the result here
print("Number of chicken wings for each student is: {}".format(chicken_wings_per_student))
print("Number of chicken wings for Mr.Fabroa is: {}".format(left_over))
