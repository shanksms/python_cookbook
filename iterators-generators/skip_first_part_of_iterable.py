"""
Problem: You want to iterate over items in an iterable,
but the first few items aren’t of interest and you just want to discard them.
"""
import itertools
with open('password.txt') as f:
    for line in itertools.dropwhile(lambda l: l.startswith('#'), f):
        print(line, end='')


