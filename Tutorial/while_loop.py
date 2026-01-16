# Usage: Basic while loop to print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Usage: While loop to print even numbers from 1 to 10
i = 2
while i <= 10:
    print(i)
    i += 2

# Usage: While loop to calculate sum of numbers from 1 to 5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print(total)

# Usage: While loop with continue statement
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# Usage: While loop with break statement
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

# Usage: Example of infinite while loop (do not run)
# while True:
#     print("Infinite loop")
