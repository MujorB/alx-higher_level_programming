#!/usr/bin/python3
def search_replace(my_list, search, replace):

    newlist = my_list[:]
    list_len = len(my_list)

    for i in range(list_len):
        if newlist[i] == search:
            newlist[i] = replace
    return newlist
