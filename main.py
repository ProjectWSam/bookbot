def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(produce_report(chars_sorted_list, book_path, num_words))


def produce_report(sorted_list, book_name, word_count):
    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count} words found in the document")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End Report ---")

def sorted_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for key in num_chars_dict:
        sorted_list.append({"char": key, "num": num_chars_dict[key]})
    sorted_list.sort(reverse=True, key=sorted_on)
    return sorted_list
    

def get_chars_dict(text):
    text = text.lower()
    chars = {}
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()