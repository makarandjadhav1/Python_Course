'''A set in Python is an unordered collection of unique elements.
It automatically removes duplicate values and is mainly used for 
membership testing and mathematical operations.'''
# Usage: Creating a set
numbers = {10, 20, 30, 40, 50}
print(numbers)

# Usage: Creating a set with duplicate values (duplicates removed)
data = {1, 2, 2, 3, 4}
print(data)

# Usage: Adding an element to set
numbers.add(60)
print(numbers)

# Usage: Removing an element using remove()
numbers.remove(30)
print(numbers)

# Usage: Removing an element using discard() (no error if not found)
numbers.discard(100)
print(numbers)

# Usage: Looping through a set
for num in numbers:
    print(num)

# Usage: Checking membership in set
if 20 in numbers:
    print("20 is present in the set")

# Usage: Length of set
print(len(numbers))

# Usage: Set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# Usage: Set intersection
print(set1.intersection(set2))

# Usage: Set difference
print(set1.difference(set2))

# Usage: Clearing all elements from set
numbers.clear()
print(numbers)
