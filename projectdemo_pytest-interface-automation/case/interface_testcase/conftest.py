import pytest
from common.yaml_until import clear_yaml
'''
fixture固件（装饰器）
    scope =
        "function"(default) 函数级别
        "class"             类级别
            需要装饰器调用pytest.mark.usefixture("usefixtureName")
        "module"            模块级别
        "package"           包级别/会话级别
        "session"           会话级别
    autouse =       自动执行
        True
'''


# 执行数据库语句
@pytest.fixture(scope="session", autouse=True)
def execute_database_sql():
    # 在所有请求---------------之前执行
    clear_yaml()
    yield
    # 在所有请求---------------之后执行


# 在每个用例之前执行一次，如: 打开浏览器、加载网页
# @pytest.fixture(autouse=True)
def setup():
    print("----------")


# 在每个用例执行之后执行，如: 关闭浏览器
def teardown():
    pass


# 在每个类之前执行一次，如: 创建日志对象，创建数据库连接
def setup_class():
    pass


# 在每个类之后执行一次，如: 关闭数据库，销毁日志对象
def teardown_class():
    pass
