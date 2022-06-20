#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for elem in my_list[:x]:
            print(elem, end="")
            counter += 1
        print()
        return counter
    except unknownError:
        ret = print("I don't know what seems to be the problem")
        return ret
