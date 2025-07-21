#!/usr/bin/python3
import sys
recurse = __import__('2-recurse').recurse

if __name__ == "__main__":
    results = recurse(sys.argv[1])
    if results is not None:
        print(len(results))
    else:
        print("None")
