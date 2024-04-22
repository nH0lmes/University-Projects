
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data = pd.read_csv('sn229311293pt2.csv', usecols = [6,7,8], names=['time', 'position', 'std'], skiprows = 1, nrows = 35)
print(data)


fig = plt.figure(figsize=(10,20))
ax1 = fig.add_subplot(2,1,1)
ax1.errorbar(data['time'],
            data['position'],
            yerr = data['std'],
            marker = 'o',
            linestyle = 'none',
            color = 'black',
            capsize = 6
            )
ax1.set_xlabel('Fall time t / s' ,fontsize = 30)
ax1.set_ylabel('Position of body h /m', fontsize = 30)
plt.tick_params(direction='out',
                length = 5,
                bottom = 'on',
                left ='on',
                top='on',
                right = 'on',
                labelsize = 25
             )
ax1.text(0.1,358,'(A)', fontsize = 40)

x = np.log(data['time']/0.1)
y = np.log(data['position']/0.1)
yerror = np.log(np.e)*(data['std']/data['position'])
print(yerror)
def line(x, a, b):
    return a*x+b
popt, pcov = curve_fit(line,x,y,sigma = yerror)

slope = popt[0]
intercept = popt[1]
err_slope = np.sqrt(float(pcov[0][0]))
err_intercept = np.sqrt(float(pcov[1][1]))

best_fit = [slope*i + intercept for i in x]
ax2 = fig.add_subplot(2,1,2)
ax2.errorbar(x,
              y,
              yerror,             
              marker ='o',
              linestyle = 'none',
              color = 'black',
              capsize = 6
              )
ax2.plot(x,best_fit, color = 'black')
ax2.set_xlabel('log$_{10}$( t/0.1 s)', fontsize = 30)
ax2.set_ylabel('log$_{10}$( h/0.1 m)', fontsize = 30)
ax2.text(0.9,7.7,'(B)', fontsize = 40)
plt.tick_params(direction='in',
                length = 5,
                bottom = 'on',
                left ='on',
                top='on',
                right = 'on',
                labelsize = 25
                )
print(slope)
print(err_slope)