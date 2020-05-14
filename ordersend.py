import time
import MetaTrader5 as mt5
import pandas as pd

# display data on the metatrader5 package

print ("Metatrader5 Package Autor",mt5.__author__)
print ("Metatrader5 Package Version",mt5.__version__)
print ("Autors of the bot: Machineblock and R6Doc")
print ("Bot version 0.01")

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    
# get account currency
account_currency=mt5.account_info().currency
print("Account сurrency:",account_currency)
# arrange the symbol list
symbols=("EURUSD")
print("Symbols to check margin:", symbols)
action=mt5.ORDER_TYPE_BUY
lot=0.01
for symbol in symbols:
    symbol_info=mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol,"not found, skipped")
        continue
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol,True):
            print("symbol_select({}}) failed, skipped",symbol)
            continue
    ask=mt5.symbol_info_tick(symbol).ask
    margin=mt5.order_calc_margin(action,symbol,lot,ask)
    if margin != None:
        print("   {} buy {} lot margin: {} {}".format(symbol,lot,margin,account_currency));
    else:
        print("order_calc_margin failed: , error code =", mt5.last_error())




# display data on MetaTrader 5 version
print(mt5.version())
# connect to the trade account without specifying a password and a server
account=28896895
authorized=mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered
if authorized:
    print("connected to account #28896895".format(account))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
 
# now connect to another trading account specifying the password
account=28896895
authorized=mt5.login(account, password="xzrtv8do")
if authorized:
    # display trading account data 'as is'
    print(mt5.account_info())
    # display trading account data in the form of a list
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("".format(prop, account_info_dict[prop]))
else:
    print("failed to connect at account #28896895, error code:".format(account, mt5.last_error()))
 
