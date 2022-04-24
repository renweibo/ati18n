
__author__ = """painterg"""
__email__ = '22396997@qq.com'


import pandas as pd

class BaseCheck:

    """ 抽取文件数据抽取成字典格式：把每份文件的内容抽取成字典表 """
    def extract_dict(self, f):
        pass
        
    
    """ 数据内容会被整理成dataFrame格式进行后续的检查工作"""
    def output_result(self, df):
        pass

    """ 
        path：i18n文件路径，不允许有子目录
        regex：获取i18n文件的正则表达式
    """
    def check(self, path, regex):
        df = self.load_file(path, regex)
        self.output_result(df)        


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



class CheckJava(BaseCheck):

    def extract_dict(self, f):
        properties = {}
        for line in f:
            if line.find('=') > 0:
                strs = line.replace('\n', '').split('=')
                if strs[1]:
                    properties[strs[0]] = strs[1]
        return properties

    
    def output_result(self, df):
        result = df[df.isnull().T.any()]
        print('----------------------------------------------')
        print(result)
        print('----------------------------------------------')
        print('异常项总数为:%s' % len(result))


class CheckVue(BaseCheck):
    pass


class CheckFlask(BaseCheck):
    pass