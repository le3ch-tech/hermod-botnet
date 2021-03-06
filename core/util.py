import datetime

from pyfiglet import Figlet
from src.colors import BColors

def print_banner(text):
	print(BColors.RED + Figlet(font='banner3-D').renderText(text))

def print_spacer():
	print(BColors.WHITE + "\n\n :::..:::::..::::::::..:::::..::..:::::..::..:::::..::........:.\n")

# Print Info Function Lambda
print_info = lambda info_string:\
	print("{}{}[INFO]  {}{}".format(timestamp(), BColors.PURPLE, BColors.WHITE, info_string))

# Print Error Function Lambda
print_error = lambda err_string:print("{}{}[ERROR] {}".format(timestamp(), BColors.RED, err_string))

# Return Timestamp
def timestamp():
	x = datetime.datetime.now()
	return x.strftime('{}[%d.%m.%y %H:%M:%S]'.format(BColors.PURPLE))