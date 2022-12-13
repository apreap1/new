import re

result = None
operand = None
operator = None
wait_for_number = True

state_iter = 0

while True:
    input_data = input(">>> ")
    if input_data == "=":
        print(result)
        exit()
    if wait_for_number:
        if not re.search(r'^[0-9]*[.,]?[0-9]+$', input_data):
            print("exception")
            continue
    else:
        if (not input_data in '/*-+') or (not len(input_data) == 1):
            print("exception")
            continue

    if state_iter == 0:
        result = input_data
    elif state_iter == 1:
        operator = input_data
    elif state_iter == 2:
        state_iter = 0
        operand = input_data
        if operator == "+":
            result = float(result) + float(operand)
        elif operator == "-":
            result = float(result) - float(operand)
        elif operator == "/":
            result = float(result) / float(operand)
        elif operator == "*":
            result = float(result) * float(operand)
    state_iter += 1
    wait_for_number = not wait_for_number
