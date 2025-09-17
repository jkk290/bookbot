def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    character_counts = {}
    for character in book_text:
        character_lowercase = character.lower()

        if character_lowercase not in character_counts:
            character_counts[character_lowercase] = 1
        else:
            character_counts[character_lowercase] += 1
    return character_counts

def get_sorted(character_counts):
    characters_list = []
    for character in character_counts:
        characters_list.append({ "char": character, "num": character_counts[character] })

    def sort_on(items):
        return items["num"]
    
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list