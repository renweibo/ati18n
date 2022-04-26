from enum import Enum


class DataType(str, Enum):
    File = "flie"
    Item = "item"


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


class OutputHead(OutputBase):

    __slots__ = ('tools', 'version', 'app_path', 'app_type', 'datetime', 'result')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class OutputResult(OutputBase):
   
    __slots__ = ('No', 'Level', 'Scope', 'Name', 'Data', 'Comment')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class OutputDataSimple(OutputBase):

    __slots__ = ('type', 'file_path')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class OutputDataItem(OutputBase):

    __slots__ = ('type', 'key_name', 'key_value', 'lang_code', 'info', 'file_path')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

