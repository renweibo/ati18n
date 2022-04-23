"""Main module."""
import pandas as pd

class Ati18n:

    def __init__(self, app_type, path):
        self.app_type=app_type
        self.path=path
    

    def start(self):
        assert self.path.is_dir(), 'argument path is not directory: %s' % self.path
        if (self.app_type == 'Java'):
            self.check_java()
        elif (self.app_type == 'Vue'):
            self.check_vue()
        elif (self.app_type == 'Flask'):
            self.check_flask()


    # 对java属性文件进行检查
    def check_java(self):
        data = {}
        for file in self.path.glob('*.properties'):
            assert file.is_file(), 'the directory contain sub directory'
            data[file.name] = self.load_file(file)
        df = pd.DataFrame(data)
        print(df[df.isnull().T.any()])
    

    def check_vue(self):
        pass


    def check_flask(self):
        pass


    # 读取属性文件
    def load_file(self, file):
        with file.open('r') as f:
            properties = self.extract_dict(f)
            return properties

    
    # 抽取文件数据整理成字典格式
    def extract_dict(self, f):
        properties = {}
        for line in f:
            if line.find('=') > 0:
                strs = line.replace('\n', '').split('=')
                if strs[1]:
                    properties[strs[0]] = strs[1]
        return properties