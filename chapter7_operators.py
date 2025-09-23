# Chapter 7: Operators in Python, The Tools Behind Every Decision

# 1. assignment operator (=)

age = 20

# shortcut
score = 10
score += 5   # same as score = score + 5
print(score) # 15

# 2. arithmetic operators: +, -, *, /, %, **, //
print(10 + 5)   # 15
print(10 - 3)   # 7
print(4 * 2)    # 8
print(10 / 3)   # 3.333... (normal division, always gives float)
print(10 // 3)   # 3 (floor division, cuts off decimal)
print(10 % 3)   # 1 (modulus, gives remainder)
print(2 ** 3)   # 8 (2 raised to power 3)

# 3. comparison operators: ==, !=, >, <, >=, <=
print(5 == 5)   # True (equal to)
print(5 != 3)   # True (not equal)
print(10 > 7)   # True
print(2 < 5)    # True
print(7 >= 7)   # True
print(3 <= 2)   # False

# 4. logical operators: and, or, not
age = 20
has_license = True

print(age >= 18 and has_license)   # True
print(age >= 18 or has_license)    # True
print(not has_license)             # False

# intro to if else

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")