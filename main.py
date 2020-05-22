import ordertick
import ordersend
import MetaTrader5 as mt5
import datetime
import time
import pandas as pd 
import pytz
import buy

def startbot():
    print("\n================================================================================================================================================================")
    print ("\n                            Metatrader5 Package Autor",mt5.__author__)
    print ("                                 Metatrader5 Package Version",mt5.__version__)
    print ("                                Autors of the bot: Machineblock and R6Doc")
    print ("                                       Bot version 0.01\n")
    print("==================================================================================================================================================================")
    time.sleep(2)
    
    print("\n                           1. Show Tick Rates                                                                       2. Real Time Price                            ")
    print(" ")
    print("                             3. OrderSend                                                                               4.  Coming Soon                               ")
    print(" ")
    print("                             5. Star buy bot                                                                                                                                            \n")
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
        print("Coming Soon")
    
    if a== "5":
        print(        "aprende a descargar office...")
        time.sleep(5)
        print(         "Ya aprendió?")
        time.sleep(5)
        print(           "muyyyyyy bien, procedamos")
        time.sleep(2)
        buy.buy1()


startbot()