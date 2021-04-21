#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[]]
print(canUnlockAll(boxes)) # True

boxes = [[], []]
print(canUnlockAll(boxes)) # False

boxes = [[1], []]
print(canUnlockAll(boxes)) # True

boxes = [[1], [], [2], [0 , 1, 2, 3]]
print(canUnlockAll(boxes)) # False

boxes = [[1], [10, 5, 3], [2], [0 , 1, 2, 3]]
print(canUnlockAll(boxes)) # True
