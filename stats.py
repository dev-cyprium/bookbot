def count_words(text: str):
    return len(text.split())


def count_letters(text: str):
    d = dict[str, int]()

    for letter in text:
        letter = letter.lower()

        if letter not in d:
            d[letter] = 0

        d[letter] += 1

    return d


def sort_on(item):
    return item["num"]


def sort_letters(d: dict[str, int]):
    l = list()

    for k, v in d.items():
        if k.isalpha():
            l.append({"char": k, "num": v})

    l.sort(reverse=True, key=sort_on)
    return l
