
def list_of_dicts_to_dict(list_of_dicts):
    new_dict = {}
    for item in list_of_dicts:
        list_of_keys = item.keys()
        for key in list_of_keys:
            if key not in new_dict:
                new_dict[key] = item[key]
            elif type(new_dict[key]) == list:
                new_dict[key].append(item[key])
            else:
                new_dict[key] = [new_dict[key], item[key]]
    return new_dict


list_of_dicts = [{'name': 'John Doe', 'age': 37, 'sex': 'M'}, 
        {'name': 'Lisa Simpson', 'age': 17, 'sex': 'F'}, 
        {'name': 'Bill Clinton', 'age': 57, 'sex': 'M'}]


new_dict = list_of_dicts_to_dict(list_of_dicts)
print(new_dict)