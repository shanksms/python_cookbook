"""
You want to iterate over a sequence,
but would like to keep track of which element of the sequence is currently being processed
"""
from collections import defaultdict


def enumerate_example(my_list):
    for index, value in enumerate(my_list):
        print(index, value)

def word_summary():
    word_dict = defaultdict(list)
    with open('words.txt') as f:
        lines = f.readlines()

    for index, line in enumerate(lines, 1):
        words = [word.strip().lower() for word in line.split(' ')]
        for word in words:
            word_dict[word].append(index)
    return word_dict

if __name__ == '__main__':
    #enumerate_example(my_list = [1, 2, 3])
    print(word_summary())