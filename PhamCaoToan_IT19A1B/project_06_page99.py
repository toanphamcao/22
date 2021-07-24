"""
Author: Phạm Cao Toàn
Date: 24/07/2021
Program: project_06_page99.py
Problem:
    Explain how to check for an invalid input number and prevent it being used in a program.
     You may assume that the user enters a number.
Solution:
    ....
"""
number=float(input("Enter the number iterations: "))
pi=0
div=1

while(div<=number):
    positive_value = 4/(2*div-1)
    pi += positive_value
    div=div+2

div=2

while(div<=number):
    negative_value=4/(2*div-1)
    pi -=negative_value
    div=div+2

print("The approximation of pi is %.16f "%pi)