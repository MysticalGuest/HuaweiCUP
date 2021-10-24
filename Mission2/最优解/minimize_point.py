import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# 4组锚点坐标
# anchor = [[x0, y0, z0],
#           [x1, y1, z1],
#           [x2, y2, z2],
#           [x3, y3, z3]]

# 4个测试距离
# S=[s1, s2, s3, s4]


# def f(x_pa, y_pa, z_pa, anc, s):
#     # 默认为对输入参数中的所有元素进行求和
#     r = []
#     for i in range(4):
#         sum = np.sum((x_pa-anc[i][0])**2 + (y_pa-anc[i][1])**2 + (z_pa-anc[i][2])**2)
#         r[i] = s[i]-np.sqrt(sum)
#     return np.sum(r[0]+r[1]+r[2]+r[3])
def fun(anc, s):
    # 默认为对输入参数中的所有元素进行求和
    r = []
    for i in range(4):
        v = lambda loc: np.sum(
            abs(s[0] - np.sqrt(np.sum((loc[0] - anc[0][0]) ** 2 + (loc[1] - anc[0][1]) ** 2 + (loc[2] - anc[0][2]) ** 2))) +
            abs(s[1] - np.sqrt(np.sum((loc[0] - anc[1][0]) ** 2 + (loc[1] - anc[1][1]) ** 2 + (loc[2] - anc[1][2]) ** 2))) +
            abs(s[2] - np.sqrt(np.sum((loc[0] - anc[2][0]) ** 2 + (loc[1] - anc[2][1]) ** 2 + (loc[2] - anc[2][2]) ** 2))) +
            abs(s[3] - np.sqrt(np.sum((loc[0] - anc[3][0]) ** 2 + (loc[1] - anc[3][1]) ** 2 + (loc[2] - anc[3][2]) ** 2)))
        )/4
    return v

# def fun():
#     # 默认为对输入参数中的所有元素进行求和
#     # r = []
#     for i in range(4):
#         # np.abs()
#         v = lambda loc: np.sum(
#             abs(6150.86719540553 - np.sqrt(np.sum((loc[0] - 0) ** 2 + (loc[1] - 0) ** 2 + (loc[2] - 1300) ** 2)))+
#             abs(4675.71438789596 - np.sqrt(np.sum((loc[0] - 5000) ** 2 + (loc[1] - 0) ** 2 + (loc[2] - 1700) ** 2))) +
#             abs(4124.17304883773 - np.sqrt(np.sum((loc[0] - 0) ** 2 + (loc[1] - 5000) ** 2 + (loc[2] - 1700) ** 2))) +
#             abs(1104.20385896011 - np.sqrt(np.sum((loc[0] - 5000) ** 2 + (loc[1] - 5000) ** 2 + (loc[2] - 1300) ** 2)))
#         )/4
#     return v

# def fun(anc, s):
#     # 默认为对输入参数中的所有元素进行求和
#     r = []
#     for i in range(4):
#         v1, v2, v3 = lambda x, y, z: np.sum(
#             s[0] - np.sqrt(np.sum((x-anc[0][0])**2 + (y-anc[0][1])**2 + (z-anc[0][2])**2)) +
#             s[1] - np.sqrt(np.sum((x - anc[1][0]) ** 2 + (y - anc[1][1]) ** 2 + (z - anc[1][2]) ** 2)) +
#             s[2] - np.sqrt(np.sum((x - anc[2][0]) ** 2 + (y - anc[2][1]) ** 2 + (z - anc[2][2]) ** 2)) +
#             s[3] - np.sqrt(np.sum((x - anc[3][0]) ** 2 + (y - anc[3][1]) ** 2 + (z - anc[3][2]) ** 2))
#         )
#     return v1, v2, v3


# def con(anc, s):
#     in_con = ({'type': 'ineq', 'fun':
#                 lambda x, y, z:s[0]-np.sqrt(np.sum(
#                     (x - anc[0][0]) ** 2 +
#                     (y - anc[0][1]) ** 2 +
#                     (z - anc[0][2]) ** 2))
#                },
#               {'type': 'ineq', 'fun':
#                   lambda x, y, z: s[1] - np.sqrt(np.sum(
#                       (x - anc[1][0]) ** 2 +
#                       (y - anc[1][1]) ** 2 +
#                       (z - anc[1][2]) ** 2))
#                },
#               {'type': 'ineq', 'fun':
#                   lambda x, y, z: s[2] - np.sqrt(np.sum(
#                       (x - anc[2][0]) ** 2 +
#                       (y - anc[2][1]) ** 2 +
#                       (z - anc[2][2]) ** 2))
#                },
#                {'type': 'ineq', 'fun':
#                    lambda x, y, z: s[3] - np.sqrt(np.sum(
#                        (x - anc[3][0]) ** 2 +
#                        (y - anc[3][1]) ** 2 +
#                        (z - anc[3][2]) ** 2))
#                 }
#               )
#     return in_con


# def con(anc, s):
#     in_con = ({'type': 'ineq', 'fun':
#                 lambda loc: s[0]-np.sqrt(np.sum(
#                     (loc[0] - anc[0][0]) ** 2 +
#                     (loc[1] - anc[0][1]) ** 2 +
#                     (loc[2] - anc[0][2]) ** 2))
#                },
#               {'type': 'ineq', 'fun':
#                   lambda loc: s[1] - np.sqrt(np.sum(
#                       (loc[0] - anc[1][0]) ** 2 +
#                       (loc[1] - anc[1][1]) ** 2 +
#                       (loc[2] - anc[1][2]) ** 2))
#                },
#               {'type': 'ineq', 'fun':
#                   lambda loc: s[2] - np.sqrt(np.sum(
#                       (loc[0] - anc[2][0]) ** 2 +
#                       (loc[1] - anc[2][1]) ** 2 +
#                       (loc[2] - anc[2][2]) ** 2))
#                },
#                {'type': 'ineq', 'fun':
#                    lambda loc: s[3] - np.sqrt(np.sum(
#                        (loc[0] - anc[3][0]) ** 2 +
#                        (loc[1] - anc[3][1]) ** 2 +
#                        (loc[2] - anc[3][2]) ** 2))
#                 }
#               )
#     return in_con

# 设置整个区域
def con():
    in_con = ({'type': 'ineq', 'fun':lambda loc: loc[0]},
              {'type': 'ineq', 'fun':lambda loc: 5000-loc[0]},
              {'type': 'ineq', 'fun':lambda loc: loc[1]},
               {'type': 'ineq', 'fun':lambda loc: 5000-loc[1]},
              {'type': 'ineq', 'fun': lambda loc: loc[2]},
              {'type': 'ineq', 'fun': lambda loc: 3000 - loc[2]},
              )
    return in_con


def optimize(anchor, distance, guess_v):
    con_in = con()
    # result = minimize(fun(anchor, distance), guess_v, method='COBYLA', constraints=con_in)
    result = minimize(fun(anchor, distance), guess_v, method='SLSQP', constraints=con_in)
    # print(res.fun)
    # result = minimize(fun(anchor, distance), guess_v, method='TNC', constraints=con_in)
    # result = minimize(fun(anchor, distance), guess_v, method='trust-krylov', constraints=con_in)
    # print(res.success)
    # print(res.x)
    return result.success, result.x

if __name__ == "__main__":
    # 4组锚点
    ancs = [[0, 0, 1300],
            [5000,0, 1700],
            [0, 5000, 1700],
            [5000, 5000, 1300]]

    # 4个测量距离值
    # ce_s = [844, 4552, 4567, 6419]

    # cons = con(ancs, ce_s)
    cons = con()
    # 设置初始预测值
    # init_value = np.asarray([4000, 4500, 880])
    # 第18个点
    ce_s = [1164.11285653602, 4077.63829079632, 4650.05459344922, 6084.20606170416]
    init_value = np.asarray([2200, 500, 880]) # 初始猜测值
    # [1000, 500, 880]

    # res = minimize(fun(), init_value, method='SLSQP', constraints=cons)
    # res = minimize(fun(ancs, ce_s), init_value, method='SLSQP', constraints=cons)
    res = minimize(fun(ancs, ce_s), init_value, method='COBYLA', constraints=cons)
    # res = minimize(fun(), init_value, method='SLSQP', constraints=cons)

    print(res.fun)
    print(res.success)
    print(res.x)