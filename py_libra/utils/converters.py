import json


def dict_to_json(dictionary):
    return json.dumps(dictionary, indent=4, sort_keys=True)