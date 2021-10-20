import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# 设置图例字号
mpl.rcParams['legend.fontsize'] = 10

# 方式2：设置三维图形模式
fig = plt.figure()
ax = fig.gca(projection='3d')

# 测试数据
# np.linspace用来创建等差数列
x = np.linspace(-4 * np.pi, 4 * np.pi, 30)
print(x)
y = x + np.random.randn(x.shape[-1]) * 0.7
z = x * x

# 绘制图形
ax.plot(x, y, z, label='parametric1 curve')
# 数据拟合
p_yx = np.polyfit(y, x, 5)
x_out = np.polyval(p_yx, y)
p_yz = np.polyfit(y, z, 5)

z_out = np.polyval(p_yz, y)
ax.plot(x_out, y, z_out, label='parametric2 curve')

# 显示图例
ax.legend()

# 显示图形
plt.show()