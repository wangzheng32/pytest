# -*- coding:utf-8 -*-
# from common.web_key import Key
from common import excel_driver


"""
def test_dq_material_platform_add():
    data = excel_driver.read_excel("./data/Excel/webui_dq_Material_Platform_add.xlsx")
    excel_driver.implement_case(data)
"""


def test_dq_material_platform_approval():
    data = excel_driver.read_excel("./data/Excel/webui_dq_Material_Platform_approval.xlsx")
    excel_driver.implement_case(data)
