import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys
sys.path.append('./')
from lagrange_interpolation import lagurange as lg
from yml_io import read_yml

data = read_yml()

def linear_fit(x,a,b):
    return a*x + b

def square_fit(x,a,b,c):
    return a*x*x + b*x + c

color_list = ['r','g','b','c','m','y','k','w']
fig, host = plt.subplots()

#y
host.set_ylabel('N [rpm]', fontsize=14)
#x
host.set_xlabel('V [V]', fontsize=14)
host.xaxis.set_minor_locator(ticker.MultipleLocator(1))
host.xaxis.set_major_locator(ticker.MultipleLocator(10))

for i in range(3):
    j = (i + 8)/10
    num_name = '{}A'.format(j)
    volt = data[num_name]
    points_x = np.array(volt['V'])
    points_y = np.array(volt['N'])
    ix=np.arange(80, 133, 1)
    param, cov = curve_fit(linear_fit, points_x, points_y)
    point_fit = param[0] * points_x + param[1]
    iy=lg(ix, points_x, point_fit)
    style =color_list[i] +'+'
    plt.plot(points_x, points_y,style)
    plt.plot(ix, iy, color=color_list[i], linestyle='solid')

host.grid(b=True, which='major', color='grey', linestyle='-')
plt.show()
