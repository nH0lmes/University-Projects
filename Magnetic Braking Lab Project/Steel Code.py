
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from scipy.optimize import curve_fit

def exponential_func(x,a,b,c):
    return a*np.exp(-b*x)+c
def exponential_derivative(x,a,b,c):
    return -a*b*np.exp(-b*x) + c
def labels(axis,ylabel,xlabel,title):
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
    axis.set_title(title)
    #axis.legend()
    plt.tight_layout()
fig0 = plt.figure(figsize = (5,5))
ax0 = fig0.add_subplot(1,1,1)
labels(ax0,'Angular Velocity','Time / s','Aluminium with no Magnetic Field')

fig1 = plt.figure(figsize = (5,5))
ax1 = fig1.add_subplot(1,1,1)
labels(ax1,'Angular Velocity','Time / s','Steel')

fig2 = plt.figure(figsize = (5,5))
ax2 = fig2.add_subplot(1,1,1)
labels(ax2,'Angular Velocity','Time / s','Aluminium in presence of Magnetic Field')

fig3 = plt.figure(figsize = (5,5))
ax3 = fig3.add_subplot(2,1,1)
ax4 = fig3.add_subplot(2,1,2)
labels(ax3,'Angular Acceleration','Angular Velocity',None)
labels(ax4,'Angular Acceleration','Angular Velocity',None)

fig5 = plt.figure(figsize = (5,5))
ax5 = fig5.add_subplot(1,1,1)
labels(ax5,'Angular Acceleration','Angular Velocity',None)

vals = pd.read_csv('Steelmag.csv', header = 0, names = ('t1','v1','t2','v2','t3','v3','t4','v4'))
nomag_vals = pd.read_csv('Coppernomag.csv', header = 0, names = ('time','voltage'))
nomag_vals['voltage']*=200*np.pi

value_counts = nomag_vals['voltage'].value_counts()
nomag_newvals = nomag_vals[(nomag_vals['voltage']>(nomag_vals['voltage'].min()+5))&(nomag_vals['voltage']<(nomag_vals['voltage'].max()-8))]

ax0.plot(nomag_vals['time'],nomag_vals['voltage'])

poptog,pcovog = curve_fit(exponential_func,nomag_newvals['time'],nomag_newvals['voltage'])

ax0.plot(nomag_newvals['time'],exponential_func(nomag_newvals['time'],*poptog),'black', linestyle = '--')
#value_counts = vals['voltage'].value_counts()
b_dependance = pd.DataFrame(columns = ['gradient', 'b_field'])
                                       

for i in range (1,5):
    vals[f'v{i}']*=(200*np.pi)
    ax1.plot(vals[f"t{i}"],vals[f'v{i}'],label=str("{:.2f}".format(i*0.05))+' T')
    newvals = vals[(vals[f'v{i}']>(vals[f'v{i}'].min()+7))&(vals[f'v{i}']<(vals[f'v{i}'].max()-10))]
    popt,pcov = curve_fit(exponential_func,newvals[f't{i}'],newvals[f'v{i}'],maxfev = 100000)
    #ax1.plot(newvals[f't{i}'],exponential_func(newvals[f't{i}'],*popt),'black',linestyle = '--')
    ax2.plot(newvals[f't{i}'],exponential_func(newvals[f't{i}'],*popt))
    ax3.plot(exponential_func(newvals[f't{i}'],*popt),exponential_derivative(newvals[f't{i}'],*popt),)
    ax4.plot(np.arange(0, 100), -popt[1] * np.arange(0, 100))
    ax5.plot(np.arange(0, 100), (-popt[1]+poptog[1]) * np.arange(0, 100))
    print(popt[1])
    b_dependance = b_dependance.append({'gradient':popt[1],'b_field':(0.05*i)**2},ignore_index =True)
print (poptog[1])
#ax1.plot(newvals['time'], exponential_derivative(newvals['time'],*popt))
print(b_dependance)
fig6 = plt.figure(figsize = (5,5))
ax6 = fig6.add_subplot(1,1,1)
ax6.scatter(b_dependance['b_field'],b_dependance['gradient'],marker = 'x',color = 'black')
a,b = np.polyfit(b_dependance['b_field'],b_dependance['gradient'],1)
ax6.plot(b_dependance['b_field'],a*b_dependance['b_field']+b)
labels(ax6,'$B^2$ / $T^2$','Gradient',None)
ax1.legend()
#plt.show()
#print(popt[1])
#plt.style.use = ("gg.plot")

