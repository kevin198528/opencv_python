import numpy as np

X = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0], [1], [1], [0]])

lr = 1
h1_dim = 100
h2_dim = 100
h3_dim = 1

w1 = np.random.randn(3, h1_dim)
w2 = np.random.randn(h1_dim, h2_dim)
w3 = np.random.randn(h2_dim, h3_dim)

print('w1: mean:{}, std:{} var:{}'.format(np.mean(w1), np.std(w1), np.var(w1)))
print('w2: mean:{}, std:{} var:{}'.format(np.mean(w2), np.std(w2), np.var(w2)))
print('w3: mean:{}, std:{} var:{}'.format(np.mean(w3), np.std(w3), np.var(w3)))

w1 = np.random.randn(3, h1_dim)
w2 = np.random.randn(h1_dim, h2_dim) * 0.1
w3 = np.random.randn(h2_dim, h3_dim) * 0.1

def sigmod(x):
    s = 1/(1 + np.exp(-x))
    return s

def dsigmod(y):
    return y*(1 - y)

def drelu(x):
    s = x
    s[x > 0] = 1
    s[x <= 0] = 0
    return s

def relu(x):
    s = x
    s[x <= 0] = 0
    return s

def L2_loss(y, h_y):
    return np.sum(np.square(np.abs(np.ravel(y) - np.ravel(h_y))))

for j in range(1000):
    pre_layer1 = np.dot(X, w1)
    layer1 = sigmod(pre_layer1)

    pre_layer2 = np.dot(layer1, w2)
    layer2 = sigmod(pre_layer2)

    pre_layer3 = np.dot(layer2, w3)
    layer3 = sigmod(pre_layer3)
    print('===========================')
    print(L2_loss(layer3, y))

    layer3_delta = (layer3 - y) * dsigmod(layer3)
    layer2_delta = layer3_delta.dot(w3.T) * dsigmod(layer2)
    layer1_delta = layer2_delta.dot(w2.T) * (dsigmod(layer1))

    w3 -= lr * layer2.T.dot(layer3_delta)
    w2 -= lr * layer1.T.dot(layer2_delta)
    w1 -= lr * X.T.dot(layer1_delta)

    print('w1 - mean:{:.3f}  std:{:.3f}  var:{:.3f}'.format(np.mean(w1), np.std(w1), np.var(w1)))
    print('w2 - mean:{:.3f}  std:{:.3f}  var:{:.3f}'.format(np.mean(w2), np.std(w2), np.var(w2)))
    print('w3 - mean:{:.3f}  std:{:.3f}  var:{:.3f}'.format(np.mean(w3), np.std(w3), np.var(w3)))
    print('---------------------------')
    print('X          - mean:{:6.3f}  std:{:6.3f}  var:{:6.3f}'.format(np.mean(X), np.std(X), np.var(X)))
    print('pre_layer1 - mean:{:6.3f}  std:{:6.3f}  var:{:6.3f}'.format(np.mean(pre_layer1), np.std(pre_layer1), np.var(pre_layer1)))
    print('layer1     - mean:{:6.3f}  std:{:6.3f}  var:{:6.3f}'.format(np.mean(layer1), np.std(layer1), np.var(pre_layer1)))
    print('pre_layer2 - mean:{:6.3f}  std:{:6.3f}  var:{:6.3f}'.format(np.mean(pre_layer2), np.std(pre_layer2), np.var(pre_layer2)))
    print('layer2     - mean:{:6.3f}  std:{:6.3f}  var:{:6.3f}'.format(np.mean(layer2), np.std(layer2), np.var(layer2)))
    print('pre_layer3 - mean:{:6.3f}  std:{:6.3f}  var:{:6.3f}'.format(np.mean(pre_layer3), np.std(pre_layer3), np.var(pre_layer3)))
    print('layer3     - mean:{:6.3f}  std:{:6.3f}  var:{:6.3f}'.format(np.mean(layer3), np.std(layer3), np.var(layer3)))
    print(layer3)

# X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
# y = np.array([[0,1,1,0]]).T
# syn0 = 2*np.random.random((3,4)) - 1       #随机初始化权重
# syn1 = 2*np.random.random((4,1)) - 1       #随机初始化权重
# for j in xrange(60000):                    #迭代次数
#     l1 = 1/(1+np.exp(-(np.dot(X,syn0))))    #正向传播
#     l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))   #正向传播
#     l2_delta = (y - l2)*(l2*(1-l2))         #反向传播
#     l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))   #反向传播
#     syn1 += l1.T.dot(l2_delta)              #更新权重
#     syn0 += X.T.dot(l1_delta)               #更新权重

np.save('pre_layer1', pre_layer1)
np.save('pre_layer2', pre_layer2)
np.save('pre_layer3', pre_layer3)

np.save('w1', w1)
np.save('w2', w2)
np.save('w3', w3)
