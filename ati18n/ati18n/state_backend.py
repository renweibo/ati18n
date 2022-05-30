
__author__ = 'painterg'
__email__ = '22396997@qq.com'

''' 
   如果整体程序结构是流式处理方式的话，那么针对一些需要先前状态数据的需求，无法做到纯函数式
   因此定一个状态存储，而为了状态结构的简单化，暂时使用单层字典结构，使用时需要组合数据成为key或value
'''

class StateBackend(object):
    ''' {name:{key:value}} '''
    state_dict = {}
    
    _instance = None
    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance
    
    def __init__(self):
        pass
    
    def get_dict(self, name):
        return self.state_dict[name]
    
    def get_value(self, name ,key):
        return self.state_dict[name][key] if name in self.state_dict and key in self.state_dict[name] else None
    
    def exists_dict(self, name):
        return True if name in self.state_dict else False
    
    def exists_key(self, name ,key):
        return True if key in self.state_dict[name] else False
    
    def create_dict(self, name):
        self.state_dict[name] = {}
    
    def put(self, name, key, value):
        if self.exists_dict(name):
            value_dict = self.state_dict[name]
            value_dict[key] = value
            self.state_dict[name] = value_dict
        else:
            self.state_dict[name] = {key : value}
            
    def delete(self, name, key):
        del self.state_dict[name][key]
        
    def clear(self, name):
        del self.state_dict[name]
