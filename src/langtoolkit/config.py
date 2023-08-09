import os
import yaml


import pkg_resources

__BASE_PATH = os.getcwd()

__CONFIG = None
# __CONFIG_FILE = os.path.join(__BASE_PATH, 'config.yaml')
__CONFIG_FILE = pkg_resources.resource_filename('langtoolkit', 'resources/config.yaml')


def get_config(config_file=None):
    config_file = config_file if config_file else __CONFIG_FILE
    global __CONFIG
    if __CONFIG is None:

        with open(config_file, 'r') as config_data:
            __CONFIG = yaml.load(config_data, Loader=yaml.FullLoader)

    return __CONFIG


def get_path():
    return __BASE_PATH
