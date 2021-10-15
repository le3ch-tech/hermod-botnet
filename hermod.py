import os
import json

command = lambda x: os.system(x)
command('clear')

def check_config():
    try:
        config_file = open('core/config/config.json')
        config = json.load(config_file)

        if config['quickstart']:
            os.system('python3 core/server.py')
        elif not config['quickstart']:
            return print('CONFIG: Quickstart: -> false\n')
    except FileNotFoundError:
        print('CONFIG: Not found, Installed Correctly?')
        exit()
    except json.decoder.JSONDecodeError as err:
        print("Unable to read JSON File:\n" + format(err))
        exit()
    except KeyError:
        pass

if __name__ == "__main__":

    try:
        check_config()

        print('1) Install Dependecies\n')
        print('2) Launch Server      \n')

        choice = input('Please select: ->  [1, 2, ...] : ')
        if choice == '1':
            os.system('python3 core/src/dependencies.py')
        elif choice == '2':
            os.system('python3 core/server.py')
        else:
            print(f'Invalid Input: {choice}')
            os.system('python3 hermod.py')
    
    except KeyboardInterrupt:
        print("\nProgram closed by user (CTRL+C)\n")
        exit()