path_to_file = "books/frankenstein.txt"

def read_file(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def main():
    text = read_file(path_to_file)
    print(text)
    print(f"Word count: {word_count(text)}")

main()
