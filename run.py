# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

x = random.randint(1, 10)

def welcome():
    print('Please insert min number')
    min = int(input())
    print('Please insert max number')
    max = int(input())
    print('Please inert number of rolls')
    rolls = int(input())
    print('..............................................')

    i = 0
    while i < rolls:
        rand = random.randint(min, max)
        print(rand)
        i += 1
    
    print('Again y/n')
    again = input()
    if again == 'y':
        print('..............................................')
        welcome()
    else:
        exit()

welcome()