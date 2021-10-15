import os as o
from time import sleep

def osname():
    if o.name == 'nt':
        return 'pip install typing'
    else:
        return 'python3 -m pip install typing'

try:
    import typing
except ModuleNotFoundError:
    try:
        if o.name == "nt":
            o.system('pip install typing')
        else:
            o.system('python3 -m pip install typing')
    except:
        print(f'ERROR: {osname()}')
        sleep(2)
        exit()

print('BOT: Typing Installed!')
if o.name == 'nt':
    o.system('python ../../hermod.py')
else:
    try:
        o.system('python3 ../../hermod.py')
    except:
        o.system('python ../../hermod.py')