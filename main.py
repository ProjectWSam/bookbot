def read(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)

def count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        counted_words = len(words)
        print(f"--- Begin report of {file_path} ---")
        print(f"{counted_words} words found in the document")
        return counted_words

def character_count(file_path):
    letters = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
        'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
        'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
        'z': 0
    }
    with open(file_path) as f:
        file_contents = f.read()
        lowered_contents = file_contents.lower()

        for char in lowered_contents:
            if char in letters:
                letters[char] += 1
    return letters

def sort_on(dict_item):
    return dict_item["num"]

if __name__ == '__main__':
    file_path = "books/frankenstein.txt"

    # Count words and begin report
    word_count = count(file_path)
    
    # Character count
    counts = character_count(file_path)

    # Convert the dictionary to a list of dictionaries
    count_list = [{"char": k, "num": v} for k, v in counts.items()]
    
    # Sort the list
    count_list.sort(reverse=True, key=sort_on)

    # Print the sorted character counts
    for item in count_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")