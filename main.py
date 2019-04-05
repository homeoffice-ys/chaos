import matplotlib.pyplot as plt
import os
import pandas as pd

filename = 'EURUSD-2019-02.csv'
full_path = r'C:\Users\Yochanan\Documents\Data\EURUSD'

df = pd.read_csv(os.path.join(full_path, filename))
print(df.columns)

test_date = df['datetime'].values[200000] # '20190201 16:19:50.787'
print(test_date)

train_d = df.loc[(df.datetime <= test_date)]
train_d = train_d['high']
test_d = df.loc[(df.datetime > test_date)]
test_d = test_d['high']

plt.plot(train_d, label='Train')
plt.plot(test_d, 'r', label='Test')
# plt.title('%s adjusted daily close prices' % instrument)
plt.legend()
plt.show()

# train_d = low[:test_date]
# test_d = closes[test_date:]

t = pd.to_datetime(df['datetime'])
tt = pd.to_timedelta(t)
tt = tt.dt.total_seconds()
t = tt - tt[0]
n = 60*60*24

print(data.columns)
# plt.plot(t/n, data['high'].values, t/n, data['low'].values)
plt.plot(data['high'].values)
plt.plot(data['low'].values)
plt.show()
