# 汇总所有的错误信息

## 1001

```json
{
  "No": "1001",
  "Level": "错误",
  "Scope": "单个翻译项",
  "Name": "源代码中有的 item 没有对应的翻译",
  "Data": {
    "type": "item",
    "key_name": "xxxx",
    "key_value": "xxxx",
    "info": "",
    "file_position": ["xxx/xxx.java#123", "xxx/xxx.jsp#13"]
  },
  "Comment": ""
}
```



## 1002

```json
{
  "No": "1002",
  "Level": "错误",
  "Scope": "单个翻译项",
  "Name": "源代码中有的 item 没有对应的翻译",
  "Data": {
    "type": "item",
    "key_name": "xxxx",
    "key_value": "xxxx",
    "info": "",
    "file_position": ["xxx/xxx.java#123", "xxx/xxx.jsp#13"]
  },
  "Comment": ""
}
```



## 2001：

```json
{
  "No": "2001",
  "Level": "错误",
  "Scope": "单个翻译项",
  "Name": "",
  "Data": {
    "type": "item",
    "key_name": "xxxx",
    "info": "",
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

## 3001

```json
{
  "No": "3001",
  "Level": "错误",
  "Scope": "单个翻译项",
  "Name": "源代码中有的 item 没有对应的翻译",
  "Data": {
    "type": "item",
    "key_name": "xxxx",
    "key_value": "xxxx",
    "info": "",
    "file_position": ["xxx/xxx.java#123", "xxx/xxx.jsp#13"]
  },
  "Comment": ""
}
```



## 3002

```json
{
  "No": "3002",
  "Level": "错误",
  "Scope": "单个翻译项",
  "Name": "源代码中有的 item 没有对应的翻译",
  "Data": {
    "type": "item",
    "key_name": "xxxx",
    "key_value": "xxxx",
    "info": "",
    "file_position": ["xxx/xxx.java#123", "xxx/xxx.jsp#13"]
  },
  "Comment": ""
}
```

