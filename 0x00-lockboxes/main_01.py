#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[]]
print("[0]: True = ", end="")
print(canUnlockAll(boxes)) # True

boxes = [[], []]
print("[1]: False = ", end="")
print(canUnlockAll(boxes)) # False

boxes = [[1], []]
print("[2]: True = ", end="")
print(canUnlockAll(boxes)) # True

boxes = [[1], [], [2], [0 , 1, 2, 3]]
print("[3]: False = ", end="")
print(canUnlockAll(boxes)) # False

boxes = [[1], [10, 5, 3], [2], [0 , 1, 2, 3]]
print("[4]: True = ", end="")
print(canUnlockAll(boxes)) # True

boxes = [[1]]
print("[5]: True = ", end="")
print(canUnlockAll(boxes)) # True

boxes = [[]]
print("[6]: True = ", end="")
print(canUnlockAll(boxes)) # True
