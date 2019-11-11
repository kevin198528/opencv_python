import cv2
import numpy as np
import matplotlib.pyplot as plt

bayer = np.zeros((256, 256, 3), np.uint8)

# R, G, G, B

bayer[0:128, 0:128, 0] = 255

bayer[0:128:, 128:256, 1] = 255
bayer[128:256, 0:128, 1] = 255

bayer[128:256, 128:256, 2] = 255

# cv2.imwrite('bayer.jpg', bayer)

plt.imshow(bayer)
plt.show()
