import matplotlib.pyplot as plt
import os
import pandas as pd
# import quandl
from ssa_core import ssa, ssa_predict, ssaview, inv_ssa, ssa_cutoff_order
import numpy as np
import config
from offline import get_files


def mape(f, t):

    return 100*((f - t)/t).abs().sum()/len(t)


def mae(f, t):

    return 100*(f - t).abs().sum()/len(t)


dir_list = get_files()

for f in dir_list:
    print(f)
    df = pd.read_csv(os.path.join(config.config['hist_data_dir'], f))


# filename = 'EURUSD-2019-03.csv'
# full_path = r'C:\Users\Yochanan\Documents\Data\EURUSD'
# df = pd.read_csv(os.path.join(full_path, filename))
# print(df.columns)

# highs = df['datetime'].between('20190203','20190202')
# plt.plot(df['high'].values[highs])

test_date = df['datetime'].values[800000] # '20190201 16:19:50.787'

print(test_date)

n_values = 1258

MAX_LAG_NUMBER = config.ssa_params['MAX_LAG_NUMBER']
samples_to_predict = config.ssa_params['samples_to_predict']

# train_d = df.loc[(df.datetime <= test_date)]
# train_d = df['high']
# test_d = df.loc[(df.datetime > test_date)]
# test_d = test_d['high']

train_d = df['high'][:n_values]
test_d = df['high'][:n_values+n_values]
test_d = test_d.reindex(np.arange(n_values, 2*n_values))

plt.plot(train_d, label='Train')
plt.plot(test_d, 'r', label='Test')
# plt.title('%s adjusted daily close prices' % instrument)
plt.legend()
plt.show()

# train_d = low[:test_date]
# test_d = closes[test_date:]

# t = pd.to_datetime(df['datetime'])
# tt = pd.to_timedelta(t)
# tt = tt.dt.total_seconds()
# t = tt - tt[0]
# n = 60*60*24
#
# print(df.columns)
# # plt.plot(t/n, data['high'].values, t/n, data['low'].values)
# plt.plot(df['high'].values)
# plt.plot(df['low'].values)
# plt.show()

fig = plt.figure()
ssaview(train_d, MAX_LAG_NUMBER , [0,1,2,3])

pc, _, v = ssa(train_d, MAX_LAG_NUMBER )
reconstructed = inv_ssa(pc, v, [0,1,2,3])
noise = train_d - reconstructed
plt.hist(noise, 50)
plt.show()

n_co = ssa_cutoff_order(train_d, dim=MAX_LAG_NUMBER, show_plot=True)

forecast = ssa_predict(train_d.values, n_co, list(range(8)), samples_to_predict, 1e-5)

# prev_ser = closes[datetime.date.isoformat(parser.parse(test_date) - timedelta(120)):test_date]
# plt.plot(prev_ser, label='Train Data')

plt.plot(forecast, label='forecast')
plt.plot(test_d.values[:samples_to_predict], label='actual')
plt.legend()
plt.show()
print('The end')

# f_ser = pd.DataFrame(data=forecast, index=test_d.index[:samples_to_predict], columns=['close'])
# orig = pd.DataFrame(test_d[:samples_to_predict])
#
# plt.plot(orig, label='Test Data')
# plt.plot(f_ser, 'r-', marker='.', label='Forecast')
# plt.legend()
# plt.title('Forecasting %s for %d days, MAPE = %.2f%%' % (instrument, days_to_predict, mape(f_ser, orig)))
# plt.show()
