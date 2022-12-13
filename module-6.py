import shutil
import base64
import re


def total_salary(path):
    fh = open(path, 'r', encoding="utf-8")

    pattern = r'\d+'
    a = 0
    result = []

    while True:
        line = fh.readline()
        result += re.findall(pattern, line)
        if not line:
            break

    fh.close()

    for i in result:
        a += float(i)
    return a


# print(total_salary("test.txt"))


def write_employees_to_file(employee_list, path):
    employee_list_new = []
    if len(employee_list) > 1:
        for i in employee_list:
            employee_list_new.extend(i)
    else:
        employee_list_new.extend(employee_list)

    file = open(path, 'w', encoding="utf-8")
    for a in employee_list_new:
        a = a + "\n"
        file.write(a)

    file.close()

    return


# print(write_employees_to_file(
#     [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19'], ['Alex Stivenson,19']], "test.txt"))


def read_employees_from_file(path):
    employee_list = []
    file = open(path, 'r', encoding="utf-8")
    while True:
        line = file.readline()
        if line != "":
            line = line.replace("\n", "")
            employee_list.append(line)
        if not line:
            break
    file.close()
    return employee_list


# print(read_employees_from_file("test.txt"))


def add_employee_to_file(record, path):
    file = open(path, 'a', encoding="utf-8")
    a = record + "\n"
    file.write(a)
    file.close()
    return


# print(add_employee_to_file("Drake Mikelsson,19", "test.txt"))

def get_cats_info(path):
    with open(path, 'r') as file:
        get_cats = []
        cats = {}
        new_cats = {}
        while True:
            line = file.readline()
            if line != "":
                line = line.replace("\n", "")
                cat_split = line.split(",")

                cats.update(
                    {"id": cat_split[0],
                     "name": cat_split[1],
                     "age": cat_split[2]})
                new_cats = cats.copy()

                print(new_cats)

                get_cats.append(new_cats)

            if not line:
                break

    return get_cats


# print(get_cats_info("test.txt"))


def get_recipe(path, search_id):
    with open(path, 'r') as file:
        while True:
            line = file.readline()
            if line != "" and line.find(search_id) != -1:
                recipe = {}
                line = line.replace("\n", "")
                ingredients = line.split(",")
                id = ingredients.pop(0)
                name = ingredients.pop(0)

                recipe.update({
                    "id": id,
                    "name": name,
                    "ingredients": ingredients

                })
                break
            else:
                recipe = None

            if not line:
                break

    return recipe


# print(get_recipe("test.txt", "60b90c3b13067a15887e1ae4"))


def sanitize_file(source, output):
    with open(source, 'r') as file:
        data = file.read()
        pattern = r'\d+'
        data2 = re.sub(pattern, "", data)

        with open(output, 'w') as file2:
            file2.write(data2)

    return data2


# print(sanitize_file("test.txt", "test2.txt"))


def save_applicant_data(source, output):
    with open(output, "w") as out:
        for i in source:
            line = list(i.values())
            string = ",".join(map(str, line))
            # if source.index(i) != len(source)-1:
            out.write(string + "\n")
            # else:
            #     out.writelines(string)


# print(save_applicant_data([{'name': 'Kovalchuk Oleksiy', 'specialty': 301, 'math': 175, 'lang': 180, 'eng': 155}, {'name': 'Ivanchuk Boryslav',
#       'specialty': 101, 'math': 135, 'lang': 150, 'eng': 165}, {'name': 'Karpenko Dmitro', 'specialty': 201, 'math': 155, 'lang': 175, 'eng': 185}], "test2.txt"))


def is_equal_string(utf8_string, utf16_string) -> bool:
    a = utf8_string.decode('utf-8')
    b = utf16_string.decode('utf-16')
    # print(utf8_string, utf16_string)
    # print(a, b)
    if a.casefold() == b.casefold():
        return True
    else:
        return False


# print(is_equal_string(b'hello', b'\xff\xfeh\x00e\x00l\x00l\x00o\x00'))

def save_credentials_users(path, users_info):
    with open(path, 'wb') as file:
        for key in users_info:
            username = key
            password = users_info.get(key)
            string = username + ":" + password + "\n"
            string_b = string.encode()
            file.write(string_b)
            print(string_b)

# print(save_credentials_users(
#     "test.txt", {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}))


def get_credentials_users(path):
    with open(path, 'rb') as file:
        credentials_users = []
        while True:
            line = file.readline()
            a = line.decode()
            a = a.replace("\n", "")
            if a != "":
                credentials_users.append(a)
            if not line:
                break
    return credentials_users


# print(get_credentials_users("test.txt"))


def encode_data_to_base64(data):
    encode_data = []
    for i in data:
        i_bytes = i.encode("utf-8")
        base64_bytes = base64.b64encode(i_bytes)
        base64_message = base64_bytes.decode("utf-8")
        encode_data.append(base64_message)
        # print(i_bytes, base64_bytes, base64_message)

    return encode_data


# print(encode_data_to_base64(['andry:uyro18890D', 'steve:oppjM13LL9e']))


def create_backup(path, file_name, employee_residence):
    with open(path + '/' + file_name, 'wb') as file:
        for key in employee_residence:
            username = key
            country = employee_residence.get(key)
            string = username + " " + country + "\n"
            string_b = string.encode()
            file.write(string_b)
            print(string_b)

        archive_name = shutil.make_archive(
            'backup_folder', 'zip', path)

    return archive_name


# print(create_backup("test", "backup_folder", {
#       'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}))


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)


# print(unpack("backup_folder.zip", "test"))
