import sys
from stats import word_count, char_count, sort_char_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def args(argv):
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(argv) == 2:
        path = argv[1]
    return path

def main():
    book_path = args(sys.argv)
    print("============ BOOKBOT ============")
    text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    num_words = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    char_dir = char_count(text)
    sort_dict = sort_char_dict(char_dir)
    print("--------- Character Count -------")
    j = 0
    for i in sort_dict:
        if sort_dict[j]["char"].isalpha():
            print(f"{sort_dict[j]["char"]}: {sort_dict[j]["num"]}")
        j += 1
    print("============= END ===============")

main()
