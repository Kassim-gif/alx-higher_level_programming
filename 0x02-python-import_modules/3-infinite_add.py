#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    print(sum(int(arg, 10) for arg in sys.argv[1:]))

