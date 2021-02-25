from csv import reader
import matplotlib.pyplot as plt

y = []
x = []

with open('rawdata119870.csv', 'r') as csvfile:
    data = list(reader(csvfile))


for row in data:
    x.append(float(row[0]))
    y.append(float(row[1]))


plt.plot(x, y)
plt.title('graph')
plt.ylabel('y')
plt.xlabel('x') 
plt.show()
