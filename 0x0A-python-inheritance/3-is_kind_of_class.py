#!/usr/bin/python3
"""Defines tha class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if tha object is an instance or inherited instance of tha class.

    Args:
        obj (any): Tha object to check.
        a_class (type): Tha class to match tha type of obj to.
    Returns:
        If obj is tha instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
