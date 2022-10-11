import allure
import json
import pytest
from common import yaml_until
from common.api_key import ApiKey

ak = ApiKey()


@allure.feature("插入数据接口")
@allure.story("插入数据")
# @pytest.mark.parametrize('data', YamlUntil("./data/interface_Project_query.yaml").read_yaml())
@pytest.mark.parametrize('data', yaml_until.load_yaml("./data/Yaml/zhgd_intodata.yaml"))
def test_personnel_query(data):
    """
    用例描述：插入数据
    :param data:
    :return:
    """

    request = data['request']
    method = request['method']
    url = request['url']
    vales = json.dumps(request["params"])
    headers = request["headers"]
    headers['Authorization'] = headers['Authorization'] + " " + yaml_until.read_extract_yaml("token")

    res = ak.send_request(method, url=url, data=vales, headers=headers)
    print(res.text)

    # vales_json = json.loads(res.text)
    vales_json = ak.get_text(res.text, 'msg')
    # assert vales_json['msg'] == data['eq']['msg'], "登录失败！"
    assert vales_json == data['eq']['msg'], "登录失败！"
