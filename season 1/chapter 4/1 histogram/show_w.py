import numpy as np
import matplotlib.pyplot as plt

w1 = np.load('w1.npy')
w2 = np.load('w2.npy')
w3 = np.load('w3.npy')

print(w1.shape, w2.shape, w3.shape)

w1 = np.reshape(w1, 300)
w2 = np.reshape(w2, 100*100)
w3 = np.reshape(w3, 100)

plt.scatter(np.arange(300), w1)
plt.figure()
plt.scatter(np.arange(100*100), w2)
plt.figure()
plt.scatter(np.arange(100), w3)
plt.show()

plt.scatter()
