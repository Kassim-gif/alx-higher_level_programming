#!/usr/bin/python3
"""Defines tha text file-reading function."""


def read_file(filename=""):
    """Print tha contents of tha UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
