
def list_to_counted_dict(worked_list):
    dict = {}
    for i in worked_list:
        dict[i] = dict.get(i, 0) + 1
    return dict


input_string = input("Enter a list element separated by space ")
worked_list = input_string.split()

if not worked_list:
    print('List is empty')
else :
    print(list_to_counted_dict(worked_list))
