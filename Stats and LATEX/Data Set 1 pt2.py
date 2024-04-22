# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:52:12 2023

@author: nphol
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('sn229311293pt2.csv', usecols = [0,1], names=['Current','Uncertainty'], skiprows = 1  )
values = [3,5,10,50,100,10000]
weight = 0
results = []
for i in values:
    newdata = [n*10**3 for n in data['Current'][:i]]
    total = sum(newdata)
    mean = total/i
    #print(mean)
    weight = [1/(j*10**3)**2 for j in data['Uncertainty']]
    current = [k for k in data['Current']]
    curwei = [weight[l]*newdata[l]for l in range(0,i)]
    weight_mean = sum(curwei) /sum(weight[:i])
    print(weight_mean)
    std_error = 1/np.sqrt(sum(weight[:i]))
    print(std_error)
    
   # weightsum = sum([(1/data.loc[j,'Uncertainty']^2) * data.loc[j,'Current']  for j in range(0,i)])
   # weight = data['Uncertainty'][:i].sum()
  #  weightmean = weightsum/weight
   # print(weightmean)
