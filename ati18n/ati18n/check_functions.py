
__author__ = 'painterg'
__email__ = '22396997@qq.com'

from .constants import ERROR_1001, ERROR_1002, ERROR_2001, ERROR_2002
from .utils import out_template_file, out_template_item, determine_lang

''' 在函数返回元组之前，根据检测类型添加元组中第一个数据项 '''
CHECK_TYPE_FILE = 'FILE'
CHECK_TYPE_ITEM = 'ITEM'

def check_1001(app_type, file_name, key, value):
    result = None
    if len(value) == 0: 
        result = out_template_file(file_name, ERROR_1001)
    return (CHECK_TYPE_FILE, ERROR_1001['no'], result.json) if result is not None else None

def check_1002(app_type, file_name, key, value):
    result = None
    if len(value) > 0 and not determine_lang(file_name, value, app_type)[0]:
        result = out_template_file(file_name, ERROR_1002)
    return (CHECK_TYPE_FILE, ERROR_1002['no'], result.json) if result is not None else None

def check_2001(app_type, file_name, key, value):
    result = None
    if len(value) > 0:
        lang_type = determine_lang(file_name, value, app_type)
        if not lang_type[0]:
            result = out_template_item(file_name, ERROR_2001, key, value, lang_type[1])
    return (CHECK_TYPE_ITEM, ERROR_2001['no'], result.json) if result is not None else None

def check_2002(app_type, file_name, key, value):
    result = None
    if len(value) == 0:
        result = out_template_item(file_name, ERROR_2002, key, value, '')
    return (CHECK_TYPE_ITEM, ERROR_2002['no'], result.json) if result is not None else None
