'''A list in Python is an ordered collection 
of items that can hold multiple values.'''
# Usage: Creating a list
numbers = [10, 20, 30, 40, 50]
print(numbers)

# Usage: Accessing list elements using index
print(numbers[0])
print(numbers[-1])

# Usage: Modifying list elements
numbers[1] = 25
print(numbers)

# Usage: Adding element using append()
numbers.append(60)
print(numbers)

# Usage: Adding element at specific position using insert()
numbers.insert(2, 15)
print(numbers)

# Usage: Removing element using remove()
numbers.remove(40)
print(numbers)

# Usage: Removing last element using pop()
numbers.pop()
print(numbers)

# Usage: Length of list
print(len(numbers))

# Usage: Looping through a list
for num in numbers:
    print(num)

# Usage: Checking element exists in list
if 30 in numbers:
    print("30 is in the list")

# Usage: Sorting list
numbers.sort()
print(numbers)

# Usage: Reversing list
numbers.reverse()
print(numbers)

# Usage: Copying a list
new_list = numbers.copy()
print(new_list)

# Usage: Clearing all elements from list
numbers.clear()
print(numbers)
