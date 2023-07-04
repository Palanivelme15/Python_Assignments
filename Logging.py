import logging
from logging import *

# logging.basicConfig(level=logging.WARNING)
#
#
# def addition(a, b):
#     logging.warning(f"variables are {a} and {b}.")
#     return a + b
#
#
# print(addition(12, 12))
#
# logging.basicConfig(level=logging.INFO)
#
# def login_details(username):
#     logging.info(f"{username}  is logged in.")
#
# login_details("palanivel")

# logging.basicConfig(level=logging.WARNING)
#
#
# def BalanceCheck(amount):
#     if amount < 500:
#         logging.warning(f"Amount is {amount}. You should maintain balance equal or above 500.")
#
#
# BalanceCheck(350)

#
# import os
#
# print(os.getcwd())




import os
import logging

# Specify the directory and file
dir_path = r'C:\Users\HP\PycharmProjects\exception'
log_file = 'system.txt'
full_path = os.path.join(dir_path, log_file)

# Check if the directory exists and create it if necessary
os.makedirs(dir_path, exist_ok=True)

# Set up logging
# Get a logger instance (this will fetch the root logger)
logger = logging.getLogger()

# Set the level of the logger to CRITICAL
# This means it will handle events of level CRITICAL and above
logger.setLevel(logging.CRITICAL)

# Create a FileHandler instance to write logs to a file
handler = logging.FileHandler(full_path)

# Set the format of the logs using a Formatter
# This format includes the log timestamp, log level and log message
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))

# Add the handler to the logger
# This connects the logger to the handler so that logs get written to the file
# logger.addHandler(handler)
#
#
# def LetUsCheckSystem(sys):
#     if sys != 'OK':
#         logging.critical('System failure: %s', sys)
#
# LetUsCheckSystem('You need to handle the issue now')
# handler.close()

















