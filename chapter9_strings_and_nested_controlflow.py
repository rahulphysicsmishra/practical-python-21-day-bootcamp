# Chapter 9: Strings in Depth + Nested Control Flow

# strings example

name = "Rahul"
greeting = 'Hello there'

# strings indexing

word = "Python"

print(word[0])   # P (first letter)
print(word[1])   # y
print(word[5])   # n (last letter)

# negative indexing

word = "Python"

print(word[-1])   # n (last character)
print(word[-2])   # o

# slicing strings

text = "Hello, World"

print(text[0:5])   # Hello (0 to 4)
print(text[:5])    # Hello (start is optional)
print(text[7:])    # World (end is optional)

# string methods

# changing case
msg = "Python is Fun"

print(msg.lower())   # python is fun
print(msg.upper())   # PYTHON IS FUN

# removing whitespace
text = "   hello   "
print(text.strip())   # hello

# checking content

print("123".isnumeric())   # True
print("hello".isalpha())   # True (letters only)
print("abc123".isalnum())  # True (letters + numbers)

# finding things

sentence = "I love Python"
print(sentence.startswith("I"))    # True
print(sentence.endswith("Python")) # True
print("love" in sentence)          # True (checks if word exists)

# strings with control flow

# example : password  check
password = input("Enter password: ")

if password.lower() == "python123":
    print("Access granted.")
else:
    print("Wrong password.")

# nested examples

"""
Example 1: Coffee Order
Write a Python program that asks the user to order a coffee.
The user should be able to enter the coffee size (small / medium / large).


The program should set the base price as:


Small → ₹100


Medium → ₹150


Large → ₹200


Next, ask the user if they want an extra shot (yes/no). 
If yes, add ₹30 to the price.


Finally, display the total coffee price.

"""

size = input("Enter coffee size (small/medium/large): ").lower()
extra_shot = input("Do you want an extra shot? (yes/no): ").lower()

if size == "small":
    price = 100
elif size == "medium":
    price = 150
else:
    price = 200

if extra_shot == "yes":
    price += 30

print(f"Your final coffee price is ₹{price}")


"""
Example 2: Online Login System
Write a Python program that simulates a simple login system.
Ask the user to enter a username and password.


If the username is "admin" (case-insensitive) and the password is "1234", display "Welcome Admin!"


If the username is "admin" but the password is wrong, display "Wrong password."


For any other username, display "Unknown user."

"""

username = input("Enter username: ")
password = input("Enter password: ")

if username.lower() == "admin":
    if password == "1234":
        print("Welcome Admin!")
    else:
        print("Wrong password.")
else:
    print("Unknown user.")



"""
Example 3: Festival Discount System
Write a Python program that calculates a discount on a customer’s bill.
Ask the user to enter their bill amount.


Ask if today is a festival (yes/no).


Apply discounts based on these rules:


If the bill is ₹500 or more:


Festival day → 30% discount


Normal day → 20% discount


If the bill is less than ₹500:


Festival day → 10% discount


Normal day → No discount


Finally, display the final amount after discount.

"""


bill = float(input("Enter your bill amount: "))
festival = input("Is there a festival today? (yes/no): ").lower()

if bill >= 500:
    if festival == "yes":
        discount = 0.3   # 30% during festival
    else:
        discount = 0.2   # 20% normal
else:
    if festival == "yes":
        discount = 0.1
    else:
        discount = 0.0

final_amount = bill - (bill * discount)
print(f"Final bill after discount: ₹{final_amount}")


