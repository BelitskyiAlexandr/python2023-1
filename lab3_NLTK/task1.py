import re

text = """
It`s first sentence.
This is second sentence.
Third sentence - third.
Fourth sentence, fourth!
After all, fifth sentence.
"""

# a. Кількість слів у тексті
word_count = len(re.findall(r'\b\w+\b', text))
print(f'a. Number of words: {word_count}')

# b. Слова, що починаються на голосну та їх кількість
vowel_words = re.findall(r'\b[aeiouAEIOU]\w*\b', text)
print(f'b. Words starting with a vowel: {vowel_words}, Number: {len(vowel_words)}')

# c. Слова, що починаються на приголосну
consonant_words = re.findall(r'\b[^aeiouAEIOU\s]\w*\b', text)
print(f'c. Words that start with a consonant: {consonant_words}')

# d. Три будь-яких слова і їх позиції
selected_words = ['sentence', 'second', 'fifth']
positions = {word: [match.start() for match in re.finditer(fr'\b{re.escape(word)}\b', text)] for word in selected_words}
print(f'd. Positions of selected words: {positions}')

# e. Заміна слова на прізвище
modified_text = re.sub(r'sentence', 'Belitskyi', text)
print(f'e. The text is replaced by the last name:\n{modified_text}')
