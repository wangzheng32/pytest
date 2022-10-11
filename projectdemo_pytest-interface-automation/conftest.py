import pytest
from common.yaml_until import clear_yaml
from common.web_key import Key
from common.loggerController import log

'''
fixture固件（装饰器）
    scope =
        "function"(default) 函数级别：在每个测试函数中只执行一次【默认】
        "class"             类级别：在每个测试类中只执行一次
            需要装饰器调用pytest.mark.usefixture("usefixtureName")
        "module"            模块级别：在模块级别(测试文件)中只执行一次
        "package"           包级别/会话级别
        "session"           会话级别：一次运行只执行一次
    autouse = 
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
@pytest.fixture(autouse=True)
def setup():
    print("-----setup-----")


# 在每个用例执行之后执行，如: 关闭浏览器
def teardown():
    print("---teardown---")
    log.info("当前用例结束，关闭当前浏览器--------")
    Key.quit()


# 在每个类之前执行一次，如: 创建日志对象，创建数据库连接
def setup_class():
    pass


# 在每个类之后执行一次，如: 关闭数据库，销毁日志对象
def teardown_class():
    pass
