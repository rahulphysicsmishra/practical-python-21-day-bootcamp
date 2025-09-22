# Chapter 2: Variables in Python

#  labeled boxes where you keep information.
#  Here are some examples of variables in Python:

name = "Alice"
age = 25
is_student = True

#  In this example, we have three variables:
#  - name: a string variable that holds the name "Alice"
#  - age: an integer variable that holds the age 25
#  - is_student: a boolean variable that indicates whether the person is a student (True)

# rules for naming variables:
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# 2. The rest of the variable name can contain letters, numbers (0-9), and underscores (_).
# 3. Variable names are case-sensitive (e.g., myVariable and myvariable are different).
# 4. Variable names cannot be the same as Python reserved words (like if, else, while, etc.).
# 5. Use descriptive names that make it clear what the variable represents.

# Examples of valid and invalid variable names:

name = "Bob"     # ✅ Valid
_name = "Eve"    # ✅ Valid

# uncommenting the line below will raise a SyntaxError
# 1name = "Zoe"    # ❌ Invalid (starts with a number)

# Uncommenting the line below will raise a SyntaxError
# print(1name) 


cool2 = "yes"    # ✅ Valid

# uncommenting the line below will raise a SyntaxError
# 2cool = "nope"   # ❌ Invalid

user_name = "Rahul"   # ✅ Good
username123 = "Mark"  # ✅ Good

# Uncommenting the lines below will raise SyntaxErrors
# user-name = "Alex"    # ❌ Invalid
# user name = "Lily"    # ❌ Invalid

score = 10
Score = 20
print(score)  # 10
print(Score)  # 20

# Quick Example: Bad vs Good Naming

# ❌ Not recommended
a = 5
b = "John"

# ✅ Much better
age = 5
name = "John"