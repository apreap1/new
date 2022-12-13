
import re
from ast import Delete


def real_len(text):
    a = len(text)
    b = 0
    for i in text:
        if i == '\n' or i == '\f' or i == '\r' or i == '\t' or i == '\v':
            b += 1
        # elif i == '\f':
        #     b += 1
        # elif i == '\r':
        #     b += 1
        # elif i == '\t':
        #     b += 1
        # elif i == '\v':
        #     b += 1
    c = a - b
    return c


# print(real_len('Alex\nKdfe23\t\f\v.\r'))


articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    new_articles_dict = []
    for i in articles_dict:
        a = str(i)
        lower_key = key.lower()
        lower_a = a.lower()

        if a.find(key) != -1 and letter_case == True:
            new_articles_dict.append(i)

        elif lower_a.find(lower_key) != -1 and letter_case == False:
            new_articles_dict.append(i)

    return new_articles_dict


# print(find_articles('Ocean', letter_case=False))


def sanitize_phone_number(phone):
    chars = "()-+ "
    new_phone = ""
    for i in phone:
        a = i.strip()
        for c in chars:
            if c in a:
                a = a.replace(c, "")

        new_phone += a
        new_phone_b = new_phone.lstrip()

    return new_phone_b


phone = ["    +38(050)123-32-34",
         "     0503451234",
         "(050)8889900",
         "38050-111-22-22",
         "38050 111 22 11   "]

# print(sanitize_phone_number(phone))


def is_check_name(fullname, first_name) -> bool:
    if fullname.find(first_name) != -1:
        return True
    return False


# print(is_check_name('Alex Old', 'Alex'))

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone


def sanitize_phone_number(phone):
    chars = "()-+ "
    new_phone = []
    for i in phone:
        a = i.strip()
        for c in chars:
            if c in a:
                a = a.replace(c, "")

        new_phone.append(a)

    return new_phone


def get_phone_numbers_for_countries(list_phones):
    a = []
    a = sanitize_phone_number(list_phones)

    UA, JP, TW, SG = [], [], [], []
    phone_numbers = {}
    for i in a:
        if i.find('81') == 0:
            JP.append(i)
        elif i.find('886') == 0:
            TW.append(i)
        elif i.find('65') == 0:
            SG.append(i)
        else:
            UA.append(i)

    phone_numbers.update({"UA": UA, "JP": JP, "TW": TW, "SG": SG})
    return phone_numbers


# print(get_phone_numbers_for_countries(
    # ['065-875-94-11', '(81)8765347', '8867658976', '657658976', '(65)765-89-77']))

def is_spam_words(text, spam_words, space_around=False):
    lower_text = text.lower()
    for i in spam_words:
        b = lower_text.find(i)-1
        d = (lower_text[b])
        if lower_text.find(i) != -1 and space_around == False:
            a = True
        elif lower_text.find(i) != -1 and space_around == True:
            if lower_text.find(i) == 0 or d == " ":
                a = True
            else:
                a = False
        else:
            a = False

    return a


# print(is_spam_words('Ты хорош, но выглядишь как Молох.', ['лох'], True))


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    a = str()
    for i in name:
        a = a + str(TRANS.get(ord(i)))
        a = a.replace("None", " ")

    return a


# print(translate("Юрій Лялюк Григорович"))
# print(TRANS)


grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    i = 0
    sp = []
    for el in students:
        i += 1
        a = students.get(el)
        b = grades.get(a)

        s = "{:>4}|{:<10}|{:^5}|{:^5}".format(i, el, a, b)
        sp.append(s)

    return sp


students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# print(formatted_grades(students))


def formatted_numbers():
    sp = []
    sp.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
    for el in range(16):
        s = '|{:<10d}|{:^10x}|{:>10b}|'.format(el, el, el)
        sp.append(s)
    return sp


# print(formatted_numbers())


def find_word(text, word):
    a = {}
    result = re.search(word, text)
    if result != None:
        first_index, last_index = result.span()
        a.update({
            'result': True,
            'first_index': first_index,
            'last_index': last_index,
            'search_string': result.group(),
            'string': text
        })
    else:
        a.update({
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        })

    return a


# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))


def find_all_words(text, word):
    s = []
    s = re.findall(word, text, re.IGNORECASE)

    return s


# print(find_all_words(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))

def replace_spam_words(text, spam_words):
    p = text
    for i in spam_words:
        p = re.sub(i, '*'*len(i), p, flags=re.IGNORECASE)

    return p


# print(replace_spam_words(
#     'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', ['began', 'Python']))


def find_all_emails(text):
    pattern = r"[A-Za-z]{1}[\w\.]+@[A-Za-z]+\.[A-Za-z]{2,3}"
    result = re.findall(pattern, text)
    return result


# print(find_all_emails('Ima.Fo`ol@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana. or a@test.com abc111@test.com.net'))


def find_all_phones(text):
    pattern = r'\+380\(\d{2}\)\d{3}-\d-\d{3}|\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{3}-\d{4}'
    result = re.findall(pattern, text)
    return result


# print(find_all_phones('Irma + 380(67)777-7-771 second + 380(67)777-77-77 aloha a@test.com abc111@test.com.net + 380(67)111-777-777+380(67)777-77-787'))


def find_all_links(text):
    result = []
    pattern = r"((http|https)\:\/\/)([www]+[.][a-zA-Z0-9]+|[a-zA-Z0-9]+)\.([a-zA-Z]){2,6}"
    iterator = re.finditer(pattern, text)
    for match in iterator:
        result.append(match.group())
    return result


# print(find_all_links('The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com '))
