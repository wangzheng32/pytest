import json
import pytest
import allure
from common import yaml_until
from common.api_key import ApiKey
from common.loggerController import log


# 实例化已封装的接口调用
ak = ApiKey()


@allure.feature("登录 获取token")
@allure.story("登录/获取token")
@pytest.mark.run(order=1)
@pytest.mark.parametrize('data', yaml_until.load_yaml("./data/Yaml/rto_login.yaml"))
def test_01_login(data):
    """
    用例描述：登录接口/获取token
    :param data:
    :return:
    """

    # 请求
    request = data['request']
    url = request['url']
    vales = json.dumps(request["params"])
    headers = request["headers"]
    method = request['method']
    res = ak.send_request(method, url=url, data=vales, headers=headers)
    vales_token = ak.get_text(res.text, "token")
    # print(res.text)
    log.info("返回结果为：{}".format(res.text))
    try:
        extract_data = {"token": vales_token}
        yaml_until.wite_yaml(extract_data)
    except:
        # 断言
        # assert vales_json['access_token'] is not data['eq'], "登录失败！"
        assert vales_token is not data['eq'], "操作成功"
