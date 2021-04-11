# Operators: Operators are used to perform operations on variable values

# Arithmetic Operators: Arithmetic operators are used with numeric values to perform common mathematical operations. 
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

# ** --> Exponentiation
exponent = x ** y
print("x to the power of y is: ",exponent)

# // --> Floor Division


#---------------------------------------------#

# Assignment Operators: Assignment operators are used to assign values to variables. 
# Operator --> Example --> Same As
# = --> x = 5 --> x = 5
# += --> x += 5 --> x = x + 5
# -= --> x -= 5 --> x = x - 5
# *= --> x* = 5 --> x = x * 5
# /= --> x /= 5 --> x = x / 5
# %= --> x %= 5 --> x = x % 5
# //= --> x //= 5 --> x = x // 5
# **= --> x **= 5 --> x = x ** 5
# &= --> x &= 5 --> x = x & 5
# |= --> x |= 5 --> x = x | 5
# ^= --> x ^= 5 --> x = x ^ 5
# >>= --> x >>= 5 --> x = x >> 5
# <<= --> x <<= 5 --> x = x << 5

#---------------------------------------------#

# Comparison Operators: Comparison operators are used to compare two values. 
# Operator --> Example --> Same As
# == --> Equal --> x == y
# != --> Not Equal --> x != y
# > --> Greater Than --> x > y
# < --> Less Than --> x < y
# >= --> Greater Than or Equal To --> x >= y
# <= --> Less Than or Equal To --> x <= y

#---------------------------------------------#

# Logical Operators: Logical operators are used to combine conditional statements. 
# Operator --> Description --> Example
# and --> Returns True if both statemensts are true --> x < 5 and x < 10
# or --> Returns Ture if one of the statements is true --> x < 5 or x < 4
# not --> Reverse the result, returns False if the result is true --> not(x < 4 and x < 5)

#---------------------------------------------#

# Identity Operators: Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object with the same memory location.
# Operator --> Description --> Example
# is --> Returns True if both variables are the same object --> x is y
# is not --> Returns True if both variables are not the same object --> x is not y

#---------------------------------------------#

# Membership Operators: Membership operators are used to test if a sequence is presented in an object.
# Operator --> Description --> Example
# in --> Returns True if a sequence with a specified value is present in the object --> x in y
# Not in --> Returns True if a sequence with a specified value is not present in the object --> x Not in y

#---------------------------------------------#

# Bitwise Operators: Bitwise operators are used to compare(binary) numbers. 
# Operator --> Name --> Description
# & --> AND --> Sets each bit to 1 if both bits are 1
# | --> OR --> Sets each bit to 1 if one of two bits is 1
# ^ --> XOR --> Sets each bit to 1 if only one of two bits is 1
# ~ --> NOT --> Inverts all the bits
# << --> Zero fill left shift --> Shift left by pushing zeros in from the right to let the left most bits fall off
# >> --> Signed right shift --> Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
