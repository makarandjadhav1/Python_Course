'''A tuple in Python is an ordered and immutable collection of elements.
Once created, its values cannot be changed, which makes tuples safe, fast, 
and memory-efficient.'''
# Usage: Creating a tuple
numbers = (10, 20, 30, 40, 50)
print(numbers)

# Usage: Creating a tuple with mixed data types
mixed = (1, "Python", 3.5, True)
print(mixed)

# Usage: Accessing tuple elements using index
print(numbers[0])
print(numbers[-1])

# Usage: Tuple slicing
print(numbers[1:4])

# Usage: Looping through a tuple
for num in numbers:
    print(num)

# Usage: Checking element exists in tuple
if 30 in numbers:
    print("30 is in the tuple")

# Usage: Length of tuple
print(len(numbers))

# Usage: Counting occurrences of an element
print(numbers.count(20))

# Usage: Finding index of an element
print(numbers.index(40))

# Usage: Nested tuple
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple)

# Usage: Converting tuple to list (to modify)
temp_list = list(numbers)
temp_list.append(60)
numbers = tuple(temp_list)
print(numbers)

# Usage: Tuple unpacking
a, b, c, d, e, f = numbers
print(a, b, c, d, e, f)
