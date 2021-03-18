# Data Types
# int
age = 24

# float 
height = 5.11

# string
name = "Rasheed Jan"

# boolean
True
False 

# printing to screen
print("My name is",name,", I am",age, "years old and my height is",height)

# ----------------------------------------- #

# Variables
# variables are dyanamically typed in Python
age = 20 # int
name = "Rasheed Jan" # string

# a variable name cannot start with a number
# 1name = # invalid variable name

# varibles names are case sensitive
name = "Rasheed Jan"
NAME = "Rasheed Jan" # two different variables

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

