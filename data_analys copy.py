import numpy as np
import json
import matplotlib.pyplot as plt
from csv import reader
from scipy.interpolate import make_interp_spline, BSpline

y = []
x = []
times = []

with open('data_analys_py/rawdata119870.csv', 'r') as csvfile:
    data = list(reader(csvfile))

for row in data:
    x.append(float(row[0]))
    y.append(float(row[1]))

for number in x:
    time += number
    times.append(time)

# SMOOTHING
xNew = np.linspace(min(x), max(x), 300) 

spl = make_interp_spline(x, y, k=1)  # type: BSpline
ySmooth = spl(xNew)

# MAX
ymax = 0
xmax = 0
index = 0

for number in y:
    if number > ymax:
        ymax = number
        print(x[index])
        print()
        # xmax = x[index]
    else:
        pass

    index += 1



plt.plot(x, y)
plt.plot(xNew, ySmooth)
plt.plot(105,ymax,'ro')
plt.title('graph')
plt.show()