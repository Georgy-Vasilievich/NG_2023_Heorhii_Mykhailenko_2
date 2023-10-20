"""Parse a JSON file and output one of its keys asked by user"""

import json


def search(data):
    """Asks user input and attempts to find a matching key in `data` dictionary
    Recursive if another dictionary is detected"""
    key = input("Enter a key to search for: ")
    if key in data:
        if isinstance(data[key], dict):
            print("Another dictionary detected.")
            search(data[key])
            return
        print(data[key])
    else:
        print("Not found.")


filename = input("Input file name: ")

with open(filename, "r", encoding="utf-8") as f:
    content = json.loads(f.read())

search(content)
