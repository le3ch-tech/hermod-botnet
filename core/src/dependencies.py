import os
import subprocess

def check():
    os.system('clear')

    try:
        from colors import BColors
    except ModuleNotFoundError:
        print('core/src/colors.py missing. Did you install this program correctly?')
        exit()
    except ImportError:
        print('core/src/colors.py exists, but is corrupted. Did you install this program correctly?')

    try: 
        import pyfiglet
    except ModuleNotFoundError:
        if os.name != 'nt':
            os.system('python3 -m pip install pyfiglet==0.7')
        else:
            print('This program is not ment for Windows. ...Closing')
            exit()
    
    try:
        import time 
        import sys
    except ModuleNotFoundError:
        print("Some Modules are not correctly installed.\n time;sys")
        dwnl = input('Want to install now? [y/n]')
        if dwnl == "y" or dwnl == 'Y':
            if os.name != 'nt':
                os.system('apt install python3')
                os.system("python3 -m pip install time")
                os.system("python3 -m pip install sys")
                check()
            else:
                print('This program is not ment for Windows. ...Closing')
                exit()
        else:
            exit()
    
    try:
        import typing
    except ModuleNotFoundError:
        if os.name != 'nt':
            os.system('python3 -m pip install typing')
            check()
        else:
            print('This program is not ment for Windows. ...Closing')
            exit()

def menue():
    print("Modules correctly installed. Restart Menue?")
    start = input("[y/n]")
    if start == "y" or start == "Y":
        os.system("python3 hermod.py")

if __name__ == '__main__':
    try:
        check() # check dep
        menue() # start menue
    except KeyboardInterrupt:
        print("\nProgram closed by user (CTRL+C)")
        exit()