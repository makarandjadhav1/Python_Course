# Usage: Basic for loop to print numbers from 0 to 4
for i in range(5):
    print(i)

# Usage: for loop with custom start and end values
for i in range(1, 6):
    print(i)

# Usage: for loop with step value (prints odd numbers)
for i in range(1, 11, 2):
    print(i)

# Usage: for loop to iterate through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Usage: for loop to iterate through a string
name = "Python"
for char in name:
    print(char)

# Usage: for loop with if condition to print even numbers
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Usage: for loop to calculate sum of numbers
total = 0
for i in range(1, 6):
    total += i
print(total)

# Usage: nested for loop to print a star pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# Usage: for loop with break statement
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Usage: for loop with continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
