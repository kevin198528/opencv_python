from matplotlib import pyplot as plt
import cv2
import numpy as np

def zimshow(img, name='window_name'):
    plt.figure(name)
    plt.imshow(img)

def zplot(data, name='window_name'):
    plt.figure(name)
    plt.plot(data)

img = cv2.imread('../img_src/yiquan-01.jpg')

print(type(img))
print(img.data)

exit()

zimshow(img[:, :, [2, 1, 0]], 'before')

hr = cv2.calcHist([img], [0], None, [256], [0, 256])

zplot(hr)

r = img[:, :, 2]
g = img[:, :, 1]
b = img[:, :, 0]

br = cv2.equalizeHist(r)
bg = cv2.equalizeHist(g)
bb = cv2.equalizeHist(b)

bimg = np.stack((br, bg, bb), axis=2)

bhr = cv2.calcHist([bimg], [0], None, [256], [0, 256])

zplot(bhr, 'bhr')

zimshow(bimg, 'after')

plt.show()
