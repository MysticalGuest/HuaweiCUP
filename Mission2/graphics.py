import matplotlib.pyplot as plt
import openpyxl


class MyReadExcel(object):

    def __init__(self, file_name, sheet_name):
        self.wb = openpyxl.load_workbook(file_name, data_only=True)
        self.sh = self.wb[sheet_name]

    def read_data(self):
        row_data = list(self.sh.rows)[1:]
        one_data = []
        all_data = []
        # symbol = 0
        for data in row_data:
            # 数据处理
            for elem in data:
                one_data.append(elem.value)
                # symbol += 1
            all_data.append(one_data)
            one_data = []
            # print(data.value, end=",")
            self.wb.close()
        return all_data


# 散点绘制（Scatter plots）
def drawMyGraph(all_data):
    fig = plt.figure()
    # 111，指的就是将这块画布分为1×1，然后1对应的就是1号区
    ax = fig.add_subplot(111, projection='3d')
    for data in all_data:
        ax.scatter(data[5], data[6], data[7], c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


if __name__ == '__main__':
    r = MyReadExcel('全部324条正常数据平均值(带坐标).xlsx', 'Sheet')
    data1 = r.read_data()
    drawMyGraph(data1)