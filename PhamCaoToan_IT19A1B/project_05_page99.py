"""
Author: Phạm Cao Toàn
Date: 24/07/2021
Program: project_05_page99.py
Problem:
    Explain how to check for an invalid input number and prevent it being used in a program.
     You may assume that the user enters a number.
Solution:
    ....
"""
P0 = -1
while (float(P0)<=0):
P0 = input(" How many initial population ??? :>")
R=-1
while float(R)<0:
R = input(" Please input the growth rate :>")
t = -1
while float(t)<0:
t = input("please input the time :>")
N = -1
while int(N)<0:
N = input(" how many interations ??? :>")
print(" initial population = " + str(P0) + " : growth rate = " + str(R) + " : time = " + str(t) + " : " + str(N) + " iterations ")

P = P0
print("Time Population")

for i in range(int(N)):

timeT = int(i)*float(t)

print(" " + str(timeT) + " " + str(P))

P = float(R)*float(P)