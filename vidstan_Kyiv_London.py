import math


# a · x2 + b · x + c = 0
# -2x2 + 7x -6


a = -2
b = 7
c = -6
D = math.pow(b, 2) - 4*a*c
x1 = (-b + math.pow(D, 0.5))/(2*a)
x2 = (-b - math.pow(D, 0.5))/(2*a)

print(f"D - {D}  X1 - {x1} and X2 - {x2}")
