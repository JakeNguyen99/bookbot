def main():
    os_path = "C:/Works/Bookbot/bookbot/"
    book_path = os_path + "books/frankenstein.txt"
    text = get_book_text(book_path)
    report(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(count_words(text)) + " words found in the document\n\n")

    list = count_letters(text)
    sorted_list = []
    for c in list:
        sorted_list.append({"char": c, "num": list[c]})
    sorted_list.sort(reverse=True,key=sort_on)

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


    

main()