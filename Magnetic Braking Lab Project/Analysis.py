import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from scipy.optimize import curve_fit

def exponential_func(x,a,b,c):
    return a*np.exp(-b*x)+c
def exponential_derivative(x,a,b,c):
    return -a*b*np.exp(-b*x) + c

fig = plt.figure(figsize = (5,5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
vals = pd.read_csv('Al nomag.csv', header = 0, names = ('time','voltage'))

value_counts = vals['voltage'].value_counts()




newvals = vals.groupby('voltage').filter(lambda x: len(x)<2)
fig = plt.figure(figsize = (5,5))
ax1.plot(vals['time'],vals['voltage'])

poptog,pcovog = curve_fit(exponential_func,newvals['time'],newvals['voltage'])

ax1.plot(newvals['time'],exponential_func(newvals['time'],*poptog),'black', linestyle = '--')
#plt.style = ("gg")
ax1.plot(newvals['time'], exponential_derivative(newvals['time'],*poptog))
ax2.plot(exponential_func(newvals['time'],*poptog),exponential_derivative(newvals['time'],*poptog),)
plt.show()
print(poptog[1])
