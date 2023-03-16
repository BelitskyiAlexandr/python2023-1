
def print_list_with_dot_and_comma(worked_list):
    print(*worked_list, sep='; ')


input_string = input("Enter a list element separated by space ")
worked_list = input_string.split()

if not worked_list:
    print('List is empty')
else :
    print_list_with_dot_and_comma(worked_list)

