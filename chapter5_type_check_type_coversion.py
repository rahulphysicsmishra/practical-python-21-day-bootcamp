# chapter 5: Type Checking and Type Conversion

name = "Alice"
age = 25
print(name + " is " + age + " years old")  # This will raise a TypeError

# To fix the error, we need to convert the integer 'age' to a string
print(name + " is " + str(age) + " years old")  # Correct way

# Checking types
name = "Alice"
print(type(name))    # <class 'str'>

age = 25
print(type(age))     # <class 'int'>

pi = 3.14
print(type(pi))      # <class 'float'>

is_student = True
print(type(is_student))   # <class 'bool'>

# Converting Between Types

# example 1 - Numbers to Strings

age = 25
print("Alice is " + str(age) + " years old")
# Output: Alice is 25 years old


# example 2 - Strings to Numbers

num1 = "10"
num2 = "20"

# By default, they're strings
print(num1 + num2)     # 1020 (just joins as text)

# Convert to int for math
print(int(num1) + int(num2))   # 30

# example 3 - Float to int

pi = 3.14
print(int(pi))    # 3  (cuts off the decimal, no rounding)

age = 25
print(float(age)) # 25.0


# example 4 - int to bool

print(bool(0))   # False
print(bool(1))   # True
print(bool(10))  # True