# -*- coding: utf-8 -*-

#import pylab as plt
import matplotlib.pyplot as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
 
plt.figure(figsize=(15,18))
plt.clf()
plt.subplot(321)
plt.title('Linear plot')
plt.ylim(0,900)
plt.xlabel('Sample points')
plt.ylabel('Linear function')
plt.plot(mySamples, myLinear, 'b-',label= 'Linear', linewidth=2)
plt.legend(loc='upper left')   

plt.subplot(322)
plt.title('Quadratic plot')
plt.ylim(0,900)
plt.xlabel('Sample points')
plt.ylabel('Quadratic function')  
plt.plot(mySamples, myQuadratic, 'go', label = 'Quadratic', linewidth=3)
plt.legend(loc='upper left') 

plt.subplot(323)
plt.title('Cubic plot')
plt.xlabel('Sample points')
plt.ylabel('Cubic function')
plt.plot(mySamples, myCubic, 'r^',label = 'Cubic', linewidth=4)
plt.ylim(0,140000)
plt.legend(loc='upper left')   

plt.subplot(324)
plt.title('Exponential plot')
plt.ylim(0,140000)
plt.xlabel('Sample points')
plt.ylabel('Exponential function')  
plt.plot(mySamples, myExponential, 'k--', label = 'Exponential', linewidth=5)
plt.legend(loc='upper left') 

plt.subplot(325)
plt.title('Cubic and Exponential plots')
plt.xlabel('Sample points')
plt.ylabel('Cubic and Exponential functions')
plt.plot(mySamples, myCubic, 'r^',label = 'Cubic', linewidth=4)
plt.yscale('log') 
plt.plot(mySamples, myExponential, 'k--', label = 'Exponential', linewidth=5)
plt.legend(loc='upper left') 


def retire(monthly, rate, terms):
    base = [0]
    savings = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings

def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure(figsize=(10, 6))
    plt.title('retireMonthly')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label='retire:' + str(monthly))
        plt.legend(loc = 'upper left')
        
monthlies = [x * 100 for x in range(5,12)]
displayRetireWMonthlies(monthlies, 0.05, 40 * 12)