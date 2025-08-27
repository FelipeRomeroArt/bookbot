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
