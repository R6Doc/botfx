import MetaTrader5 as mt5 
import time
import datetime
import pandas as pd
from ordertick import rates

def buy1():
 while True: 
     if rates > 30:
            symbol=("EURUSD")
     
            lot = 0.1
            point = mt5.symbol_info(symbol).point
            price = mt5.symbol_info_tick(symbol).ask
            deviation = 20
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": lot,
                "type": mt5.ORDER_TYPE_BUY,
                "price": price,
                "tp": price + 80 * point,
                "deviation": deviation,
                "magic": 234000,
                "comment": "python script open",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_RETURN,
            }
buy1()

