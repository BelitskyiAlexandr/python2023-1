import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')


text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. In hac habitasse platea dictumst.
Proin at facilisis mi. Integer vel lacus vel felis vehicula hendrerit. Etiam ultricies tortor vel dapibus varius.
Quisque varius ex vel mi suscipit, eu volutpat libero eleifend. Suspendisse potenti.
"""

# Токенізація за реченнями
sentences = sent_tokenize(text)
print("Text:")
for sentence in sentences:
    print(sentence)

# Токенізація за словами та вилучення розділових знаків та стоп-слів
stop_words = set(stopwords.words("english"))
tokenized_words = []
for sentence in sentences:
    words = word_tokenize(sentence)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]
    tokenized_words.extend(filtered_words)

print("\nWords after tokenize and filtration:")
print(tokenized_words)

# Визначення частин мови
pos_tags = pos_tag(tokenized_words)
print("\nDefinition of parts of speech:")
print(pos_tags)


#Завдання 9
#1. Підрахунок кількості слів у кожному реченні
word_counts_per_sentence = [len(word_tokenize(sentence)) for sentence in sentences]
print("\nNumber of words in each sentence:", word_counts_per_sentence)

#2. Визначення кількості стоп-слів у тексті
stop_word_count = sum(1 for word in tokenized_words if word in stop_words)
print("Number of stopwords in the text:", stop_word_count)

#3. Визначення найдовшого слова
longest_word = max(tokenized_words, key=len)
print("Longest word:", longest_word)

#4. Скільки слів у тексті містять 4 символи
four_char_word_count = sum(1 for word in tokenized_words if len(word) == 4)
print("Number of four char words:", four_char_word_count)



#Завдання 10
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')

# Стемінг
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokenized_words]

# Лематизація
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokenized_words]

print("Words after stemmer:", stemmed_words)
print("Worsd after lemmatizer:", lemmatized_words)
