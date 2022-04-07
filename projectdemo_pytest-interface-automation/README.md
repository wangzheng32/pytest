#作者：WZ
****
##框架介绍：
### python+pytest+allure+Jekins
#### 设计模式：关键字驱动 或者 POM
#### 数据驱动：Excel、Yaml
#### 框架结构：
####   1、代码与数据分离
####   2、测试代码与逻辑代码分离
####   框架的编码不是固定的，重要的是设计思路
#### Excel库的装载： pip install openpyxl

****
##目录介绍
#### allure-report  :存放allure测试报告
#### allure-results :存放数据
#### case           :存放测试用例
####   interface        :存放接口测试用例
####   webui            :存放webUI测试用例
#### common         :存放公共部分yaml操作、excel操作以及数据库等，存放接口和请求封装
#### configs        :存放域名，登录，数据库等数据
#### data           :存放yaml、excel测试用例数据

#### main           :主函数
#### pytest.ini     :配置文件

****
###参数
####失败重跑：--reruns=NUM

#### conftest.py    :固件配置文件
#### extract_data.yaml:管理所有全局变量

****
### requests的相关方法
#### `res.json()`           把返回值转化成一个dict对象
#### `res.text`             把返回值转换成文本
#### `res.content`          把返回值转换成字节类型
#### `res.status_code`      返回码
#### `res.reason`           返回信息
#### `res.cookies`          返回的cookie信息
#### `res.encoding`         返回编码格式
#### `res.headers`          响应头
#### `res.request.method`   request包含所有请求数据