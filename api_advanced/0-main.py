#!/usr/bin/python3
import sys
number_of_subscribers = __import__('0-subs').number_of_subscribers

if __name__ == "__main__":
    print("{:d}".format(number_of_subscribers(sys.argv[1])))
