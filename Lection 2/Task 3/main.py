"""Print all numbers from 1 to a user-specified integer in one column,
also print all their divisors in another column.
In the end, print all primes."""


def get_divisors(number):
    """Returns all divisors of a number"""
    divisors = []
    for integer in range(1, int(number / 2) + 1):
        if number % integer == 0:
            divisors.append(integer)
    divisors.append(number)
    return divisors


primes = []
max_number = int(input("Enter a number: "))

for num in range(1, max_number + 1):
    divisors = get_divisors(num)
    if len(divisors) == 2:
        primes.append(num)
    print(f"{num}\t{', '.join(map(str,divisors))}")

if primes:
    print(", ".join(map(str, primes)))
