# Data Types: Data type is the representation of nature and type of data that has been going to be used in programming
#Python has the following data types by default
#Text type: str
#Numeric types: int, float, complex
#Sequence types: list, tuple, range
#Mapping types: set, frozenset
#Boolean type: bool
#Binary types: Bytes, bytearray, memoryview

# ----------------------------------------- #

# Numeric Types: int, float, complex

#int: A number with no decimal
age = 24
print(type(age))

#float: A number with a decimal
height = 5.11
print(type(height))

#complex: A number with a letter
a = 5j
print(type(a))

# ----------------------------------------- #

# Text/String type: str

#str: Text enclosed in single or double quotes
name = "Rasheed Jan"
print(type(name))

# ----------------------------------------- #

# Sequence Types: list, tuple, range

#list: Can hold same or different types of values/datatypes and enclosed in square brackets
#lists are used to store multiple items in a single variable
#lists are mutable, means that the values can be changed
items = [1, 4, 20.5, 'eggs']
print(type(items))

#tuple: Can hold same or different types of values/datatypes and enclosed in parenthesis
#they are immutable, means that the values cannot be changed
stuff = ('carrot', 'photato', 4, 30.4)
print(type(stuff))

#range: A function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
a = range(9)
print(a)
print(type(a))

# ----------------------------------------- #

# Boolean
True
False 

# ----------------------------------------- #


# Taking input form the user
name = input("Enter your name: ") # input always returns a string
print("You entered:",name)

# ----------------------------------------- #

# Arithmetic Operators
# + --> Addition
x = 3
y = 2
sum = x + y
print("The sum is: ",sum)

# - --> Subtraction
sub = x - y
print("x minus y is: ",sub)

# * --> Multiplication
product = x * y
print("The product is: ",product)

# / --> Division
division = x / y
print("The division is: ",division)

# % --> Modulus
reminder = x % y
print("The reminder is: ",reminder)

# ** --> Exponent/Power
exponent = x ** y
print("x to the power of y is: ",exponent)

# ----------------------------------------- #

# Order of Operation
# python mathematic instructions takes BEDMAS Arithmetic operation
# B - Bracket
# E - Exponent
# D - Division
# M - Multiplication
# A - Addition
# S - Subtraction

x = 2
y = 3
answer = 5 - 3 * (x + y)** 2 # first x + y --> 5, then 5 square --> 25, then 25 multiplied by 3 --> 75 and then 5 - 75 --> -70
print(answer)

# ----------------------------------------- #

