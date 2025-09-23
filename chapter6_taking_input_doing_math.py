# Chapter 6: Taking Input, Doing Math, and Printing It Neatly

# 1. taking input from the user
name = input("What is your name? ")
print("Hello " + name) 

# if you type something and press enter, it will be stored in the variable 'name'

# 2. checking input type
age = input("Enter your age: ")
print(type(age))   # <class 'str'>

# 3. converting input to int
age = int(input("Enter your age: "))
print("Next year you'll be", age + 1)

# 4. math functions

import math

print(math.sqrt(16))     # 4.0 → square root
print(math.pow(2, 3))    # 8.0 → power
print(math.ceil(3.4))    # 4   → round up
print(math.floor(3.9))   # 3   → round down
print(math.pi)           # 3.141592653589793

# string formatting

# option 1
name = "Alice"
age = 25
print(f"{name} is {age} years old")
# Output: Alice is 25 years old

# option 2
name = "Alice"
age = 25
print("{} is {} years old".format(name, age))

# option 3 

name = "Alice"
age = 25
print("%s is %d years old" % (name, age))

# formatting numbers
pi = 3.14159
print(f"Value of pi up to 2 decimals: {pi:.2f}")
# Output: Value of pi up to 2 decimals: 3.14