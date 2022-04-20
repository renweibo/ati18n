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

## 检查结果

针对应用的多语言检查，会发现相应的问题，这里定义一下返回问题的可能情况

- 级别：错误、警告、提示
- 范围：整体翻译，单个翻译项，多个翻译项

| 编号 | 级别 | 范围     | 错误名称         | 详细信息 |
| ---- | ---- | -------- | ---------------- | -------- |
| 1001 | 错误 | 整体翻译 | 翻译条目数不匹配 |          |
|      |      |          |                  |          |
|      |      |          |                  |          |

