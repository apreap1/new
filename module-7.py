from setuptools import setup
import re


def do_setup(args_dict):
    setup(**args_dict)
    return


# print(do_setup({'name': 'useful', 'version': '1', 'description': 'Very useful code', 'url': 'http://github.com/dummy_user/useful',
#       'author': 'Flying Circus', 'author_email': 'flyingcircus@example.com', 'license': 'MIT', 'packages': ['useful']}))

def test_zirochka():
    fruits = ['lemon', 'pear', 'watermelon', 'tomato']
    print(fruits[0], fruits[1], fruits[2], fruits[3])
    print(*fruits)

    date_info = {'year': "2020", 'month': "01", 'day': "01"}
    track_info = {'artist': "Beethoven", 'title': 'Symphony No 5'}
    filename = "{year}-{month}-{day}-{artist}-{title}.txt".format(
        **date_info,  **track_info, )
    print(filename)  # '2020-01-01-Beethoven-Symphony No 5.txt'


def transpose_list(list_of_lists):
    # a = []
    # a = zip(*list_of_lists)
    # print(a)
    return [
        list(row)
        for row in zip(*list_of_lists)
    ]


# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))

def do_setup(args_dict, requires):
    a = args_dict
    a.update({'install_requires': requires})
    setup(**a)

    return


# print(do_setup({'name': 'useful', 'version': '1', 'description': 'Very useful code', 'url': 'http://github.com/dummy_user/useful',
#       'author': 'Flying Circus', 'author_email': 'flyingcircus@example.com', 'license': 'MIT', 'packages': ['useful']}, ['markdown']))

def do_setup(args_dict, requires, entry_points):
    a = args_dict
    a.update({'install_requires': requires, 'entry_points': entry_points})
    setup(**a)
    return a


# print(do_setup({'name': 'useful', 'version': '1', 'description': 'Very useful code', 'url': 'http://github.com/dummy_user/useful',
#       'author': 'Flying Circus', 'author_email': 'flyingcircus@example.com', 'license': 'MIT', 'packages': ['useful']}, ['markdown'], {'console_scripts': ['helloworld = useful.some_code:hello_world']}))


def is_integer(s) -> bool:
    s = (s.strip().replace("+", "").replace("-", ""))
    if len(s) >= 1 and s.isdigit():
        return True
    else:
        return False


# print(is_integer("  +34 "))

def capital_text(s):
    upper_word = re.split(r"[.!?]\s+", s)
    for i in upper_word:
        i_upper = i.capitalize()
        s = re.sub(i, i_upper, s)
    return s, upper_word


# print(capital_text("function searches. the? string for! a match, and? returns"))


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    solve = ""
    result = re.search(start_letter, riddle)
    if result != None:
        first_index, last_index = result.span()
        if reverse == False:
            word_length += first_index
            solve = riddle[first_index:word_length:1]
        elif reverse == True:
            word_length = first_index - word_length
            solve = riddle[first_index:word_length:-1]
    return result


# print(solve_riddle('mi1powperet', 3, 'r', True))


def data_preparation(list_data):
    preparation = []
    for i in list_data:
        if len(i) > 2:
            i.sort()
            max = i.pop(0)
            min = i.pop(-1)
            preparation.extend(i)
        else:
            preparation.extend(i)
    preparation.sort()
    preparation.reverse()

    return preparation


# print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))

def token_parser(s):
    if len(s) == 0:
        token = []
    else:
        chars = "()-+*/"
        s = s.replace(" ", "")

        for i in chars:
            s = s.replace(i, " " + i + " ")
            s = s.strip()

        token = re.split(r"\s+", s)

    return token


# print(token_parser("(2+ 3) *4 - 5 * 3"))


def all_sub_lists(data):
    sub_lists = [[]]
    i = 0
    while not i >= len(data):
        a = 0
        b = 0
        i += 1
        while not b >= len(data):
            b = a + i
            slice = data[a:b]
            sub_lists.append(slice)
            a += 1
    return sub_lists


# [[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]
# print(all_sub_lists([4, 6, 1, 3, 5, 9, 5]))


def make_request(keys, values):
    dict_request = {}
    i = 0
    if len(keys) != len(values):
        return dict_request
    else:
        # while i < len(keys):
        #     dict_request.update({keys[i]: values[i]})
        #     i += 1
        for a, b in zip(keys, values):
            dict_request.update({a: b})
    return dict_request


# print(make_request(['name', 'age', 'email'], ['Nick', '23', 'nick@test.com']))


dict = {
    1: ".,?!:",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
    0: " "
}


def sequence_buttons(string):
    string = string.upper()
    seq_buttons = ""
    for i in string:
        for key, value in dict.items():
            if value.find(i) != -1:
                b = value.find(i)+1
                a = str(key)
                seq_buttons += a*b
                break
    return seq_buttons


# print(sequence_buttons('Hi there!'))


def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as file:
        file.write(additional_info)
    with open(path, 'r') as file:
        file.seek(start_pos)
        all_file = file.read(count_chars)

    return all_file


# print(file_operations("test.txt", "Hello", 10, 5))


def get_employees_by_profession(path, profession):
    with open(path, 'r') as file:
        by_profession = []
        line = file.readlines()
        for i in line:
            if i.find(profession) != -1:
                i = i.replace("\n", "")
                by_profession.append(i)

        string = "".join(by_profession).replace(profession, "").strip()

    return string


# print(get_employees_by_profession("test.txt", "courier"))


def to_indexed(source_file, output_file):
    a = 0
    with open(source_file, 'r') as file_s:
        line = file_s.readlines()
        for i in line:
            with open(output_file, 'w') as file_o:
                b = str(a)
                i = b + ": " + i
                file_o.write(i)
            a += 1

    return


# print(to_indexed("test.txt", "test2.txt"))

def flatten(data):
    first_list = list()
    second_list = list()
    if data == []:
        return data
    else:
        first_el = data[0]
        second_el = data[1::]
        if type(first_el) == list:
            return flatten(data[0]) + flatten(data[1::])

        else:
            first_list.append(first_el)
            second_list = flatten(second_el)

    return first_list + second_list


# print(flatten([[5, 6], 2, [3, 4, [5, 6]], 7]))

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))    # 120


def decode(data):
    first_list = list()
    second_list = list()
    if data == []:
        return data
    else:
        first_list.append(data[0])
        second_list = data[1]

    return first_list * second_list + decode(data[0+2::])


# print(decode(["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]))


def encode(data):
    first_list = list()
    a = 0
    if data == [] or data == "":
        data = []
        return data
    else:
        if type(data) == str:
            data_split = re.findall(r"[XYZ]", data)
            return encode(data_split)
        else:
            data_copy = data.copy()
            first_el = data_copy[0]

            for i in data_copy:

                if first_el != i:
                    first_list = [first_el, a]
                    break
                else:
                    last = data.pop(0)
                    a += 1
                    if data == []:
                        first_list = [first_el, a]

    return first_list + encode(data)


# print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))
# ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
