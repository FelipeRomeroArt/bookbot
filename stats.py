def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dir = {}
    for char in text:
        lowchar = char.lower()
        if lowchar in char_dir:
            char_dir[lowchar] += 1
        else:
            char_dir[lowchar] = 1
    return char_dir

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dir):
    list_of_dicts = []
    for char in char_dir:
        num = char_dir[char]
        tmp_dict = {
                "char": char,
                "num": num
                }
        list_of_dicts.append(tmp_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

