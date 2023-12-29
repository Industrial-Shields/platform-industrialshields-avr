from json_generator import *
from itertools import chain



SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
BOARDS_DIRECTORY = os.path.join(SCRIPT_DIRECTORY, "boards/")



def add_family_variants(plc: tuple[str, str, str, str, str], filename: str, name: str,
                        extra_macros: str, url: str) -> tuple[str, str, str, str, str]:
    return (plc[FILE_NAME]+filename, plc[NAME]+name, plc[VARIANT], \
            plc[EXTRA_FLAGS] + f" {extra_macros}", url)



mega_basejson = """
{
    "build": {
	"core": "industrialshields",
	"extra_flags": "",
	"f_cpu": "16000000L",
	"mcu": "atmega2560",
	"variant": ""
    },
    "bootloader": {
	"led_pin": "B7",
	"uart0_pins": "uart0_rxe0_txe1",
	"uart1_pins": "uart1_rxd2_txd3",
	"uart2_pins": "uart2_rxh0_txh1",
	"uart3_pins": "uart3_rxj0_txj1"
    },
    "frameworks": [
	"arduino"
    ],
    "name": "",
    "upload": {
	"maximum_ram_size": 8192,
	"maximum_size": 262144,
	"protocol": "urclock",
	"require_upload_port": true,
	"speed": 115200
    },
    "url": "",
    "vendor": "Industrial Shields"
}
"""


mduino_plcs = [("mduinoplc_19r", "M-Duino PLC 19R", "mduinorelay", "-DMDUINO -DMDUINO_19R", ""),
               ("mduinoplc_21", "M-Duino PLC 21", "mduino", "-DMDUINO -DMDUINO_21", ""),
               ("mduinoplc_38r", "M-Duino PLC 38R", "mduinorelay", "-DMDUINO -DMDUINO_38R", ""),
               ("mduinoplc_42", "M-Duino PLC 42", "mduino", "-DMDUINO -DMDUINO_42", ""),
               ("mduinoplc_57r", "M-Duino PLC 57R", "mduinorelay", "-DMDUINO -DMDUINO_57R", ""),
               ("mduinoplc_58", "M-Duino PLC 58", "mduino", "-DMDUINO -DMDUINO_58", "")]

mduinoplus_plcs = \
    [("mduinoplc_19r+", "M-Duino PLC 19R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_19R_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-19r-8"),
     ("mduinoplc_21+", "M-Duino PLC 21+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_21_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-21-3670"),
     ("mduinoplc_38ar+", "M-Duino PLC 38AR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_38AR_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-38ar-12"),
     ("mduinoplc_38r+", "M-Duino PLC 38R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_38R_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-38r-10"),
     ("mduinoplc_42+", "M-Duino PLC 42+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_42_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-42-3667"),
     ("mduinoplc_50rra+", "M-Duino PLC 50RRA+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_50RRA_PLUS", "www.industrialshields.com/shop/is-mduino-50rra-m-duino-ethernet-plc-arduino-50rra-488"),
     ("mduinoplc_53arr+", "M-Duino PLC 53ARR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_53ARR_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-53arr-468"),
     ("mduinoplc_54ara+", "M-Duino PLC 54ARA+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_54ARA_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-54ara-688"),
     ("mduinoplc_57aar+", "M-Duino PLC 57AAR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_57AAR_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-57aar-436"),
     ("mduinoplc_57r+", "M-Duino PLC 57R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_57R_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-57r-13"),
     ("mduinoplc_58+", "M-Duino PLC 58+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_58_PLUS", "www.industrialshields.com/shop/m-duino-ethernet-plc-arduino-58-176")]

    

mduinoplus_dali_plcs = [add_family_variants(plc, "_dali", " DALI", "-DMDUINO_DALI_PLUS", plc[URL])
                        for plc in mduinoplus_plcs]

mduinoplus_gprs_plcs = [add_family_variants(plc, "_gprs", " GPRS", "-DMDUINO_GPRS_PLUS", plc[URL])
                        for plc in mduinoplus_plcs]

mduinoplus_lora_plcs = [add_family_variants(plc, "_lora", " LoRa", "-DMDUINO_LORA_PLUS", plc[URL])
                    for plc in mduinoplus_plcs]

mduinoplus_wifi_plcs = [add_family_variants(plc, "_wifi", " WiFi/BT", "-DMDUINO_WIFI_PLUS", plc[URL])
                        for plc in mduinoplus_plcs]

mduinoplus_wifi_gprs_plcs = [add_family_variants(plc, "_wifi_gprs", " WiFi/BT + GPRS", "-DMDUINO_WIFI_GPRS_PLUS", "")
                             for plc in mduinoplus_plcs]


for plc in chain(mduino_plcs, mduinoplus_plcs, mduinoplus_dali_plcs, mduinoplus_gprs_plcs,
                 mduinoplus_lora_plcs, mduinoplus_wifi_plcs, mduinoplus_wifi_gprs_plcs):
    generate_file(BOARDS_DIRECTORY, mega_basejson, plc)


    
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

ardbox_plcs = [("ardbox_analog", "Ardbox Analog", "ardboxanalog", "-DARDBOX -DARDBOX_ANALOG", ""),
               ("ardbox_analog_hf_rs232", "Ardbox Analog HF w/ HW RS-232", "ardboxanaloghf", "-DARDBOX_HF -DARDBOX_ANALOG_HF -DARDBOX_ANALOG_HF_RS232", ""),
               ("ardbox_analog_hf_rs485", "Ardbox Analog HF w/ HW RS-485", "ardboxanaloghf", "-DARDBOX_HF -DARDBOX_ANALOG_HF -DARDBOX_ANALOG_HF_RS485", ""),
               ("ardbox_analog_hf_legacy", "Ardbox Analog HF (legacy)", "ardboxanaloghf", "-DARDBOX_HF -DARDBOX_ANALOG_HF -DARDBOX_ANALOG_HF_LEGACY", ""),
               ("ardbox_relay", "Ardbox Relay", "ardboxrelay", "-DARDBOX -DARDBOX_RELAY", ""),
               ("ardbox_relay_hf_rs232", "Ardbox Relay HF w/ HW RS-232", "ardboxrelayhf", "-DARDBOX_HF -DARDBOX_RELAY_HF -DARDBOX_RELAY_HF_RS485", ""),
               ("ardbox_relay_hf_rs485", "Ardbox Relay HF w/ HW RS-485", "ardboxrelayhf", "-DARDBOX_HF -DARDBOX_RELAY_HF -DARDBOX_RELAY_HF_RS485", ""),
               ("ardbox_relay_hf_legacy", "Ardbox Relay HF (legacy)", "ardboxrelayhf", "-DARDBOX_HF -DARDBOX_RELAY_HF -DARDBOX_RELAY_HF_LEGACY", ""),
               ("ardbox_basic", "Ardbox Basic Controller", "ardboxbasic", "-DARDBOX -DARDBOX_BASIC", "")]

ardbox_hfplus_plcs = [("ardbox_analog_hfplus_rs232", "Ardbox Analog HF+ w/ HW RS-232", "ardboxanaloghf", "-DARDBOX_HF_PLUS -DARDBOX_ANALOG_HF_PLUS -DARDBOX_ANALOG_HF_PLUS_RS232", "www.industrialshields.com/shop/plc-arduino-ardbox-analog-17"),
                      ("ardbox_analog_hfplus_rs485", "Ardbox Analog HF+ w/ HW RS-485", "ardboxanaloghf", "-DARDBOX_HF_PLUS -DARDBOX_ANALOG_HF_PLUS -DARDBOX_ANALOG_HF_PLUS_RS485", "www.industrialshields.com/shop/plc-arduino-ardbox-analog-17"),
                      ("ardbox_relay_hfplus_rs232", "Ardbox Relay HF+ w/ HW RS-232", "ardboxrelayhf", "-DARDBOX_HF_PLUS -DARDBOX_RELAY_HF_PLUS -DARDBOX_RELAY_HF_PLUS_RS232", "www.industrialshields.com/shop/plc-arduino-ardbox-plc-relay-18"),
                      ("ardbox_relay_hfplus_rs485", "Ardbox Relay HF+ w/ HW RS-485", "ardboxrelayhf", "-DARDBOX_HF_PLUS -DARDBOX_RELAY_HF_PLUS -DARDBOX_RELAY_HF_PLUS_RS485", "www.industrialshields.com/shop/plc-arduino-ardbox-plc-relay-18")]

ardbox_hfplus_dali_plcs = [add_family_variants(plc, "_dali", "DALI", "-DARDBOX_DALI_HF_PLUS", plc[URL])
                           for plc in ardbox_hfplus_plcs]

ardbox_hfplus_gprs_plcs = [add_family_variants(plc, "_gprs", "GPRS", "-DARDBOX_GPRS_HF_PLUS", plc[URL])
                           for plc in ardbox_hfplus_plcs]

ardbox_hfplus_wifi_plcs = [add_family_variants(plc, "_wifi", "WiFi", "-DARDBOX_WIFI_HF_PLUS", plc[URL])
                           for plc in ardbox_hfplus_plcs]

ardbox_hfplus_lora_plcs = [add_family_variants(plc, "_lora", "LoRa", "-DARDBOX_LORA_HF_PLUS", plc[URL])
                           for plc in ardbox_hfplus_plcs]

for plc in chain(ardbox_plcs, ardbox_hfplus_plcs, ardbox_hfplus_dali_plcs,
                 ardbox_hfplus_gprs_plcs, ardbox_hfplus_wifi_plcs,
                 ardbox_hfplus_lora_plcs):
    generate_file(BOARDS_DIRECTORY, leonardo_basejson, plc)
    
    
spartan_leonardo_plcs = [("spartan_16da", "Spartan 16DA", "spartan", "-DSPARTAN -DSPARTAN_16DA", ""),
                         ("spartan_16rda", "Spartan 16RDA", "spartan", "-DSPARTAN -DSPARTAN_16RDA", "")]
for plc in spartan_leonardo_plcs:
    generate_file(BOARDS_DIRECTORY, leonardo_basejson, plc)
    
spartan_mega_plcs = [("spartan_19r", "Spartan 19R", "spartan", "-DSPARTAN -DSPARTAN_19R", ""),
                     ("spartan_21", "Spartan 21", "spartan", "-DSPARTAN -DSPARTAN_21", "")]
for plc in spartan_mega_plcs:
    generate_file(BOARDS_DIRECTORY, mega_basejson, plc)
