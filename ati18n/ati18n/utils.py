__author__ = 'painterg'
__email__ = '22396997@qq.com'

import py3langid as langid
import time, datetime, pytz

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
            return True
        else:
            return False
