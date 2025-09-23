# Chapter 8: Control Flow in Python, Teaching Your Code to Think

# 1. if statement, Asking a Question

age = 20

if age >= 18:
    print("You are an adult.")

# 2. if-else statement

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 3. if-elif-else statement

marks = 72

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

# 4. nested if statements

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
    else:
        print("You need a license to drive.")
else:
    print("You are too young to drive.")

# Real world examples

# Example 1: Movie Ticket Pricing

age = int(input("Enter your age: "))

if age < 12:
    print("Ticket price: $5")
elif age < 18:
    print("Ticket price: $8")
else:
    print("Ticket price: $12")

# Example 2: ATM Withdrawal

balance = 1000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Transaction successful!")
    balance -= amount
    print("Remaining balance:", balance)
else:
    print("Insufficient funds.")

# Example 3: Password Checker

password = input("Enter password: ")

if password == "python123":
    print("Access granted.")
else:
    print("Access denied.")