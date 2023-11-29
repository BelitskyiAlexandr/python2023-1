import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from uk_stemmer import UkStemmer

nltk.download('punkt')
nltk.download('stopwords')

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_text(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def remove_punctuation(words):
    return [word for word in words if word.isalnum()]

def remove_stop_words(words, stop_words):
    return [word for word in words if word.lower() not in stop_words]

def stemming(words):
    stemmer = UkStemmer()  # Український стеммер
    return [stemmer.stem_word(word) for word in words]

def lemmatization(words):
    lemmatizer = WordNetLemmatizer()  # Використовуємо для української мови, так як не знайшов окремого українського лематизатора
    return [lemmatizer.lemmatize(word) for word in words]

# Завантаження тексту та стоп-слів
text_path = 'xtext_ukr.txt'
stop_words_path = 'xstop_words_ukr.txt'
text = read_text(text_path)
stop_words = set(read_text(stop_words_path).split())

# Токенізація та вилучення розділових знаків
tokenized_words = word_tokenize(text)
tokenized_words = remove_punctuation(tokenized_words)

# Вилучення стоп-слів
filtered_words = remove_stop_words(tokenized_words, stop_words)

# Статистична інформація: кількість слів, кількість розділових знаків, кількість стопслів
word_count = len(tokenized_words)
count = lambda l1,l2: sum([1 for x in l1 if x in l2])
punctuation_count = count(text, string.punctuation)
stop_words_count = word_count - len(filtered_words)

# Стемінг та лематизація
stemmed_words = stemming(filtered_words)
lemmatized_words = lemmatization(filtered_words)

# Висновки
print("Words after tokenization and removal of punctuation:", tokenized_words)
print("Words after removing stop words:", filtered_words)
print("Statistics:")
print(f"Word count: {word_count}")
print(f"Number of punctuation marks: {punctuation_count}")
print(f"Number of stop words: {stop_words_count}")
print(f"Number of words after removing stop words: {len(filtered_words)}")
print("Words after stemming:", stemmed_words)
print("Words after lemmatization:", lemmatized_words)

# Збереження результатів
write_text('xfiltered_text_ukr.txt', ' '.join(filtered_words))
