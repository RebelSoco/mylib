import random
import string
import os


# generates string of random words
def wordList(length, seperator, camelCase, list):
    if length < 2:
        raise Exception('Must contain at least 2 words')

    if list == 'large':
        dict_file = '.large.txt'
    elif list == 'medium':
        dict_file = '.medium.txt'
    elif list == 'small':
        dict_file = 'small.txt'
    else:
        raise Exception('Invalid value for dict_list, choices are "large", "medium" or "small"')

    with open(dict_file) as f:
        lst = [line.strip() for line in f]

    pw = ''
    for i in range(length):
        random.seed = (os.urandom(1024))
        if camelCase is True:
            word = random.choice(lst) + seperator
            pw += word.title()
        else:
            pw += random.choice(lst) + seperator

    return pw