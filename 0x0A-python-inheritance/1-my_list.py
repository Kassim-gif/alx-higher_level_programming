#!/usr/bin/python3
"""
contains tha MyList class
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initialize tha object"""
        super().__init__()

    def print_sorted(self):
        """printing tha sorted list"""
        print(sorted(self))
