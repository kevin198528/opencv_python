import cv2
import numpy as np
import matplotlib.pyplot as plt

img_rgb = cv2.imread('matlab_log.png')

img_rgb = img_rgb[:, :, ::-1]

img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)

img_hsv[:, :, 0] = img_hsv[:, :, 0]*(255/180)

green_maskA = img_hsv[:, :, 0] == 85
green_maskB = img_hsv[:, :, 1] > 1

green_mask = green_maskA & green_maskB

# c, v = np.histogram(img_hsv[:, :, 1])
for i in range(3):
    img_rgb[:, :, i][green_mask == False] = 255

plt.imshow(img_rgb)
plt.show()
