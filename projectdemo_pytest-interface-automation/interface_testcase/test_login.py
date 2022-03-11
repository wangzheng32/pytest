import json,pytest,requests

import allure

from common import yaml_until
from common.api_key import ApiKey


# 实例化已封装的接口调用
ak = ApiKey()

@allure.feature("登录 或 退出登录")
@allure.story("登录/获取token")
@pytest.mark.run(order=1)
# @pytest.mark.login
# 参数化：@pytest.mark.parametrize()
# @pytest.mark.parametrize("data", YamlUntil("./data/interface_data.yaml").read_yaml())
@pytest.mark.parametrize('data', yaml_until.load_yaml("./data/interface_data.yaml"))
# @pytest.fixture()
def test_01_login(data):
    """
    用例描述：登录接口/获取token
    :param data:
    :return:
    """

    # url = data['request']['url']
    # vale = data['request']['params']
    # headers = data['request']['headers']
    # res = requests.post(url=url, params=vale, headers=headers)
    # print(res.text)

    #请求
    request = data['request']
    url = request['url']
    vales = request["params"]
    headers = request["headers"]
    method = request['method']
    # res = requests.post(url=url, params=vales, headers=headers)
    res = ak.send_request(method, url=url, data=vales, headers=headers)
    # 原生方法，没有使用jsonpath提取关键字的方法
    # vales_json = json.loads(res.text)
    vales_token = ak.get_text(res.text, "access_token")
    print(res.text)
    try:
        # 接口关联，将token保存到全局变量管理文件中
        # extract_data = {"token":vales_json['access_token']}
        extract_data = {"token":vales_token}
        yaml_until.wite_yaml(extract_data)
        print(yaml_until.read_extract_yaml("token"))
    except:
        # 断言
        # assert vales_json['access_token'] is not data['eq'], "登录失败！"
        assert vales_token is not data['eq'], "登录失败！"


@allure.feature("登录 或 退出登录")
@allure.story("退出登录")
def test_loginout():
    """
    用例描述：退出登录
    :return:
    """
    print("退出登录")