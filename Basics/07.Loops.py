# Python has two primitive loops commands:
# While loop
# for loop

# With the while loop we can execute a set of statements as long as a condition is true.
# Break statement can stop the loop even if the condition is true
# A Continue statement we can stop the current iteration

# while loop
i = 1
while i <= 10:
    print(i)
    i+=1

# break statement
j = 1
while j <= 6:
    print(j)
    if j == 3:
        break
    j = j+1

# continue statement
print only odd numbers
k = 1
while k <= 10:
    if k % 2 != 0:
        print(k)
    k+=1
    continue

# A Continue statement we can stop the current iteration
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method 
# as found in other object-orientated programming languages.

# Looping through a list
Os = ['Windows', 'Linux', 'MacOS']
for item in Os:
    print(item)

# Looping through a String
for i in 'Windows':
    print(i)

# range() function with for loop
for j in range(11):
    print(j)

# range(Start_point, Ends_before_this_point, Step_size)
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
# and stops before a specified number. The former two parameters are optional.

# Else statement with for loop
for k in range(6):
    print(k)
else:
    print('The loop ended')
