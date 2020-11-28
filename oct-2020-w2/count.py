from collections import Counter
import re


def count_words(words):
    s = re.findall(r"'?\w[\w']*", words.lower())
    return Counter(s)
