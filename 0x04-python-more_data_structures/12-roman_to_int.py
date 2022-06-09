#!/usr/bin/python3
def roman_to_int(roman_string):

    if roman_string == None or type(roman_string) != str:
        return 0
    val = 0
    sl = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num_l = len(roman_string)
    for i in range(len(roman_string)):
        if i != num_l - 1 and (sl[roman_string[i + 1]] > sl[roman_string[i]]):
            val -= sl[roman_string[i]]
        else:
            val += sl[roman_string[i]]
    return val
