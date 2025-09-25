# Lecture 19: OOP Essentials, Encapsulation, Inheritance & Special Methods

# encapsulation in bank account example

class BankAccount:
    def __init__(self, owner, balance=0):
        # public variable
        self.owner = owner  
        # private variable (double underscore)
        self.__balance = balance  

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Withdraw money if balance is enough"""
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        """Read-only method to view balance"""
        return self.__balance

# create account
acc = BankAccount("Asha", 1000)

# Deposit and withdraw using methods
acc.deposit(500)        # 500 deposited. New balance: 1500
acc.withdraw(2000)      # Insufficient funds

# Access balance safely using method
print(acc.get_balance())  # 1500

# Direct access to __balance will not work
# print(acc.__balance)   # ❌ Error: AttributeError



# Inheritance example using Vehicle

# parent class
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def start(self):
        print(f"{self.brand} is starting...")

# child class
class Car(Vehicle):
    def __init__(self, brand, wheels, fuel):
        # call parent constructor
        super().__init__(brand, wheels)
        self.fuel = fuel

    def show_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}, Fuel: {self.fuel}")

# child class
class Bike(Vehicle):
    def __init__(self, brand, wheels, type):
        super().__init__(brand, wheels)
        self.type = type

    def show_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}, Type: {self.type}")

# create objects
c1 = Car("Toyota", 4, "Petrol")
b1 = Bike("Yamaha", 2, "Sports")

c1.start()       # Toyota is starting...
c1.show_info()   # Brand: Toyota, Wheels: 4, Fuel: Petrol

b1.start()       # Yamaha is starting...
b1.show_info()   # Brand: Yamaha, Wheels: 2, Type: Sports


# Methods overriding example


class Animal:
    def sound(self):
        print("This animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# test
d = Dog()
c = Cat()

d.sound()   # Dog barks
c.sound()   # Cat meows


# Special methods example

# __str__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        # custom string when object is printed
        return f"Student(name={self.name}, marks={self.marks})"

s1 = Student("Asha", 90)
print(s1)
# Output: Student(name=Asha, marks=90)


# custom __len__

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        # make len(playlist) return number of songs
        return len(self.songs)

p = Playlist(["Song1", "Song2", "Song3"])
print(len(p))   # 3