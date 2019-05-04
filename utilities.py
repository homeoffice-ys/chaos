import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


def cool_plot(df):

    spread = df['high'] - df['low']
    dated = df['datetime']
    date = pd.to_datetime(dated)
    fig, ax1 = plt.subplots()
    ax1.plot(date, df['high'])
    ax1.plot(date, df['low'])
    plt.gca().get_yaxis().get_major_formatter().set_useOffset(False)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.locator_params(nbins=30, axis='x')

    max_xticks = 30
    xloc = plt.MaxNLocator(max_xticks)
    ax1.xaxis.set_major_locator(xloc)

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    # ax1_2 = ax1.twinx()
    # ax1_2.xaxis.set_major_locator(xloc)
    # ax1_2.fill_between(date, 0, spread,  interpolate=True, facecolor='g', alpha=.3)
    plt.grid(True)
    plt.subplots_adjust(bottom=.2)
    plt.show()


def configurations():

    config = {'window': 10,
              'stride': 1}
    
    return config


class RunningStats:

    def __init__(self):
        self.n = 0
        self.old_m = 0
        self.new_m = 0
        self.old_s = 0
        self.new_s = 0
        self.old_val = 0
        self.new_val = 0
        self.cum_val = 0

    def clear(self):
        self.n = 0

    def push(self, x):
        self.n += 1

        if self.n == 1:
            self.old_m = self.new_m = x
            self.old_s = 0
            self.new_val = x
            self.old_val = 0
        else:
            self.new_m = self.old_m + (x - self.old_m) / self.n
            self.new_s = self.old_s + (x - self.old_m) * (x - self.new_m)

            self.old_m = self.new_m
            self.old_s = self.new_s
            self.cum_val = self.delta() + (x - self.old_val)
            self.old_val = self.new_val
            self.new_val = x

    def mean(self):
        return self.new_m if self.n else 0.0

    def variance(self):
        return self.new_s / (self.n - 1) if self.n > 1 else 0.0

    def standard_deviation(self):
        return math.sqrt(self.variance())

    def delta(self):
        return self.new_val - self.old_val if self.n > 1 else 0.0




