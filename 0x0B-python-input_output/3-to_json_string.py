#!/usr/bin/python3
"""Defines tha string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return tha JSON representation of a string object."""
    return json.dumps(my_obj)
