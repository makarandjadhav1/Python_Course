# Tutorial: Python If Else Statements
print("Python If Else Statement Examples\n")

# 1. Age Check
age = 18
print("1. Age Check")
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

print("\n-------------------------\n")

# 2. Positive or Negative Number
num = -5
print("2. Positive or Negative Check")
if num > 0:
    print("Number is positive")
else:
    print("Number is negative or zero")

print("\n-------------------------\n")

# 3. Student Marks Result
marks = 65
print("3. Student Result Check")
if marks >= 35:
    print("Student is passed")
else:
    print("Student is failed")

print("\n-------------------------\n")

# 4. Nested If Else Example
print("4. Nested If Else Example")
age = 20

if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")

print("\n-------------------------\n")

print("End of If Else Tutorial")
