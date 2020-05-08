import MetaTrader5 as mt5
import pandas as pd
from MetaTrader5._core import terminal_info

# display data on the metatrader5 package

print ("metatrader5 package autor",mt5.__author__)
print ("metatrader5 package version",mt5.__version__)
print ("autors of the bot: Machine block and R6Doc")
print ("bot version 1.0")

# establish MetaTrader 5 connection to a specified trading account

if mt5.initialize(login=27865035, server="MetaQuotes-Demo",password="vlnp3nkt"):
    print("initialize failed error code =",mt5.last_error())
   

# display data on metatrader5
print(mt5.version())
 
# display info on the terminal settings and status
if terminal_info != None:

   print(terminal_info)
terminal_info=mt5.terminal_info()
if terminal_info!=None:
    # display the terminal data 'as is'
    print(terminal_info)
    # display data in the form of a list
    print("Show terminal_info()._asdict():")
    terminal_info_dict = mt5.terminal_info()._asdict()
    for prop in terminal_info_dict:
        print("  {}={}".format(prop, terminal_info_dict[prop]))
    print()
   # convert the dictionary into DataFrame and print
    df=pd.DataFrame(list(terminal_info_dict.items()),columns=['property','value'])
    print("terminal_info() as dataframe:")
    print(df)
 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()




