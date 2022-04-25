
__author__ = """painterg"""
__email__ = '22396997@qq.com'

import pandas as pd
from .common import *
from . import *
import json

class BaseCheck:

    """ 抽取文件数据抽取成字典格式：把每份文件的内容抽取成字典表 """
    def extract_dict(self, f):
        pass
        
    
    """ 数据内容会被整理成dataFrame格式进行后续的检查工作 """
    def output_result(self, df):
        pass

    """ check errors about the type of 1001 return list"""
    def check_1001(self,data):
        return []


    """ check errors about the type of 1002 return list"""
    def check_1002(self,data):
        return []


    """ check errors about the type of 2001 return list"""
    def check_2001(self,data):
        return []

    """ 
        path：i18n文件路径，不允许有子目录
        regex：获取i18n文件的正则表达式
    """
    def check(self, path, regex):
        df = self.load_file(path, regex)
        data1 = self.check_1001(df)
        data2 = self.check_1002(df)
        data3 = self.check_2001(df)
        data = data1 + data2 + data3
        # self.output_result(data)        


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

    
    def check_1001(self, df):
        results = []
        for row in df.iterrows():
            name = row[0]
            value = row[1]
            for item in value.items():
                file_name = item[0]
                v = item[1]
                if len(v) == 0:
                    data = OutputDataSimple(type=DataType.File.value, file_path=item[0])
                    result = OutputResult(No=ERROR_1001['no'], Level=ERROR_1001['level'], Scope=ERROR_1001['scope'], Name=ERROR_1001['name'], Data=data.json, comment=ERROR_1001['comment'])
                    print(result.json)
                    results.append(result)
        return results


    def output_result(self, data):
        
        result = df[df.isnull().T.any()]
        print('----------------------------------------------')
        print(result)
        print('----------------------------------------------')
        print('异常项总数为:%s' % len(result))


class CheckVue(BaseCheck):
    pass


class CheckFlask(BaseCheck):
    pass