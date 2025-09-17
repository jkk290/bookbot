import sys
from stats import get_word_count, get_character_count, get_sorted

def get_book_text(path_to_file):
    with open(path_to_file) as book_file:
        file_contents = book_file.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frankenstein = get_book_text(sys.argv[1])
    frankenstein_words = get_word_count(frankenstein)
    frankenstein_character_counts = get_character_count(frankenstein)
    sorted_word_counts = get_sorted(frankenstein_character_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_words} total words")
    print(f"--------- Character Count -------")
    for word_count in sorted_word_counts:
        if word_count["char"].isalpha():
            print(f"{word_count["char"]}: {word_count["num"]}")
    print("============= END ===============")

main()