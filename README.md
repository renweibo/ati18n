![](https://img.shields.io/pypi/v/ati18n.svg) ![Documentation Status](https://readthedocs.org/projects/ati18n/badge/?version=latest)

# 基本用法

```
Usage: cli.py [OPTIONS] PATH

  Console script for ati18n.

  用来检查国际化是否有问题或可疑点的工具，支持Java应用、Vue应用、Flask应用中的多语言功能，检查其中是否有些可能的问题点，方便研发人员快速解决问题。

Arguments:
  PATH    应用路径  [required]

Options:
  -t, --type [Java|Vue|Flask]     specify the app type. 指定应用类型  [default:
                                  Java]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```

# Feature 特性

- 可以检查多语言的条目数是否匹配，主要是针对其他语言的条目数不等于英文（默认比较对象）的条目数，也可以比较切换默认比较对象为其他语言，如中文。
- 支持检查J2EE应用中使用properties文件来做多语言支持

# Design Notes 概要设计

## 使用方法说明

本工具的目标是更实用为多语言类应用提供支持，提升这方面的效率。主要的使用方法有三类：

- 命令行调用直接检查，直观的输出结果
- 命令行调用，输出数据结果文件，方便不同工具之间的衔接
- 可以集成到各类IDE中，方便在IDE中交互式使用

### 中间数据结果

在第二种方式中，ati18n会根据检查结果生成一个检查结果数据文件，实际的数据结果文件是检查信息数据结构的一个数组，举例如下：

```json
{
    "tools": "ati18n",
    "version": "0.1.0",
    "app_path": "/xxx/xxx",
    "app_type": "Java",
    "datetime": "1990-01-01 12:12:12",
    "result": [
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
        },
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
        },
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
    ]
}
```



#### 检查信息数据结构

针对应用的多语言检查，会发现相应的问题，这里定义一下返回问题的可能情况

- 级别：错误、警告、提示
- 范围：整体翻译，单个翻译项，多个翻译项

| 编号 No | 级别 Level | 范围 Scope | 错误名称 Name                        | 详细信息 Data            | 备注 Comment |
| ------- | ---------- | ---------- | ------------------------------------ | ------------------------ | ------------ |
| 1001    | 错误       | 整体翻译   | 翻译条目数不匹配                     | 检查的数据文件和相关信息 |              |
| 1002    | 错误       | 整体翻译   | 文件名指定的语言种类和文件内容不匹配 | 检查的数据文件和相关信息 |              |
| 2001    | 警告/错误  | 单个翻译项 | 翻译项和指定的语言类型不匹配         | 检查的数据项和相关信息   |              |



## 检查规则汇总

在应用中的多语言检查，会有各种规则，这里列出来可能适合的规则

| 规则编号 | 范围         | 规则名称                                                     | 关联检查信息 | 备注 |
| -------- | ------------ | ------------------------------------------------------------ | ------------ | ---- |
| G1001    | 整体翻译     | [Support Check j2ee i18n properties for item number](https://github.com/renweibo/ati18n/issues/3) | 1001         |      |
| G1002    | 整体翻译     | 翻译文件语言种类和文件名称不匹配                             | 1002         |      |
| G2001    | 单个翻译条目 | 翻译文件语言种类和待翻译项名称不匹配                         | 2001         |      |

# Reference

- [Documentation (Not ready)](https://ati18n.readthedocs.io)
- [ati18n · PyPI](https://pypi.org/project/ati18n/) 