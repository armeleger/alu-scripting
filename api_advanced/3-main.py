#!/usr/bin/python3
import sys
count_words = __import__('3-count').count_words

if __name__ == "__main__":
    count_words(sys.argv[1], [x for x in sys.argv[2].split()])
