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



def generate_file(boards_directory: str, base_json: str, plc: tuple[str, str, str, str, str]) -> None:
    file_directory = boards_directory + plc[FILE_NAME] + ".json"
    with open(file_directory, 'w', encoding="utf-8") as new_file:
        new_file.write(generate_json(base_json, plc))
