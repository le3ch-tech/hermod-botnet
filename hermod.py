import os
from time import sleep

print('-> 1) Install Dependecies')
print('~~~~~~~~~~~~~~~~~~~~~~~~~')
print('-> 2) Launch Bot         ')

choice = input('Please select: ->  [1, 2, ...] : ')
if choice == 1:
    os.system('python3 core/src/dependencies.py')
elif choice == 2:
    sleep(1)
    os.system('python3 core/server.py')