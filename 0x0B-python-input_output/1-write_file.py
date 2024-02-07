#!/usr/bin/python3
"""Defines tha file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): Tha name of tha file to write.
        text (str): Tha text to write to tha file.
    Returns:
        Tha number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
