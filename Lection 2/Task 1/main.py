"""Ask a user for a list of elements and return unique elements"""

lst = input("Enter a comma separated list of elements: ").split(",")

unique = set(lst)

print("Unique elements:", unique)
