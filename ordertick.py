import MetaTrader5 as mt5
import datetime
import time
import pandas as pd 
import pytz

def ordertick():
    print ("Metatrader5 Package Autor",mt5.__author__)
    print ("Metatrader5 Package Version",mt5.__version__)
    print ("Autors of the bot: Machineblock and R6Doc")
    print ("Bot version 0.01")

    if not mt5.initialize():
        print("initialize() failed, error code =",mt5.last_error())

    print(mt5.version())    
    times = datetime.datetime.now()
    account=28896895
    authorized=mt5.login(account, password="xzrtv8do")
    if authorized:
        # display trading account data 'as is'
        print(mt5.account_info())
        # display trading account data in the form of a list
        print("Show account_info()._asdict():")
        account_info_dict = mt5.account_info()._asdict()
        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))
    else:
        print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

def extract():
    while True: 
     selected= mt5.symbol_select("EURUSD",True)
     symbol_info = mt5.symbol_info_tick("EURUSD")
  
     
     times = datetime.datetime.now()
     if symbol_info:
        print(symbol_info)
        time.sleep(2)

def rates():
   while True:
     rate= mt5.copy_rates_from_pos("EURUSD",mt5.TIMEFRAME_M5, 0, 1)
     
     times= datetime.datetime.now()
     if rate:
        print(rate)
        time.sleep(2)