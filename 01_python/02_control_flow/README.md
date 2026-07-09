# Python Control Flow - Complete Guide

## Table of Contents
1. [Conditional Statements](#conditional-statements)
2. [Loops](#loops)
3. [Loop Control](#loop-control)
4. [Pattern Programs](#pattern-programs)
5. [Real-World Examples](#real-world-examples)

## Conditional Statements

### if Statement

```python
# Simple if
age = 20
if age >= 18:
    print("You are an adult")

# if-else
score = 45
if score >= 50:
    print("Pass")
else:
    print("Fail")

# if-elif-else
marks = 75
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# Multiple conditions
age = 25
income = 60000
employed = True

if age >= 25 and income >= 50000:
    print("Eligible for loan")
elif employed and income >= 30000:
    print("May be eligible with guarantor")
else:
    print("Not eligible")
```

### Nested if

```python
# Nested conditions
age = 25
income = 60000
credit_score = 750

if age >= 21:
    if income >= 50000:
        if credit_score >= 700:
            print("Excellent: Approve loan with low interest")
        else:
            print("Good: Approve loan with standard interest")
    else:
        print("Income too low")
else:
    print("Too young")

# Better approach: Use logical operators instead of nesting
if age >= 21 and income >= 50000 and credit_score >= 700:
    print("Excellent: Approve loan with low interest")
elif age >= 21 and income >= 50000 and credit_score >= 650:
    print("Good: Approve loan with standard interest")
elif age >= 21 and income >= 30000:
    print("May be eligible")
else:
    print("Not eligible")
```

### Ternary Operator

```python
# Traditional if-else
age = 25
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary operator (one-liner)
status = "Adult" if age >= 18 else "Minor"

# Nested ternary
score = 75
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"

# Data processing example
value = None
result = value if value is not None else 0
```

## Loops

### for Loop

```python
# Loop through range
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Range with start and end
for i in range(1, 6):  # 1 to 5
    print(i)

# Range with step
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

for i in range(10, 0, -1):  # 10, 9, 8, ..., 1
    print(i)

# Loop through list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop through string
word = "Python"
for char in word:
    print(char)

# Loop with enumerate (get index and value)
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry

# Loop through dictionary
person = {"name": "John", "age": 30, "city": "NYC"}
for key, value in person.items():
    print(f"{key}: {value}")

# Only keys
for key in person:
    print(key)

# Only values
for value in person.values():
    print(value)
```

### while Loop

```python
# Simple while loop
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0, 1, 2, 3, 4

# Sentinel-controlled loop
password = ""
while password != "secret":
    password = input("Enter password: ")

# Event-controlled loop
sum_values = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    sum_values += number
    number = int(input("Enter a number (0 to stop): "))

print(f"Sum: {sum_values}")

# Data processing example
data = [10, 20, 30, 0, 40, 50]
index = 0
while index < len(data) and data[index] != 0:
    print(data[index])
    index += 1
# Output: 10, 20, 30 (stops at 0)
```

### Nested Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}", end="  ")
    print()  # New line

# Pattern: Rectangle of *
for i in range(3):
    for j in range(5):
        print("*", end=" ")
    print()

# Data matrix iteration
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()
```

## Loop Control

### break Statement

```python
# Exit loop when condition met
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4

# Search example
found = False
target = 30
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        found = True
        break

if not found:
    print(f"{target} not found")

# Exit nested loop
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break  # Exits inner loop only
        print(f"({i}, {j})", end=" ")
```

### continue Statement

```python
# Skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
# Output: 0, 1, 3, 4

# Process only valid records
records = [10, -5, 20, -3, 30]

for record in records:
    if record < 0:
        continue  # Skip negative values
    print(record)
# Output: 10, 20, 30

# Data validation example
for order_id in range(1, 6):
    if order_id == 3:
        continue  # Skip order 3
    print(f"Processing order {order_id}")
```

### pass Statement

```python
# Placeholder for future code
for i in range(5):
    if i == 2:
        pass  # Do nothing for i=2
    print(i)

# Not ready to implement
def process_data():
    pass  # TODO: Implement later

# Exception handling placeholder
try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # Ignore division by zero

# Class placeholder
class DataProcessor:
    pass

# Condition placeholder
if x > 10:
    pass  # To be implemented
else:
    print("x is 10 or less")
```

## Pattern Programs

### Pyramid Patterns

```python
# Pattern 1: Triangle of *
# *
# **
# ***
# ****
for i in range(1, 5):
    print("*" * i)

# Pattern 2: Inverted Triangle
# ****
# ***
# **
# *
for i in range(4, 0, -1):
    print("*" * i)

# Pattern 3: Diamond
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
n = 4
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Pattern 4: Number Triangle
# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pattern 5: Floyd's Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
```

## Real-World Examples

### Example 1: Grade Calculator

```python
def calculate_grade(marks):
    """Calculate grade based on marks."""
    if marks >= 90:
        return "A (Excellent)"
    elif marks >= 80:
        return "B (Very Good)"
    elif marks >= 70:
        return "C (Good)"
    elif marks >= 60:
        return "D (Satisfactory)"
    elif marks >= 50:
        return "E (Pass)"
    else:
        return "F (Fail)"

def process_student_marks():
    """Process marks for multiple students."""
    students = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 45,
        "Eve": 88
    }
    
    for name, marks in students.items():
        grade = calculate_grade(marks)
        print(f"{name:10} - Marks: {marks:3} - Grade: {grade}")

process_student_marks()
```

### Example 2: Data Validation Loop

```python
def validate_and_process_records(records):
    """Validate records and process valid ones."""
    processed = 0
    skipped = 0
    
    for record in records:
        # Validate required fields
        if not record.get('id') or not record.get('name'):
            print(f"Skipping invalid record: {record}")
            skipped += 1
            continue
        
        # Validate data types
        if not isinstance(record['id'], int) or record['id'] <= 0:
            print(f"Skipping invalid ID: {record['id']}")
            skipped += 1
            continue
        
        # Process valid record
        print(f"Processing: {record['name']} (ID: {record['id']})")
        processed += 1
    
    print(f"\nProcessed: {processed}, Skipped: {skipped}")

# Test
records = [
    {'id': 1, 'name': 'Alice'},
    {'id': 0, 'name': 'Bob'},  # Invalid ID
    {'name': 'Charlie'},        # Missing ID
    {'id': 3, 'name': 'Diana'}
]

validate_and_process_records(records)
```

### Example 3: File Processing Simulation

```python
def process_csv_records(csv_lines):
    """Process CSV-like records."""
    headers = None
    records_processed = 0
    errors = 0
    
    for line_num, line in enumerate(csv_lines, 1):
        try:
            # Skip empty lines
            if not line.strip():
                continue
            
            # Parse header
            if line_num == 1:
                headers = line.split(',')
                print(f"Headers: {headers}")
                continue
            
            # Parse record
            fields = line.split(',')
            
            if len(fields) != len(headers):
                print(f"Line {line_num}: Column mismatch")
                errors += 1
                continue
            
            record = dict(zip(headers, fields))
            print(f"Record: {record}")
            records_processed += 1
            
        except Exception as e:
            print(f"Error on line {line_num}: {e}")
            errors += 1
    
    return records_processed, errors

# Test
csv_data = [
    "id,name,salary",
    "1,Alice,50000",
    "2,Bob,60000",
    "3",  # Invalid - missing fields
    "4,Diana,75000"
]

processed, errors = process_csv_records(csv_data)
print(f"\nTotal: Processed={processed}, Errors={errors}")
```

### Example 4: While Loop - Retry Logic

```python
def retry_operation(max_retries=3):
    """Attempt operation with retries."""
    attempt = 0
    
    while attempt < max_retries:
        try:
            # Simulate operation that might fail
            print(f"Attempt {attempt + 1}/{max_retries}")
            
            # Replace with actual operation
            result = perform_operation()
            
            print("Operation successful!")
            return result
            
        except Exception as e:
            attempt += 1
            print(f"Error: {e}")
            
            if attempt < max_retries:
                print(f"Retrying... ({max_retries - attempt} attempts left)")
            else:
                print("Max retries exceeded")
                raise

def perform_operation():
    """Simulate an operation that might fail."""
    import random
    if random.random() > 0.5:
        return "Success"
    else:
        raise Exception("Random failure")

# Call with retry
try:
    result = retry_operation(max_retries=3)
    print(f"Final result: {result}")
except Exception as e:
    print(f"Operation failed after retries: {e}")
```

---

**Control Flow Guide Version**: 1.0  
**Last Updated**: June 2026  
**Total Examples**: 80+
