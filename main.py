# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Mission1.task1_data_preprocess import data_preprocess
from Mission2.merge_all_error_data import merge
from Mission2.subtract_500_from_error import subtract
from Mission2.average_after_subtract_500 import average_after_subtract


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    '''
    任务1：数据预处理（清洗）
    @:param1:第1个参数是数据路径（附件1：UWB数据集//正常数据//，附件1：UWB数据集//异常数据//）
    @:param2:第2个参数是数据类型（正常，异常）
    @:param3:第3个参数是处理后数据的存储路径（Mission1//正常数据//，"Mission1//异常数据//"）
    注：存储路径文件必须存在，重点列出4个文件：1.异常.xlsx，24.正常.xlsx，100.异常.xlsx，109.正常.xlsx
    '''
    # 所有正常数据处理
    data_preprocess("附件1：UWB数据集//正常数据//", "正常", "Mission1//正常数据//")
    # 所有异常数据处理
    data_preprocess("附件1：UWB数据集//异常数据//", "异常", "Mission1//异常数据//")

    '''
    任务2: 定位模型
    '''
    '''
    merge(root_dir, save_name)
    @:param1:所有正常或异常数据（1.异常.xlsx，2.异常.xlsx...）的路径
    @:param2:存储文件名
    '''
    # 合并所有处理后的正常数据到一个excel中
    merge("Mission1\\正常数据\\", "所有正常数据.xlsx")
    # 合并所有处理后的异常数据到一个excel中
    merge("Mission1\\异常数据\\", "所有异常数据.xlsx")
    '''
    subtract(root_dir, file_name, save_path)
    @:param1:所有异常数据（1.异常.xlsx，2.异常.xlsx...）的路径
    @:param2:根据这个文件判断哪些数据异常
    @:param3:处理后的文件存储路径
    '''
    subtract("Mission1\\异常数据\\", "全部324条正常数据平均值.xlsx", "异常数据减500\\")
    average_after_subtract("异常数据减500\\", "全部324条异常数据减去500再平均值.xlsx")


