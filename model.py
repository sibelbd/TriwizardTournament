import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier

print("i'm here")

data = np.loadtxt('data.txt')
print(data.shape)
label = np.loadtxt('labels.txt')
print(label.shape)

model = KNeighborsClassifier(n_neighbors=1)


model = model.fit(data,label)
temp = np.loadtxt('test.txt')
np.transpose(temp)

print(temp.shape)

print(model.predict([temp]))






