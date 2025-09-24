# Lecture 14: Tuples & Sets in Python 

# 1. Creating a Tuple

colors = ("red", "green", "blue")
print(colors)
# ('red', 'green', 'blue')

# 2. Accessing Tuple Items
colors = ("red", "green", "blue")

print(colors[0])   # red
print(colors[-1])  # blue
print(colors[0:2]) # ('red', 'green')

# 3. Tuple methods
numbers = (10, 20, 30, 20, 40)
print(numbers.count(20))   # 2 (counts occurrences of 20)
print(numbers.index(30))   # 2 (index of first occurrence of 30)


# 4. Creating a Set
fruits = {"apple", "banana", "apple", "mango"}
print(fruits)
# {'apple', 'banana', 'mango'}   (no duplicates, order may vary)

# 5. Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # union → {1, 2, 3, 4, 5}
print(a & b)   # intersection → {3}
print(a - b)   # difference → {1, 2}
print(a ^ b)   # symmetric difference → {1, 2, 4, 5}

# 6. set methods
fruits = {"apple", "banana"}

fruits.add("mango")
print(fruits)    # {'apple', 'banana', 'mango'}

fruits.remove("banana")
print(fruits)    # {'apple', 'mango'}

print(len(fruits))   # 2

# some practical examples

# example 1 - Days of the Week (Tuple)

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

for d in days:
    print("Day:", d)

# example 2 - coordinates (Tuple)
location = (28.61, 77.20)   # Delhi coordinates
print("Latitude:", location[0])
print("Longitude:", location[1])

# example 3 - remove duplicates from a list (Set)

names = ["Asha", "Ravi", "Maya", "Ravi", "Asha"]

unique_names = set(names)
print(unique_names)
# {'Asha', 'Ravi', 'Maya'}

# example 4 - common students

math_class = {"Asha", "Ravi", "Maya"}
science_class = {"Ravi", "Karan", "Maya"}

both = math_class & science_class
print("Students in both classes:", both)
# Students in both classes: {'Ravi', 'Maya'}

# example 5 - unique words in a sentence

sentence = "apple banana apple orange banana"
words = sentence.split()
unique_words = set(words)

print("Unique words:", unique_words)
# Unique words: {'banana', 'apple', 'orange'}
