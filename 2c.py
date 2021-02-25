import numpy as np
import matplotlib.pyplot as plt
from csv import reader

x = []
y = []
values = []
max_values = []

# HÄMTA DATA
with open('rawdata119870.csv', 'r') as csvfile:
    data = list(reader(csvfile))

for row in data:
    values.append({'x': float(row[0]), 'y': float(row[2])})

# RÄKNA UT MEDLET
index = 0
lenSample = 27

while index < len(values):
    n = 0
    xv = 0 
    yv = 0
    try:
        while n < lenSample:
            yv += values[index]['y']
            xv += values[index]['x']
            n += 1
            index += 1

        x.append(xv/lenSample)
        y.append(yv/lenSample)
    except IndexError:
        pass

plt.plot(x, y)
plt.title('graph')
plt.show()