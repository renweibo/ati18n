"""Main module."""
from .aticheck import CheckJava
from .aticheck import CheckVue
from .aticheck import CheckFlask
from enum import Enum


class Ati18n:

    def __init__(self, app_type, path):
        self.app_type=app_type
        self.path=path
    

    def start(self):
        assert self.path.is_dir(), 'argument path is not directory: %s' % self.path
        if (self.app_type == 'Java'):
            check_obj = CheckJava()
            regex = '*.properties'
        elif (self.app_type == 'Vue'):
            check_obj = CheckVue()
            regex = ''
        elif (self.app_type == 'Flask'):
            check_obj = CheckFlask
            regex = ''
        check_obj.check(self.path, regex)


""" 定义一个pojo风格输出对象的基类 """
class OutputBase:
    
    __slots__ = ()

    def __init__(self, **kwargs):
        for k in kwargs.fromkeys(self.__slots__):
            if k in kwargs:
                setattr(self, k, kwargs[k])
    
    @property
    def json(self):
        return {s: getattr(self, s) for s in self.__slots__ if hasattr(self, s)}


class OutputResult(OutputBase):
   
    __slots__ = ('No', 'Level', 'Scope', 'Name', 'Data', 'Comment')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DataType(str, Enum):
    File = "flie"
    Item = "item"


class OutputDataSimple(OutputBase):

    __slots__ = ('type', 'file_path')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class OutputDataItem(OutputBase):

    __slots__ = ('type', 'key_name', 'key_value', 'lang_code', 'info', 'file_path')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

