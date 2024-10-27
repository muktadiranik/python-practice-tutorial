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
