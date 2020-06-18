import cv2
import numpy as np
import matplotlib.pyplot as plt

trainingData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
label = np.random.randint(0, 2, (25, 1)).astype(np.float32)
red = trainingData[label.ravel()==1]
blue = trainingData[label.ravel()==0]
newMember = np.random.randint(0, 100, (1, 2)).astype(np.float32)

plt.scatter(red[:, 0], red[:, 1], 100, 'r', 's')
plt.scatter(blue[:, 0], blue[:, 1], 100, 'b', 's')
plt.scatter(newMember[:, 0], newMember[:, 1], 100, 'g', 's')
knn = cv2.ml.KNearest_create()
knn.train(trainingData, 0, label)
temp ,goals, neighbor, distance = knn.findNearest(newMember, 3)

print('goal: {}\n'.format(goals))
print('neighbor: {}\n'.format(neighbor))
print('distance: {}\n'.format(distance))

plt.show()