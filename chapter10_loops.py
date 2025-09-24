# Chapter 10: Loops, Repeat Things Without Rewriting Code

# 1. for loop, Read each character

word = "hello"

for ch in word:
    # ch will be 'h', then 'e', then 'l', ...
    print("Character:", ch)

# count vowels in a name

name = input("Enter your name: ")
vowels = 0

for ch in name.lower():   # lower() so we don't worry about case
    if ch in "aeiou":
        vowels += 1

print("Number of vowels in your name:", vowels)

# 2. while loop, Repeat until a condition is met

answer = ""
while answer.lower() not in ("yes", "no"):
    answer = input("Is it raining? (yes/no): ")
print("You said:", answer)


# Example: Count from 1 to 5 with while
count = 1
while count <= 5:
    print("Count is", count)
    count = count + 1  # update so loop will stop eventually

# 3. break and continue

# Example: Stop on first error (break)
messages = "ok ready error done"
# treat this string as space-separated messages (we haven't taught split/lists),
# so we simulate by checking substring positions -- but here we keep it simple:

for msg in "ok*ready*error*done".split("*"):  # simple split used only as convenience
    if "error" in msg:
        print("Found error:", msg)
        break  # stop searching after first error

# example : skip spaces (continue)
text = "a b c  d"
for ch in text:
    if ch == " ":
        continue  # skip spaces
    print("Letter:", ch)


# 4. avoid infinite loops

i = 0
while i < 3:
    print("hello")
    # forgot to change i -> infinite loop

# Corrected version
i = 0
while i < 3:
    print("hello")
    i += 1

# 5. Practical, real-world examples (stepwise, beginner-friendly)

"""
Example A : PIN retry (while + break)
Ask the user for a 4-digit PIN until correct, allow three attempts:
Real-life: ATM PIN checks.

"""

# Set the correct PIN that the user must enter
correct_pin = "1234"
# Keep track of how many attempts the user has made
attempts = 0
# The user is allowed a maximum of 3 attempts
while attempts < 3:
    # Ask the user to enter a PIN
    pin = input("Enter 4-digit PIN: ")

    # Increase the attempt count after each try
    attempts += 1

    # Check if the entered PIN matches the correct one
    if pin == correct_pin:
        print("PIN accepted. Welcome!")
        break   # Exit the loop immediately since login is successful
    else:
        # If wrong, tell the user how many attempts remain
        print("Wrong PIN. Attempts left:", 3 - attempts)

# The 'else' block of a while loop runs only if the loop was not broken
# i.e., all attempts are used and the correct PIN was never entered
else:
    print("Too many failed attempts. Try later.")

# Example B : Sum numbers until user types 'done'

# Start with total = 0.0 because we want to add up numbers entered by the user
total = 0.0

# Use an infinite loop so the program keeps asking until the user types 'done'
while True:
    # Ask the user to enter a number or 'done' to stop
    s = input("Enter a number (or 'done' to finish): ")

    # If the user types 'done' (any case like DONE/Done), stop the loop
    if s.lower() == "done":
        break

    # Check if the entered value looks like a number
    # s.replace('.', '', 1) removes at most one dot → e.g. "12.5" → "125"
    # .isnumeric() checks if the remaining characters are digits
    if s.replace('.', '', 1).isnumeric():
        # Convert the string to float and add it to the total
        total += float(s)
    else:
        # If the input is not a number or 'done', show an error message
        print("Please enter a valid number or 'done'.")

# After the loop ends, show the final total
print("Total:", total)


# Example C : Password attempts without lists

# Set the correct password
correct_password = "python123"

# Keep track of how many attempts the user has made
tries = 0

# Allow the user a maximum of 5 attempts
while tries < 5:
    # Ask the user to enter the password
    pwd = input("Enter password: ")

    # Increase attempt count after each try
    tries += 1

    # Check if the entered password is correct
    if pwd == correct_password:
        print("Access granted")
        break   # Exit the loop immediately once the password is correct
    else:
        # If wrong password entered, inform the user
        print("Wrong password")
