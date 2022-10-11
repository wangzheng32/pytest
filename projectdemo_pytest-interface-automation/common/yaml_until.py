# -*- coding:utf-8 -*-
import yaml


# 读取用例yaml文件
def load_yaml(path):
    file = open(path, encoding="utf-8")
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data


# 读取参数化yaml文件
def read_extract_yaml(key):
    file = open("./extract_data.yaml", encoding="utf-8")
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data[key]


# 写入参数化yaml文件,mode="a"表示追加的方式写入
def wite_yaml(data):
    ''' 将关联参数写入文件 '''
    file = open("./extract_data.yaml", encoding="utf-8", mode="a")
    yaml.dump(data, stream=file, allow_unicode=True)


# 清空参数化yaml文件
def clear_yaml():
    ''' 将关联参数的文件清空 '''
    with open("./extract_data.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()


# class YamlUntil:
#     def __init__(self, yaml_file):
#         self.yaml_file = yaml_file
#
#     # 读取yaml文件
#     def read_yaml(self):
#         with open(self.yaml_file, encoding="utf-8") as f:
#             data = yaml.load(f, Loader=yaml.FullLoader)
#             return data
#
#     # 写入yaml文件,mode="a"表示追加的方式写入
#     def wite_yaml(self, data):
#         with open(self.yaml_file, encoding="utf-8", mode="a") as f:
#             yaml.dump(data, stream=f, allow_unicode=True)
#
#     # 清空yaml文件
#     def clear_yaml(self):
#         with open(self.yaml_file, encoding="utf-8", mode="w") as f:
#             f.truncate()
