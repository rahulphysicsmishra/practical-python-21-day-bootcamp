# Lecture 18: Classes, Objects & Methods

# defining a class

class Student:
    pass   # empty class for now

# create objects
s1 = Student()
s2 = Student()

print(type(s1))
print(type(s2))

# attributes(instance variables)

class Student:
    def __init__(self, name, age):
        self.name = name   # instance variable
        self.age = age

# create objects
s1 = Student("Asha", 20)
s2 = Student("Ravi", 22)

print(s1.name, s1.age)   # Asha 20
print(s2.name, s2.age)   # Ravi 22

# methods(functions inside class)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Maya", 88)
s2 = Student("Karan", 92)

s1.show()   # Name: Maya, Marks: 88
s2.show()   # Name: Karan, Marks: 92

# real world example : bank account

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance")

# create accounts
acc1 = BankAccount("Rahul", 1000)
acc1.deposit(500)     # 1500
acc1.withdraw(2000)   # Insufficient balance

# another example : product inventory

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def purchase(self, qty):
        if qty <= self.stock:
            self.stock -= qty
            print(f"{qty} {self.name}(s) purchased. Remaining stock: {self.stock}")
        else:
            print("Not enough stock!")

# create products
p1 = Product("Laptop", 50000, 10)
p1.purchase(3)   # Laptop purchased
p1.purchase(12)  # Not enough stock