"""
Author: Phạm Cao Toàn
Date: 24/07/2021
Program: project_01_page99.py
Problem:
    Explain how to check for an invalid input number and prevent it being used in a program.
     You may assume that the user enters a number.
Solution:
    ....
"""
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("tam giác đều")
elif x==y or y==z or z==x:
	print("tam giác cân")
else:
	print("tam giác vuông")