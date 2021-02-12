from os import close, write

from numpy.core.numeric import NaN
from numpy.lib.shape_base import column_stack
from pandas.core.frame import DataFrame
#from settings import Settings
from config import parse_config,_parse_args
from starter import Starter, Buffer
from trader import create_trader
from signaler import Signal
import iqoptionapi.constants as api_constants
#import logging
import time
from datetime import datetime,timezone,timedelta
from pprint import pprint
from frame_dance import Robot

from patterns.curve_fit import CURVE_FIT
args = _parse_args()
config = parse_config(args.config_path)

a = config.get_connection_username()
print(a)
#logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(message)s')

be = Starter(config)
check, reason = be.create_connection()
print(check, reason)
be.api.change_balance('REAL')
print("REAL balance: ", be.api.get_balance())

print(be.change_balance_mode(config.get_balance_mode()))

print(be.api.check_connect())

#actives = be.check_open_markets()

traders = be.start_traders()

price_d = be.start_data_frame()

price_df = price_d.frame
df = price_df.frame

#with open("dataframe.txt",'a') as f:
    #f.write(df.to_string())

import pandas as pd
from matplotlib import pyplot
from numpy import arange
import numpy as np
from scipy.optimize import curve_fit
from patterns.bollinger_rsi import BOLLINGER_RSI

test = BOLLINGER_RSI('EURGBP-OTC', price_d.frame.frame.loc['EURGBP-OTC'])

tail = test._frame_
print(test.call())
print(test.put())
c = test._frame_['v10']
b = test._frame_['close']
print(b)
print(c)
#print(CURVE_FIT.ma_future_cross())

#print(test.candles_direction())
"""
d = np.array([-1,2,-3,4,-5])
e = d[d>0]
print(e)


x_real = tail.index.values
x = np.arange(1, len(x_real)+1, 1)
y=tail['rsi14'].values
z=tail['band_lower'].values
x_close = tail.loc[:,'close'].values



o = np.polyfit(x,y,3)
f = np.poly1d(o)

m = np.polyfit(x,z,3)
n = np.poly1d(m)

x_new = np.linspace(x[0],x[-1],50)
y_new = f(x_new)
z_new = n(x_new)


g = f - n
x_bounds = np.linspace(x[-2],x[-1]+1,100)
idx = np.argwhere(np.diff(np.sign(g(x_bounds))))
#pyplot.plot(x[idx], f[idx], 'ro')
print(idx)
print(x_bounds[idx],f(x_bounds[idx]),g(x_bounds[idx]))
pyplot.plot(x_new, z_new,'b--')
pyplot.plot(x_new, y_new,'g--')
"""


pyplot.figure()
pyplot.plot(b)
pyplot.figure()

pyplot.plot(c)
#pyplot.plot(x, x_close)
pyplot.ylim(0,0.009)
pyplot.show()



"""
print(be.api.get_all_profit()['EURUSD']['turbo'])
"""
