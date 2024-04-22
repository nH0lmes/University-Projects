
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
from matplotlib.pyplot import cm
from scipy.optimize import curve_fit

def piticker(axis):
    axis.xaxis.set_major_formatter(tck.FormatStrFormatter('%g $\pi$'))
    axis.xaxis.set_major_locator(tck.MultipleLocator(base=0.5))
    
def labels(axis,xlabel,ylabel,title):
    axis.set_xlabel(xlabel)
    axis.set_ylabel(ylabel)
    axis.set_title(title)
    axis.legend
    plt.tight_layout()
    axis.legend()

h1 = pd.read_csv('h1.txt', header = None, names = ['real', 'imaginary','time'])
ift_h1 = pd.read_csv('ift_h1.txt', header = None, names =['real', 'imaginary','time'])

h2 = pd.read_csv('h2.txt', header = None, names = ['real', 'imaginary','time'])
ift_h2 = pd.read_csv('ift_h2.txt', header = None, names =['real', 'imaginary','time'])

h3 = pd.read_csv('h3.txt', header = None, names = ['number', 'time','real', 'imaginary'])
ift_h3 = pd.read_csv('newift_h3vals.txt', header = None, names =['real', 'imaginary','time'])

fig1 = plt.figure(figsize = (5,5))
ax1 = fig1.add_subplot(2,1,1)
ax2 = fig1.add_subplot(2,1,2)

ax1.plot(h1['time']/50,h1['real'], label =  r"$h_{1}$")
ax1.plot(ift_h1['time']/50,ift_h1['real'], label = r"$h'_{1}$")
piticker(ax1)
labels(ax1,'Time','Value',r'$h_{1}$ real')



ax2.plot(h1['time']/50,h1['imaginary'], label =  r"$h_{1}$")
ax2.plot(ift_h1['time']/50,ift_h1['imaginary'], label =  r"$h'_{1}$")
piticker(ax2)
labels(ax2,'Time','Value',r'$h_{1}$ imaginary')
fig1.tight_layout()


fig2 = plt.figure(figsize = (5,5))
ax3 = fig2.add_subplot(2,1,1)
ax6 = fig2.add_subplot(2,1,2)

ax3.plot(h2['time']/50,h2['real'], label = r"$h_{2}$")
ax3.plot(ift_h2['time']/50,ift_h2['real'], label = r"$h'_{2}$")
piticker(ax3)
labels(ax3,'Time','Value',r"$h_{2}$ real")

ax6.plot(h2['time']/50,h2['imaginary'], label = r"$h_{2}$")
ax6.plot(ift_h2['time']/50,ift_h2['imaginary'], label = r"$h'_{2}$")
piticker(ax6)
labels(ax6,'Time','Value',r"$h_{2}$ imaginary")


fig1 = plt.figure(figsize = (5,5))
ax4 = fig1.add_subplot(2,1,1)
ax5 = fig1.add_subplot(2,1,2)

ax4.plot(h3['number']/100,h3['real'], label = r"$h_{3}$")
ax4.plot(ift_h3['time']/100,ift_h3['real'], label=r"$h'_{3}$")
piticker(ax4)
labels(ax4,'Time','Value',r"$h_{3}$ real")
ax5.plot(h3['number']/100,h3['imaginary'], label = r"$h_{3}$")
ax5.plot(ift_h3['time']/100,ift_h3['imaginary'], label = r"$h'_{3}$")
piticker(ax5)
labels(ax5,'Time','Value',r"$h_{3}$ imaginary")