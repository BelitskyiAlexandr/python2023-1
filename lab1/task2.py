
def list_to_counted_dict(list):
    dict = {}
    for i in list:
        dict[i] = dict.get(i, 0) + 1
    return dict


input_string = input("Enter a list element separated by space ")
list = input_string.split()

if not list:
    print('List is empty')
else :
    print(list_to_counted_dict(list))
