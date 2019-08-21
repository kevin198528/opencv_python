import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def deep_show(img, c=0, s=100):
    d = len(img.shape)
    dst = cv2.resize(img, (s, s), interpolation=cv2.INTER_LINEAR)
    if d == 3:
        plt.imshow(dst[:, :, (2, 1, 0)])
    else:
        plt.imshow(dst, cmap='gray')

    mask = dst[:, :, 0] < 200

    dst[:, :, 0][mask] = 0


    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(0, s, 1)
    Y = np.arange(0, s, 1)
    X, Y = np.meshgrid(X, Y)

    if d == 3:
        # ax.plot_surface(Y, X, dst[:, :, c], rstride=1, cstride=1, cmap='jet')
        # ax.scatter3D(Y, X, dst[:, :, 0], c='b')
        ax.scatter3D(Y, X, dst[:, :, 1], c='g')
        # ax.scatter3D(Y, X, dst[:, :, 2], c='r')
    # else:
    #     # ax.plot_surface(Y, X, dst, rstride=1, cstride=1, cmap='jet')
    #     ax.scatter3D(Y, X, dst, cmap='Greens')
    #     ax.scatter3D(Y, X, dst[:, :, c], cmap='Greens')
