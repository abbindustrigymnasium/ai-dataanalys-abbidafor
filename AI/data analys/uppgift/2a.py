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


index = 0
y1 = 0
y2 = 0
y3 = 0
x1 = 0
x2 = 0
x3 = 0

while index < len(values):
    try:
        y1 = values[index]['y']
        y2 = values[index + 1]['y']
        y3 = values[index + 2]['y']

        x1 = values[index]['x']
        x2 = values[index + 1]['x']
        x3 = values[index + 2]['x']

        yv = (y1 + y2 + y3)/3
        xv = (x1 + x2 + x3)/3

        x.append(xv)
        y.append(yv)

    except IndexError:
        pass

    index += 3


plt.plot(x, y)
plt.title('graph')
plt.show()