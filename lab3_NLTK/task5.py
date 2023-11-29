import re


text_with_numbers = "333334 333 123 2334 2555 555 12345 557555 123456"

# Регулярний вираз для пошуку чисел з послідовностями цифр 5 довжиною від 2-х до 3-х символів
pattern = r'\b\d*5{2,3}\d*\b'

# Знаходження чисел за допомогою регулярного виразу
matching_numbers = re.findall(pattern, text_with_numbers)

print(f"sequence of numbers: {matching_numbers}")
