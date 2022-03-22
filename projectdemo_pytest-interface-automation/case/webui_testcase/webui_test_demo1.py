# -*- coding:utf-8 -*-
import pytest
from common.web_key import Key
from common import excel_driver


# 线性代码
# key = Key("Chrome")
# key.open("https://www.baidu.com")
# key.input('id', 'kw', 'jenkins')
# key.click('id', 'su')
# key.sleep(5)
# key.quit()

def test_login1():
    data = excel_driver.read_excel("./data/Excel/webui_data_demo1.xlsx")
    excel_driver.implement_case(data)


def test_login2():
    data = excel_driver.read_excel("./data/Excel/webui_data_demo2.xlsx")
    excel_driver.implement_case(data)


def test_login_duo():
    data = excel_driver.read_excel("./data/Excel/webui_data_demo_duo.xlsx")
    excel_driver.implement_case(data)
