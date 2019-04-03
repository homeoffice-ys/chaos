import matplotlib.pyplot as plt
import os
import pandas as pd

flnm = 'EURUSD-2019-02.csv'
data = pd.read_csv(os.path.join(r'C:\Users\Yochanan\Downloads\EURUSD-2019-02', flnm))

t = pd.to_datetime(data['datetime'])
tt = pd.to_timedelta(t)
tt = tt.dt.total_seconds()
# t0 = data['Seconds'].values[0]
t = tt - tt[0]
n = 60*60*24
# print(data['datetime'].values[0])
# print(data['datetime'].values[-1])
print(data.columns)
# plt.plot(t/n, data['high'].values, t/n, data['low'].values)
plt.plot(data['high'].values)
plt.plot(data['low'].values)
plt.show()
