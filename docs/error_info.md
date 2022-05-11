# 汇总所有的错误信息

## 1001：翻译条目数不匹配

```json
{
  "No": "1001",
  "Level": "错误",
  "Scope": "整体翻译",
  "Name": "翻译条目数不匹配",
  "Data": {
    "type": "file",
    "file_path": "/xxx.properties"
  },
  "Comment": ""
}
```



## 1002：文件名指定的语言种类和文件内容不匹配

```json
{
  "No": "1002",
  "Level": "错误",
  "Scope": "整体翻译",
  "Name": "文件名指定的语言种类和文件内容不匹配",
  "Data": {
    "type": "file",
    "file_path": "/xxx.properties"
  },
  "Comment": ""
}
```



## 2001：翻译项和指定的语言类型不匹配

```json
{
  "No": "2001",
  "Level": "警告",
  "Scope": "单个翻译项",
  "Name": "翻译项和指定的语言类型不匹配",
  "Data": {
    "type": "item",
    "key_name": "xxxx",
    "key_value": "xxxx",
    "lang_code": "zh_CN",
    "info": "翻译项全是英文，没有中文字符",
    "file_path": "/xxx.properties"
  },
  "Comment": ""
}
```



## 2002：翻译项在 item 级别为空

```json
{
  "No": "2002",
  "Level": "错误",
  "Scope": "单个翻译项",
  "Name": "翻译项在 item 级别为空",
  "Data": {
    "type": "item",
    "key_name": "xxxx",
    "lang_code": "zh_CN",
    "info": "翻译项只有key，value部分值为空",
    "file_path": "/xxx.properties"
  },
  "Comment": ""
}
```

这里指的是没有实际翻译内容的翻译项。

## 2003：源代码中有的 item 没有对应的翻译

```json
{
  "No": "2003",
  "Level": "错误",
  "Scope": "单个翻译项",
  "Name": "源代码中有的 item 没有对应的翻译",
  "Data": {
    "type": "item",
    "key_name": "xxxx",
    "key_value": "xxxx",
    "info": "本翻译项没有对应的翻译，这种情况一共出现了 x 次",
    "file_position": ["xxx/xxx.java#123", "xxx/xxx.jsp#13"]
  },
  "Comment": ""
}
```

`xxx/xxx.java#123`，#号前面是文件名，后面是行号

## 3001：多个相同 key ，但是 value 不一致

```json
{
    "No": "3001",
    "Level": "错误",
    "Scope": "多个翻译项",
    "Name": "多个相同 key ，但是 value 不一致",
    "Data": {
        "type": "items",
        "keys": [
            {
                "file": "xxx/xxxx.properties",
                "key": "key_name",
                "value": "value_info"
            }
        ]
    },
    "Comment": ""
}
```



## 3002：同一个语言的value，对应的其他语言翻译不一样

```json
{
  "No": "3002",
  "Level": "错误",
  "Scope": "多个翻译项",
  "Name": "同一个语言的value，对应的其他语言翻译不一样",
  "Data": {
    "type": "items",
    "keys": [
      {
        "file": "xxx/xxxx.properties",
        "key": "key_name",
        "value": "value_info"
      }
    ]
  },
  "Comment": ""
}
```

