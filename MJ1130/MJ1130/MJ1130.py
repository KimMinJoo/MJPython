﻿import numpy as np
from matplotlib import pyplot as plt

data = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(data+2)
print(data-2)
print(data*data)
print(data/3)
print(data**2)
print(data**0.5)
print(data.dot(data))
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])
print(a==b)
print(a>b)
print(np.array_equal(a, b))
print(np.array_equal(a, c))
a=np.array([1,1,0,0],dtype=bool)
a=np.array([1,0,1,0],dtype=bool)
print(np.logical_or(a,b))
print(np.logical_and(a,b))
print(np.all([True,True,False]))
print(np.any([True,True,False]))
a = np.arange(5)
print(np.sin(a))
print(np.log(a))
print(np.exp(a))
a=np.triu(np.ones((3, 3)), 1)
print(a)
print(a.T)
x = np.array([1, 2, 3, 4])
print(np.sum(x))
print(x.sum())
x = np.array([[1, 1],[ 2, 2]])
print(x.sum())
print(x.sum(axis=0)) #columns (first dimension)
print(x.sum(axis=1)) #rows (second dimension)
print((x[0, :].sum(), x[1, :].sum()))
x = np.array([1, 3, 2])
print(x.min())
print(x.max())
print(x.argmin()) # index of minimum
print(x.argmax()) # index of maximum
np.all([True, True, False])
np.any([True, True, False])
# 배열비교할때주로사용
a = np.zeros((100,100))
print(np.any(a!=0))
print(np.all(a==a))
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
print(x.mean())
print(np.median(x))
print(np.median(y, axis=-1)) # last axis
print(x.std()) # full population standard dev.
data = np.loadtxt('data.txt')
year, hares, lynxes, carrots = data.T
#plt.plot(year, hares, year, lynxes, year, carrots)
#plt.show()
print(data)
print(data.mean(axis=0))
print(data.std(axis=0))
for item in data.argmax(axis=0):
    print(year[item])
    
data = np.array([i*10 for i in range(6)])
print(data.shape)
data = np.array([[i*10 for i in range(6)]]).T
print(data.shape)
data2 = np.array([i for i in range(6)])
print(data+data2)

