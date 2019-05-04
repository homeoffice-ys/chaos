import matplotlib.pyplot as plt
import os
import pandas as pd
# import quandl
from ssa_core import ssa_main
import numpy as np
import config
from utilities import RunningStats, cool_plot
from offline import get_files


dir_list = get_files()
rs = RunningStats()
ls = RunningStats()
start_time = None

for f in dir_list:
    df = pd.read_csv(os.path.join(config.config['hist_data_dir'], f))
    print(df.columns)
    cool_plot(df)

    for idx in range(len(df)):
        if start_time is None:
            start_time = pd.to_datetime(df.datetime[idx])
        print((pd.to_datetime(df.datetime[idx]) - start_time).total_seconds())
        rs.push(df['high'].values[idx])
        ls.push(df['low'].values[idx])
        print('High = %2.5f, Low = %2.5f, Spread = %2.5f' % (df['high'].values[idx], df['low'].values[idx],
                                                             df['high'].values[idx] - df['low'].values[idx]))
        print('<High> = %2.5f, Delta = %2.5f, Std = %2.5f' %
              (rs.mean(), rs.delta(), rs.standard_deviation()))
        print('<Low> = %2.5f, Delta = %2.5f, Std = %2.5f' %
              (ls.mean(), ls.delta(), ls.standard_deviation()))

        # train_d = df.values
        # test_d = df.values
        # err = ssa_main(train_d, test_d)


