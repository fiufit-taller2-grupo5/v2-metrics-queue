import json

def is_valid_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True