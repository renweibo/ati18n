"""Main module."""


from .aticheck import CheckJava
from .aticheck import CheckVue
from .aticheck import CheckFlask


class Ati18n:

    def __init__(self, app_type, path):
        self.app_type = app_type
        self.path = path

    def start(self, config_path):
        print(config_path)
        assert self.path.is_dir(), 'argument path is not directory: %s' % self.path
        if (self.app_type.lower() == 'java'.lower()):
            check_obj = CheckJava()
            regex = '*.properties'
        elif (self.app_type.lower() == 'vue'.lower()):
            check_obj = CheckVue()
            regex = ''
        elif (self.app_type.lower() == 'flask'.lower()):
            check_obj = CheckFlask
            regex = '' 
        check_obj.register_check_function(self.app_type, config_path)
        check_obj.check(self.app_type, self.path, regex)
