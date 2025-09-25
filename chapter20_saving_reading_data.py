# Lecture 20: File Handling in Python, Saving & Reading Data

# 1. opening and closing files

# open a file
file = open("myfile.txt", "w")  # open in write mode

# write something
file.write("Hello, Python!")

# always close the file when done
file.close()

# 2. writing to a file

# simple write
f = open("notes.txt", "w")
f.write("This is my first file in Python.\n")
f.write("I can write multiple lines!\n")
f.close()

# writing a list

f = open("fruits.txt", "w")
fruits = ["apple\n", "banana\n", "mango\n"]
f.writelines(fruits)  # write list of strings
f.close()


# 3. Reading from a file

# read entire file

f = open("notes.txt", "r")
content = f.read()
print(content)
f.close()

# read line by line

f = open("notes.txt", "r")
print(f.readline())   # reads first line
print(f.readline())   # reads second line
f.close()

# read all lines into a list

f = open("notes.txt", "r")
lines = f.readlines()
print(lines)   # ['This is my first file in Python.\n', 'I can write multiple lines!\n']
f.close()

# 4. append mode

f = open("notes.txt", "a")
f.write("Adding a new line here.\n")
f.close()

# 5. using 'with' statement

with open("notes.txt", "r") as f:
    data = f.read()
    print(data)

# 6. read world examples

# save student scores

students = {"Asha": 90, "Ravi": 76, "Maya": 88}

with open("scores.txt", "w") as f:
    for name, marks in students.items():
        f.write(f"{name}: {marks}\n")

# read student scores

with open("scores.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())   # strip removes \n


# simple notes app

# write a note
with open("mynotes.txt", "a") as f:
    f.write("Remember to practice Python daily.\n")

# read all notes
with open("mynotes.txt", "r") as f:
    notes = f.read()
    print("Your Notes:\n", notes)


# logging atm transactions

def log_transaction(user, action, amount):
    with open("atm_log.txt", "a") as f:
        f.write(f"User: {user}, Action: {action}, Amount: {amount}\n")

log_transaction("Rahul", "Deposit", 1000)
log_transaction("Rahul", "Withdraw", 500)

with open("atm_log.txt", "r") as f:
    print(f.read())