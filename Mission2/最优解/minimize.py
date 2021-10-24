import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
labels = ['company', 'school', 'girl']


def f(coord, x, y):
    # 默认为对输入参数中的所有元素进行求和
    return np.sum((coord[0]-x)**2+(coord[1]-y)**2)


x = np.array([1, 4, 9])

y = np.array([1, 6, 2])

initial = np.array([50,2])

print(f(initial, x, y))

res = minimize(f, initial, args=(x,y))

print(res.x)

print(f(res.x, x, y))

plt.scatter(x,y)

for i in range(3):
    plt.arrow(res.x[0], res.x[1], -res.x[0]+x[i], -res.x[1]+y[i],
              head_length=-0.1, head_width=0.1, fc='k')
    plt.text(x[i], y[i], labels[i])
plt.text(res.x[0], res.x[1], 'house')

plt.show()

# 限制房子在五环边上
cons = {'type':'eq', 'fun':lambda coord:coord[0]**2+coord[1]**2-100}
res=minimize(f, initial, args=(x,y), constraints=cons)
for i in range(3):
    plt.arrow(res.x[0], res.x[1], -res.x[0]+x[i], -res.x[1]+y[i],
              head_length=-0.1, head_width=0.1, fc='k')
    plt.text(x[i], y[i], labels[i])
plt.text(res.x[0], res.x[1], 'house')
x=np.linspace(0.0, 10.0, 100)
y=(100-x**2)**0.5
plt.plot(x,y)

plt.show()