x = 0

# for i in range(-100, 101):
#     b = i**3 - 300*i
#     if b == 2961:
#         x = i

# print(x)

# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }


# def calculate_distance(coordinates):
#     if len(coordinates) in (0, 1):
#         return 0
#     return points[tuple(sorted([coordinates[len(coordinates)-2], coordinates[len(coordinates)-1]]))]+calculate_distance(coordinates[:-1])


# print(calculate_distance([0, 1, 3, 2, 0, 2]))


def game(terra, power):
    c = 0 + power
    for i in terra:
        for a in i:
            if a <= power or a <= c:
                c += a
            else:
                break

    return c


print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))
