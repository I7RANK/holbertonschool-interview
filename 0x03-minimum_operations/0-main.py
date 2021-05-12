#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 42
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 7
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))



print("\n =========== MORE TESTS FOR 2 BAD CHECKERS =========== ")
""" MORE TESTS FOR 2 BAD CHECKERS """
n = 1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 2.3
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 111111111111
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 111111111111.1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 0 # infinite loop fixed
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 0.1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = None
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = True
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = "H"
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = [123]
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 1.1
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
