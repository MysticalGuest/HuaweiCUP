import re
from openpyxl import Workbook


with open("附件3：测试集（实验场景2）无干扰.txt", 'r') as txtData:
    lines = txtData.readlines()
    wb = Workbook()
    ws = wb.create_sheet()
    sheet = wb.active
    title = ["Tag编号", "A0", "A1", "A2", "A3", "数据序列号", "数据编号"]
    sheet.append(title)
    i=0
    while i<len(lines):
        print(lines[i])
        arr = re.findall(r"\d+", lines[i])
        t = arr[0]
        a_list = [arr[3]]
        check_no = arr[5]
        serial = arr[6]
        for j in range(1, 4):
            arr_temp = re.findall(r"\d+", lines[i+j])
            a_list.append(arr_temp[3])
        sheet.append([t, int(a_list[0]), int(a_list[1]), int(a_list[2]), int(a_list[3]), check_no, serial])
        i += 4

wb.save("附件3中的正常数据.xlsx")
# wb.save("附件3中的异常数据.xlsx")