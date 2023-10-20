"""Ask a user for a file name and output the amount of characters in it
Output a dictionary that has characters as keys and their occurences as values"""

amounts = {}

filename = input("Input file name: ")

with open(filename, "r", encoding="utf-8") as f:
    for char in f.read():
        if char in amounts:
            amounts[char] += 1
        else:
            amounts[char] = 1

print(amounts)
