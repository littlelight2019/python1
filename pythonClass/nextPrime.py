# -*- coding: utf-8 -*-

import math

def genPrimes():
    p = 2
    while True:
        yield p
        p += 1
        while hasFactor(p):
            p += 1
    
def hasFactor(num):
    for factor in range(2, int(math.sqrt(num)) + 2):
        if num%factor == 0:
            return True
    return False        

p = genPrimes()

for i in range(100):
    print(p.__next__())