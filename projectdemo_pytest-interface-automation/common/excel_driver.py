# -*- coding:utf-8 -*-
"""
    Excel文件读写
        获取excel文件
        获取sheet页
        获取单元格内容
"""
import openpyxl
from web_key import Key

# 获取excel文件
excel = openpyxl.load_workbook("../data/Excel/test_demo1.xlsx")
# 获取sheet页信息
sheet = excel['Sheet1']
# 获取指定单元格内容
# cell = sheet['A2'].value
# 获取所有的sheet页
sheets = excel.sheetnames
# 循环赋值sheet的名称
for name in sheets:
    sheet = excel[name]
    print("*******{}*******".format(name))
    # 获取整个sheet页的内容

    for values in sheet.values:
        # 进入测试用例正文
        if type(values[0]) is int:
            """
                提取内容：
                    操作行为
                    对应参数
            """
            data = {
                "name": values[2],
                "value": values[3],
                "txt": values[4]
                }
            # 将参数中为None值全部去掉
            for keyvalue in list(data.keys()):
                if data[keyvalue] is None:
                    del data[keyvalue]
            print(data)
            # 基于关键字行为进行测试内容的执行
            if values[1] == "open_browser":
                # 当读取到open_browser时需要实例化
                key = Key(**data)
            else:
                getattr(key, values[1])(**data)
