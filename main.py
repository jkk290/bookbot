from stats import get_word_count, get_character_count, get_sorted

def get_book_text(path_to_file):
    with open(path_to_file) as book_file:
        file_contents = book_file.read()
    return file_contents

def main():
    frankenstein = get_book_text('books/frankenstein.txt')
    frankenstein_words = get_word_count(frankenstein)
    frankenstein_character_counts = get_character_count(frankenstein)
    # print(f"{frankenstein_words} words found in the document")
    # print(frankenstein_character_counts)
    get_sorted(frankenstein_character_counts)

main()