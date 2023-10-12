"""Ask a user for a list of elements and return unique elements"""

lst = []

number = int(input("How many elements do you want to enter? "))

for element in range(number):
    lst.append(input(f"Element {element}: "))

unique = set(lst)

print("Unique elements:", unique)
