from stats import get_num_words
from collections import OrderedDict
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        data = file.read()
        return data
    


def count_words_text(text):
    words_text = text.split('\n', -1)
    count_words = []
    new_data = []
    for line in words_text:
        new_data += line.split(' ', -1)
    for data in new_data:
        if len(data) != 0:
            count_words.append(data)
    return len(count_words)


def main():
    if len(sys.argv) > 1:
        av = sys.argv[1]
        data = get_book_text(av)
        num_words = count_words_text(data)
        dict_words = get_num_words(data)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for d in dict_words:
            if d.isalpha():
                print(f"{d}: {dict_words[d]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()