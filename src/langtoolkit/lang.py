import yaml
import os
import pickle

from langtoolkit.config import BASE_PATH

DICTIONARY = None

CONFIG_FILE = os.path.join(BASE_PATH, 'config.yaml')


def load_data(config_file=CONFIG_FILE):
    global DICTIONARY
    if DICTIONARY is None:
        DICTIONARY = {}
        with open(config_file, 'r') as config_data:
            config = yaml.load(config_data, Loader=yaml.FullLoader)

        for lang in config['lang']:
            lang_file = os.path.join(
                BASE_PATH, 'resources', config['lang'][lang])
            with open(lang_file, 'rb') as handle:
                DICTIONARY[lang] = pickle.load(handle)

    return DICTIONARY
