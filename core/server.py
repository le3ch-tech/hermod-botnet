import socket
import os
import time
import pyfiglet

import util
from src.colors import BColors
from src.dependencies import *

command = lambda x: os.system(x)
refresh = lambda x: os.system('python3 core/' + x)
command('clear')

def menue(title):
    util.print_banner(title)
    print(BColors.RED + '\n                              BOTNET')
    print(BColors.WHITE + '\n                        Written by ' + BColors.RED + 'DAEM0N\n')
    util.print_spacer()

if __name__ == '__main__':
    menue('HERMOD')
    
    while True:

        try:
            input = input(BColors.RED + ">>" + BColors.WHITE + " ")

            if input == 'ping':
                print('pinged')
                time.sleep(0.5)
            elif input == '2':
                print('2')
            else:
                print('Invalid Syntax!')
                time.sleep(0.5)
                refresh('server.py')

        except KeyboardInterrupt:
            print("\nProgram closed by user (CTRL+C)\n")
            exit()