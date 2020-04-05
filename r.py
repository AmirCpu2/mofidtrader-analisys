import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime
import MetaTrader5 as mt5
import ta
import sys
while True:
    
        
    nem=input('nemad ra vared konid : ')
    if not mt5.initialize():
        print("initialize() failed")
    period=50
    shakhes = mt5.copy_rates_from("شاخص کل6", mt5.TIMEFRAME_D1, datetime.now(), period)
    nemad = mt5.copy_rates_from(nem, mt5.TIMEFRAME_D1, datetime.now(), period)
    mt5.shutdown()
    df = pd.DataFrame(nemad)
    ds = pd.DataFrame(shakhes)
    print(nem,list(df.columns))
    df['time'] = pd.to_datetime(df['time'], unit='s')
    dfp = df["close"]
    dsp = ds["close"]
    