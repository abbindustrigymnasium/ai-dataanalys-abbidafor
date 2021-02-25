import numpy as np
import json
import matplotlib.pyplot as plt
from csv import reader
from scipy.interpolate import make_interp_spline, BSpline, splrep

first = []
second = []
times = []
#6300 time
# HÄMTA DATA
with open('rawdata119870.csv', 'r') as csvfile:
    data = list(reader(csvfile))

for row in data:
    first.append(float(row[0]))
    second.append(float(row[1]))

x = np.array(first)
y = np.array(second)

# FILTRERING
# for item in range(6400):

# SMOOTHING
#xNew = np.linspace(min(x), max(x), 200) 

#spl = make_interp_spline(x, y, k=1)  # type: BSpline
#ySmooth = spl(xNew)

t, c, k = splrep(x, y, s=0, k=4)
print('''\
t: {}
c: {}
k: {}
'''.format(t, c, k))
N = 100
xmin, xmax = x.min(), x.max()
xNew = np.linspace(xmin, xmax, N)
spline = BSpline(t, c, k, extrapolate=False)



plt.plot(x, y)
plt.plot(xNew, spline(xNew), 'r', label='BSpline')
# plt.plot(x, y)
# plt.plot(xNew, spline(xNew))
plt.title('graph')
plt.show()