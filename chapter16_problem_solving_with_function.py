# Lecture 16: Problem Solving with Functions

# Example 1 : Greeting Users

"""
Situation:
You are building a website where you need to greet many users. Without a function, you’d repeat:

"""

print("Hello Rahul, welcome!")
print("Hello Asha, welcome!")
print("Hello Maya, welcome!")

# Using a function to avoid repetition

def greet_user(name):
    print("Hello", name, "welcome!")

# Now just call it for anyone
greet_user("Rahul")
greet_user("Asha")
greet_user("Maya")

# Example 2 : BMI Calculator

# without function

weight = 70
height = 1.75
bmi = weight / (height ** 2)
print("BMI:", bmi)

weight = 80
height = 1.82
bmi = weight / (height ** 2)
print("BMI:", bmi)

# with function

def calculate_bmi(weight, height):
    return weight / (height ** 2)

print("BMI 1:", calculate_bmi(70, 1.75))
print("BMI 2:", calculate_bmi(80, 1.82))

# Example 3 : Shopping Cart Total

# without function

cart1 = [120, 250, 75]
total1 = 0
for price in cart1:
    total1 += price
print("Bill:", total1)

cart2 = [300, 150]
total2 = 0
for price in cart2:
    total2 += price
print("Bill:", total2)

# with function

def calculate_bill(cart):
    total = 0
    for price in cart:
        total += price
    return total

print("Bill 1:", calculate_bill([120, 250, 75]))
print("Bill 2:", calculate_bill([300, 150]))

# example 4 : grade calculator

# without function
marks = 88
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

marks = 45
# ... repeat the same code again


# with function

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

print("Student 1:", get_grade(88))
print("Student 2:", get_grade(45))


# example 5 : word frequency counter

# without function
sentence = "apple banana apple orange banana apple"
words = sentence.split()
counter = {}

for w in words:
    if w in counter:
        counter[w] += 1
    else:
        counter[w] = 1

print(counter)

# with function

def word_count(sentence):
    words = sentence.split()
    counter = {}
    for w in words:
        counter[w] = counter.get(w, 0) + 1
    return counter

print(word_count("apple banana apple orange banana apple"))
# {'apple': 3, 'banana': 2, 'orange': 1}

# example 6 : student gradebook

# without function

grades = {"Asha": 90, "Ravi": 76, "Maya": 88, "Karan": 95}
topper = None
highest = 0

for name, marks in grades.items():
    if marks > highest:
        highest = marks
        topper = name

print("Topper:", topper, "with", highest)

# with function

def find_topper(grades):
    topper = None
    highest = 0
    for name, marks in grades.items():
        if marks > highest:
            highest = marks
            topper = name
    return topper, highest

students = {"Asha": 90, "Ravi": 76, "Maya": 88, "Karan": 95}
print(find_topper(students))
# ('Karan', 95)

# example 7 : atm withdrawal

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount
        return balance, "Withdrawal successful"
    else:
        return balance, "Insufficient funds"

# test
bal, msg = withdraw(5000, 1200)
print(msg, "→ New Balance:", bal)

bal, msg = withdraw(bal, 6000)
print(msg, "→ New Balance:", bal)

# example 8 : password strength checker

def check_password(password):
    if len(password) < 8:
        return "Weak: Too short"

    has_digit = any(ch.isdigit() for ch in password)
    has_alpha = any(ch.isalpha() for ch in password)

    if has_digit and has_alpha:
        return "Strong password"
    else:
        return "Weak: must contain letters and numbers"

print(check_password("abc"))        # Weak
print(check_password("python123"))  # Strong password