# -*- coding:utf-8 -*-
import json
import jsonpath
import requests

# 请求方式的选择封装
session = requests.session()  # 会话

data = {
    "url": "http://172.1.0.160:8080/system/scheduleUnitPro",
    "method": "post",
    "data": {
        'projectCode': 'qqqqooooooossssssssssdd5555',
        'projectName': '底基层',
        'projectUnit': 'm2',
        'projectNum': 6754.73,
        "projectCompleteNum": 0,
        "sort": 0
    },
    "headers": {
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbklkIjoic3lzX3VzZXI6MSIsInJuIjoieW9EQjRoMzhMWk9hRkNGcktZNGJwR3FvTkhHODdUWUIifQ.N_U6aoKZ41n8EJ6wj4zyTEALmsNR5R2V0oLkC8itdCk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
    }
}
data_ = json.dumps(data["data"])
print(type(data_))
res = session.request(method=data["method"], url=data["url"], data=data_, headers=data["headers"])
# res = requests.post(url, data, headers=headers)
print(res.text)
print(res.request.body)
