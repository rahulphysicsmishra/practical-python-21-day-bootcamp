# Lecture 17: Thinking Deeper with Functions Using Recursion, Lambda & Scope


# 1. recursion

# factorial of a number without recursion

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# with recursion
def factorial(n):
    if n == 1:   # base case
        return 1
    return n * factorial(n-1)   # recursive case

print(factorial(5))  # 120

# fibonacci sequence using recursion

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(6)])
# [0, 1, 1, 2, 3, 5]


# sum of list

def sum_list(numbers):
    if not numbers:   # base case: empty list
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([1, 2, 3, 4]))  # 10

# 2. lambda function

# normal function

def square(x):
    return x * x

# lambda function

square = lambda x: x * x
print(square(5))  # 25

# map function

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)   # [1, 4, 9, 16]

# filter function

numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [10, 20, 30]

# sorted function

students = [("Asha", 90), ("Ravi", 76), ("Maya", 88)]
# sort by marks
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
# [('Asha', 90), ('Maya', 88), ('Ravi', 76)]


# 3. scope of variables

# local scope

def greet():
    message = "Hello"   # local variable
    print(message)

greet()
# print(message)   # ❌ Error, message not defined

# global scope

message = "Hello, world"  # global variable

def greet():
    print(message)        # can access global

greet()
print(message)            # works

# modifying global variable

count = 0

def increase():
    global count
    count += 1

increase()
increase()
print(count)  # 2


# variable lookup

x = "global"

def outer():
    x = "enclosed"
    def inner():
        x = "local"
        print(x)  # local wins
    inner()
    print(x)      # enclosed
outer()
print(x)          # global