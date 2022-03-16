# -*- coding:utf-8 -*-
from common.web_key import Key

key = Key("Chrome")
key.open("https://www.baidu.com")
key.input('id', 'kw', 'jenkins')
key.click('id', 'su')
key.sleep(5)
key.quit()
