"""
Author: Phạm Cao Toàn
Date: 24/07/2021
Program: project_09_page99.py
Problem:
    Explain how to check for an invalid input number and prevent it being used in a program.
     You may assume that the user enters a number.
Solution:
    ....
"""
theSum = 0.0
data = input("Enter a number: ")
while data != "":
    number = float(data)
    theSum += number
    data = input("Enter the next number: ")
print("The sum is", theSum)