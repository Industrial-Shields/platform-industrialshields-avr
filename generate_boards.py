"""
Copyright (c) 2023 Boot&Work Corp., S.L. All rights reserved

This file is part of platform-industrialshields-avr.

platform-industrialshields-avr is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

platform-industrialshields-avr is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


PLC Configuration Generator

This script generates all the configuration files that PlatformIO
needs for all the Industrial Shields PLCs based on Arduino boards.
"""
from json_generator import JSON_PLC
import os
from itertools import chain



SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
BOARDS_DIRECTORY = os.path.join(SCRIPT_DIRECTORY, "boards/")


mega_basejson = """
{
    "build": {
	"core": "industrialshields",
	"extra_flags": "-DARDUINO_AVR_MEGA2560",
	"f_cpu": "16000000L",
        "hwids": [
            [
		"0x2341",
		"0x0042"
            ]
        ],
	"mcu": "atmega2560",
	"variant": "mega"
    },
    "bootloader": {
	"efuse": "0xFD",
	"file": "stk500v2/stk500boot_v2_mega2560.hex",
	"hfuse": "0xD8",
	"lock_bits": "0x0F",
	"lfuse": "0xFF",
	"unlock_bits": "0x3F"
    },
    "frameworks": [
	"arduino"
    ],
    "name": "",
    "upload": {
	"maximum_ram_size": 8192,
	"maximum_size": 253952,
	"protocol": "wiring",
	"require_upload_port": true,
	"speed": 115200
    },
    "url": "",
    "vendor": "Industrial Shields"
}
"""


def M(file_name: str, name: str, variant: str, extra_flags: str, url: str) \
        -> JSON_PLC:
    """
    Create a JSON_PLC instance for Arduino Mega based PLCs.
    """
    return JSON_PLC(file_name, name, variant, extra_flags, url, mega_basejson)


mduino_plcs = [M("mduinoplc_19r", "M-Duino PLC 19R", "mduinorelay", "-DMDUINO -DMDUINO_19R", "NOURL"),
               M("mduinoplc_21", "M-Duino PLC 21", "mduino", "-DMDUINO -DMDUINO_21", "NOURL"),
               M("mduinoplc_38r", "M-Duino PLC 38R", "mduinorelay", "-DMDUINO -DMDUINO_38R", "NOURL"),
               M("mduinoplc_42", "M-Duino PLC 42", "mduino", "-DMDUINO -DMDUINO_42", "NOURL"),
               M("mduinoplc_57r", "M-Duino PLC 57R", "mduinorelay", "-DMDUINO -DMDUINO_57R", "NOURL"),
               M("mduinoplc_58", "M-Duino PLC 58", "mduino", "-DMDUINO -DMDUINO_58", "NOURL")]

mduinoplus_plcs = \
    [M("mduinoplc_19r+", "M-Duino PLC 19R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_19R_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-19r-8"),
     M("mduinoplc_21+", "M-Duino PLC 21+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_21_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-21-3670"),
     M("mduinoplc_38ar+", "M-Duino PLC 38AR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_38AR_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-38ar-12"),
     M("mduinoplc_38r+", "M-Duino PLC 38R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_38R_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-38r-10"),
     M("mduinoplc_42+", "M-Duino PLC 42+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_42_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-42-3667"),
     M("mduinoplc_50rra+", "M-Duino PLC 50RRA+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_50RRA_PLUS", "www.industrialshields.com/shop/is-mduino-50rra-m-duino-ethernet-plc-arduino-50rra-488"),
     M("mduinoplc_53arr+", "M-Duino PLC 53ARR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_53ARR_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-53arr-468"),
     M("mduinoplc_54ara+", "M-Duino PLC 54ARA+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_54ARA_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-54ara-688"),
     M("mduinoplc_57aar+", "M-Duino PLC 57AAR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_57AAR_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-57aar-436"),
     M("mduinoplc_57r+", "M-Duino PLC 57R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_57R_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-57r-13"),
     M("mduinoplc_58+", "M-Duino PLC 58+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_58_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-58-176")]



mduinoplus_dali_plcs = [plc.add_family_variants("_dali", " DALI", "-DMDUINO_DALI_PLUS", "SAMEURL")
                        for plc in mduinoplus_plcs]

mduinoplus_gprs_plcs = [plc.add_family_variants("_gprs", " GPRS", "-DMDUINO_GPRS_PLUS", "SAMEURL")
                        for plc in mduinoplus_plcs]

mduinoplus_lora_plcs = [plc.add_family_variants("_lora", " LoRa", "-DMDUINO_LORA_PLUS", "SAMEURL")
                    for plc in mduinoplus_plcs]

mduinoplus_wifi_plcs = [plc.add_family_variants("_wifi", " WiFi/BT", "-DMDUINO_WIFI_PLUS", "SAMEURL")
                        for plc in mduinoplus_plcs]

mduinoplus_wifi_gprs_plcs = [plc.add_family_variants("_wifi_gprs", " WiFi/BT + GPRS", "-DMDUINO_WIFI_GPRS_PLUS", "NOURL")
                             for plc in mduinoplus_plcs]


for plc in chain(mduino_plcs, mduinoplus_plcs, mduinoplus_dali_plcs, mduinoplus_gprs_plcs,
                 mduinoplus_lora_plcs, mduinoplus_wifi_plcs, mduinoplus_wifi_gprs_plcs):
    plc.generate_file(BOARDS_DIRECTORY)



leonardo_basejson = """
{
    "build": {
	"core": "industrialshields",
	"extra_flags": "",
	"f_cpu": "16000000L",
	"hwids": [
	    [
		"0x2341",
		"0x8036"
	    ],
	    [
		"0x2341",
		"0x0036"
	    ],
	    [
		"0x2A03",
		"0x0036"
	    ],
	    [
		"0x2A03",
		"0x8036"
	    ]
	],
	"mcu": "atmega32u4",
        "usb_product": "Arduino Leonardo",
	"variant": ""
    },
    "bootloader": {
	"efuse": "0xCB",
	"file": "caterina/Caterina-Leonardo.hex",
	"hfuse": "0xD8",
	"lock_bits": "0x2F",
	"lfuse": "0xFF",
	"unlock_bits": "0x3F"
    },
    "frameworks": [
	"arduino"
    ],
    "name": "",
    "upload": {
	"disable_flushing": true,
	"maximum_ram_size": 2560,
	"maximum_size": 28672,
	"protocol": "avr109",
	"require_upload_port": true,
	"speed": 57600,
	"use_1200bps_touch": true,
	"wait_for_upload_port": true
    },
    "url": "",
    "vendor": "Industrial Shields"
}
"""


def L(file_name: str, name: str, variant: str, extra_flags: str, url: str) \
        -> JSON_PLC:
    """
    Create a JSON_PLC instance for Arduino Leonardo based PLCs.
    """
    return JSON_PLC(file_name, name, variant, extra_flags, url, leonardo_basejson)


ardbox_plcs = [L("ardbox_analog", "Ardbox Analog", "ardboxanalog", "-DARDBOX -DARDBOX_ANALOG", "NOURL"),
               L("ardbox_analog_hf_rs232", "Ardbox Analog HF w/ HW RS-232", "ardboxanaloghf", "-DARDBOX_HF -DARDBOX_ANALOG_HF -DARDBOX_ANALOG_HF_RS232", "NOURL"),
               L("ardbox_analog_hf_rs485", "Ardbox Analog HF w/ HW RS-485", "ardboxanaloghf", "-DARDBOX_HF -DARDBOX_ANALOG_HF -DARDBOX_ANALOG_HF_RS485", "NOURL"),
               L("ardbox_analog_hf_legacy", "Ardbox Analog HF (legacy)", "ardboxanaloghf", "-DARDBOX_HF -DARDBOX_ANALOG_HF -DARDBOX_ANALOG_HF_LEGACY", "NOURL"),
               L("ardbox_relay", "Ardbox Relay", "ardboxrelay", "-DARDBOX -DARDBOX_RELAY", "NOURL"),
               L("ardbox_relay_hf_rs232", "Ardbox Relay HF w/ HW RS-232", "ardboxrelayhf", "-DARDBOX_HF -DARDBOX_RELAY_HF -DARDBOX_RELAY_HF_RS485", "NOURL"),
               L("ardbox_relay_hf_rs485", "Ardbox Relay HF w/ HW RS-485", "ardboxrelayhf", "-DARDBOX_HF -DARDBOX_RELAY_HF -DARDBOX_RELAY_HF_RS485", "NOURL"),
               L("ardbox_relay_hf_legacy", "Ardbox Relay HF (legacy)", "ardboxrelayhf", "-DARDBOX_HF -DARDBOX_RELAY_HF -DARDBOX_RELAY_HF_LEGACY", "NOURL"),
               L("ardbox_basic", "Ardbox Basic Controller", "ardboxbasic", "-DARDBOX -DARDBOX_BASIC", "NOURL")]

ardbox_hfplus_plcs = [L("ardbox_analog_hfplus_rs232", "Ardbox Analog HF+ w/ HW RS-232", "ardboxanaloghf", "-DARDBOX_HF_PLUS -DARDBOX_ANALOG_HF_PLUS -DARDBOX_ANALOG_HF_PLUS_RS232", "www.industrialshields.com/shop/plc-arduino-ardbox-analog-17"),
                      L("ardbox_analog_hfplus_rs485", "Ardbox Analog HF+ w/ HW RS-485", "ardboxanaloghf", "-DARDBOX_HF_PLUS -DARDBOX_ANALOG_HF_PLUS -DARDBOX_ANALOG_HF_PLUS_RS485", "www.industrialshields.com/shop/plc-arduino-ardbox-analog-17"),
                      L("ardbox_relay_hfplus_rs232", "Ardbox Relay HF+ w/ HW RS-232", "ardboxrelayhf", "-DARDBOX_HF_PLUS -DARDBOX_RELAY_HF_PLUS -DARDBOX_RELAY_HF_PLUS_RS232", "www.industrialshields.com/shop/plc-arduino-ardbox-plc-relay-18"),
                      L("ardbox_relay_hfplus_rs485", "Ardbox Relay HF+ w/ HW RS-485", "ardboxrelayhf", "-DARDBOX_HF_PLUS -DARDBOX_RELAY_HF_PLUS -DARDBOX_RELAY_HF_PLUS_RS485", "www.industrialshields.com/shop/plc-arduino-ardbox-plc-relay-18")]

ardbox_hfplus_dali_plcs = [plc.add_family_variants("_dali", " DALI", "-DARDBOX_DALI_HF_PLUS", "SAMEURL")
                           for plc in ardbox_hfplus_plcs]

ardbox_hfplus_gprs_plcs = [plc.add_family_variants("_gprs", " GPRS", "-DARDBOX_GPRS_HF_PLUS", "SAMEURL")
                           for plc in ardbox_hfplus_plcs]

ardbox_hfplus_wifi_plcs = [plc.add_family_variants("_wifi", " WiFi", "-DARDBOX_WIFI_HF_PLUS", "SAMEURL")
                           for plc in ardbox_hfplus_plcs]

ardbox_hfplus_lora_plcs = [plc.add_family_variants("_lora", " LoRa", "-DARDBOX_LORA_HF_PLUS", "SAMEURL")
                           for plc in ardbox_hfplus_plcs]

for plc in chain(ardbox_plcs, ardbox_hfplus_plcs, ardbox_hfplus_dali_plcs,
                 ardbox_hfplus_gprs_plcs, ardbox_hfplus_wifi_plcs,
                 ardbox_hfplus_lora_plcs):
    plc.generate_file(BOARDS_DIRECTORY)


spartan_leonardo_plcs = [L("spartan_16da", "Spartan 16DA", "spartan", "-DSPARTAN -DSPARTAN_16DA", "NOURL"),
                         L("spartan_16rda", "Spartan 16RDA", "spartan", "-DSPARTAN -DSPARTAN_16RDA", "NOURL")]
for plc in spartan_leonardo_plcs:
    plc.generate_file(BOARDS_DIRECTORY)


spartan_mega_plcs = [M("spartan_19r", "Spartan 19R", "spartan", "-DSPARTAN -DSPARTAN_19R", "NOURL"),
                     M("spartan_21", "Spartan 21", "spartan", "-DSPARTAN -DSPARTAN_21", "NOURL")]
for plc in spartan_mega_plcs:
    plc.generate_file(BOARDS_DIRECTORY)
