# for loops

print("for loops")
for i in range(10):
    print(i)

# Give some examples of arrays and lists

array = [1, 2, 3, 4, 5]
lists = [1, 2, 3, 4, 5]

print(array[1])
print(lists[1])

# Example of for in with start, stop and step
print("Example of for in with start, stop and step")
for i in range(1, 10, 2):
    print(i)

# Print all odd numbers from 1 to 10
print("Print all odd numbers from 1 to 10")
for i in range(1, 10, 2):
    print(i)

# Write it using modulo operator
print("Write it using modulo operator")
for i in range(1, 10):
    if i % 2 == 1:
        print(i)

print("Height of the tree")
tree = """
    #
   ###
  #####
 #######
#########
    #
"""
# What is the height of the tree
# se a while list and 3 for loops

tree_height = 6
spaces = tree_height - 1

hashes = 1
stump_spaces = tree_height - 1

for i in range(stump_spaces):
    print(" " * spaces, end="")
    print("#" * hashes)
    spaces -= 1
    hashes += 2

print()

spaces -= 1
hashes += 2
tree_height -= 1

for i in range(stump_spaces):
    print(" " * spaces, end="")

print("#")

# This is a python advanced tutorial
# Give as much info and examples as possible

a = 10
b = 20
c = 30

if a > b:
    print("a is greater than b")
elif b > c:
    print("b is greater than c")
else:
    print("b is equal to c")

# This is a python advanced tutorial
# Give as much info and examples as possible


random_string = """           this is a random string and this is another random string, this is yet another random string      """
print(f"random_string: {random_string}")
print(f"random_string.strip(): {random_string.strip()}")
print(f"random_string.lstrip(): {random_string.lstrip()}")
print(f"random_string.rstrip(): {random_string.rstrip()}")
print(f"random_string.split(): {random_string.split()}")
print(f"random_string.splitlines(): {random_string.splitlines()}")
print(f"random_string.title(): {random_string.title()}")
print(f"random_string.upper(): {random_string.upper()}")
print(f"random_string.lower(): {random_string.lower()}")
print(f"random_string.capitalize(): {random_string.capitalize()}")
print(f"random_string.swapcase(): {random_string.swapcase()}")
print(f"random_string.count('r'): {random_string.count('r')}")

# Create a string list
string_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(f"string_list: {string_list}")
for i in string_list:
    print(i)
print()
print(f"string_list[0:5]: {string_list[0:5]}")
print(f"string_list[5:10]: {string_list[5:10]}")
print(f"string_list[0:10:2]: {string_list[0:10:2]}")

# Create an integer list
integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"integer_list: {integer_list}")
for i in integer_list:
    print(i)
print()
print(f"integer_list[0:5]: {integer_list[0:5]}")
print(f"integer_list[5:10]: {integer_list[5:10]}")
print(f"integer_list[0:10:2]: {integer_list[0:10:2]}")
print(f"integer_list[::-1]: {integer_list[::-1]}")
print(f"integer_list[::-2]: {integer_list[::-2]}")
print(f"integer_list[5::-2]: {integer_list[5::-2]}")
print(f"integer_list[5:0:-2]: {integer_list[5:0:-2]}")
print(f"integer_list[5:1:-2]: {integer_list[5:1:-2]}")
print(f"integer_list[::]: {integer_list[::]}")
print(f"integer_list[1:]: {integer_list[1:]}")
print(f"integer_list[:]: {integer_list[:]}")
print(f"integer_list[:-1]: {integer_list[:-1]}")
print(f"integer_list[:1]: {integer_list[:1]}")
print(f"integer_list[:-2]: {integer_list[:-2]}")

print(f"How many elements are in the list? {len(integer_list)}")
print("How many 'is' are in the random string?", random_string.count("is"))
print("Where is 'string' in the random string?", random_string.find("string"))
print(
    "Replace 'random' with 'randomly' in the random string",
    random_string.replace("random", "randomly"),
)

"""
Convert to Acronym: Random Access Memory
"""
# Convert to Acronym: Random Access Memory
original_string = (
    "This is the original string that was before being converted to acronym"
)
list_or_words = original_string.split()

for word in list_or_words:
    print(word, word[0], word[-1], end="")

print()

letter_z = "z"
number_3 = 3
a_space = " "

print(f"Is z a number or letter? {letter_z.isalnum()}")
print(f"Is 3 a letter? {str(number_3).isalpha()}")
print(f"Is a space a letter? {a_space.isspace()}")
print(f"Is z is in uppercase? {letter_z.isupper()}")
print(f"Is z is in lowercase? {letter_z.islower()}")


def is_float(string_value):
    try:
        float(string_value)
        return True
    except ValueError:
        return False


print(is_float("10.0"))
print(is_float("10"))


def is_int(string_value):
    try:
        int(string_value)
        return True
    except ValueError:
        return False


print(is_int("10.0"))
print(is_int("10"))

message = """This is a message which contains nothing but a random string. It is also a random string. It is totally AI generated."""
secret_message = ""

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += 2

        if char.isupper():
            if char_code > ord("Z"):
                char_code -= 26
            elif char_code < ord("A"):
                char_code += 26
        else:
            if char_code > ord("z"):
                char_code -= 26
            elif char_code < ord("a"):
                char_code += 26
        secret_message += chr(char_code)

    else:
        secret_message += char

print(f"secret_message: {secret_message}")

original_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code -= 2

        if char.isupper():
            if char_code < ord("A"):
                char_code += 26
        else:
            if char_code < ord("a"):
                char_code += 26
        original_message += chr(char_code)

    else:
        original_message += char

print(f"original_message: {original_message}")


def add_numbers(a, b):
    return a + b


print(f"add_numbers(10, 20): {add_numbers(10, 20)}")


def assign_name(name):
    name = "John"


name = "Alice"
assign_name(name)
print(f"name: {name}")


def change_name(old_name, new_name):
    old_name = new_name
    return old_name


print(f"change_name(name, 'Bob'): {change_name(name, 'Bob')}")

# Define globally accessible variables
global_variable = 10


def modify_global_variable():
    global global_variable
    global_variable += 1
    return global_variable


print(f"modify_global_variable(): {modify_global_variable()}")
print(f"global_variable: {global_variable}")


def solve_equation(equation):
    num_1, operation, num_2 = equation.split()
    num_1, num_2 = int(num_1), int(num_2)
    return (
        f"{num_1} {operation} {num_2} = {num_1 + num_2}",
        f"{num_1} {operation} {num_2} = {num_1 - num_2}",
    )


print(solve_equation("5 + 5"))


# Create a function that returns more than one result
def add_numbers(a, b):
    return a + b, a - b


print(f"add_numbers(10, 20): {add_numbers(10, 20)}")


def multiply_divide(a, b):
    return a * b, a / b


print(f"multiply_divide(10, 20): {multiply_divide(10, 20)}")


def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(f"is_prime(10): {is_prime(10)}")
print(f"is_prime(11): {is_prime(11)}")


def get_prime_numbers(n):
    prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers


print(f"get_prime_numbers(10): {get_prime_numbers(10)}")
prime_numbers = get_prime_numbers(100)


def sum_all(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")


def get_sum_of_all_prime_numbers(n):
    prime_numbers = get_prime_numbers(n)
    return sum_all(*prime_numbers)


print(f"get_sum_of_all_prime_numbers(10): {get_sum_of_all_prime_numbers(100)}")

import math


def rectangle_area(width, height):
    return width * height


def circle_area(radius):
    return math.pi * radius * radius


def get_area(shape):
    shape = shape.lower()
    if shape == "circle":
        return circle_area(10)
    elif shape == "rectangle":
        return rectangle_area(10, 20)
    else:
        return 0


print(f"get_area('circle'): {get_area('circle')}")
print(f"get_area('rectangle'): {get_area('rectangle')}")

import random

random_list = ["string", 1, 2.2, True, None]
for i in random_list:
    print(i)

one_to_ten = list(range(11))
for i in one_to_ten:
    print(i)

random_list = random_list + one_to_ten
for i in random_list:
    print(i)

first_3 = random_list[:3]
last_3 = random_list[-3:]

print(f"len(random_list): {len(random_list)}")
print(f"first_3(random_list): {random_list[:3]}")
print(f"last_3(random_list): {random_list[-3:]}")
print(f"'string' in random_list: {'string' in random_list}")
print(f"first_3 * 3: {first_3 * 3}")
print(f"last_3 * 3: {last_3 * 3}")
print(f"index of 'string' in random_list: {random_list.index('string')}")
print(f"How many 'string' are in the list? {random_list.count('string')}")

random_list[0] = "new string"
print(f"random_list: {random_list}")

random_list.append("new string")
print(f"random_list: {random_list}")

number_list = []
for i in range(10):
    number_list.append(random.randrange(0, 100))
print(f"number_list: {number_list}")

i = len(number_list) - 1

while i > 1:
    j = 0
    while j < i:
        print(f"i: {i}, j: {j}")
        print()

        if number_list[j] > number_list[j + 1]:
            temp = number_list[j]
            number_list[j] = number_list[j + 1]
            number_list[j + 1] = temp
        else:
            j += 1

        for k in number_list:
            print(k)
        print()
    i -= 1

for k in number_list:
    print(k, end=" ")

print()

number_list = [random.randrange(1, 100) for i in range(10)]
number_list.sort()
for i in number_list:
    print(i, end=" ")

print()

number_list.insert(2, 50)
for i in number_list:
    print(i, end=" ")

print()

number_list.remove(50)
for i in number_list:
    print(i, end=" ")

print()

print(f"number_list.pop(0): {number_list.pop(0)}")

even_numbers = [i * 2 for i in range(10)]
for i in even_numbers:
    print(i, end=" ")

print()

values = [[math.pow(i, 2), math.pow(i, 3), math.pow(i, 4)] for i in range(5)]
print(f"values: {values}")

multi_dimensional_list = [[0] * 10 for i in range(5)]
print(f"multi_dimensional_list: {multi_dimensional_list}")

multi_dimensional_list[0][0] = 1
print(f"multi_dimensional_list: {multi_dimensional_list}")

list_table = [[0] * 10 for i in range(5)]
for i in list_table:
    for j in i:
        print(j, end=" ")
    print()

for i in range(list_table.__len__()):
    for j in range(list_table[i].__len__()):
        list_table[i][j] = random.randint(0, 100)

for i in list_table:
    for j in i:
        print(j, end=" ")
    print()

print()

for i in range(len(list_table)):
    for j in range(len(list_table[i])):
        list_table[i][j] = i * j

print()

for i in list_table:
    for j in i:
        print(j, end=" ")
    print()

print()

random_value_multi_dimensional_list = [[random.randint(0, 100)] * 10 for i in range(5)]
for i in random_value_multi_dimensional_list:
    for j in i:
        print(j, end=" ")
    print()

print()
