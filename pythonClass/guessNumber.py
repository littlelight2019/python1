# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:56:47 2019

@author: qjane
"""

print('Please think of a number between 0 and 100!')
low = 0
high = 100
while True:
    mid = (low + high) // 2
    print('Is your secret number %d?' % mid)
    char = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly. ")
    while char not in list('hlc'):
        print('Sorry, I did not understand your input.') 
        print('Is your secret number %d?' % mid)
        char = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly. ")
    if char == 'h':
        high = mid
    elif char == 'l':
        low = mid
    else:
        print('Game over. Your secret number was: %d' % mid)
        break
    