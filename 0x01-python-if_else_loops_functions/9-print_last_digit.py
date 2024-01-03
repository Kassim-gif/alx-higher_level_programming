#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_digit = number % -(10)
        print(-(last_digit), end='')
    else:
        last_digit = number % 10
        print(last_digit, end='')
    return abs(last_digit)

# Test the function
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

