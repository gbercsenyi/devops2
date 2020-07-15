import json

print("Hello World")

json_text = '"key1": "value1", "key2": "value2"'

json_dict = json.loads(json_text)

print(json.dumps(json_dict, indent=2))
