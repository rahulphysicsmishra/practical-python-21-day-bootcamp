# Lecture 13: Dictionaries in Python, Storing Data as Key–Value Pairs

# 1. Creating a Dictionary

# Example: student marks
marks = {"Asha": 90, "Ravi": 85, "Maya": 78}

print(marks)
# {'Asha': 90, 'Ravi': 85, 'Maya': 78}

# 2. accessing a value by key
print(marks["Ravi"])   # 85

print(marks.get("Maya"))      # 78
print(marks.get("Karan"))     # None (doesn't crash)
print(marks.get("Karan", 0))  # 0 (default value if not found)

# 3. adding or updating a key-value pair
marks["Karan"] = 88    # add new student
marks["Asha"] = 95     # update Asha's marks

print(marks)
# {'Asha': 95, 'Ravi': 85, 'Maya': 78, 'Karan': 88}

# 4. removing a key-value pair
marks.pop("Ravi")  
print(marks)
# {'Asha': 95, 'Maya': 78, 'Karan': 88}

# Remove last inserted item
marks.popitem()  
print(marks)

# 5. dictionary methods

student = {"name": "Rahul", "age": 21, "course": "Python"}

print(student.keys())     # dict_keys(['name', 'age', 'course'])
print(student.values())   # dict_values(['Rahul', 21, 'Python'])
print(student.items())    # dict_items([('name', 'Rahul'), ('age', 21), ('course', 'Python')])

# 6. iterating through a dictionary

# print all keys
for key in student:
    print(key)

# print all values

for value in student.values():
    print(value)

# print key-value pairs

for key, value in student.items():
    print(key, ":", value)

# 7. Real world examples

# phonebook
phonebook = {
    "Asha": "9876543210",
    "Ravi": "9123456780",
    "Maya": "9988776655"
}

name = input("Whose number do you want? ")

if name in phonebook:
    print("Number:", phonebook[name])
else:
    print("Sorry, not found")

# product prices

prices = {"apple": 120, "banana": 40, "mango": 60}

item = input("Enter product name: ")

if item in prices:
    print(f"Price of {item} is ₹{prices[item]}")
else:
    print("Item not available")

# login system

users = {"admin": "1234", "rahul": "python123"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid credentials")

# student grade

grades = {"Asha": 90, "Ravi": 76, "Maya": 88, "Karan": 95}

highest_student = None
highest_marks = 0

for name, score in grades.items():
    if score > highest_marks:
        highest_marks = score
        highest_student = name

print("Topper is:", highest_student, "with", highest_marks, "marks")