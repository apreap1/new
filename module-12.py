from copy import deepcopy, copy
import copy
import csv
import json
import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fh:
        pickle.dump(contacts, fh)


def read_contacts_from_file(filename):
    with open(filename, "rb") as fh:
        unpacked = pickle.load(fh)
    return unpacked


# print(write_contacts_to_file("file.dat", [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792',
#       'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}]))
# print(read_contacts_from_file("test.txt"))


def write_contacts_to_file(filename, contacts):
    file_json = {}
    file_json.update({"contacts": contacts})

    with open(filename, "w") as fh:
        json.dump(file_json, fh)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = json.load(fh)
    file_json = unpacked.get("contacts")
    return file_json


# print(write_contacts_to_file("contacts.json", [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792',
#       'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}]))
# print(read_contacts_from_file("contacts.json"))


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as fh:
        field_names = ['name', 'email', 'phone', 'favorite']
        writer = csv.DictWriter(fh, fieldnames=field_names)
        writer.writeheader()
        for i in contacts:
            writer.writerow(i)


def read_contacts_from_file(filename):
    contacts_read = []
    with open(filename, 'r', newline='') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            favorite = True if row['favorite'] == 'True' else False
            dict = {'name': row['name'], 'email': row['email'],
                    'phone': row['phone'], 'favorite': favorite}
            contacts_read.append(dict)
    return contacts_read


# print(write_contacts_to_file("contacts.csv", [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792',
#       'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}]))
# print(read_contacts_from_file("contacts.csv"))


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    count_save = 0

    def __init__(self, filename, contacts):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.count_save = 0
        self.is_unpacking = False

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

# persons = Contacts("user_class.dat", contacts)
# persons.save_to_file()
# first = persons.read_from_file()
# first.save_to_file()
# second = first.read_from_file()
# second.save_to_file()
# third = second.read_from_file()

# print(persons.count_save)  # 0
# print(first.count_save)  # 1
# print(second.count_save)  # 2
# print(third.count_save)  # 3

# person_from_file = persons.read_from_file()
# print(persons.is_unpacking)  # False
# print(person_from_file.is_unpacking)  # True


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    copy_d = copy.copy(person)
    return copy_d


person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

# copy_person = copy_class_person(person)

# print(copy_person == person)  # False
# print(copy_person.name == person.name)  # True


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


def copy_class_person(person):
    return copy.copy(person)


class Contacts:
    def __init__(self, filename, contacts):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True


def copy_class_contacts(contacts):
    copy_d = copy.deepcopy(contacts)
    return copy_d


# persons = Contacts("user_class.dat", contacts)

# new_persons = copy_class_contacts(persons)

# new_persons.contacts[0].name = "Another name"

# print(persons.contacts[0].name)  # Allen Raymond
# print(new_persons.contacts[0].name)  # Another name

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        copy_obj = Person(self.name, self.email, self.phone, self.favorite)
        copy_obj.name = copy.copy(self.name)
        copy_obj.email = copy.copy(self.email)
        copy_obj.phone = copy.copy(self.phone)
        copy_obj.favorite = copy.copy(self.favorite)
        return copy_obj


class Contacts:
    def __init__(self, filename, contacts):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        copy_obj = Contacts(self.filename, self.contacts)
        copy_obj.filename = copy(self.filename)
        copy_obj.contacts = copy(self.contacts)
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Contacts(self.filename, self.contacts)
        memo[id(self)] = copy_obj
        copy_obj.filename = deepcopy(self.filename, memo)
        copy_obj.contacts = deepcopy(self.contacts, memo)
        return copy_obj


person = Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

copy_person = copy.copy(person)

print(copy_person == person)  # False
# print(copy_person.name == person.name)  # True
