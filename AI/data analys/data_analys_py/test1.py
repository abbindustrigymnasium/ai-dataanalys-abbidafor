import numpy as np
import json
import matplotlib.pyplot as plt
from csv import reader
from scipy.interpolate import make_interp_spline, BSpline

y = []
x = []
times = []
T = np.array([6, 7, 8, 9, 10, 11, 12, 15, 20])
power = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00, 8.30E+00, 15.60E+00])

# SMOOTHING
# 300 represents number of points to make between min(x) and max(x)


xNew = np.linspace(min(T), max(T), 300) 

spl = make_interp_spline(T, power, k=3)  # type: BSpline
ySmooth = spl(xNew)


plt.plot(T, power)
plt.plot(xNew, ySmooth)
plt.title('graph')
plt.show()