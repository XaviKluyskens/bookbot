import sys
from pathlib import Path
from stats import number_of_words, sorted_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = Path(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    number_of_words(book_path)
    print("--------- Character Count -------")
    sorted_dictionary(book_path)
    print("============= END ===============")


if __name__ == "__main__":
    main()
