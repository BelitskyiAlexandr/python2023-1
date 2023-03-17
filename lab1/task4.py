
def list_into_lists_by_numbers(list_with_values):
    translated_list = []
    for item in list_with_values:
        translated_list.append(list(range(0, item + 1)))

    return translated_list


def transform_strlist_to_intlist(list_with_values):
    int_list = [eval(i) for i in list_with_values]
    return int_list

input_string = input("Enter a list element separated by space ")
list_with_values = input_string.split()

print(list_with_values)

if not list_with_values:
    print('List is empty')
elif not all([item.isdigit() for item in list_with_values]):
    print('List contains non integer value')
else:
    list_with_values = transform_strlist_to_intlist(list_with_values)
    if any(i < 1 for i in list_with_values):
        print('List contains value less than 1')
    else:
        print('Result: ' + str(list_into_lists_by_numbers(list_with_values)))
