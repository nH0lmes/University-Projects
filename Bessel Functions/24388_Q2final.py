# -*- coding: utf-8 -*-
"""
Created on Thu May  4 08:44:46 2023

@author: nphol
"""

import numpy as np
import matplotlib.pyplot as plt
# I started by defining the function inside the integral, meaning i could easily call on it any time it was needed.
def func(a,m,x):
    y = np.cos(m*a-x*np.sin(a))
    return y
# I then defined the Bessel function
# The main bit of the code is the integration, using the trapezium rule.
def Jm(m,x):
    a=0
    b=np.pi
    N=10000
    h=(b-a)/N
    integration = func(a,m,x)+func(b,m,x)
    for i in range(1,N):
        xi = a + i*h
        integration +=2*func(xi,m,x)
    area = (h/(2*np.pi))*integration
    return(area)

# Next, I plotted the first 3 bessel functions
xvalues = np.linspace(0,20,201)
function = [0,1,2]

fig1,ax1 = plt.subplots()

for m in function:
    y = [Jm(m,x)for x in xvalues]
    plt.plot(xvalues,y, linewidth = '0.8', label =r'$J_{{{}}}(x)$'.format(m))

ax1.set_title('The first 3 bessel functions as a function of x')
ax1.set_ylim(-1,1.25)
ax1.set_xlim(0,20)
ax1.axhline(y=0,color = 'black', linewidth = '0.5')
ax1.legend()

#Plotting the intensity as a function of radius
fig2, ax2 = plt.subplots()    
w=500*10**-9
rvalues = np.linspace(-25*10**-6,25*10**-6,500)
x = [(np.pi*r)/(w*10)for r in rvalues]

intensity = [1*(2*Jm(1,n)/n)**2 for n in x]
    
ax2.plot(rvalues,intensity)
ax2.set_ylabel('Intensity')
ax2.set_xlabel('r / µm')
ax2.set_title('Diffraction pattern for a circular lens')

# This final plot shows the radius as a circle with 2 dimensions and the intensity is represented by the opacity of the circles
fig3, ax3 = plt.subplots()

for r, i in zip(rvalues, intensity):
    circle = plt.Circle((0, 0), abs(r), color='black', alpha = i, linewidth=1, fill = False)
    ax3.add_artist(circle)

ax3.set_aspect('equal')

# Set the limits of the plot
ax3.set_xlim([-max(rvalues), max(rvalues)])
ax3.set_ylim([-max(rvalues), max(rvalues)])

# Set labels and title
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_title('Diffraction pattern for a circular lens')

# Display the plot
plt.show()

