__author__ = 'painterg'
__email__ = '22396997@qq.com'

import py3langid as langid
import time, datetime, pytz
from .common import *

def get_now():
        utc = pytz.timezone('Asia/Shanghai')
        t = datetime.datetime.now(tz=utc).strftime('%Y-%m-%d %H:%M:%S')
        return t 


def determine_lang(file_name, value, app_type):
        lang = langid.classify(value)
        lang_type = lang[0]
        if (lang_type == 'zh' and app_type == 'Java'):
            lang_type = 'zh_CN'
        end = file_name.find('.properties')
        start = end - len(lang_type)
        type_from_file_name=file_name[start:end]
        if (lang_type == type_from_file_name):
            return (True, lang_type)
        else:
            return (False, lang_type)


def out_template_file(file_name, error):
    data = OutputDataSimple(type=DataType.File.value, file_path=file_name)
    result = OutputResult(No=error['no'], Level=error['level'], Scope=error['scope'], Name=error['name'], Data=data.json, Comment=error['comment'])
    return result


def out_template_item(file_name, error, key, value, code):
    data = OutputDataSimple(type=DataType.File.value, file_path=file_name)
    data = OutputDataItem(type=DataType.Item.value, file_path=file_name, key_name=key, key_value=value, lang_code=code, info='')
    result = OutputResult(No=error['no'], Level=error['level'], Scope=error['scope'], Name=error['name'], Data=data.json, Comment=error['comment'])
    return result
