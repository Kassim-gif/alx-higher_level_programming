#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        print("{}".format(char), end="")
    print()

