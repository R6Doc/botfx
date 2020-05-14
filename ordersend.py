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
account=27865035
authorized=mt5.login(account)  # the terminal database password is applied if connection data is set to be remembered
if authorized:
    print("connected to account #27865035".format(account))
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
 
# prepare the buy request structure
symbol = "EURUSD"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "not found, can not call order_check()")
    mt5.shutdown()
    quit()
 
# if the symbol is unavailable in MarketWatch, add it
if not symbol_info.visible:
    print(symbol, "is not visible, trying to switch on")
    if not mt5.symbol_select(symbol,True):
        print("symbol_select(EURUSD) failed, exit",symbol)
        mt5.shutdown()
        quit()
 
lot = 0.01
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask
deviation = 20
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price - 74 * point,
    "tp": price + 84 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}
 
# send a trading request
result = mt5.order_send(request)
# check the execution result
print("1. order_send(): by botfx in eurusd lots at 0.01 with deviation=20 points".format(symbol,lot,price,deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send failed, retcode=".format(result.retcode))
    # request the result as a dictionary and display it element by element
    result_dict=result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field,result_dict[field]))
        # if this is a trading request structure, display it element by element as well
        if field=="request":
            traderequest_dict=result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
    print("shutdown() and quit")
    mt5.shutdown()
    quit()
 
print("2. order_send done, ", result)
print("   opened position with POSITION_TICKET={}".format(result.order))
print("   sleep 2 seconds before closing position #{}".format(result.order))
time.sleep(2)
# create a close request
position_id=result.order
price=mt5.symbol_info_tick(symbol).bid
deviation=20
request={
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "position": position_id,
    "price": price,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script close",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}
# send a trading request
result=mt5.order_send(request)
# check the execution result
print("3. close position #{}: sell {} {} lots at {} with deviation={} points".format(position_id,symbol,lot,price,deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("4. order_send failed, retcode={}".format(result.retcode))
    print("   result",result)
else:
    print("4. position #{} closed, {}".format(position_id,result))
    # request the result as a dictionary and display it element by element
    result_dict=result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field,result_dict[field]))
        # if this is a trading request structure, display it element by element as well
        if field=="request":
            traderequest_dict=result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))
 

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()