import yaml
import pkg_resources

__RESOURCES_PATH = pkg_resources.resource_filename('langtoolkit', 'resources')

__CONFIG = None

__CONFIG_FILE = pkg_resources.resource_filename(
    'langtoolkit', 'resources/config.yaml')


def get_config(config_file=None):
    global __CONFIG
    config_file = config_file if config_file else __CONFIG_FILE
    if __CONFIG is None:
        with open(config_file, 'r') as config_data:
            __CONFIG = yaml.load(config_data, Loader=yaml.FullLoader)

    return __CONFIG


def get_resources_path():
    return __RESOURCES_PATH
