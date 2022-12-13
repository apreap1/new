# import math

# print("{:.100}".format(3.861))

# print(pow(3.86100000000000020961010704923, 20))
# print(pow(3.861, 20))


# print(pow(3.861, 20))
# print(pow(541995938947.92816, 0.05))


# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for a in message:
#     if a == "r":
#         result = result + 1

# print(result)


# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# i = 1
# while i <= num:
#     sum += i
#     i += 1
#     print(sum)


# num = int(input("Enter an integer number: "))

# is_even = True if num % 2 == 0 else False


# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))

# gcd = min(first, second)


# while not (first % gcd == 0 and second % gcd == 0):
#     gcd = gcd - 1

# print(gcd)


# num = int(input("Введіть число (0 для виходу): "))

# while num != 0:
#     repeat = int(input("Скільки разів помножити число на 2? "))
#     for i in range(repeat):
#         num = num * 2
#     print(num)
#     num = int(input("Введіть число (0 для виходу): "))


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


# num = int(input("Enter integer (0 for output): "))
# sum = 0

# while num != 0:
#     for i in range(num):
#         num = num + i

#     sum = sum + num
#     num = int(input("Enter integer (0 for output): "))
# print(sum)


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break

#     for i in range(num + 1):
#         sum = sum + i


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for ch in message:
#     if ord(ch) > 96:
#         pos = ord(ch) - ord('a')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a"))
#     elif 47 < ord(ch) < 91:
#         pos = ord(ch) - ord('A')
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("A"))
#     elif ord(ch) < 47:
#         new_char = ch

#     encoded_message += new_char

# print(encoded_message)


# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

# pool = 1000
# quantity = int(input("Enter the number of mailings: "))
# try:
#     chunk = pool // quantity
# except ZeroDivisionError:
# print('Divide by zero completed!')

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz

# result = 0
# operand = None
# operator = None
# wait_for_number = True

# while True:
#     if wait_for_number == True:
#         operand = input("Enter operand ")
#         try:
#             operand = int(operand)
#             wait_for_number = False

#             if operator == '+':
#                 result = result + operand
#             elif operator == '-':
#                 result = result - operand
#             elif operator == '*':
#                 result = result * operand
#             elif operator == '/':
#                 if operand != 0:
#                     result = result / operand
#                 else:
#                     print("Деление на ноль!")
#             else:
#                 result = operand

#         except ValueError:
#             print(f"{operand} is not a number. Try again.")

#     elif wait_for_number == False:

#         operator = input("Enter operator ")

#         if operator == "+" or operator == "-" or operator == "*" or operator == "/":
#             wait_for_number = True

#         elif operator == "=":
#             break

#         else:
#             print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")

#     print(result)
# print(result)

# zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
import string


def decorator_name(func):
    def wrapper(name, surname):
        result = func(name, surname)
        print("Bye bye")
        return result
    return wrapper


def prefix_decorator_name(func):
    def wrapper(name, surname):
        print("Prefix!")
        result = func(name, surname)
        print("Prefix end")
        return result
    return wrapper


@prefix_decorator_name
@decorator_name
def full_name(name, surname):
    print(f"Hello {name} {surname} ")


full_name("Ivan", "Petrovych")
# ---------------------------------------------------


names = ["ivan", "petro", "oksana", "iryna"]


def normalize(name):
    return name.title()


# 1
new_name = []
for name in names:
    new_name.append(name.title())
print(new_name)

# 2
new_name = map(normalize, names)
print(list(new_name))

# 3
new_name = map(str.title, names)
print(list(new_name))

# 4
new_name = map(lambda name: name.title(), names)
print(list(new_name))

# 5
new_name = [name.title() for name in names]
print(new_name)


class NameTooShortError(Exception):
    pass


class NameStartsFromLowError(Exception):
    pass


def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError


while True:
    try:
        name = enter_name()
        break
    except NameTooShortError:
        print('Name is too short, need more than 3 symbols. Try again.')
    except NameStartsFromLowError:
        print('Name should start from capital letter. Try again.')


# ----------------------------------------------------------
class Mammal:
    phrase = ''

    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)  # Recorded "Meow!"
r.record_animal(dog)  # Recorded "Bark!"
r.record_animal(strange_animal)  # Recorded "Whooooo!!!"
