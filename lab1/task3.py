
def print_list_with_dot_and_comma(list):
    print(*list, sep='; ')


input_string = input("Enter a list element separated by space ")
list = input_string.split()

if not list:
    print('List is empty')
else :
    print_list_with_dot_and_comma(list)

