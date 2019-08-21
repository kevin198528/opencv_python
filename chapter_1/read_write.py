import cv2
import matplotlib.pyplot as plt

gd_img = cv2.imread('../img_src/gaoda.jpg')

cv2.imwrite('../img_src/gaoda_copy.jpg', gd_img)

plt.imshow(gd_img[:, :, (2, 1, 0)])

plt.show()
