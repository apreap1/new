import sys
from pathlib import Path
from random import randint
from ast import While

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum += value
    return sum


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

# data = [1, -3, 4, 100, 0, -5, 10, 1, 1]


def prepare_data(data):
    data.sort()
    minimal = 0
    maximum = 0
    for value in data:

        if value > maximum:
            maximum = value
        elif value < minimal:
            minimal = value

    data.remove(minimal)
    data.remove(maximum)

    return data


# print(prepare_data(data))
def prepare_data(data):
    data.sort()

    data.pop(0)
    data.pop()

    return data


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
items = ['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar']


# def format_ingredients(items):

#     new_items = items.copy()
#     # new_items.pop()
#     # new_items.pop()
#     q = len(items)
#     a = str()

#     for i in new_items:
#         a += i + ', '

#     last0 = items.pop(-1)
#     last1 = items.pop(-1)
#     b = a + last1 + ' and ' + last0

#     return q


# print(format_ingredients(items))


# items = ['2 eggs', '1 liter sugar', '1 tsp salt', 'vinegar']

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


def format_ingredients(items):
    a = len(items)
    if a == 0 or a == 1:
        e = ''.join(items)
    elif a == 2:
        e = ' and '.join(items)
    else:
        b = items.pop(-1)
        c = ', '.join(items)
        e = c + ' and ' + b

    return e


# print(format_ingredients(items))

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


def get_grade(key):
    dict = {"F": 1, "FX": 2, "E": 3, "D": 3,
            "C": 4, "B": 5, "A": 5}
    result = dict.get(key)

    return result


def get_description(key):
    dict = {"F": "Unsatisfactorily", "FX": "Unsatisfactorily", "E": "Enough", "D": "Satisfactorily",
            "C": "Good", "B": "Very good", "A": "Perfectly"}
    result = dict.get(key)

    return result


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

def lookup_key(data, value):
    empty_list = []
    for l, a in data.items():

        if a == value:
            empty_list.append(l)

    return empty_list


# print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


def split_list(grade):
    b = []
    c = []
    if len(grade) != 0:
        a = sum(grade)/len(grade)
    else:
        a = 0
    for i in grade:

        if i <= a:
            b.append(i)
        elif i > a:
            c.append(i)

    return b, c


# print(split_list([1, 12, 3, 24, 5]))


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    i = 1
    distance = 0
    if len(coordinates) < 2:
        return 0
    else:
        while i != len(coordinates):
            i += 1
            b = points[tuple(sorted([coordinates[(i)-1],
                                    coordinates[(i)-2]]))]
            distance += b
    return distance


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


# print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1))

def is_valid_pin_codes(pin_codes):

    set_pin_codes = set(pin_codes)

    c = True if len(pin_codes) == len(
        set_pin_codes) and len(pin_codes) > 0 else False

    for i in pin_codes:

        if len(i) == 4 and i.isdigit():
            c = c and True
        else:
            c = False

    return c


# print(is_valid_pin_codes(['1101', '9034', '0013']))


def get_random_password():
    password = str()
    while len(password) < 8:
        random_num = chr(randint(40, 126))
        password += random_num
    return password


# print(get_random_password())


def is_valid_password(password):

    a = True if len(password) == 8 else False
    b = False
    c = False
    d = False

    for i in password:
        if 65 <= ord(i) <= 90:
            b = True
        elif 97 <= ord(i) <= 122:
            c = True
        elif 48 <= ord(i) <= 57:
            d = True

    valid = a and b and c and d
    return valid


# print(is_valid_password('NmlDl1V0'))


def get_password():
    i = 0
    while i < 100:
        a = get_random_password()
        if is_valid_password(a):
            break
        else:
            i += 1
            continue

    print(is_valid_password(a))
    print(i)
    return a


print(get_password())


# p = Path('/Users/qwerty/Downloads')  # p Вказує на теку /home/user/Downloads
# for i in p.iterdir():
#     print(i.name)  # Виведе у циклі імена всіх тек та файлів у /home/user/Downloads


def parse_folder(path):
    files = []
    folders = []
    for i in Path(path).iterdir():

        if i.is_dir():
            folders.append(i.name)
        else:
            files.append(i.name)
    return files, folders


print(parse_folder('/Users/qwerty/Downloads'))


def parse_args():
    result = ''
    i = 0
    for arg in sys.argv:
        a = len(sys.argv)

        if 0 < i < len(sys.argv)-1:
            result += str(arg) + " "
        elif i == len(sys.argv)-1:
            result += str(arg)
        i = i + 1

    return result


# print(parse_args())


# print(parse_args())
