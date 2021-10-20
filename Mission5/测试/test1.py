import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

'''
散点图连成线
'''

# 两个是配置代码，第一行表示，允许使用中文，第二个表示允许使用负数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 这三个表示就跟名字一样，标识作用
plt.title("Four Nodes State")
plt.xlabel("Time(sec)")
plt.ylabel("State xi i=0,1,...4")

# 这个前两参数表示横坐标的开始和结尾，第三个参数表示你要分成多少份
x = np.linspace(0, 10, 1000)

# 下面是节点个状态信息，一定要使用numpy自带的array，不然会出错
node1State = np.array([-4, -3, -2, -1, 0, 1, 2, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0, -1, 0, 1, 0])
times = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10])

# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model0 = make_interp_spline(times, node1State)
ys0 = model0(x)

# 给每条线设定颜色，和添加label，linestyle表示你要使用曲线的样式，有多少种网上有
plt.plot(x, ys0, color='red', label='Node 0', linestyle='-.')

# legend() 函数只有在你需要使用laber 这个参数的时候才会用到
plt.legend()
plt.show()
