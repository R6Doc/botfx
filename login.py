import MetaTrader5 as mt5
import pandas as pd
from MetaTrader5._core import terminal_info

# display data on the metatrader5 package

print ("Metatrader5 Package Autor",mt5.__author__)
print ("Metatrader5 Package Version",mt5.__version__)
print ("Autors of the bot: Machineblock and R6Doc")
print ("Bot version 0.01")

# establish connection to the MetaTrader 5 terminal
if not mt5.initialize(login=27865035, server="MetaQuotesDemo",password="vlnp3nkt"):
    print("initialize() failed, error code =",mt5.last_error())
    

# display data on MetaTrader 5 version
print(mt5.version())
# connect to the trade account without specifying a password and a server
account=27865035
authorized=mt5.login(account,password="vlnp3nkt")  # the terminal database password is applied if connection data is set to be remembered
if authorized:
    print("connected to account #{}".format(account))
else:
    print("failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))
 
# now connect to another trading account specifying the password

 
# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()