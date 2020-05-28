import ordertick
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

def startbot1():
    print(" ")
    print("\n                           1. Show Tick Rates                                                                       2. Real Time Price                            ")
    print(" ")
    print("                             3. Start Buy                                                                             4.  Start Sell                               ")
    print(" ")
    print("                                                                                                                                                                       \n")
    print("  ")
    print("  ")
    a = input("                                                           Press Any Number:  ")
    
    if a == "1":
        print(        "Loading...")
        print(" ")
        time.sleep(2)
        ordertick.ordertick()
        ordertick.extract()

    if a == "2":
        print("        Loading...")
        print(" ")
        time.sleep(2)
        ordertick.ordertick()
        ordertick.rates()
        
    if a == "3":
        print("        Loading...")
        print(" ")
        time.sleep(2)
        functions.buy1()
    
    if a == "4":
        print("         Loading...")
        print(" ")
        time.sleep(2)
        functions.sell1()
    startbot1()

startbot()
startbot1()