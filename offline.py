import os
import config


def get_files():

    return os.listdir(config.config['hist_data_dir'])


