import matplotlib.pyplot as plt
import os
import pandas as pd
# import quandl
from ssa_core import ssa_main
import numpy as np
import config
from offline import get_files


dir_list = get_files()

for f in dir_list:
    df = pd.read_csv(os.path.join(config.config['hist_data_dir'], f))
    print(df.columns)

    for idx in range(len(df)):
        print(df.datetime[idx])
        train_d = df.values
        test_d = df.values
        err = ssa_main(train_d, test_d)


