import yaml
import pkg_resources

_RESOURCES_PATH = pkg_resources.resource_filename('langtoolkit', 'resources')
_CONFIG_FILE = pkg_resources.resource_filename('langtoolkit', 'resources/config.yaml')
_CONFIG = None



def set_config(config_file):
    global _CONFIG_FILE
    _CONFIG_FILE = config_file


def get_config():
    global _CONFIG
    
    if _CONFIG is None:
        with open(_CONFIG_FILE, 'r', encoding='utf-8') as config_data:
            _CONFIG = yaml.load(config_data, Loader=yaml.FullLoader)

    return _CONFIG


def get_resources_path():
    return _RESOURCES_PATH
