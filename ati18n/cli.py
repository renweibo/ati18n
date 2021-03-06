"""Console script for ati18n."""
from pathlib import Path
import os, typer
from enum import Enum
from ati18n.ati18n import Ati18n


main = typer.Typer(help="Awesome CLI user manager.")


class APPType(str, Enum):
    Java = "Java"
    Vue = "Vue"
    Flask = "Flask"


@main.command()
def check(path: Path = typer.Argument(..., help="应用路径"),
          app_type: APPType = typer.Option("Java", "--type", "-t", help="specify the app type. 指定应用类型")):

    """Console script for ati18n.

    用来检查国际化是否有问题或可疑点的工具，支持Java应用、Vue应用、Flask应用中的多语言功能，检查其中是否有些可能的问题点，方便研发人员快速解决问题。"""
    arg_path = {path}.pop()
    arg_app_type = {app_type}.pop()
    ati = Ati18n(arg_app_type.value.lower(), arg_path)
    config_path = os.path.dirname(__file__) + '/config.ini'
    ati.start(config_path)
    return 0


if __name__ == "__main__":
    main()
