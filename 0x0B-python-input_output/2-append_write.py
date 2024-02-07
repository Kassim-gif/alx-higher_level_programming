#!/usr/bin/python3
"""Defines tha file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to tha end of a UTF8 text file.

    Args:
        filename (str): Tha name of the file to append to.
        text (str): The string to append to tha file.
    Returns:
        Tha number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
