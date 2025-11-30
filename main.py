import math
from stats import count_letters, count_words, sort_letters


def get_book_text(book_path):
    file_contents = None
    with open(book_path) as f:
        file_contents = f.read()

    return file_contents


def print_stats(book_path: str):
    print(f"Analyzing book found at {book_path}")


def tabed_header(label: str, spacing: int = 2, width: int = 33, char="-"):
    label_len = len(label) + spacing
    total_leftover = width - label_len
    padding_left = math.ceil(total_leftover / 2.0)
    padding_right = math.floor(total_leftover / 2.0)

    buffer = str()

    buffer += padding_left * char
    buffer += " "
    buffer += label
    buffer += " "
    buffer += padding_right * char
    print(buffer)


def print_chars(lst):
    for d in lst:
        print(f"{d["char"]}: {d["num"]}")


def main():
    # CONFIG
    software_name = "BOOKBOT"
    book_path = "./books/frankenstein.txt"

    # LOGIC
    book_text = get_book_text(book_path)
    letter_counts = count_letters(book_text)
    lst = sort_letters(letter_counts)

    # STDOUT
    tabed_header(software_name, char="=")
    print_stats(book_path)
    tabed_header(
        "Word Count",
    )
    print(f"Found {count_words(book_text)} total words")
    tabed_header("Character Count")
    print_chars(lst)
    tabed_header("END", char="=")


if __name__ == "__main__":
    main()
