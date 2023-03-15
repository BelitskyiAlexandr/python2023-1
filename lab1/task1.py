
def first_or_last_is_same(list1, list2):
    if list1[0] == list2[0] or list1[-1] == list2[-1]:
        return True
    else:
        return False


input_string = input("Enter a list element separated by space ")
list1 = input_string.split()

input_string = input("Enter a list element separated by space ")
list2 = input_string.split()

print(list1)
print(list2)

if not list1 or not list2:
    print('List is empty')
elif not all([item.isdigit() for item in list1]) or not all([item.isdigit() for item in list2]):
    print('List contains non integer value')
else:
    print('Result: ' + str(first_or_last_is_same(list1, list2)))

