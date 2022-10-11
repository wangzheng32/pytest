"""
    selenium常用关键字封装
        元素定位    locator >      name, value
        点击       click   >      name, value
        输入       input   >      name, value, txt
        访问url    open    >      txt
        关闭浏览器  quit
        强制等待    sleep   >      txt
        断言       assert_txt  >  name, value, txt
"""
import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import os


def head_less(browser):
    """
    浏览器进行无界面化
    :param browser:浏览器名称
    :return:option
    """
    b_O = browser + "Options"
    option = getattr(webdriver, b_O)()
    option.add_argument('--headless')
    return option


def open_browser(txt):
    """
    if type_ == "Chrome":
        driver = webdriver.Chrome()
    elif type_ == "Firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()
    """
    try:
        option = head_less(txt)
        # python的反射机制
        driver = getattr(webdriver, txt)(options=option)
        # 不隐藏浏览器
        # driver = getattr(webdriver, txt)()
    except Exception as e:
        print(e)
        option = head_less(txt)
        driver = webdriver.Chrome(options=option)
        # 不隐藏浏览器
        # driver = webdriver.Chrome()
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

    # 不可交互式的元素点击
    def click_script(self, name, value):
        self.driver.execute_script("arguments[0].click()", self.locator(name, value))

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
        time.sleep(txt)

    # 断言
    def assert_txt(self, name, value, txt):
        at = self.locator(name, value)
        et = "实际结果与预期结果:{}不同".format(value)
        assert (at.text == txt), et

    # 当前页面
    def sreach_w(self):
        self.driver.current_window_handle

    # 上传本地pdf文件
    def up_load_pdf(self, name, value, txt):
        self.locator(name, value).send_keys(os.getcwd(), "/data/Document/{}.pdf".format(txt))

    # 上传本地png图片
    def up_load_png(self, name, value, txt):
        self.locator(name, value).send_keys(os.getcwd(), "/data/Document/{}.png".format(txt))
