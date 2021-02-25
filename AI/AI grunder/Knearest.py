import numpy as np
from math import sqrt
import matplotlib.pyplot as plt 
from matplotlib import style
import warnings
from collections import Counter
style.use("fivethirtyeight")

# def eucdist(goalplot, plot):
#     euc = sqrt((plot[0]-goalplot[0])**2 + ((plot[1]-goalplot[1])**2))
#     print(euc)
#     plt.scatter(plot[0], plot[1], s=100)

# plot = [1,3]
# goalplot = [2,5]
# plt.scatter(goalplot[0], goalplot[1], s=150)
# eucdist(goalplot, plot)
# plot2=[4,7]
# eucdist(goalplot, plot2)

# eucdist(goalplot, goalplot)
# plt.show()
dataset = {
    "k": [[2, 5], [4, 1], [6, 5]], 
    "g": [[3, 2], [6, 3], [4, 5]], 
    "r": [[5, 5], [7, 7], [8, 6]]
    }

dataset = {
    "Hus": [[35,35],[37,37],[42,32],[60,34],[63,36],[61,35],[65,22],[76,16]],
    "Hyresrätt": [[23,12], [26,33], [28,20], [19,6], [23,9]],
    "Bostadsrätt": [[57,45],[24,28],[26,30]],
    "Radhus": [[37,21],[45,47],[32,42],[55,24],[61,25]]
}

newFeature = [33, 23]

def K_nearest(data, predict, k=3):
    if len(data) >= k:
        warnings.warn("K is set to a value less then total valid groups")
    distance = []

    for group in data:
        for feature in data[group]:
            euclidanDistance = np.linalg.norm(
                np.array(feature) - np.array(predict))
            distance.append([euclidanDistance, group])

    votes = [i[1] for i in sorted(distance)[:k]]
    print(Counter(votes).most_common(1))
    votesResult = Counter(votes).most_common(1)[0][0]

    return votesResult

result = K_nearest(dataset, newFeature, k=6)

print('Du bor i', result)
colors={'Hus': 'r', 'Hyresrätt': 'b', 'Bostadsrätt': 'g', 'Radhus': 'k'}
[[plt.scatter(ii[0], ii[1], color = colors[i]) for ii in dataset[i]] for i in dataset]
plt.scatter(newFeature[0], newFeature[1], s=100)
plt.ylabel("Inkomst")
plt.xlabel("Ålder")
plt.show()