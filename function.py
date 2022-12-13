
def invite_to_event(username):
    a = (f"Dear {username}, we have the honour to invite you to our event")

    return a

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global total_trip
    total_trip += 1

    return base_rate + price_per_km*path


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price -= price*discount

    apply_discount()
    return price
# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


def get_fullname(first_name, last_name, middle_name=False):
    if middle_name == False:
        a = (f"{first_name} {last_name}")
    else:
        a = (f"{first_name} {middle_name} {last_name}")

    return a


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

def format_string(string, length):

    if len(string) >= length:
        a = string
    elif len(string) < length:
        b = (length - len(string)) // 2
        d = " "
        a = b*d + string

    return a


# print(format_string(length=15, string='abaa'))

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
def first(size, *numbers):
    size += len(numbers)
    return size


def second(size, **numbers):
    size += len(numbers)
    return size

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


def cost_delivery(quantity, *_, discount=0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""

    cost = 5 * (1-discount) if quantity == 1 else (5 +
                                                   (quantity-1)*2) * (1-discount)
    return cost


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


def number_of_groups(n, k):
    return int(factorial(n)/(factorial(n-k)*factorial(k)))


# print(factorial(5))
# print(number_of_groups(5, 2))

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


def fibonacci(n):
    if n >= 1:
        if 1 <= n < 2:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    elif n < 1:
        return 0


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
