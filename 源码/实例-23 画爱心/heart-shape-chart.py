#原作者：https://blog.csdn.net/qq_27017791/article/details/85040244

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
ln, = ax.plot([], [], '-',color='r', lw=1)
time_template = 'LOVE = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
def init():
    ax.set_xlim(-3,3)
    ax.set_ylim(-2, 3)
    return ln,
def update(ii):
    xdata, ydata = [], []
    for i in range(0,183):
        xi=(182-i)/100
        xdata.append(0.01*i-1.82)
        yi=(xi**(2/3))+(0.9*(3.3-xi**2)**0.5)*np.cos(ii*(np.pi)*xi)
        if type(yi)=='complex':
            yi=np.around(abs(yi),decimals=4)
        yi=np.around(yi, decimals=3)
        ydata.append(yi)
        
    for i in range(0,182):
        xi=i/100
        xdata.append(xi) 
        yi=(xi**(2/3))+(0.9*(3.3-xi**2)**0.5)*np.cos(ii*(np.pi)*xi)
        if type(yi)=='complex':
            yi=np.around(abs(yi),decimals=4)
        yi=np.around(yi, decimals=3)
        ydata.append(yi)
    ln.set_data(xdata, ydata)
    time_text.set_text(time_template %(ii))
    return ln,
ani = FuncAnimation(fig, update, np.linspace(0, 13.14, 100),init_func=init, interval=100)
ani.save('love.gif', writer='imagemagick', fps=60)
plt.show()