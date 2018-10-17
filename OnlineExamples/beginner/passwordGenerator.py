"""
Write a program to generate new password
"""

import string
import random

newstr = string.digits+string.punctuation+string.ascii_letters
passwordlen = random.randint(8, 40)
pwd = []
count = 0
print("Generating a password of length ",passwordlen)
print("".join(random.sample(newstr, passwordlen)))
