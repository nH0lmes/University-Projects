# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:44:18 2023

@author: nphol
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = pd.read_excel('data.xlsx', sheet_name = 'Sheet2', usecols = [0,1], names = ['current','mfs'])
ydata = data['mfs']
xdata = data['current']

def line(x, a, b):
    return a*x+b
popt, pcov = curve_fit(line,xdata,ydata)

slope = popt[0]
intercept = popt[1]
err_slope = np.sqrt(float(pcov[0][0]))
err_intercept = np.sqrt(float(pcov[1][1]))

best_fit = [slope*i + intercept for i in xdata]


fig = plt.figure(figsize = (5,5))
ax = fig.add_subplot(1,1,1)

ax.errorbar(xdata,
            ydata,
            marker = 'o',
            linestyle = 'none',
            color = 'black')
plt.tick_params(direction='in',
                length = 5,
                bottom = 'on',
                left ='on',
                top='on',
                right = 'on',
                labelsize = 12
                )
ax.plot(xdata,best_fit, color = 'black')
ax.set_xlabel('Current / A', fontsize = 15)
ax.set_ylabel('Magnetic Field / mT', fontsize = 15)

print(slope)
print(err_slope)

