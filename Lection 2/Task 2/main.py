"""Ask a user for a list of elements and return numbers"""

lst = input("Enter a comma separated list of elements: ").split(",")

for value in lst:
    if value.isnumeric():
        print(value)
