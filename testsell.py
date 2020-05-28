import MetaTrader5 as mt5
import time

# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()
 
# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())

info = mt5.terminal_info()
if info.trade_allowed == False:
    print( "Auto-trading disabled in Terminal, enable it" )
    quit()

symbol = "XAUUSD"       # set to whatever symbol or currency
lot = 0.01              # buy/sell lot
slminprofit = 20 * lot  # number pips * lotsize


positions=mt5.positions_get(symbol=symbol)
    if positions==None:
        print("No positions, error code={}".format(mt5.last_error()))
    if len(positions)>0:
        print("Total positions on", symbol,":",len(positions))
        # display all active orders
        for position in positions:
            if position.type == 0:
                ptype = "Buy"
            elif position.type == 1:
                ptype = "Sell"
            print("id:", position.identifier, ptype, position.profit, position.ORDER_VOLUME_CURRENT)

            
            #stoploss
            position_id=position.identifier
            if position.type == 1 and position.profit > slminprofit: #if ordertype sell 
                request={
                    "action": mt5.TRADE_ACTION_SLTP,
                    "position": position_id,
                    "sl": v_ask - 100 * lot,
                    "comment": "python trailing sl",
                    "deviation": 20,
                    "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_RETURN,
                    "volume": position.ORDER_VOLUME_CURRENT
                }
                # send a trading request
                result=mt5.order_send(request)
                # check the execution result
                print("3. SL SELL update sent on position #{}: {} {} lots".format(position_id,symbol,lot));
                if result.retcode != mt5.TRADE_RETCODE_DONE:
                    print("4. order_send failed, retcode={}".format(result.retcode))
                    print("   result",result)
                else:
                    print("4. position #{} SL Updated, {}".format(position_id,result))
            elif position.type == 0 and position.profit > slminprofit: #if ordertype buy 
                request={
                    "action": mt5.TRADE_ACTION_SLTP,
                    "position": position_id,
                    "sl": v_bid + 100 * lot,
                    "comment": "python trailing sl",
                    "deviation": 20,
                    "type_time": mt5.ORDER_TIME_GTC,
                    "type_filling": mt5.ORDER_FILLING_RETURN,
                    "volume": position.ORDER_VOLUME_CURRENT
                }
                # send a trading request
                result=mt5.order_send(request)
                # check the execution result
                print("3. SL BUY update sent on position #{}: {} {} lots".format(position_id,symbol,lot));
                if result.retcode != mt5.TRADE_RETCODE_DONE:
                    print("4. order_send failed, retcode={}".format(result.retcode))
                    print("   result",result)
                else:
                    print("4. position #{} SL Updated, {}".format(position_id,result))
            
    else:
        print("Positions on", symbol,"not found.")