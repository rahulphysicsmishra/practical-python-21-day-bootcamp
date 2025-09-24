# Lecture 15: Functions, Your Reusable Building Blocks

# 1. Defining a Function

def greet():
    print("Hello! Welcome to Python.")

greet()   # calling the function

# 2. Function with Parameters

def greet(name):
    print("Hello", name)

greet("Asha")   # Hello Asha
greet("Ravi")   # Hello Ravi

# 3. Function with Return Value

def add(a, b):
    return a + b

result = add(5, 7)
print(result)   # 12

# 4. why function matters - importance of function

# customer 1
total1 = 100 + 250 + 75
print("Bill:", total1)

# customer 2
total2 = 300 + 120
print("Bill:", total2)

# using function to avoid repetition
def calculate_bill(prices):
    return sum(prices)

print("Bill:", calculate_bill([100, 250, 75]))
print("Bill:", calculate_bill([300, 120]))



# 5. Default Parameter Values

def greet(name="Guest"):
    print("Hello", name)

greet()        # Hello Guest
greet("Rahul") # Hello Rahul

# 6. multiple arguments

def add_numbers(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add_numbers(1, 2, 3))       # 6
print(add_numbers(10, 20, 30, 40))# 100

# 7. keyword arguments

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Asha", age=20, course="Python")

# 8. order of arguments

def example(a, *args, b=10, **kwargs):
    print("a:", a)
    print("args:", args)
    print("b:", b)
    print("kwargs:", kwargs)

example(5, 6, 7, b=20, x=1, y=2)

# 9. unpacking

# unpacking a list
nums = [3, 5, 7]
print(sum(nums))        # same as sum([3,5,7])
print(sum(*[nums]))     # ❌ wrong
print(sum(nums))        # ✅ correct

def add(a, b, c):
    return a + b + c

print(add(*nums))       # 15 (unpacked list into 3 arguments)

# unpacking a dictionary
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

info = {"name": "Asha", "age": 21}
introduce(**info)       # unpacks keys into arguments

# 10. turning repeated code into functions

marks1 = [90, 80, 70]
avg1 = sum(marks1) / len(marks1)
print("Average 1:", avg1)

marks2 = [85, 75, 65]
avg2 = sum(marks2) / len(marks2)
print("Average 2:", avg2)

def average(marks):
    return sum(marks) / len(marks)

print("Average 1:", average([90, 80, 70]))
print("Average 2:", average([85, 75, 65]))