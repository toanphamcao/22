"""
Author: Phạm Cao Toàn
Date: 24/07/2021
Program: project_03_page99.py
Problem:
    Explain how to check for an invalid input number and prevent it being used in a program.
     You may assume that the user enters a number.
Solution:
    ....
"""
count = 0

print()
while True:
    count += 1
    myNumber = (smaller + larger) // 2
    print('%d %d' % (smaller, larger))
    print('Your number is %d' % myNumber)
    choice = input('Enter =, <, or >: ')
    if choice == '=':
        print("Hooray, I've got it in %d tries" % count)
        break
    elif smaller == larger:
        print("I'm out of guesses, and you cheated")
    elif choice == '<':
        larger = myNumber - 1
    else:
        smaller = myNumber + 1

