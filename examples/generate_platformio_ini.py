"""
Script to generate the PlatformIO configuration for Arduino-based PLCs.
The generated configuration file is saved in the same location from
which the script is called.
"""

import os
from os import path
from itertools import chain

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
BOARDS_DIRECTORY = os.path.join(SCRIPT_DIRECTORY, "../boards/")

# base content of the PlatformIO configuration file
BASE_PLATFORMIO_INI = \
"""
; PlatformIO Project Configuration File
;
;   Build options: build flags, source filter, extra scripting
;   Upload options: custom port, speed and extra flags
;   Library options: dependencies, extra library storages
;
; Please visit documentation for the other options and examples
; https://docs.platformio.org/page/projectconf.html

[env]
platform_packages =
   framework-industrialshields-avr@http://localhost:8000/avr.tar.bz2

"""

# Base content of a generic environment for Arduino-based boards
BASE_ENV = \
"""
[env:{}]
platform = https://github.com/Industrial-Shields/platform-industrialshields-avr
framework = arduino
board = {}
"""



def separate_if_discriminator(strings_list: list[str, ...], discriminator: str) \
        -> (list[str, ...], list[str, ...]):
    """
    Separates a list of strings based on the presence of a discriminator.

    Args:
        strings_list (list): List of strings to be separated.
        discriminator (str): Discriminator string for separation.

    Returns:
        tuple: Two lists, one containing strings with the discriminator, and the other without.
    """
    complying_boards_names, noncomplying_boards_names = [], []

    for board in strings_list:
        if discriminator in board:
            complying_boards_names.append(board)
        else:
            noncomplying_boards_names.append(board)

    return complying_boards_names, noncomplying_boards_names



# Generate a list of board names by removing ".json" extension from files in the boards directory
boards_names = [f.replace(".json", "") for f in os.listdir(BOARDS_DIRECTORY)
                if path.isfile(path.join(BOARDS_DIRECTORY, f))]


# Separate boards that have the character '+' in its name
mduinoplus_boards, leftover_boards_names = separate_if_discriminator(boards_names, '+')

# Separate boards that have the string "hfplus" in its name
ardboxhfplus_boards, leftover_boards_names = \
    separate_if_discriminator(leftover_boards_names, "hfplus")


# Write the PlatformIO configuration to a new file
with open("platformio.ini", 'w', encoding="utf-8") as new_file:

    new_file.write(BASE_PLATFORMIO_INI)

    for board_name in chain(mduinoplus_boards, ardboxhfplus_boards, leftover_boards_names):
        # PlatformIO doesn't support '+' characters in an environment name.
        env_name = board_name.replace('+', "plus")

        new_file.write(BASE_ENV.format(env_name, board_name))
