import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import datetime
import MetaTrader5 as mt5
import ta
import sys,os
import traceback
while True:
    os.system('cls')
    nem = input('nemad ra vared konid : ')
    if nem=='ض':break
    if not mt5.initialize():
        print("initialize() failed")
    period=50
    shakhes = mt5.copy_rates_from("شاخص کل6", mt5.TIMEFRAME_D1, datetime.now(), period)
    lw=9
    try:
        if nem[-1]=='ح':
            print('hagh taghadom\n\n############################################################\n\n')
            input()
            continue
        
        nemad = mt5.copy_rates_from(nem, mt5.TIMEFRAME_D1, datetime.now(), period)
        df = pd.DataFrame(nemad)
        print(df)
        if (list(df.columns)==[]):
            print(nem,'server err\n\n###########################################################\n\n')
            
        ds = pd.DataFrame(shakhes)
        
        df['time'] = pd.to_datetime(df['time'], unit='s')
        dfp = df["close"]
        dsp = ds["close"]        
        div=list(ta.trend.ema(dsp,lw,True).divide(ta.trend.ema(dfp,lw,True)))
        n = list(dfp)
        s = list(dsp)
        sx = [s[i]/div[i] for i in range(len(s))]
        print(nem,'\ndone\n\n')
        plt.figure(figsize=(9, 3))
        plt.plot(df['time'], n)
        plt.plot(df['time'], sx)
        plt.suptitle(nem)
        plt.show()
    except Exception as err:
        print(nem,traceback.print_exc())
        print('\n\n#############################################################################################################\n\n\n\n')
        input()
mt5.shutdown()
    
    

