"""Top-level constant definition for ati18n."""

OUTPUT_HEAD = {'tools': 'ati18n', 'version': '0.1.0', 'app_type': 'java'}
ERROR_1001 = {
    'no': '1001',
    'level': '错误',
    'scope': '整体翻译',
    'name': '翻译条目数不匹配',
    'data': '检查的数据文件和相关信息',
    "comment": ''}
ERROR_1002 = {
    'no': '1002',
    'level': '错误',
    'scope': '整体翻译',
    'name': '文件名指定的语言种类和文件内容不匹配',
    'data': '检查的数据文件和相关信息',
    "comment": ''}
ERROR_2001 = {
    'no': '2001',
    'level': '警告/错误',
    'scope': '单个翻译项',
    'name': '翻译项和指定的语言类型不匹配',
    'data': '检查的数据项和相关信息',
    "comment": ''}
ERROR_2002 = {
    'no': '2002',
    'level': '错误',
    'scope': '单个翻译项',
    'name': '翻译项在item级别为空',
    'data': '检查的数据项和相关信息',
    "comment": ''}
ERROR_3001 = {
    'no': '3001',
    'level': '警告/错误',
    'scope': '多个翻译项',
    'name': '多个相同key，但是value不一致',
    'data': '检查的数据项和关联所有翻译项信息',
    "comment": ''}
