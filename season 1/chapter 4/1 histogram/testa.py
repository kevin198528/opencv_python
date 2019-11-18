import numpy as np
import matplotlib.pyplot as plt

a = np.load('pre_layer1.npy')
b = np.load('pre_layer2.npy')
c = np.load('pre_layer3.npy')

print(a.shape, b.shape, c.shape)

a = np.reshape(a, 400)
b = np.reshape(b, 400)
c = np.reshape(c, 4)

x = np.linspace(1, 400, 400)

plt.scatter(x, a)
plt.figure()
plt.scatter(x, b)
plt.figure()
plt.scatter([1, 2, 3, 4], c)
plt.show()

# plt.scatter()
