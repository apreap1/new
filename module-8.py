from datetime import datetime, timedelta, date
import re
import random
from decimal import Decimal, getcontext
import collections
from collections import Counter
from collections import deque


def get_days_from_today(date):
    date_split = date.split("-")
    date_datetime = datetime(
        year=int(date_split[0]), month=int(date_split[1]), day=int(date_split[2]))
    current_datetime = datetime.now()
    difference = current_datetime - date_datetime

    return difference.days


# print(get_days_from_today('2021-10-09'))


def get_days_in_month(month, year):
    this_month = datetime(year=year, month=month, day=1)
    if month < 12:
        interval = month + 1
        next_month = datetime(year=year, month=interval, day=1)
        get_days = next_month - this_month
        return get_days.days
    else:
        get_days = 31

        return get_days


# print(get_days_in_month(12, 2021))


def get_str_date(date):
    data_split = re.findall(r"\d+", date)
    date_datetime = datetime(
        year=int(data_split[0]), month=int(data_split[1]), day=int(data_split[2]))

    d = date_datetime.strftime('%A %d %B %Y')

    return d


# print(get_str_date('2021-05-27 17:08:34.149Z'))


def get_numbers_ticket(min, max, quantity):
    get_numbers = []
    a = set()
    if not min < quantity < max or min < 1 or max > 1000:
        return get_numbers
    else:
        while len(a) != quantity:
            i = random.randrange(min, max)
            a.add(i)
        b = list(a)
        b.sort()

    return b


# print(get_numbers_ticket(1, 49, 6))


def get_random_winners(quantity, participants):
    winners = []
    if quantity > len(participants):
        return winners
    else:
        x = participants.keys()
        x = list(x)
        random.shuffle(x)
        winners = random.sample(x, k=quantity)

    return winners


# print(get_random_winners(2, {'605884760742316c07eae603': 'vitanlhouse@gmail.com',
#       '605b89080c318d66862db390': 'elhe2013@gmail.com'}))


def decimal_average(number_list, signs_count):
    a = 0
    b = len(number_list)
    getcontext().prec = signs_count
    for i in number_list:
        a += Decimal(i)
    average = Decimal(a)/Decimal(b)
    return average


# print(decimal_average([3, 5, 77, 23, 0.57], 6))


Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    cats_new = []
    for i in cats:
        if type(i) == dict:
            c_idx = i.get("nickname")
            cat = Cat(i.get("nickname"), i.get("age"), i.get("owner"))
            cats_new.append(cat)
        else:
            cat_dict = {}
            cat_dict.update({"nickname": i.nickname,
                             "age": i.age, "owner": i.owner})
            cats_new.append(cat_dict)

    return cats_new


# print(convert_list([Cat(nickname='Mick', age=5, owner='Sara'), Cat(
#     nickname='Barsik', age=7, owner='Olga'), Cat(nickname='Simon', age=3, owner='Yura')]))
# print(convert_list([{"nickname": "Mick", "age": 5, "owner": "Sara"}, {
#       "nickname": "Barsik", "age": 7, "owner": "Olga"}, {"nickname": "Simon", "age": 3, "owner": "Yura"}, ]))

ips = ['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', '76.98.129.245', '66.50.38.43', '248.95.93.236',
       '173.37.214.238', '76.98.129.245', '76.98.129.245', '85.157.172.253', '66.50.38.43', '66.50.38.43', '66.50.38.43']


def get_count_visits_from_ip(ips):
    count_visits = collections.Counter(ips)
    return count_visits


def get_frequent_visit_from_ip(ips):
    a = get_count_visits_from_ip(ips)
    frequent_visit = a.most_common(1)
    return frequent_visit[0]


# print(get_count_visits_from_ip(ips))
# print(get_frequent_visit_from_ip(ips))

MAX_LEN = 5

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)
    print(element)
    print(lifo)


def pop():
    a = lifo.popleft()
    return a

# ---------------------------------------------------------------------


MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)


def pop():
    a = fifo.popleft()
    return a
