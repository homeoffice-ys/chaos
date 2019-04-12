import matplotlib.pyplot as plt
import os
import pandas as pd
import quandl
from ssa_core import ssa, ssa_predict, ssaview, inv_ssa, ssa_cutoff_order


filename = 'EURUSD-2019-02.csv'
full_path = r'C:\Users\Yochanan\Documents\Data\EURUSD'


# yrd

df = pd.read_csv(os.path.join(full_path, filename))
print(df.columns)

# highs = df['datetime'].between('20190201','20190202')
# plt.plot(df['high'].values[highs])

test_date = df['datetime'].values[800000] # '20190201 16:19:50.787'

print(test_date)

nvalues = 1258

train_d = df.loc[(df.datetime <= test_date)]
train_d = df['high']
test_d = df.loc[(df.datetime > test_date)]
test_d = test_d['high']

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
ssaview(train_d, 120, [0,1,2,3])

pc, _, v = ssa(train_d, 120)
reconstructed = inv_ssa(pc, v, [0,1,2,3])
noise = train_d - reconstructed
plt.hist(noise, 50)
plt.show()

pc, _, v = ssa(train_d, 120)
reconstructed = inv_ssa(pc, v, [0,1,2,3])
noise = train_d - reconstructed
plt.hist(noise, 50)
plt.show()

MAX_LAG_NUMBER = 120 # 4*30 = 1 quarter max
n_co = ssa_cutoff_order(train_d, dim=MAX_LAG_NUMBER, show_plot=True)

MAX_LAG_NUMBER = 120 # 4*30 = 1 quarter max
n_co = ssa_cutoff_order(train_d, dim=MAX_LAG_NUMBER, show_plot=True)


days_to_predict = 15
forecast = ssa_predict(train_d, n_co, list(range(8)), days_to_predict, 1e-5)

prev_ser = closes[datetime.date.isoformat(parser.parse(test_date) - timedelta(120)):test_date]
plt.plot(prev_ser, label='Train Data')

test_d = closes[test_date:]
f_ser = pd.DataFrame(data=forecast, index=test_d.index[:days_to_predict], columns=['close'])
orig = pd.DataFrame(test_d[:days_to_predict])

plt.plot(orig, label='Test Data')
plt.plot(f_ser, 'r-', marker='.', label='Forecast')
plt.legend()
plt.title('Forecasting %s for %d days, MAPE = %.2f%%' % (instrument, days_to_predict, mape(f_ser, orig)))
plt.show()