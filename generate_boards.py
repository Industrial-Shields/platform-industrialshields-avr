import json
import os


FILE_NAME = 0
NAME = 1
VARIANT = 2
EXTRA_FLAGS = 3
URL = 4


def generate_json(base_json: str, plc: tuple[str, str, str, str, str]) -> str:
    new_json = json.loads(base_json)

    new_json["name"] = plc[NAME]
    new_json["build"]["variant"] = plc[VARIANT]
    new_json["build"]["extra_flags"] += ' ' + plc[EXTRA_FLAGS]
    new_json["url"] = plc[URL]
    
    return json.dumps(new_json, indent=4)

SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
BOARDS_DIRECTORY = os.path.join(SCRIPT_DIRECTORY, "boards/")
def generate_file(base_json: str, plc: tuple[str, str, str, str, str]) -> None:
    file_directory = BOARDS_DIRECTORY + plc[FILE_NAME] + ".json"
    with open(file_directory, 'w') as f:
        f.write(generate_json(base_json, plc))


if __name__ == "__main__":
    from itertools import chain

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
    "name": "ATmega2560",
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


    mduino_plcs = [("mduinoplc_19r", "M-Duino PLC 19R", "mduinorelay", "-DMDUINO -DMDUINO_19R", "www.industrialshields.com/shop/esp32-plc-21-2801"),
                   ("mduinoplc_21", "M-Duino PLC 21", "mduino", "-DMDUINO -DMDUINO_21", "www.industrialshields.com/shop/esp32-plc-19r-2905"),                   
                   ("mduinoplc_38r", "M-Duino PLC 38R", "mduinorelay", "-DMDUINO -DMDUINO_38R", "www.industrialshields.com/shop/esp32-plc-38r-2906"),
                   ("mduinoplc_42", "M-Duino PLC 42", "mduino", "-DMDUINO -DMDUINO_42", "www.industrialshields.com/shop/esp32-plc-42-2907"),
                   ("mduinoplc_57r", "M-Duino PLC 57R", "mduinorelay", "-DMDUINO -DMDUINO_57R", "www.industrialshields.com/shop/esp32-plc-57r-2908"),
                   ("mduinoplc_58", "M-Duino PLC 58", "mduino", "-DMDUINO -DMDUINO_58", "www.industrialshields.com/shop/esp32-plc-58-2909")]

    mduinoplus_plcs = \
        [("mduinoplc_19r+", "M-Duino PLC 19R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_19R_PLUS", "www.industrialshields.com/shop/esp32-plc-21-2801"),
         ("mduinoplc_21+", "M-Duino PLC 21+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_21_PLUS", "www.industrialshields.com/shop/esp32-plc-19r-2905"),
         ("mduinoplc_38ar+", "M-Duino PLC 38AR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_38AR_PLUS", "www.industrialshields.com/shop/esp32-plc-38r-2906"),
         ("mduinoplc_38r+", "M-Duino PLC 38R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_38R_PLUS", "www.industrialshields.com/shop/esp32-plc-38r-2906"),
         ("mduinoplc_42+", "M-Duino PLC 42+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_42_PLUS", "www.industrialshields.com/shop/esp32-plc-42-2907"),
         ("mduinoplc_50rra+", "M-Duino PLC 50RRA+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_50RRA_PLUS", "www.industrialshields.com/shop/esp32-plc-50rra-2912"),
         ("mduinoplc_53arr+", "M-Duino PLC 53ARR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_53ARR_PLUS", "www.industrialshields.com/shop/esp32-plc-53arr-2913"),
         ("mduinoplc_54ara+", "M-Duino PLC 54ARA+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_54ARA_PLUS", "www.industrialshields.com/shop/esp32-plc-54ara-2914"),
         ("mduinoplc_57aar+", "M-Duino PLC 57AAR+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_57AAR_PLUS", "www.industrialshields.com/shop/esp32-plc-57aar-2911"),
         ("mduinoplc_57r+", "M-Duino PLC 57R+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_57R_PLUS", "www.industrialshields.com/shop/esp32-plc-57r-2908"),
         ("mduinoplc_58+", "M-Duino PLC 58+", "mduinoplus", "-DMDUINO_PLUS -DMDUINO_58_PLUS", "www.industrialshields.com/shop/esp32-plc-58-2909")]
    
    
    for plc in chain(mduino_plcs, mduinoplus_plcs):
        generate_file(mega_basejson, plc)
