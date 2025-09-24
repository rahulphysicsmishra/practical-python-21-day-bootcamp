# Lecture 11 : Advanced Loop Patterns: range, enumerate, break, continue, and Nested Loops

# 1. range() : counting and simple sequences

# count from 0 up to 4 (0,1,2,3,4)
for i in range(5):
    print(i)

# count from 2 up to 5 (2,3,4,5)
for i in range(2, 6):
    print(i)

# even numbers from 0 up to 8 (0,2,4,6,8)
for i in range(0, 9, 2):
    print(i)

# countdown 5,4,3,2,1
for n in range(5, 0, -1):
    print("T-minus", n)
print("Lift off!")

# 2. enumerate() : get index and value when looping

names = ["Asha", "Ravi", "Maya"]

# enumerate gives (index, item)
for index, name in enumerate(names, start=1):
    print(index, "-", name)

# 3. break and continue : alter the loop’s flow

#find first number divisible by 7
for n in range(1, 50):
    if n % 7 == 0:
        print("First multiple of 7 is", n)

# skip even numbers
for n in range(1, 7):
    if n % 2 == 0:
        continue   # skip even numbers
    print(n)

# 4. nested loops : loop inside a loop

# generate multiplication table 1..3 (small for clarity)
for i in range(1, 4):         # outer loop: i = 1, then 2, then 3
    print("Row for", i)
    for j in range(1, 4):     # inner loop: j = 1..3 for each i
        product = i * j
        print(f"{i} x {j} = {product}")
    print("--- done row ---")

# break inside nested loops

for i in range(1, 4):
    print("i =", i)
    for j in range(1, 6):
        if j == 4:
            print("breaking inner loop when j =", j)
            break   # stops inner loop only
        print(" j =", j)
    print("outer loop continues\n")


# Stopping the outer loop from inside the inner loop : common patterns

found = False
for i in range(1, 6):
    for j in range(1, 6):
        print("checking", i, j)
        if i * j == 12:
            found = True
            break   # breaks inner loop
    if found:
        break   # breaks outer loop when flag is True

print("Stopped after finding product 12")

# Seating chart problem

rows = ["A", "B"]
seats_per_row = 3
reserved = "B2"

stop = False
for r in rows:
    for num in range(1, seats_per_row + 1):
        seat = r + str(num)           # e.g., "A1"
        print("Checking seat", seat)
        if seat == reserved:
            print("Reserved seat found:", seat)
            stop = True
            break   # stops inner loop scanning this row
    if stop:
        break       # stops outer loop scanning rows too

print("Finished scanning seats.")