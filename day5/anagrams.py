from anagram_checker import AnagramChecker

def display_menu():
    print("\nMenu:")
    print("1. Input a word")
    print("2. Exit")

def get_user_input():
    return input("Enter your choice: ")

def get_word_input():
    word = input("Enter a word: ").strip()
    if ' ' in word:
        print("Error: Only a single word is allowed.")
        return None
    elif not word.isalpha():
        print("Error: Only alphabetic characters are allowed.")
        return None
    return word

def display_word_info(word, valid, anagrams):
    print("\nYour word:", word)
    if valid:
        print("This is a valid English word.")
        print("Anagrams for your word:", ', '.join(anagrams))
    else:
        print("This is not a valid English word.")

def main():
    word_list_file = "sowpods.txt"  
    anagram_checker = AnagramChecker(word_list_file)

    while True:
        display_menu()
        choice = get_user_input()

        if choice == '1':
            word = get_word_input()
            if word:
                word = word.lower()
                valid = anagram_checker.is_valid_word(word)
                anagrams = anagram_checker.get_anagrams(word)
                display_word_info(word, valid, anagrams)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
