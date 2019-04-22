import os
import config


def get_files():
    print(config.config['data_dir'])
    return os.listdir(config.config['data_dir'])


