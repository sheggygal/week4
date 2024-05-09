import random

def get_words_from_file(open_file):
    with open('random.txt', 'r') as f:
        words = f.read().split()
    return words

def get_random_sentence(length, words):
    random_words = random.choices(words, k=length)
    sentence = ' '.join(random_words)
    return sentence.lower()

def main():
    print("Welcome to the Random Sentence Generator!")
    print("This program will generate a random sentence based on the length you specify.")
    print("Please enter the length of the sentence you want (between 2 and 20):")

    while True:
        try:
            length = int(input("Enter sentence length: "))
            if length < 2 or length > 20:
                print("Error: Sentence length must be between 2 and 20.")
            else:
                break
        except ValueError:
            print("Error: Please enter a valid integer.")

    words = get_words_from_file('word_list.txt')

    if len(words) == 0:
        print("Error: Word list is empty. Please check the file and try again.")
        return

    sentence = get_random_sentence(length, words)
    print("Random sentence:", sentence)

if __name__ == "__main__":
    main()
