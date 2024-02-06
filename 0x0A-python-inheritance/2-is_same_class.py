#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if tha  object is exactly an instance of tha given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly tha instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
