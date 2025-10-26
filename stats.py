def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main(path):
    text = get_book_text(path)
    print(text)

def number_of_words(path):
    text = get_book_text(path)
    all_words = text.split()
    print(f"Found {len(all_words)} total words")

def number_of_characters(path):
    text = get_book_text(path).lower()

    character_teller = {}

    for character in text:
        if character in character_teller:
            character_teller[character] += 1
        else:
            character_teller[character] = 1

    return character_teller
            
def sorted_dictionary(path):
    dict = number_of_characters(path)
    character_list = [{"char": char, "num": count} for char, count in dict.items()]

    def sort_by_num(item):
        return item["num"]
    
    character_list.sort(key=sort_by_num, reverse=True)


    for item in character_list:
        char = item["char"]
        num = item["num"]
        # enkel letters (inclusief accenten) toelaten
        if char.isalpha():
            print(f"{char}: {num}")



