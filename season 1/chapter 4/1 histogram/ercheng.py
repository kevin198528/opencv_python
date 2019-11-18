import numpy as np
import sklearn
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn import linear_model


def generate_data():
    np.random.seed(0)
    X, y = datasets.make_moons(200, noise=0.20)
    return X, y


def visualize(X, y, model):
    # plt.scatter(X[:, 0], X[:, 1], s=40, c=y, cmap=plt.cm.Spectral)
    # plt.show()
    plot_decision_boundary(lambda x:predict(model,x), X, y)
    plt.title("Logistic Regression")


def plot_decision_boundary(pred_func, X, y):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole gid
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Spectral)
    plt.show()



np.random.seed(0)

x, y = datasets.make_moons(200, noise=0.20)



z, b = np.histogram(y)

clf = linear_model.LogisticRegression(solver='lbfgs')
clf.fit(x, y)

plot_decision_boundary(lambda x : clf.predict(x), x, y)

# plt.scatter(x[:, 0], x[:, 1], s=30,  c=y)
# plt.show()

print(x.shape, y.shape)

# plt.scatter(x[])

# y = np.array([[1, 3, 5], [2, 6, 3]])

# x = np.array([[5, 1, 3], [7, 3, 2]])

# print(x)

# print(y)

