import pytest, allure, requests, json
from common import yaml_until
from common.api_key import ApiKey

ak = ApiKey()
# session = requests.session()


@allure.feature("关于人员信息的接口")
@allure.story("查询人员档案")
# @pytest.mark.parametrize('data', YamlUntil("./data/interface_Project_query.yaml").read_yaml())
@pytest.mark.parametrize('data', yaml_until.load_yaml("./data/Yaml/interface_Project_query.yaml"))
def test_personnel_query(data):
    """
    用例描述：查询人员档案
    :param data:
    :return:
    """

    request = data['request']
    method = request['method']
    url = request['url']
    vales = request["params"]
    headers = request["headers"]
    headers['Authorization'] = headers['Authorization'] + " " + yaml_until.read_extract_yaml("token")
    headers['Cookie'] = headers['Cookie'] + yaml_until.read_extract_yaml("token")

    # res = requests.get(url=url, params=vales, headers=headers)
    # res = session.request("get", url=url, params=vales, headers=headers)
    res = ak.send_request(method, url=url, data=vales, headers=headers)
    print(res.text)

    # vales_json = json.loads(res.text)
    vales_json = ak.get_text(res.text, 'msg')
    # assert vales_json['msg'] == data['eq']['msg'], "登录失败！"
    assert vales_json == data['eq']['msg'], "登录失败！"
