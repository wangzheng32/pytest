# -*- coding:utf-8 -*-
import json
import jsonpath
import requests
from common.loggerController import log


class ApiKey:
    """
    接口测试封装关键字
        GET： 请求指定的页面信息，并返回实体主体。
        HEAD： 只请求页面的首部。
        POST： 请求服务器接受所指定的文档作为对所标识的URI的新的从属实体。
        PUT： 从客户端向服务器传送的数据取代指定的文档的内容。
        DELETE： 请求服务器删除指定的页面。
        get 和 post比较常见 GET请求将提交的数据放置在HTTP请求协议头中；POST提交的数据则放在实体数据中
    """

    # 请求方式的选择封装
    session = requests.session()  # 会话

    # 统一请求接口:二次封装
    def send_request(self, method, url, data, **kwargs):
        # 参数上传的方式：params\json\data\files
        str_method = str(method).lower()
        if str_method == "get" or "post":
            # return self.session.request(method=str_method, url=url, params=data, **kwargs)
            if type(data) is str:
                return self.session.request(method=str_method, url=url, data=data, **kwargs)
            elif type(data) is dict:
                return self.session.request(method=str_method, url=url, params=data, **kwargs)
        # elif str_method == "post":
        #     # str_data = json.dumps(data)
        #     return self.session.request(method=str_method, url=url, params=data, **kwargs)
        else:
            print("不支持的请求方式")
            log.info("不支持的请求方式")

    # 基于jsonpath获取数据的关键字：用于提取需要的内容
    def get_text(self, txt, key):
        try:
            # jsonpath获取数据的表达式，成功返回list，失败返回false
            txt = json.loads(txt)
            json_value = jsonpath.jsonpath(txt, '$..{0}'.format(key))
            if json_value:
                if len(json_value) == 1:
                    return json_value[0]
                return json_value
        except Exception as e:
            return e
        return json_value


# 验证
# if __name__ == '__main__':
#     ak = ApiKey()
#     data = {
#         "url": "http://123.60.88.124/prod-api/auth/user/login",
#         "method": "post",
#         "params": {
#             "username": "admin",
#             "password": 123456,
#             "grant_type": "password"
#         },
#         "headers": {
#             "Content - Type": "application / json",
#             "Authorization": "Basic b2E6MTIzNDU2"
#         }
#     }
#     res = ak.send_request(data["method"], url=data["url"], data=data["params"], headers=data["headers"])
#     print(res.text)
#     print(ak.get_text(res.text, "access_token"))
