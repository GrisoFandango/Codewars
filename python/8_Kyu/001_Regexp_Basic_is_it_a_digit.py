# https://www.codewars.com/kata/regexp-basics-is-it-a-digit/train/python

# 8 kyu

# Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.
import string


def is_digit(n):
    return n.is_digit() and len(n) == 1
