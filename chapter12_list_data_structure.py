# Lecture 12: Lists in Python, Your Toolbox for Storing Multiple Items

# 1. Creating a List
fruits = ["apple", "banana", "mango", "orange"]
print(fruits)

# mixed data types
mixed = ["Rahul", 25, True, 3.14]
print(mixed)
# ['Rahul', 25, True, 3.14]

# 2. Accessing List Items
fruits = ["apple", "banana", "mango", "orange"]

print(fruits[0])   # apple
print(fruits[2])   # mango
print(fruits[-1])  # orange (last item)

# 3. getting part of the list (slicing)
print(fruits[1:3])   # ['banana', 'mango']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[2:])    # ['mango', 'orange']

# 4. Modifying List Items
fruits[1] = "grapes"
print(fruits)  
# ['apple', 'grapes', 'mango', 'orange']

# 5. list methods

numbers = [10, 20, 30]

# Add an item
numbers.append(40)  
print(numbers)   # [10, 20, 30, 40]

# Insert at position
numbers.insert(1, 15)  
print(numbers)   # [10, 15, 20, 30, 40]

# Remove by value
numbers.remove(20)  
print(numbers)   # [10, 15, 30, 40]

# Remove last item
numbers.pop()  
print(numbers)   # [10, 15, 30]

# Find length
print(len(numbers))   # 3

# 6. iterating through a list

fruits = ["apple", "banana", "mango", "orange"]

# print all fruits
for fruit in fruits:
    print("I like", fruit)

# print fruits with more than 5 letters
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit, "has more than 5 letters")

# counting even numbers
numbers = [12, 7, 9, 14, 22, 5]
count = 0

for n in numbers:
    if n % 2 == 0:
        count += 1

print("Number of even numbers:", count)

# Mini list problems

# 1. Shopping Cart Total

cart = [120, 250, 75, 300]
total = 0

for price in cart:
    total += price

print("Total bill: $", total)

# 2. attendance list

students = ["Asha", "Ravi", "Maya", "Karan"]

name = input("Enter student name: ")

if name in students:
    print(name, "is present in the class list")
else:
    print(name, "is not found")

# highest scores

scores = [45, 67, 89, 34, 76]
highest = scores[0]   # assume first is highest

for s in scores:
    if s > highest:
        highest = s

print("Highest score is:", highest)