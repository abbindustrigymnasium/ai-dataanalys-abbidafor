import numpy as np
import json
import matplotlib.pyplot as plt
from csv import reader
from scipy.interpolate import make_interp_spline, BSpline

y = []
x = []
times = []
time = 0

with open('data17-11.csv', 'r') as csvfile:
    data = list(reader(csvfile))


for row in data:

    # print(row)
    # str(row)
    row = json.dumps(row)
    

    # row.replace('\'', '')
    row = row.replace('[', '')
    row = row.replace(']', '')
    row = row.replace('"', '')
    # print(row)

    row = row.split(' ')

    x.append(row[2])
    y.append(row[1])
    time += (int(row[3]))
    times.append(time)
    
# print(x)
# print(y)
# print(times)

# xNew = np.linspace(min(x), max(x), 300) 

# spl = make_interp_spline(x, y, k=3)  # type: BSpline
# ySmooth = spl(xNew)

# xNew = np.linspace(min(times), max(times), 300) 

# spl = make_interp_spline(times, x, k=3)  # type: BSpline
# ySmooth = spl(xNew)

plt.plot(times, x)
# plt.plot(xNew, ySmooth)
plt.title('project_T')
plt.show()