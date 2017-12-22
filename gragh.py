import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import sys
sys.path.append("./")
from lagrange_interpolation import lagurange as lg
from yml_io import read_yml

#label_name
T = "torque[Nm]"
cos = "power factor[%]\n"
ef = "efficiency[%]"
Po = "Output Po[w]"
s = "slip[%]"

data = read_yml()
print (data['100V'])

def linear_fit(x,a,b):
    return (a*x) + b

def op_linear_fit(z,a,b):
    return (a/z) + b


#Points
points_s = np.array([1.4,1.73,2.27,3.07,3.53,4.33,5.07])
points_T = np.array([5.02,6.6,8.25,10.38,12.22,14.42,16.6,])
points_Po = np.array([777.4,1018.9,1266.6,1580.6,1851.7,2177.9,2474.5,])
points_cos = np.array([53.7,64,71.6,76.5,80.1,84.2,86.9,])
points_ef= np.array([82.7,82.2,83.3,83.3,84.2,84.2,82.2,])

points_x = points_s
points_y = points_cos
points_y1 = points_ef
point_test = np.arange(1.4,5.1, 0.1)
#points = np.array([points_x, points_y])
#for ticker
fig, host = plt.subplots()
#for plot
param_cos, cov_cos = curve_fit(op_linear_fit, points_x, points_y)
param_ef, cov_ef = curve_fit(linear_fit, points_x, points_y1)
point_cos = param_cos[0] / points_x + param_cos[1]
point_ef = param_ef[0] * points_x + param_ef[1]

#y
host.set_ylabel(cos + ef, fontsize=14)

#x
host.set_xlabel(s, fontsize=14)
host.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
host.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
#grid
host.grid(b=True, which='major', color='grey', linestyle='-')

#interpolation
ix = np.arange(1.4,5.1,0.1)
iy = lg(ix, points_x, point_cos)

plt.plot(points_x, points_y,"b+")
plt.plot(points_x, points_y1,"g+")
#plt.plot(points_x, point_cos,"b")
plt.plot(points_x, point_ef,"g")
plt.plot(ix, iy, "b")
plt.show()
