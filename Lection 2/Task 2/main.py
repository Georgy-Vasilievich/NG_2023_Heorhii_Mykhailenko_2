"""Ask a user for a list of elements and return numbers"""

lst = []

number = int(input("How many elements do you want to enter? "))

for element in range(number):
    lst.append(input(f"Element {element}: "))

for value in lst:
    if value.isnumeric():
        print(value)
