import numpy as np
def sigmoid(x,deriv=False):
    if deriv == True:
        return x*(1-x)
    return 1/(1+np.exp(-x))

x = np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y = np.array([[0,0,1,1]]).T

np.random(1)

syn0 =2*np.random((3,1)) - 1

for i in range(10000):
    l0 = x
    l1 = sigmoid(np.dot(l0,syn0))

l1_error = y - l1
l1_delta = l1_error * sigmoid(l1,True)

syn0 += np.dot(l0,syn0)

li_error = y - l1