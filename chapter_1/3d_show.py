import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('renlian.jpg')

# 白平衡 色彩空间 冷色调 暖色调

# cv2.imwrite('test.jpg', img)

plt.imshow(img)
plt.show()
