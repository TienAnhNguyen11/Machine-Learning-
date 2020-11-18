import numpy as np
import matplotlib.pyplot as plt
import cv2

trainningData = np.random.randint(0, 100, [25, 2]).astype(np.float32)
labels = np.random.randint(0, 2, [25, 1]).astype(np.float32)
newMember = np.random.randint(0, 100, [1, 2]).astype(np.float32)

red = trainningData[labels.ravel() == 1]
blue = trainningData[labels.ravel() == 0]

plt.scatter(red[:, 1], red[:, 0], 100, 'r', 'o')
plt.scatter(blue[:, 1], blue[:, 0], 100, 'b', 'o')
plt.scatter(newMember[:, 1], newMember[:, 0], 100, 'g', '^')

knn = cv2.ml.KNearest_create()
knn.train(trainningData, 0, labels)
temp, goal, neighbors, distance = knn.findNearest(newMember, 3)

print("goal: ", goal)
print("neighbors: ", neighbors)
print("distance: ", distance)

plt.show()