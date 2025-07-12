#!/usr/bin/python3
"""
3-main
"""
import sys

if __name__ == '__main__':
    count_words = __import__('3-count').count_words
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <subreddit> <list of keywords>")
        print(f"Ex: {sys.argv[0]} programming 'python java javascript'")
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
