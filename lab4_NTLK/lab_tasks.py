import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')

def create_bag_of_words(words):
    # set
    bag_of_words = set(words)

    return bag_of_words


sample_text = """
In that instant, everything changed.
I've always wanted to go to Tajikistan, but my cat would miss me.
He poured rocks in the dungeon of his mind.
He colored deep space a soft yellow.
Random words: yellow, yellow, rocks, Tajikistan. Yellow.
"""

# not in def, because of next task
words = word_tokenize(sample_text)
# stop-words remove
stop_words = set(stopwords.words('english'))
words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

#def1
bag_of_words = create_bag_of_words(words)

print("Bag of words:", bag_of_words)
print('----------\n\nTask2')

def calculate_tf(words, bag_of_words):
    tf = {}
    total_words = len(words)
    for word in bag_of_words:
        word_count = words.count(word)
        tf[word] = word_count / total_words

    return tf

#def2
tf_result = calculate_tf(words, bag_of_words)


print("Term Frequency (TF):")
for word, tf_value in tf_result.items():
    print(f"{word}: {tf_value}")



print('----------\n\nTask3')
import re
import math


def calculate_idf(text, bag_of_words):
   
    #idf = lg(numb_of_docs/numb_of_docs_with_word) - we don`t have docs, so we use sent as docs
    sentences = re.split(r'[.!?]', text)
    num_documents = len(sentences)
    

    idf_values = {}
    for word in bag_of_words:
        # frequency
        document_frequency = 0
        for sentence in sentences:
            if word.lower() in sentence.lower():
                document_frequency += 1

        #idf 
        idf_values[word] = math.log10(num_documents / (document_frequency))  # 

    return idf_values

#def3
idf_result = calculate_idf(sample_text, bag_of_words)

print("Inverse Document Frequency (IDF):")
for word, idf_value in idf_result.items():
    print(f"{word}: {idf_value:.3f}")


print('----------\n\nTask4')
def tf_idf_mesure(tf, idf):
    return {word: tf[word] * idf[word] for word in tf}

tf_idf_result = tf_idf_mesure(tf_result, idf_result)

print("TF-IDF static mesure:")
for word, tf_idf_value in tf_idf_result.items():
    print(f"{word}: {tf_idf_value:.3f}")


print('----------\n\nTask5')
import matplotlib.pyplot as plt

# legend
words_for_plot = list(tf_idf_result.keys())
tf_idf_values_for_plot = list(tf_idf_result.values())

# diagram sett
plt.figure(figsize=(10, 6))
plt.bar(words_for_plot, tf_idf_values_for_plot, color='green')
plt.ylabel('TF-IDF Value')
plt.title('TF-IDF Measure for Each Word')
plt.xticks(rotation=45, ha='right')  # Повертає підписи слов на 45 градусів
plt.grid(axis='y')


plt.show()



print('----------\n\nTask6')
from nltk.corpus import gutenberg
from nltk.probability import FreqDist

nltk.download('gutenberg')
hamlet_text = gutenberg.raw('shakespeare-hamlet.txt')

words = word_tokenize(hamlet_text)

target_words = ['Hamlet', 'King', 'Queen', 'Ophelia']

# frequency analisys
freq_dist = FreqDist(words)

# every word count
word_counts = [freq_dist[word] for word in target_words]


plt.bar(target_words, word_counts, color='green')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Distribution of words')
plt.show()


unique_tokens = set(words)
num_unique_tokens = len(unique_tokens)


print("Uniq tokens", num_unique_tokens)



print('----------\n\nTask7')

# uniq tokens
unique_words = [word for word, count in FreqDist(words).items() if count == 1]
print("Uniq words:", unique_words)

# word`s length
word_lengths = [len(word) for word in words]

# mode
most_common_length = FreqDist(word_lengths).max()


plt.hist(word_lengths, bins=range(min(word_lengths), min(17, max(word_lengths)) + 1), edgecolor='black', color='green')
plt.xlabel('Words` length')
plt.ylabel('Frequency')
plt.title('Distribution of words')
plt.show()

# Виведення найчастіше зустрічається довжини слів
print(f"Mode of words` length: {most_common_length}")