from string import ascii_lowercase

path_to_file = "books/frankenstein.txt"

def read_file(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def init_letters_array(letters):
    for c in ascii_lowercase:
        letters.append({'letter': c, 'count':0})
    return letters

def sort_on(dict):
    return dict['count']

def letters_count(text):
    letters = []
    init_letters_array(letters)
    text = text.lower()
    for a in text:
        if a.isalpha():
            for l in letters:
                if l['letter'] == a:
                    l['count'] +=1
    letters.sort(reverse=True, key=sort_on)
    return letters
def main():
    text = read_file(path_to_file)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"Word count: {word_count(text)}")
    letters_counted = letters_count(text)
    for l in letters_counted:
       print(f"The letter {l['letter']} appears {l['count']} times")
    print(f"--- End report ---")

main()
