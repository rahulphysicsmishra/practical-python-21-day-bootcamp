# Chapter 4: Combining and Updating Variables

# Changing the Value of a Variable

fruit = "Banana"
print(fruit)   # Banana

fruit = "Mango"
print(fruit)   # Mango

# Updating Numbers
age = 25
age = age + 1
print(age)    # 26

# shortcut version
score = 10
score += 5    # same as score = score + 5
print(score)  # 15

score -= 2   # subtract 2
score *= 3   # multiply by 3
score /= 2   # divide by 2

# updating strings
username = "rahul123"
username = "rahul_mishra"
print(username)   # rahul_mishra

# combining strings
first_name = "Rahul"
last_name = "Mishra"
full_name = first_name + " " + last_name
print(full_name)   # Rahul Mishra

city = "Delhi"
country = "India"
print(city + ", " + country)   # Delhi, India


# combining numbers
math_score = 40
science_score = 45
total_score = math_score + science_score
print(total_score)   # 85

x = 4
y = 3
print(x * y)   # 12
print(x ** y)  # 64 (x raised to power y)


# mixing numbers and strings
name = "Alice"
age = 25
print(name + " is " + age + " years old")  # will raise an error

# correct way
print(name + " is " + str(age) + " years old")
# Output: Alice is 25 years old