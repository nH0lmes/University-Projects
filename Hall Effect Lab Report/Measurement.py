# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:56:52 2023

@author: nphol
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from scipy.optimize import curve_fit

fig = plt.figure(figsize = (5,5))
ax = fig.add_subplot(1,1,1)
    
color = iter(cm.Accent(np.linspace(0,1,5)))
style = ['o','v','o','v','s']
face = ['black','black','white','white','black']
labels = ['215.8 mT','323.5 mT','410.4 mT', '540 mT','648 mT']
currents = [0.499,0.748,0.949,1.248,1.499]
mfs = [x*432.5 for x in currents]
errors = [[1,3,4,4,6,7,8,8],[2,2,4,3,6,6,7,10],[1,3,6,6,5,7,9,9],[3,4,3,3,6,8,6,9],[5,5,4,6,7,8,9,7]]
data = pd.read_excel('data.xlsx', sheet_name = 'Sheet3', usecols = list(range(0,10)), skiprows = 1, header = None, names = list(range(0,10)))
for i in range(5):
    c = next(color)
    cu = currents[i]*432.5
    ydata = data[2*i+1]
    xdata = data[2*i]
    yerror = [i/1000 for i in errors[i]]
    def line(x, a, b):
        return a*x+b
    popt, pcov = curve_fit(line,xdata,ydata,sigma = yerror)

    slope = popt[0]
    intercept = popt[1]
    err_slope = np.sqrt(float(pcov[0][0]))
    err_intercept = np.sqrt(float(pcov[1][1]))
    
    best_fit = [slope*i + intercept for i in xdata]

    
    ax.errorbar(xdata,
                ydata,
                yerr = yerror,
                marker = style[i],
                markersize = 5,
                linewidth = 1,
                linestyle = 'none',
                color = 'black',
                markerfacecolor = face[i],
                label = labels[i],
                capsize = 2
                )
    ax.plot(xdata,best_fit, color = c)
    slope = slope * 10**3
    err_slope = err_slope * 10**3
    hall_coeff = (1.06*10**-3*slope/(cu*10**-3))
    berror = cu*np.sqrt((9.5/432.5)**2+(0.001/currents[i])**2)
    hall_error = hall_coeff*np.sqrt((berror/cu)**2+(0.02/1.06)**2+(err_slope/slope)**2)
    cc = 1/(hall_coeff*1.602*10**-19)
    carrier_err = cc* np.sqrt((hall_error/hall_coeff)**2)
   # print(f"Magnetic field = {cu}, RH = {hall_coeff}")
    #print(f"carrier concentration = {cc}")
    #print(f"B error = {berror}")
    #print(f"Hall error = {hall_error}")
    #print(f"cc error = {carrier_err}")
    print(slope)
    print(err_slope)
ax.set_ylabel('Hall voltage / V',fontsize = 14)
ax.set_xlabel('Current through semiconductor / mA', fontsize = 14)
ax.legend()
ax.patch.set_edgecolor('black')  
plt.tick_params(direction='in',
                length = 5,
                bottom = 'on',
                left ='on',
                top='on',
                right = 'on',
                labelsize = 12
                )
ax.patch.set_linewidth(1)  
# print(slope)
# print(err_slope)