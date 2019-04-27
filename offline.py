import os
import config


def get_files():

    data_dir = config.config['hist_data_dir']
    if not os.path.isdir(data_dir):
        print('path to csv files not found')
        print('TODO: hard code fix in config.py file line 4')
        data_dir = input('enter full path to data files: ')
        config.config['hist_data_dir'] = data_dir
    return os.listdir(data_dir)


