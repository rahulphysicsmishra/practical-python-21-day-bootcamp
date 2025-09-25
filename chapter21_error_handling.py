# Lecture 21: Error Handling, Stay Calm, Fix Things


# 1. errors in python

print(10 / 0)   # ZeroDivisionError
f = open("notfound.txt")  # FileNotFoundError
num = int("hello")        # ValueError

# 2. the try except block

try:
    # code that might fail
    x = 10 / 0
except:
    # code that runs if error happens
    print("Something went wrong!")

# 3. catching specific errors

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("That's not a number, please try again.")


# 4. multiple except blocks

try:
    f = open("mydata.txt")
    data = f.read()
    num = int(data)
    print("Number:", num)
except FileNotFoundError:
    print("File not found, please check the name.")
except ValueError:
    print("File doesn't contain a valid number.")


# 5. using else

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)

# 6. using finally

try:
    f = open("notes.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Done trying to read file.")   # always runs


# 7. real world style examples

# safe division

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Error: Cannot divide by zero


# file reader

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found!"
    except PermissionError:
        return "You don't have permission to open this file."

print(read_file("scores.txt"))
print(read_file("not_exist.txt"))


# atm withdrawal

def withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError("Insufficient balance")  # raise your own error
        balance -= amount
        return balance
    except ValueError as e:
        return str(e)

print(withdraw(5000, 1000))  # 4000
print(withdraw(5000, 7000))  # Insufficient balance