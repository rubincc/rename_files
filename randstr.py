#!/usr/bin/env python3
# 07.02.2020 - 12:15 - CCR
# A function that generates random strings

import random, string

# generates random string using the random.choice() method
# randomly can repeat some characters
def rnd_str0(str_length = 5):
    # word = string.ascii_lowercase # string of only lowercase characters
    # word = string.ascii_uppercase # string of only uppercase characters
    word = string.ascii_letters # string of upper and lower case characters
    return ''.join(random.choice(word) for n in range(str_length))


print("Random0 string default 5:", rnd_str0())
print("Random0 string of 8:", rnd_str0(8))
print("Random0 string of 12:", rnd_str0(12))
print("Random0 string of 3:", rnd_str0(3))

# generates a random string using the random.sample() method
# does not repeat characters in the string
def rnd_str1(str_length=5):
    word = string.ascii_letters
    return ''.join(random.sample(word,str_length))

print("Random1 string of 5:", rnd_str1(5))
print("Random1 string of 10:", rnd_str1(10))

