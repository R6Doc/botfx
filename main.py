import ordertick
import ordersend
import MetaTrader5 as mt5
import datetime
import time
import pandas as pd 
import pytz
import functions

def startbot():
    print("\n===========================================================================================================================================================================")
    print ("\n                            Metatrader5 Package Autor",mt5.__author__)
    print ("                                 Metatrader5 Package Version",mt5.__version__)
    print ("                                Autors of the bot: Machineblock and R6Doc")
    print ("                                       Bot version 0.01\n")
    print("=============================================================================================================================================================================")
    time.sleep(2)
    
    print("\n                           1. Show Tick Rates                                                                       2. Real Time Price                            ")
    print(" ")
    print("                             3. OrderSend                                                                             4.  Start Sell                               ")
    print(" ")
    print("                             5. Start Buy                                                                                                                                            \n")
    a = input("                                                           Press Any Number:  ")
    
    if a == "1":
        print(        "Loading...")
        time.sleep(2)
        ordertick.ordertick()
        ordertick.extract()

    if a == "2":
        print("        Loading...")
        time.sleep(2)
        ordertick.ordertick()
        ordertick.rates()
        
    if a == "3":
        print("        Loading...")
        time.sleep(2)
        ordersend.ordersend()
    
    if a == "4":
        print("         Loading...")
        time.sleep(2)
        functions.sell1()
    if a== "5":
        print("        Loading...")
        time.sleep(2)
        functions.buy1()


startbot()