class AnagramChecker:
    def __init__(self, word_list_file):
        self.word_list = self.load_word_list(word_list_file)

    def load_word_list(self, file):
        with open('sowpods.txt', 'r') as f:
            return {word.strip().lower() for word in f}

    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    def get_anagrams(self, word):
        return [w for w in self.word_list if self.is_anagram(word, w)]

