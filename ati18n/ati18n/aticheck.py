
__author__ = 'painterg'
__email__ = '22396997@qq.com'

import pandas as pd
from .common import *
from .utils import *
from . import *
import json
import os

class BaseCheck:

    count_status = []
    lang_status = []
    check_1001 = True
    check_1002 = True
    check_2001 = True

    """ 抽取文件数据抽取成字典格式：把每份文件的内容抽取成字典表 """
    def extract_dict(self, f):
        pass
        
    
    """ 数据内容会被整理成dataFrame格式进行后续的检查工作 """
    def output_result(self, df):
        pass

    """ check errors about the type of 1001 and 1002"""
    def check_file(self, app_type, file_name, value):
        return None


    """ check errors about the type of 1003"""
    def check_item(self, app_type, file_name, value):
        return None

    """ 
        path：i18n文件路径，不允许有子目录
        regex：获取i18n文件的正则表达式
    """
    def check(self,app_type, path, regex):
        df = self.load_file(path, regex)
        data = []
        ''' 获取df中每一行的数据，name为待翻译的key，value为行数据 '''
        for row in df.iterrows():
            key = row[0]
            value = row[1]
            ''' item为每一行的列数据，item[0]为列头，item[1]为列值 '''
            for item in value.items():
                data1 = self.check_file(app_type, item[0], item[1])
                data2 = self.check_item(app_type, item[0], key, item[1])
                if data1 is not None: data.append(data1)
                if data2 is not None: data.append(data2)
        self.output_result(data)        


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

    
    def check_file(self, app_type, file_name, value):
        result = None
        if self.check_file and len(value) == 0  and self.count_status.count(file_name) == 0:
            self.count_status.append(file_name)
            result = out_template_file(file_name, ERROR_1001)
        elif self.check_1002 and len(value) > 0 and not determine_lang(file_name, value, app_type)[0] and self.lang_status.count(file_name) == 0:
            self.lang_status.append(file_name)
            result = out_template_file(file_name, ERROR_1002)
        return result.json if result is not None else None


    def check_item(self, app_type, file_name, key, value):
        result = None
        if self.check_2001 and len(value) > 0:
            lang_type = determine_lang(file_name, value, app_type)
            if not lang_type[0]:
                result = out_template_item(file_name, ERROR_2001, key, value, lang_type[1])
        return result.json if result is not None else None

    def output_result(self, data):
        app_path = os.getcwd()
        json_result = json.dumps(data, ensure_ascii=False)
        output_head = OutputHead(tools=OUTPUT_HEAD['tools'], version=OUTPUT_HEAD['version'], app_type=OUTPUT_HEAD['app_type'], app_path=app_path, datetime=get_now(), result=data)
        with open(app_path+ '/' + 'result.json', mode='w') as f:
            json.dump(output_head.json, f, ensure_ascii=False, indent=3)
            print('check is done...')


class CheckVue(BaseCheck):
    pass


class CheckFlask(BaseCheck):
    pass