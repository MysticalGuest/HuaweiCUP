# 约定俗成的写法plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
# 首先定义两个函数（正弦&余弦）
import numpy as np

'''
利用matplotlib库画3位坐标图
'''

# X = np.linspace(-np.pi, np.pi, 256, endpoint=True) #-π to+π的256个值
# C, S = np.cos(X), np.sin(X)
# plt.plot(X, C)
# plt.plot(X, S)
# # 在ipython的交互环境中需要这句话才能显示出来
# plt.show()


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# 直线绘制（Line plots）
# mpl.rcParams['legend.fontsize'] = 10
#
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# z = np.linspace(-2, 2, 100)
# r = z ** 2 + 1
# x = r * np.sin(theta)
# y = r * np.cos(theta)
# ax.plot(x, y, z, label='parametric curve')
#
#
# ax.legend()

# 散点绘制（Scatter plots）
def randrange(n, vmin, vmax):
    '''
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    '''
    return (vmax - vmin) * np.random.rand(n) + vmin


fig = plt.figure()
# 111，指的就是将这块画布分为1×1，然后1对应的就是1号区
ax = fig.add_subplot(111, projection='3d')
n = 100
# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
# 对于每组样式和范围设置，在[23,32]中的x、[0,100]中的y、[zlow，zhigh]中的z定义的框中绘制n个随机点。
for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
    # [('r', 'o', -50, -25), ('b', '^', -30, -5)]是个列表，c, m, zlow, zhigh分别取其中的值
    print(zlow, zhigh)
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
    # c, marker控制点的颜色，形状
    # 画散点图
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 线框图（Wireframe plots）
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Grab some test data.
# X, Y, Z = axes3d.get_test_data(0.05)
#
# # Plot a basic wireframe.
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# 表面图（Surface plots）
# fig = plt.figure()
# ax = fig.gca(projection='3d')
#
# # Make data.
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X ** 2 + Y ** 2)
# Z = np.sin(R)
#
# # Plot the surface.
# surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)
#
# # Customize the z axis.
# ax.set_zlim(-1.01, 1.01)
# ax.zaxis.set_major_locator(LinearLocator(10))
# ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
#
# # Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
# cset = ax.contour(X, Y, Z, cmap=cm.coolwarm)
# ax.clabel(cset, fontsize=9, inline=1)

# 二维的等高线，同样可以配合三维表面图一起绘制：
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
# ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
# cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
#
# ax.set_xlabel('X')
# ax.set_xlim(-40, 40)
# ax.set_ylabel('Y')
# ax.set_ylim(-40, 40)
# ax.set_zlabel('Z')
# ax.set_zlim(-100, 100)

# 也可以是三维等高线在二维平面的投影：
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
# ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
# cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
# cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
# cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
#
# ax.set_xlabel('X')
# ax.set_xlim(-40, 40)
# ax.set_ylabel('Y')
# ax.set_ylim(-40, 40)
# ax.set_zlabel('Z')
# ax.set_zlim(-100, 100)

plt.show()