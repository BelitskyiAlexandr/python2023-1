import json

def convert_to_json(data):
    json_data = {}
    for key, value in data.items():
        if isinstance(value, list) and (all(isinstance(item, int) for item in value) and value != []) : # без умови and value != []
                                                                                                        # чомусь додає пустий список
            json_data[key] = value
    return json.dumps(json_data)

data = {
    'name': 'John',
    'age': 30,
    'numbers': [1, 2, 3],
    'mixed': [1, 'two', 3.0],
    'empty_list': [],
    'nested_list': [[1, 2], [3, 4]],
    'integer_list': [1, 2, 3, 4],
    'string_list': ['one', 'two', 'three']
}

json_data = convert_to_json(data)
print(json_data)
