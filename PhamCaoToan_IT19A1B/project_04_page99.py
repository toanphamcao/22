"""
Author: Phạm Cao Toàn
Date: 24/07/2021
Program: project_04_page99.py
Problem:
    Explain how to check for an invalid input number and prevent it being used in a program.
     You may assume that the user enters a number.
Solution:
    ....
"""
import math
distance = 0

initial = float(input("Please enter initial height: "))

bounce = float(input("Please enter bounciness index: "))

number = int(input("Please enter number of bounces allowed: "))

distance += initial

while number > 0 :
    initial *= bounce

    distance += initial*2

    number -= 1

print("Total distance traveled is: %.3f" % distance)
print(number)
print(initial)