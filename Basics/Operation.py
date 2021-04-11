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

#----------------------------------------------------#

# Type Conversion
# Python numeric data types can be converted into each other types
# a) int to float
a = 5
a = float(a)
print(type(a))

# b) float to int
b = 5.2
b = int(b)
print(type(b))

# c) int to complex
c = 3
c = complex(c)
print(type(c))

#----------------------------------------------------#

# Casting: There may be time when you to specify a type on to a variable. This can be done with casting.
# Python is an object-oriented language, and as such it uses classes to define data types, including its primitive types.

# Casing is python is therefore using constructor functions:
# int() - constructs an integer number from an integer literal, a float literal(by rounding down to the previous whole number), or a string literal(providing
# the string represents a whole number)
d = 2.5
e = 'Hello'
d = int(d)
e = int(e)
print(tpye(d))
print(type(e))

# float() - consturcts a float number from an interger literal, a float literal, or a string literal(providing the string represents a float or an integer)
f = 2
g = 'Hello'
f = float(f)
g = float(g)
print(tpye(f))
print(type(g))

# str() - constructs a string from a wide variety of data types, inclucing strings, integer literals, and float literals
h = 5
i = 2.5
h = str(h)
i = str(i)
print(tpye(h))
print(type(i))
