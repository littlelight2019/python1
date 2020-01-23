# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:46:31 2020

@author: qjane
"""

import numpy as np
from datetime import datetime
import matplotlib.pyplot as pl

def sample_run_times(T, k=10):
    all_times=[]
    for e in T:
        n = int(10**e)
        a = np.ones([n,n])
        times = []
        
        for i in range(k):
            t0 = datetime.now()
            s = 0
            for i in range(n):
                s += sum(a[:,i])
            t1 = datetime.now()
            s=0
            for i in range(n):
                s += sum(a[i,:])
            t2 = datetime.now()
            times.append({'row minor':t1-t0, 'row major': t2-t1})
        all_times.append({'n': n, 'times': times})
    return(all_times)
    
all_times = sample_run_times(np.arange(3, 4, 0.01), k=1)
n_list = [a['n'] for a in all_times]
ratios = [a['times'][0]['row minor']/a['times'][0]['row major'] for a in all_times]

pl.figure(figsize=(10,6 ))
pl.plot(n_list, ratios)
pl.grid()
pl.xlabel('size of matrix')
pl.ylabel('ratio of running times')
pl.title('time ratio as a function of size of array')    