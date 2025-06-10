#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('making_change').makeChange

print(makeChange([1, 2, 25], 37))
print(makeChange([1, 2, 5], 11))
print(makeChange([2, 5, 10], 3))
print(makeChange([1, 3, 4], 6))
print(makeChange([1, 3, 5, 7, 9], 12))

print(makeChange([1256, 54, 48, 16, 102], 1453))
