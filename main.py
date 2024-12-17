path_to_file = "books/frankenstein.txt"
def main():
    file_contents = read_contents(path_to_file)
    words = count_words(file_contents)
    char_count = count_chars(file_contents)
    report(words, char_count)

def sort_on(dt):
    return dt["num"]

def read_contents(path):
    with open(path) as file:
        file_contents = file.read()
        return file_contents

def count_words(text):
    word_count = len(text.split())
    return word_count

def count_chars(text):
    counter = {}
    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            if char_lower not in counter:
                counter[char_lower] = 1
            else:
                counter[char_lower] += 1
    return counter

def report(word_count, count_chars):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    sorted= [{"char": char, "num":count_chars[char]} for char in count_chars]
    sorted.sort(reverse=True, key=sort_on)
    for char in sorted:
        print(f"The {char["char"]} character was found {char["num"]} times")
main()