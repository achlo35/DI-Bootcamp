# Exercise 3: String module

import string
import random

letters = string.ascii_letters

random_string = ''
for _ in range(5):
    random_string += random.choice(letters)

print("Random string of 5 characters:", random_string)