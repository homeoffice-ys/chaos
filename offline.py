import os

data_dir = r'C:\Users\Yochanan\Documents\Data\EURUSD'

def get_files():
    print(data_dir)
    return os.listdir(data_dir)


