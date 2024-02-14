import os
import random


def find_words():
    with open(os.path.join(os.getcwd(), "words_alpha.txt"), "r") as inputfile:
        words = inputfile.read().split()

    # Might be unnecessary, check perf
    # sorted(words)

    if words:
        words_to_replace = input(
            "If you are done, press Enter twice, otherwise, provide the list of words you would like replaced, seperated by spaces, and press Enter:\n").split(" ")

    words_to_replace_structured = {}
    if len(words_to_replace) and words_to_replace[0] != '':
        for word in words_to_replace:
            original_word_length = len(word)
            original_word_start = word[0]
            words_to_replace_structured[word] = []
            for possibility in words:
                if possibility[0] == original_word_start:
                    if len(possibility) == original_word_length:
                        words_to_replace_structured[word].append(possibility)

        return_strings = []
        for index in words_to_replace_structured:
            return_strings.append(words_to_replace_structured[index][random.randint(
                0, len(words_to_replace_structured[index]))])
        return " ".join(return_strings)
    else:
        return 0


if __name__ == "__main__":
    repeat = True
    while repeat:
        result = find_words()
        if result:
            print(result)
        else:
            repeat = False
