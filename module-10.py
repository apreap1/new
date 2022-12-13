import string
from collections import UserString
from collections import UserList
from collections import UserDict
import re


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi {self.name}"


p = Person("Boris", 34)
# print(p)


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass  # Порожній блок

    def change_weight(self, weight):
        self.weight = weight
        return self.weight


animal = Animal("Simon", 10)
# print(animal.change_weight(12))


class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color


first_animal = Animal("Simon", 10)
second_animal = Animal("Bob", 15)

# print(first_animal.change_color("red"))


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return f"Meow"


cat = Cat("Simon", 10)

# print(cat.say())


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return f"Woof"


dog = Dog("Barbos", 23, "labrador")

# print(dog.say())


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        owner_dict = {
            'name': self.name,
            'age': self.age,
            'address': self.address
        }
        return owner_dict


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return owner.info()


owner = Owner("Sherlock", 24, "London, 221B Baker Street")
dog = Dog("Simon", 10, "british", owner)

# print(dog.who_is_owner())
# print(owner.info())


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"


# --------------------

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys

# --------------------


class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        return sum

# --------------------


class NumberString(UserString):
    def number_count(self):
        token = re.findall(r"\d+", self.data)
        return len(token)


# --------------------
# Створіть клас IDException, який успадковуватиме клас Exception.

# Також реалізуйте функцію add_id(id_list, employee_id), яка додає до списку id_list ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.

# Функція add_id буде викликати власне виключення IDException, якщо employee_id не починається з '01', інакше employee_id буде додано до списку id_list.


class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    # employee_id_str = str(employee_id)
    if employee_id.find("01", 0, 2) == -1:
        raise IDException
    else:
        id_list.append(employee_id)
    return id_list


# print(add_id([114, 115], "013"))


# Як ми вже говорили, поліморфізм - це здатність програми вибирати різні реалізації при виклику операцій з однією і тією ж назвою.

# Але поліморфізм - це також здатність об'єктів прикидатись чимось іншим. У наведеному вище прикладі Chupakabra прикидалася собакою та кішкою.

# Для коду із завдання вам необхідно реалізувати клас CatDog, не використовуючи успадкування від класу Animal, але щоб екземпляр класу CatDog поводився як і, як екземпляр класу Cat, тобто. він повинен вдати, що він клас Cat.
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


cat = Cat("Barbos", 23)
catdog = CatDog("Barbos", 23)


# Реалізуйте клас Contacts, який працюватиме з контактами. На першому етапі ми додамо два методи.

# list_contacts повертає список контактів це змінна contacts з поточного екземпляра класу
# add_contacts додає новий контакт до списку, який є змінною об'єкту - contacts

# Клас Contacts містить змінну класу current_id. Ми будемо використовувати її при додаванні нового контакту як унікального ідентифікатора контакту. Коли ми додаємо новий контакт, то передаємо такі аргументи в метод add_contacts: name, phone, email та favorite. Метод повинен створити словник із зазначеними ключами та значеннями параметрів функції. Також необхідно додати до словника новий ключ id, значенням якого є значення змінної класу current_id.

# Приклад отриманого словника:

#     {
#         "id": 1,
#         "name": "Wylie Pope",
#         "phone": "(692) 802-2949",
#         "email": "est@utquamvel.net",
#         "favorite": True,
#     }

# Вказаний словник ми додаємо до списку contacts. Не забуваймо збільшувати змінну current_id на одиницю після кожного виклику методу add_contacts для збереження унікальності ключа id для словника.

# Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        print(self.contacts)
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                'id': self.current_id,
                'name': name,
                'phone': phone,
                'email': email,
                'favorite': favorite
            }
        )
        Contacts.current_id += 1


# c = Contacts()
# c.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# print(c.list_contacts())
# c.add_contacts("Cyrus Jackson", "(501) 472-5218",
#                "nibh@semsempererat.com", False)
# print(c.list_contacts())
# --------------------------------------------------------------------------------------------
# Продовжуємо розширювати функціональність класу Contacts. На цьому етапі ми додамо до класу метод get_contact_by_id. Метод повинен шукати контакт по унікальному id у списку contacts та повертати словник з нього із зазначеним ключем id. Якщо словника із зазначеним id у списку contacts не знайдено, метод повертає None.

# Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for i in self.contacts:
            if i.get("id") == id:
                return i


# c = Contacts()
# c.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# print(c.list_contacts())

# print(c.get_contact_by_id(2))
# --------------------------------------------------------------------------------------------

# Завершуємо функціональність класу Contacts. На цьому етапі ми додамо до класу метод remove_contacts. Метод винен видаляти контакт по унікальному id у списку contacts. Якщо словника із зазначеним id у списку contacts не знайдено, метод жодних дій над списком contacts не робить.

# Примітка: для правильного проходження тесту не створюйте екземпляр класу в коді.

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(
            filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        result = list(
            filter(lambda contact: contact.get("id") == id, self.contacts))
        self.contacts.remove(result[0])
        return self.contacts


c = Contacts()
c.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
print(c.list_contacts())

print(c.remove_contacts(1))
