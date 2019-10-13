# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:42:53 2019

@author: qjane
"""
from sys import argv

def creditCardBalance(balance, annualInterestRate, payment):
    """
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    Monthly interest rate= (Annual interest rate) / 12.0 
    """
    monthlyInterestRate = annualInterestRate / 12.0
    for month in range(12):
        balance = balance - payment
        balance += balance * monthlyInterestRate
    return balance
    

def main():
    """
    using binary search to find the minimum payment that
    pays off the balance in one year
    accuracy is set to one cent, i.e. 0.01
    
    inputs: annualInterestRate, balance
    annualInterestRate: float
    balance: float
    """
    #annualInterestRate = 0.2
    #balance = 3926
    annualInterestRate = float(argv[1])
    balance = float(argv[2])
    upperBound = balance / 12 * (1 + annualInterestRate /12) ** 12
    lowerBound = balance / 12
    epsilon = 0.01
    while True:
        lowestPayment = (upperBound + lowerBound) / 2
        endBalance = creditCardBalance(balance, annualInterestRate, lowestPayment)
        #print(i, upperBound, lowerBound, lowestPayment, endBalance)
        if endBalance > epsilon:
            lowerBound = lowestPayment
            #print('positive balance change lowerBound to %f' % lowerBound)
        elif endBalance < -epsilon:
            upperBound = lowestPayment
            #print('negative balance change upperBound to %f' % lowerBound)
        else:
            print('Lowest Payment: %.2f' % round(lowestPayment,2))
            break

if __name__ == '__main__':
    main()
    