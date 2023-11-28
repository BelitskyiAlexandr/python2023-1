import re

text_with_programming_languages = "Python, Java, C++, JavaScript, Ruby, Swift, Kotlin are some programming languages."

programming_languages_list = re.findall(r'\b(?:Python|Java|C\+\+|JavaScript|Ruby|Swift|Kotlin)\b', text_with_programming_languages, flags=re.IGNORECASE)
print(f"Список назв мов програмування: {programming_languages_list}")
