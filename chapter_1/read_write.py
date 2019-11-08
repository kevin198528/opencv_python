import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./yiquan.jpg')

img = img[:, :, [2, 1, 0]]

img[:, :, [0, 1]] = 0

plt.imshow(img)
plt.show()
