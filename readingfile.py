import json

with open('LearningPython.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open('LearningPython.txt') as file_object:
    lines = file_object.readlines()
    print(lines)
