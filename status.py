import ordersend

def status():
    print ("Metatrader5 Package Autor",mt5.__author__)
    print ("Metatrader5 Package Version",mt5.__version__)
    print ("Autors of the bot: Machineblock and R6Doc")
    print ("Bot version 0.01")
 
    print("Importing Modules")
    print("....")

    print("Ready to run, Press any key to continue")
    a = input("confirmation")
    if a:
        ordersend();