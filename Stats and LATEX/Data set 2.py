# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:31:35 2023

@author: nphol
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
data = pd.read_csv('sn229311293pt2.csv', usecols = [2,3,4], names=['Distance','Force', 'StdForce'], skiprows = 1, nrows = 40 )
x = [i/10**3 for i in data['Distance']]
y = [i/10**9 for i in data['Force']]
error = [i/10**9 for i in data['StdForce']]

def line(x, a, b):
    return a*x+b
popt, pcov = curve_fit(line,x,y)
slope = popt[0]
intercept = popt[1]
err_slope = np.sqrt(float(pcov[0][0]))
err_intercept = np.sqrt(float(pcov[1][1]))
print(f"{-slope} + {err_slope}")
print(f"{intercept} + {err_intercept}")
best_fit = [slope*i + intercept for i in x]

new_slope = -slope
equilibrium = intercept/new_slope
error2 = np.sqrt(((1/new_slope)*err_intercept)**2+((intercept/new_slope**2)*err_slope)**2)
print(equilibrium)
print(error2)
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(1,1,1)
ax.errorbar(x,
            y,
            yerr =error,
            marker = 'o',
            linestyle = 'none',
            color = 'black',
            capsize = 6
            )
ax.plot(x,best_fit, color = 'black')
ax.set_xlabel('Distance / km', fontsize = 25)
ax.set_ylabel('Force / GN', fontsize = 25)
plt.tick_params(direction='out',
                length = 5,
                bottom = 'on',
                left ='on',
                top='on',
                right = 'on',
                labelsize = 20
                )
