import numpy as np
from scipy.optimize import minimize

# 4组锚点坐标
# anchor = [[x0, y0, z0],
#           [x1, y1, z1],
#           [x2, y2, z2],
#           [x3, y3, z3]]

# 4个测试距离
# S=[s1, s2, s3, s4]

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

# 设置整个区域
def con():
    in_con = ({'type': 'ineq', 'fun':lambda loc: loc[0]},
              {'type': 'ineq', 'fun':lambda loc: 5000-loc[0]},
              {'type': 'ineq', 'fun':lambda loc: loc[1]},
               {'type': 'ineq', 'fun':lambda loc: 3000-loc[1]},
              {'type': 'ineq', 'fun': lambda loc: loc[2]},
              {'type': 'ineq', 'fun': lambda loc: 3000 - loc[2]},
              )
    return in_con


def optimize(anchor, distance, guess_v):
    con_in = con()
    # result = minimize(fun(anchor, distance), guess_v, method='COBYLA', constraints=con_in)
    result = minimize(fun(anchor, distance), guess_v, method='SLSQP', constraints=con_in)
    return result.success, result.x
