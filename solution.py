import os.path
import datetime

# counts the number of operations and operands
def count_int_and_str(clean_list):
    count_int = 0
    count_str = 0
    for i in clean_list:
        if i.isdigit():
            count_int += 1
        elif check_float(i):
            count_int += 1
        else:
            count_str += 1
    return count_str < count_int


# error handling
def get_value(clean_list, expression):

    if len(clean_list) > 2:
        pass
    else:
        return False, "Invalid input lenght: smaller than 3"
    # last character of input cannot be an operation
    if clean_list[-1].isdigit() or check_float(clean_list[-1]):
        pass
    else:
        return False, "Invalid input format: last character is operation"
    # fist character of input cannot be an operand
    if not clean_list[0].isdigit():
        pass
    else:
        return False, " Invalid input format: first character is operand"
    # number of operands in input has to be bigger than that of operations
    if count_int_and_str(clean_list):
        pass
    else:
        return False, " Invalid input format: more operations than operands in input"

    for i in expression:
        if (
                i.isdigit()
                or i == "."
                or i == "+"
                or i == "-"
                or i == "*"
                or i == "/"
                or i == " "
        ):
            pass
        elif expression.find("add") or expression.find("sub") or expression.find("mul") or expression.find("div"):
            pass
        else:
            return False, "Invalid operation symbol"

    return True, "Valid"


# converts string containing float number to type float
def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False


# gets rid of unwanted white spaces from input
def cast_input(input_string):
    numbers = []
    for word in input_string.split():
        if word.isdigit():
            numbers.append(word)
        elif check_float(word):
            numbers.append(word)
        elif word == "+" or word == "-" or word == "*" or word == "/" or word == "add" or word == "sub" or word == "mul" or word == "div":
            numbers.append(word)

    return numbers


# calculator driver function
def calculator(numbers):
    stack = []
    numbers.reverse()
    for i in numbers:
        if i.isdigit():
            stack.append(int(i))
        elif check_float(i):
            stack.append(float(i))
        else:
            if i == "+" or i == "add":
                stack[-2] = stack[-2] + stack[-1]
                stack.pop(-1)
            elif i == "-" or i == "sub":
                stack[-2] = stack[-2] - stack[-1]
                stack.pop(-1)
            elif i == "*" or i == "mul":
                stack[-2] = stack[-2] * stack[-1]
                stack.pop(-1)
            elif i == "/" or i == "div":
                stack[-2] = stack[-2] / stack[-1]
                stack.pop(-1)
    return stack


def main(expression):
    clean_list = cast_input(expression)
    a = get_value(clean_list, expression)

    if not a[0]:
        return a
    else:
        output = calculator(clean_list)
        return True, output


def log():
    with open("output_1.txt", "a+") as fd:
        if os.stat("output_1.txt").st_size != 0:
            with open("output_1.txt", "r") as f:
                lines = f.read().splitlines()
                last_line = lines[-2]
                INFO = int(last_line[14])
                ERROR = int(last_line[-1])
        else:
            INFO = 0
            ERROR = 0

        now = datetime.datetime.now()
        fd.write("Data: ")
        fd.write(now.strftime("%Y-%m-%d %H:%M:%S\n"))

        if main_result[0]:

            INFO += 1
            fd.write("{} {}\n".format("Expression:", expression))
            fd.write("{} {}\n".format("Result:", main_result[1][0]))
            fd.write("{}  INFO-{}  ERROR-{}\n\n".format("Report:", INFO, ERROR))
        else:

            ERROR += 1
            fd.write("{} {}\n".format("Expression:", expression))
            fd.write("{} {}\n".format("ERROR:", main_result[1]))
            fd.write("{}  INFO-{}  ERROR-{}\n\n".format("Report:", INFO, ERROR))


expression = input()
main_result = main(expression)
log()
