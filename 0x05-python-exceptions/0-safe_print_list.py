#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints tha x elememts of a list.

    Args:
        my_list (list): Tha list to print elements from.
        x (int): Tha number of elements of my_list to print.

    Returns:
        Tha number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
