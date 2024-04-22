# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:23:27 2023

@author: nphol
"""
import numpy as np
import scipy.constants as sci
import matplotlib.pyplot as plt
# start by defining both the function and it's derivative
def fx(x) :
    fx = np.exp(x)*(5-x)-5
    return (fx)
def deriv(x):
    d=np.exp(x)*(4-x)
    return(d)

# I then plotted a graph of the function in order to determine the approximate values of the roots
xvalues = np.linspace(-6,5.2,1000)
y = [fx(i) for i in xvalues]
plt.plot(xvalues,y)
plt.xticks(np.linspace(-6,6,13))
plt.axhline(y=0, color = 'black', linewidth = 0.5)
plt.axvline(x=0, color = 'black', linewidth = 0.5)

# Using the Newton-Raphson method to determine the root. I started at 5 as it was close to the second root.
# In the while function, I first use the equation for the NR method. 
# The next line finds the difference between this estimation and the previous estimation.
# The while loop will repeat until the difference is very small, meaning it is an accurate value
x0 =5
delta = 1
while abs(delta) >1*10**-20:
    x1 = x0-(fx(x0)/deriv(x0))
    delta = x1-x0
    x0=x1
# Finally I change my value for the root into a value for Wein's constant
h = sci.h
c = sci.c
k = sci.k

b=(h*c)/(x1*k)
print(b)