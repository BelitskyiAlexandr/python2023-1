import re

#Поштовий індекс України - 5 цифр
def validate_ukraine_postal_code(postal_code):
    regex_pattern = r'^\d{5}$'

    if re.match(regex_pattern, postal_code):
        return True
    else:
        return False

user_input = input("Enter postal code: ")
if validate_ukraine_postal_code(user_input):
    print("Postal code is correct.")
else:
    print("Postal code is incorrect.")
