#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_list = len(my_list)

    new_list = my_list[:]

    if len_list > idx >= 0:
        new_list[idx] = element

    return (new_list)
