__author__ = 'painterg'
__email__ = '22396997@qq.com'

import configparser, os, shutil
from git import Repo


class ConfigUtils:
     
    def __init__(self, app_type, config_path):
        self.app_type = app_type
        config = configparser.ConfigParser()
        config.read(config_path)
        self.config = config

    def get_plugin(self):
        value = self.config.get(self.app_type, 'plugin', fallback='check_1001')
        if len(value) == 0:
            value = 'check_1001'
        return value
    
    def get_key_separtor(self):
        value = self.config.get(self.app_type, 'key.prefix.separtor', fallback='.')
        if len(value) == 0:
            value = '.'
        return value
    
    def get_key_location(self):
        value = self.config.get(self.app_type, 'key.prefix.location', fallback='2')
        if len(value) == 0:
            value = '2'
        return value

    def get_url(self):
        return self.config[self.app_type]['repository.url']

    def get_temp_storage_prefix(self):
        return self.config[self.app_type]['repository.temp.storage']

    def get_git_name(self):
        dir_suffix = self.get_url().split('/')[-1]
        end = dir_suffix.find('.git')
        return dir_suffix[0:end]

    def get_clone_to_path(self):
        temp_prefix = self.get_temp_storage_prefix()
        dir_name = self.get_git_name()
        if temp_prefix[-1] == '/':
            return temp_prefix + dir_name
        else:
            return temp_prefix + '/' + dir_name

    def clone_repository(self):
        git_url = self.get_url()
        dir = self.get_clone_to_path()
        print(dir)
        if os.path.exists(dir):
            shutil.rmtree(dir)
        repo = Repo.clone_from(url=git_url,to_path=dir)
