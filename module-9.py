from functools import reduce
import re


def get_grade(key):
    grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
    return grade.get(key, None)


def get_description(key):
    description = {
        "A": "Perfectly",
        "B": "Very good",
        "C": "Good",
        "D": "Satisfactorily",
        "E": "Enough",
        "FX": "Unsatisfactorily",
        "F": "Unsatisfactorily",
    }
    return description.get(key, None)


def get_student_grade(option):
    if option == "grade":
        return get_grade
    elif option == "description":
        return get_description
    else:
        return None


# print(get_student_grade("grade"))

DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    discount = customer.get("discount", None)
    if discount != None:
        price = price * (1 - discount)
    else:
        price = price * (1 - DEFAULT_DISCOUNT)

    return price


# print(get_discount_price_customer(10, {"name": "Boris", "discount": 0.15}))


def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n > 0:
            if 0 < n < 3:
                result = 1
            else:
                if n in cache:
                    result = cache[n]
                    print(f"{n} in cache {result}")
                else:
                    result = fibonacci(n - 1) + fibonacci(n - 2)
                    cache[n] = result
                    print(f"{n} not in cache {result}")
        else:
            return 0

        return result

    return fibonacci


# fib = caching_fibonacci()
# f5 = fib(5)
# print(f"f(5): {f5}")

# f8 = fib(8)
# print(f"f(8): {f8}")

# f10 = fib(10)
# print(f"f(10): {f10}")


def discount_price(discount):
    def cost(price):
        cost_price = price * (1 - discount)

        return cost_price

    return cost

# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)

# price = 100
# print(cost_15(price))
# print(cost_10(price))
# print(cost_05(price))


# phone = ["    +38(050)123-32-34",
#          "     0503451234",
#          "(050)8889900",
#          "38050-111-22-22",
#          "38050 111 22 11   "]


def format_phone_number(func):
    def wrapper(phone):
        result = func(phone)
        if len(result) == 10:
            result = "+38" + result
        elif len(result) == 12:
            result = "+" + result
        return result
    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .replace("+", "")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )

    return new_phone


# print(sanitize_phone_number(' +38(050)123-32-34'))

string = 'The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100.'


def generator_numbers(string=""):
    token = re.findall(r"\d+", string)
    x = 0
    while x < len(token):
        yield token[x]
        x += 1


def sum_profit(string):
    five_to_ten_generator = generator_numbers(string)
    sum = 0
    for i in five_to_ten_generator:
        i = int(i)
        sum += i

    return sum


# print(sum_profit(string))


def normal_name(list_name):
    new_name = map(lambda name: name.title(), list_name)
    return list(new_name)


# print(normal_name(['dan', 'jane', 'steve', 'mike']))


def get_emails(list_contacts):
    list_emails = map(lambda emails: emails.get('email'), list_contacts)
    return list(list_emails)


# print(get_emails([{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net',
#       'phone': '(542) 451-7038', 'favorite': False}, {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': False}]))


def positive_values(list_payment):
    positive = filter(lambda x: x > 0, list_payment)
    return list(positive)


# print(positive_values([100, -3, 400, 35, -100]))

def get_favorites(contacts):
    favorites = filter(lambda x: x.get('favorite'), contacts)
    return list(favorites)


# print(get_favorites([{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, {'name': 'Kennedy Lane',
#       'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True}, {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]))


def sum_numbers(numbers):
    result = reduce((lambda x, y: x + y), numbers, 0)
    return result


# print(sum_numbers([3, 4, 6, 9, 34, 12]))


def amount_payment(payment):

    result = reduce((lambda x, y: x + y),
                    filter(lambda x: x > 0, payment), 0)
    return result


print(amount_payment([100, -3, 400, 35, -100]))
