from ex import *


import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 这三个表示就跟名字一样，标识作用
# plt.title("任务5：运动轨迹")
# plt.xlabel("Time(sec)")
# plt.ylabel("State xi i=0,1,...4")

# 设置图例字号
mpl.rcParams['legend.fontsize'] = 10

# 方式2：设置三维图形模式
fig = plt.figure("任务5：运动轨迹")
ax = fig.gca(projection='3d')

# 测试数据
# np.linspace用来创建等差数列
# x = np.linspace(-4 * np.pi, 4 * np.pi, 30)
# print(x)
# y = x + np.random.randn(x.shape[-1]) * 0.7
# z = x * x
x = extract_locationX()
x1 = x[:513]
# print(x)
y = extract_locationY()
y1 = y[:513]
z = extract_locationZ()
z1 = z[:513]
# for i in range(513):
#     print(x1[i], y1[i], z1[i])

# 绘制图形
# ax.plot(x, y, z, label='运动轨迹')
ax.plot(x1, y1, z1, label='运动轨迹')

ax.set_xlabel('X轴')
plt.xlim(0, 5000)
ax.set_ylabel('Y轴')
plt.ylim(0, 5000)
ax.set_zlabel('Z轴')
# plt.clim()
# # 数据拟合
# p_yx = np.polyfit(y, x, 5)
# x_out = np.polyval(p_yx, y)
# p_yz = np.polyfit(y, z, 5)
#
# z_out = np.polyval(p_yz, y)
# ax.plot(x_out, y, z_out, label='parametric2 curve')

# 显示图例
ax.legend()

# 显示图形
plt.show()

