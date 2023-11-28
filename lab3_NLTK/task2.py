import re


text = "Python is amazing and versatile."

# Отримання списку символів без пробілів
characters_without_spaces = re.findall(r'\S', text)
print(f"List of symbols without whitespaces: {characters_without_spaces}")

# Отримання списку перших двох букв кожного слова
first_two_letters_list = re.findall(r'\b\w{1,2}', text)
print(f"List of two first letters of each word:  {first_two_letters_list}")

# Створення нового списку, який включає всі символи, крім 'а' та 'б'
filtered_characters = re.findall(r'[^\sab]', text)
print(f"List without 'a' and 'b': {filtered_characters}")
