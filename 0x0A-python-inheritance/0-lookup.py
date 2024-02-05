#!/usr/bin/python3
"""Defines tha object attribute lookup function."""


def lookup(obj):
    """Returns tha list of an object available attributes."""
    return (dir(obj))
