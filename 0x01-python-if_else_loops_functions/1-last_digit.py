#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    alx = -(-number % 10)
else:
    alx = (number % 10)
if alx == 0:
    print(f"Last digit of {number} is {alx} and is 0")
elif (alx < 6) != (0):
    print(f"Last digit of {number} is {alx} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {alx} and is greater than 5")
