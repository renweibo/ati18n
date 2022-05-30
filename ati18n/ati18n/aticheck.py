
__author__ = 'painterg'
__email__ = '22396997@qq.com'

import json
import os
from signal import struct_siginfo
from unittest import result
import pandas as pd
from .constants import OUTPUT_HEAD
from .common import OutputHead
from .utils import get_now
from .config_utils import ConfigUtils
from .check_functions import *


class BaseCheck:

    functions = []
    ''' {no:{file_name:result.json}} '''
    file_results = {}
    ''' result.json列表 '''
    item_results= []
    
    """ 抽取文件数据抽取成字典格式：把每份文件的内容抽取成字典表 """

    def extract_dict(self, f):
        pass

    """ 数据内容会被整理成dataFrame格式进行后续的检查工作 """

    def output_result(self, df):
        pass

    """
        path：i18n文件路径，不允许有子目录
        regex：获取i18n文件的正则表达式
    """
    
    def register_check_function(self, app_type, config_path):
        config = ConfigUtils(app_type, config_path)
        functions = config.get_plugin()
        self.functions = functions.split(',')

    def check(self, app_type, path, regex):
        df = self.load_file(path, regex)
        datas = []
        ''' 获取df中每一行的数据，name为待翻译的key，value为行数据 '''
        for row in df.iterrows():
            key = row[0]
            value = row[1]
            ''' item为每一行的列数据，item[0]为列头(file_name)，item[1]为列值 '''
            for item in value.items():
                temp = item[1]
                if pd.isna(temp):
                    temp = ''
                for f in self.functions:
                    data = eval(f)(app_type, item[0], key, temp)
                    if data is not None:
                        if data[0] == 'FILE':
                            if data[1] in self.file_results:
                                value_map = self.file_results[data[1]]
                                value_map[item[0]] = data[2]
                                self.file_results[data[1]] = value_map
                            else:
                                self.file_results[data[1]] = {item[0]: data[2]}
                        elif data[0] == 'ITEM':
                            self.item_results.append(data[2])
        for k, v in self.file_results.items():
            for sub_k, sub_v in v.items():
                datas.append(sub_v)
        datas.extend(self.item_results)
        self.output_result(datas)

    def load_file(self, path, regex):
        data = {}
        for file in path.glob(regex):
            assert file.is_file(), 'the directory contain sub directory'
            data[file.name] = self.convert_file(file)
        return pd.DataFrame(data)

    # 读取属性文件
    def convert_file(self, file):
        with file.open('r') as f:
            properties = self.extract_dict(f)
            return properties

    # 把df转化成json文件，并保留中文显示
    def to_json(self, df):
        return df.to_json(force_ascii=False)


class CheckJava(BaseCheck):

    def extract_dict(self, f):
        properties = {}
        for line in f:
            if line.find('=') > 0:
                strs = line.replace('\n', '').split('=')
                properties[strs[0]] = strs[1]
        return properties

    def output_result(self, data):
        app_path = os.getcwd()
        output_head = OutputHead(
            tools=OUTPUT_HEAD['tools'],
            version=OUTPUT_HEAD['version'],
            app_type=OUTPUT_HEAD['app_type'],
            app_path=app_path,
            datetime=get_now(),
            result=data)
        with open(app_path + '/' + 'result.json', mode='w') as f:
            json.dump(output_head.json, f, ensure_ascii=False, indent=3)
            print('check is done...')


class CheckVue(BaseCheck):
    pass


class CheckFlask(BaseCheck):
    pass
