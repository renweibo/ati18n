
__author__ = 'painterg'
__email__ = '22396997@qq.com'

from curses import KEY_SCOMMAND
import os
from .state_backend import StateBackend
from .config_utils import ConfigUtils
from .utils import out_template_file, out_template_item, determine_lang

''' 在函数返回元组之前，根据检测类型添加元组中第一个数据项 '''
CHECK_TYPE_FILE = 'FILE'
CHECK_TYPE_ITEM = 'ITEM'

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("ati18n/")+len("ati18n/")]
configPath = os.path.abspath(rootPath + 'ati18n/config.ini') 
statebackend = StateBackend()

def check_1001(app_type, file_name, key, value):
    from .constants import ERROR_1001
    result = None
    if len(value) == 0: 
        result = out_template_file(file_name, ERROR_1001)
    return (CHECK_TYPE_FILE, ERROR_1001['no'], result.json) if result is not None else None

def check_1002(app_type, file_name, key, value):
    from .constants import ERROR_1002
    result = None
    if len(value) > 0 and not determine_lang(file_name, value, app_type)[0]:
        result = out_template_file(file_name, ERROR_1002)
    return (CHECK_TYPE_FILE, ERROR_1002['no'], result.json) if result is not None else None

def check_2001(app_type, file_name, key, value):
    from .constants import ERROR_2001
    result = None
    if len(value) > 0:
        lang_type = determine_lang(file_name, value, app_type)
        if not lang_type[0]:
            result = out_template_item(file_name, ERROR_2001, key, value, lang_type[1])
    return (CHECK_TYPE_ITEM, ERROR_2001['no'], result.json) if result is not None else None

def check_2002(app_type, file_name, key, value):
    from .constants import ERROR_2002
    result = None
    if len(value) == 0:
        result = out_template_item(file_name, ERROR_2002, key, value, '')
    return (CHECK_TYPE_ITEM, ERROR_2002['no'], result.json) if result is not None else None

def check_3001(app_type, file_name, key, value):
    if len(value) == 0:
        return None
    from .constants import ERROR_3001
    con = ConfigUtils(app_type, configPath)
    separtor = con.get_key_separtor()
    location = int(con.get_key_location()) - 1
    name = 'check3001'
    ks = key.split(separtor)
    k = ks[-1]
    if len(ks) > location:
        k = ks[location]
    result = None
    if not statebackend.exists_dict(name):
        statebackend.create_dict(name)
    old = statebackend.get_value(name, file_name + '|' + k)
    if old is None:
        statebackend.put(name, file_name + '|' + k, value)
    else:
        if old != value:
            result = out_template_item(file_name, ERROR_3001, key, value, '')
    return (CHECK_TYPE_ITEM, ERROR_3001['no'], result.json) if result is not None else None
