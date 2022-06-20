#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if int(value):
            print("{:d}".format(value))
            return True
        return False
    except ValueError:
        return False
