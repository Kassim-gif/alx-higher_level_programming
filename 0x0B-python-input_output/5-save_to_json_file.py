#!/usr/bin/python3
"""Defines tha JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to tha text file using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
