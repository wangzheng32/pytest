"""
    selenium常用关键字封装
        元素定位    locator > name, value
        点击       click   > name, value
        输入       input   > name, value, txt
        访问url    open    > txt
        关闭浏览器  quit
        强制等待    sleep   > txt
"""
from time import sleep

from selenium import webdriver


def open_browser(txt):
    # if type_ == "Chrome":
    #     driver = webdriver.Chrome()
    # elif type_ == "Firefox":
    #     driver = webdriver.Firefox()
    # else:
    #     driver = webdriver.Ie()
    try:
        # python的反射机制
        driver = getattr(webdriver, txt)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:
    # driver = webdriver.Chrome()
    # 构造函数
    def __init__(self, txt):
        self.driver = open_browser(txt)

    # 元素定位：满足八种不同的元素定位方法
    def locator(self, name, value):
        return self.driver.find_element(name, value)

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()

    # 输入
    def input(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    # 访问url
    def open(self, txt):
        self.driver.get(txt)

    # 关闭浏览器
    def quit(self):
        self.driver.quit()

    # 强制等待
    def sleep(self, txt):
        sleep(txt)
