"""Main module."""
from .aticheck import CheckJava
from .aticheck import CheckVue
from .aticheck import CheckFlask


class Ati18n:

    def __init__(self, app_type, path):
        self.app_type=app_type
        self.path=path
    

    def start(self):
        assert self.path.is_dir(), 'argument path is not directory: %s' % self.path
        if (self.app_type == 'Java'):
            check_obj = CheckJava()
            regex = '*.properties'
        elif (self.app_type == 'Vue'):
            check_obj = CheckVue()
            regex = ''
        elif (self.app_type == 'Flask'):
            check_obj = CheckFlask
            regex = ''
        check_obj.check(self.app_type, self.path, regex)

