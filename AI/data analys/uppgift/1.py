import numpy as np
import matplotlib.pyplot as plt
from csv import reader

values = []
max_values = []

# HÄMTA DATA
with open('rawdata119870.csv', 'r') as csvfile:
    data = list(reader(csvfile))

for row in data:
    values.append({'x': float(row[0]), 'y': float(row[2])})

# HÄMTAR MAXVÄRDE
length = len(values)

for n, item in enumerate(values):

    if n >= 2 or n < length-2:    
        if values[n]['y'] > values[n-1]['y'] and values[n-1]['y'] > values[n-2]['y'] and values[n]['y'] > values[n+1]['y'] and values[n+1]['y'] > values[n+2]['y']:
            max_values.append(item)


# HÄMTAR STARTTID, CYKEL LÄNGD, CYKEL INDEX OCH CYKEL TYP SAMT SKRIVER DE TILL FILEN
f = open('output1.txt', 'w')

currentCykelStart = 0
index = 0

for dic in max_values:
    cykelStart = dic['x']
    cykelTime = cykelStart - currentCykelStart
    currentCykelStart = cykelStart
    cykelIndex = index
    cykelType = 'runstride'
    index += 1
    f.write(str(cykelStart) + ', '+ str(cykelTime) + ', ' + str(cykelIndex) + ', ' + cykelType + '\n')

f.close()