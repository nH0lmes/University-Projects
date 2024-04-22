# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:47:47 2023

@author: nphol
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('sn229311293pt2.csv', usecols = [0,1], names=['Current','Uncertainty'], skiprows = 1  )
values = [3,5,10,50,100,10000]
results = []
for i in values:
    newdata = [n for n in data['Current'][:i]]
    total = sum(newdata)
    mean = total/i
    print(mean)
    squared = [(n - mean)**2 for n in newdata]
    std_deviation = np.sqrt(sum(squared)/(i-1))
    print(std_deviation)
    std_error = std_deviation/np.sqrt(i)
    print(std_error)
    results.append([mean,std_deviation,std_error])
print(mean**2*100)
print((mean+std_error)**2*100 - mean**2*100)
#graph_data = [[(n*1000).round(3) for n in inner]for inner in results]
#plt.figure(linewidth=2,
 #          edgecolor= 'black',
  #         facecolor= 'lightgray',
   #        tight_layout={'pad':1})
#table = plt.table(cellText = graph_data ,
 #                     colLabels= ['Mean','Standard Deviation', 'Standard error'],
  #                    colColours = ['red' for i in range(0,3)],
   #                   cellLoc = 'center',
    #                  loc='center')
#table.scale(1,1.5)
#ax = plt.gca()
#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)
#plt.box(on=None)
#plt.suptitle('title')
#plt.draw()

#plt.show
x = ['red' for i in range(0,2)]
    
    
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(1,1,1)
ax.errorbar([i for i in range(1,51)],
            data['Current'][:50]*10**3,
            yerr=data['Uncertainty'][:50]*10**3,
            marker = 'o',
            linestyle = 'none',
            color = 'black',
            capsize = 6
            )
plt.xlim(0,51)
ax.set_xlabel('Measurement number', fontsize = 25)
ax.set_ylabel(r'Electrical current through resistor / mA', fontsize = 25)
plt.tick_params(direction='out',
                length = 6,
                bottom = 'on',
                left ='on',
                top='on',
                right = 'on',
                labelsize = 20
                )
