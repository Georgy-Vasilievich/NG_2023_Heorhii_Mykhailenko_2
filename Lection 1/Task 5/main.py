"""Quadratic equation calculation using discriminant"""

import math
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b**2-4*a*c
if D < 0:
    print(f"x1 = {(2*c)/(-b+1j*math.sqrt(abs(D)))}")
    print(f"x2 = {(2*c)/(-b-1j*math.sqrt(abs(D)))}")
else:
    print(f"x1 = {(-b + math.sqrt(D))/(2*a)}")
    if D > 0:
        print(f"x2 = {(-b - math.sqrt(D))/(2*a)}")
