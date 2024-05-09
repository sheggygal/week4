import re
from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        word_count = Counter(self.text.split())
        return word_count.get(word, 0)

    def most_common_word(self):
        word_count = Counter(self.text.split())
        return word_count.most_common(1)[0][0]

    def unique_words(self):
        return set(self.text.split())

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            text = f.read()
        return cls(text)

import string

class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
        self.stop_words = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}

    def remove_punctuation(self):
        return self.text.translate(str.maketrans('', '', string.punctuation))

    def remove_stopwords(self):
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in self.stop_words]
        return ' '.join(filtered_words)

    def remove_special_characters(self):
        return ''.join(e for e in self.text if e.isalnum() or e.isspace())

text_string = "A good book would sometimes cost as much as a good house."
text_obj = Text(text_string)

print("Frequency of 'good':", text_obj.word_frequency('good'))
print("Most common word:", text_obj.most_common_word())
print("Unique words:", text_obj.unique_words())

stranger_text = Text.from_file('the_stranger.txt')
print("Frequency of 'the':", stranger_text.word_frequency('the'))
print("Most common word:", stranger_text.most_common_word())
print("Unique words:", stranger_text.unique_words())

text_modification_obj = TextModification(text_string)

print("Text without punctuation:", text_modification_obj.remove_punctuation())
print("Text without stopwords:", text_modification_obj.remove_stopwords())
print("Text without special characters:", text_modification_obj.remove_special_characters())


