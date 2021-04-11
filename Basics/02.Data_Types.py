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
print(age)
print(type(age))

#float: A number with a decimal
height = 5.11
print(height)
print(type(height))

#complex: A number with a letter
a = 5j
print(a)
print(type(a))

# ----------------------------------------- #

# Text/String type: str

#str: Text enclosed in single or double quotes
name = "Rasheed Jan"
print(name)
print(type(name))

# ----------------------------------------- #

# Sequence Types: list, tuple, range

#list: Can hold same or different types of values/datatypes and enclosed in square brackets
#lists are used to store multiple items in a single variable
#lists are mutable, means that the values can be changed
items = [1, 4, 20.5, 'eggs']
print(items)
print(type(items))

#tuple: Can hold same or different types of values/datatypes and enclosed in parenthesis
#they are immutable, means that the values cannot be changed
stuff = ('carrot', 'photato', 4, 30.4)
print(stuff)
print(type(stuff))

#range: A function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number
a = range(9)

print(a)
print(type(a))

# ----------------------------------------- #

# Mapping Type: dict
#dict: Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
data = {'name': 'Jhon Doe', 'age': 24, 'weight': 64.5}
print(data)
print(type(data))

# ----------------------------------------- #

# Set Types: set, frozenset
#set: A set is an unordered collection of items. 
# Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# set of integers
my_set1 = {1, 2, 3} # or my_set2 = set(1, 2, 3)
print(my_set1)
print(type(my_set1))

# set of mixed datatypes
my_set2 = {1.0, "Hello", (1, 2, 3)} # or my_set2 = set(1.0, "Hello", (1, 2, 3))
print(my_set2)
print(type(my_set2))

#forzenset: Frozen set is just an immutable version of a Python set object.
# While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 
# Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.
person = ({'name', 'age', 'sex'}) # or person = frozenset('name', 'age', 'sex')
print(person)
print(type(person))

# frozenset(): The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.
# frozenset([iterable])
# iterable (Optional) - the iterable which contains elements to initialize the frozenset with. Iterable can be set, dictionary, tuple, etc.

vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print('The set is now freezed: ', fSet)

# ----------------------------------------- #

# Boolean: bool
#bool: Booleans represent one of two values: True or False .
j = True
k = False 
print(j, k)
print(type(j))
print(type(k))

# ----------------------------------------- #

# Binary types: Bytes, bytearray, memoryview
#bytes
l = b'Hello'
print(l)
print(type(l))

#bytearray
m = bytearray(2)
print(m)
print(type(m))

#memoryview
n = memoryview(bytes(2))
print(n)
print(type(n))
