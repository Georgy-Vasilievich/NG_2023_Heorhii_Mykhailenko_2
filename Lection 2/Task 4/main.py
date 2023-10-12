"""Output only vowels from a user-specified string"""

string = input("Enter a string: ")

for letter in string:
    if letter in "aeiou":
        print(letter, end="")

print("")  # newline
