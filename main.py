import matplotlib.pyplot as plt
import numpy as np 

def f(x):
    e1 = np.exp(-x)
    return 1 / (1+e1)

t1 = np.arange(-10, 10, .5)

l = plt.plot(t1,f(t1),'r-')
#plt.setp(l, markersize=10)
#plt.setp(l, markerfacecolor='r')

plt.show()