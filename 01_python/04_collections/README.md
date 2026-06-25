# Python Collections - Complete Guide

## Table of Contents
1. [Lists](#lists)
2. [Tuples](#tuples)
3. [Sets](#sets)
4. [Dictionaries](#dictionaries)
5. [Nested Collections](#nested-collections)
6. [Comprehensions](#comprehensions)
7. [Data Processing Examples](#data-processing-examples)

## Lists

### Creating Lists

```python
# Empty list
empty_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]

# Using list() constructor
from_range = list(range(1, 6))  # [1, 2, 3, 4, 5]
from_string = list("hello")     # ['h', 'e', 'l', 'l', 'o']

# List repetition
repeated = [0] * 5  # [0, 0, 0, 0, 0]
pattern = ["A", "B"] * 3  # ["A", "B", "A", "B", "A", "B"]
```

### List Operations

```python
# Access elements
fruits = ["apple", "banana", "cherry"]
print(fruits[0])      # Output: apple
print(fruits[-1])     # Output: cherry
print(fruits[1:3])    # Output: ['banana', 'cherry']

# Modify elements
fruits[0] = "orange"
print(fruits)  # ['orange', 'banana', 'cherry']

# Add elements
fruits.append("grape")  # Add to end
fruits.extend(["kiwi", "mango"])  # Add multiple
fruits.insert(1, "date")  # Insert at position

# Remove elements
fruits.remove("banana")  # Remove by value
item = fruits.pop()  # Remove and return last item
item = fruits.pop(0)  # Remove and return first item
del fruits[0]  # Delete by index

# Search
if "apple" in fruits:
    print("Found apple")

index = fruits.index("cherry")  # Get index
count = fruits.count("apple")  # Count occurrences

# Sort
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()  # In-place sort
numbers.sort(reverse=True)  # Descending

sorted_copy = sorted(numbers)  # Create new sorted list

# Reverse
numbers.reverse()
reversed_copy = numbers[::-1]  # Using slicing

# Length
length = len(fruits)
```

### List Methods Summary

```python
fruits = ["apple", "banana", "cherry"]

# Commonly used methods
fruits.append("date")           # Add element
fruits.extend(["fig", "grape"]) # Add multiple
fruits.insert(1, "blueberry")   # Insert at position
fruits.remove("banana")         # Remove by value
removed = fruits.pop()          # Remove and return last
removed = fruits.pop(0)         # Remove and return first
fruits.clear()                  # Remove all elements

index = fruits.index("apple")   # Get index of element
count = fruits.count("apple")   # Count occurrences

fruits.sort()                   # Sort in-place
fruits.reverse()                # Reverse in-place

copy = fruits.copy()            # Shallow copy
```

## Tuples

### Creating Tuples

```python
# Empty tuple
empty = ()

# Tuple with elements
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)

# Single element tuple (note the comma!)
single = (42,)  # NOT (42) which is just a number

# Using tuple() constructor
from_list = tuple([1, 2, 3])
from_string = tuple("hello")  # ('h', 'e', 'l', 'l', 'o')

# Tuple unpacking
x, y, z = (1, 2, 3)
a, b = (10, 20)

# Ignore some values
x, _, z = (1, 2, 3)  # x=1, z=3
```

### Tuple Operations

```python
# Access (like lists)
coordinates = (10, 20, 30)
print(coordinates[0])      # Output: 10
print(coordinates[-1])     # Output: 30
print(coordinates[1:3])    # Output: (20, 30)

# Immutable - cannot modify
# coordinates[0] = 100  # ✗ TypeError: 'tuple' object does not support item assignment

# Tuple concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # (1, 2, 3, 4)

# Tuple repetition
repeated = (0,) * 3  # (0, 0, 0)

# Membership
if 20 in coordinates:
    print("Found 20")

# Length and methods
length = len(coordinates)
index = coordinates.index(20)  # Get index
count = coordinates.count(10)  # Count occurrences

# Convert to list, modify, convert back
t = (1, 2, 3)
lst = list(t)
lst.append(4)
t = tuple(lst)  # (1, 2, 3, 4)
```

### When to Use Tuples

```python
# 1. As dictionary keys (tuples are hashable)
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago"
}

lat_long = (40.7128, -74.0060)
print(locations[lat_long])  # Output: New York

# 2. Return multiple values from function
def get_user_info():
    return ("Alice", 30, "alice@example.com")

name, age, email = get_user_info()

# 3. Function default arguments
def process_data(data=()):
    pass

# 4. Database records (read-only)
database_record = ("ID001", "John", "john@example.com", 30)
```

## Sets

### Creating Sets

```python
# Set with elements
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}

# Empty set (NOT {})
empty_set = set()

# From other collections
from_list = set([1, 2, 3])
from_string = set("hello")  # {'h', 'e', 'l', 'o'}  # Note: 'l' appears once

# Set removes duplicates
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}
```

### Set Operations

```python
numbers = {1, 2, 3, 4, 5}

# Add elements
numbers.add(6)          # Add single element
numbers.update([7, 8])  # Add multiple elements

# Remove elements
numbers.remove(3)       # Remove - raises error if not found
numbers.discard(10)     # Remove - no error if not found
removed = numbers.pop() # Remove and return arbitrary element
numbers.clear()         # Remove all

# Membership
if 2 in {1, 2, 3}:
    print("Found 2")

# Length
size = len(numbers)
```

### Set Operations (Mathematical)

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (all elements)
union = set_a | set_b          # {1, 2, 3, 4, 5, 6}
union = set_a.union(set_b)

# Intersection (common elements)
intersection = set_a & set_b   # {3, 4}
intersection = set_a.intersection(set_b)

# Difference (in A but not B)
difference = set_a - set_b     # {1, 2}
difference = set_a.difference(set_b)

# Symmetric difference (in A or B but not both)
sym_diff = set_a ^ set_b       # {1, 2, 5, 6}

# Subset and Superset
small = {1, 2}
large = {1, 2, 3, 4}
print(small <= large)  # True (subset)
print(large >= small)  # True (superset)
```

### Set Example: Remove Duplicates

```python
# Remove duplicates from list
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(set(numbers))
print(unique)  # Order may vary: [1, 2, 3, 4, 5]

# Keep order while removing duplicates
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = remove_duplicates(numbers)
print(unique)  # [1, 2, 3, 4, 5]

# Data engineering: Find common customers
transactions_2023 = {101, 102, 103, 104, 105}
transactions_2024 = {103, 104, 105, 106, 107}

common_customers = transactions_2023 & transactions_2024
print(common_customers)  # {103, 104, 105}

new_customers = transactions_2024 - transactions_2023
print(new_customers)  # {106, 107}
```

## Dictionaries

### Creating Dictionaries

```python
# Dictionary with key-value pairs
person = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Empty dictionary
empty = {}

# Using dict() constructor
person2 = dict(name="Alice", age=25, email="alice@example.com")

# From list of tuples
from_tuples = dict([("a", 1), ("b", 2)])

# From zip
keys = ["name", "age", "city"]
values = ["Bob", 28, "NYC"]
person3 = dict(zip(keys, values))
```

### Dictionary Access and Modification

```python
person = {
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}

# Access
print(person["name"])           # Output: John
print(person.get("age"))        # Output: 30
print(person.get("phone", "N/A"))  # Output: N/A (default if not found)

# Modify
person["age"] = 31              # Update existing
person["phone"] = "555-1234"    # Add new

# Remove
del person["phone"]             # Delete by key
removed = person.pop("email")   # Pop and return
person.popitem()                # Remove arbitrary item

# Check key exists
if "name" in person:
    print("Name found")

if "phone" not in person:
    print("Phone not found")
```

### Dictionary Methods

```python
person = {"name": "John", "age": 30, "city": "NYC"}

# Keys, values, items
keys = person.keys()            # dict_keys(['name', 'age', 'city'])
values = person.values()        # dict_values(['John', 30, 'NYC'])
items = person.items()          # dict_items([('name', 'John'), ...])

# Iteration
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Copy
copy = person.copy()            # Shallow copy

# Update
person.update({"age": 31, "phone": "555-1234"})

# Get with default
phone = person.get("phone", "Not provided")

# Clear
person.clear()  # Remove all items

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}     # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
merged = dict1 | dict2          # Python 3.9+
```

### Dictionary Example: Data Processing

```python
# Customer records
customers = {
    "C001": {"name": "Alice", "balance": 1000},
    "C002": {"name": "Bob", "balance": 500},
    "C003": {"name": "Charlie", "balance": 1500}
}

# Access nested data
print(customers["C001"]["name"])  # Output: Alice
print(customers["C002"]["balance"])  # Output: 500

# Update
customers["C001"]["balance"] -= 100

# Add new customer
customers["C004"] = {"name": "Diana", "balance": 2000}

# Iterate
total_balance = 0
for customer_id, info in customers.items():
    print(f"{customer_id}: {info['name']} - ${info['balance']}")
    total_balance += info["balance"]

print(f"Total Balance: ${total_balance}")
```

## Nested Collections

### Lists within Lists

```python
# 2D List (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access
print(matrix[0])      # [1, 2, 3]
print(matrix[0][1])   # 2
print(matrix[2][2])   # 9

# Modify
matrix[1][1] = 50

# Iterate
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# 3D List
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
print(cube[0][1][1])  # 4
```

### Dictionaries with Lists

```python
# Dictionary with list values
data = {
    "names": ["Alice", "Bob", "Charlie"],
    "ages": [30, 25, 28],
    "scores": [85, 90, 78]
}

# Access
print(data["names"][0])  # Alice
print(data["scores"][1])  # 90

# Modify
data["names"].append("Diana")
data["ages"].extend([32, 26])

# Iterate
for i in range(len(data["names"])):
    print(f"{data['names'][i]}: Age {data['ages'][i]}, Score {data['scores'][i]}")
```

### Lists of Dictionaries

```python
# List of customer records
customers = [
    {"id": 1, "name": "Alice", "balance": 1000},
    {"id": 2, "name": "Bob", "balance": 500},
    {"id": 3, "name": "Charlie", "balance": 1500}
]

# Access
print(customers[0]["name"])  # Alice

# Find specific record
for customer in customers:
    if customer["id"] == 2:
        print(f"Found: {customer['name']}")
        break

# Add new record
customers.append({"id": 4, "name": "Diana", "balance": 2000})

# Update all records
for customer in customers:
    customer["balance"] *= 1.05  # 5% interest

# Filter
high_balance = [c for c in customers if c["balance"] > 1000]
```

## Comprehensions

### List Comprehensions

```python
# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
# Result: [1, 4, 9, 16, 25]

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]
# Result: [2, 4, 6, 8, 10]

# Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# Result: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# String processing
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
# Result: ['HELLO', 'WORLD', 'PYTHON']

# From dictionary
person = {"name": "John", "age": 30}
items = [f"{k}: {v}" for k, v in person.items()]
# Result: ['name: John', 'age: 30']

# Multiple conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x for x in numbers if x % 2 == 0 if x > 5]
# Result: [6, 8, 10]

# With else
result = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
# Result: ['odd', 'even', 'odd', 'even', 'odd']
```

### Dictionary Comprehensions

```python
# Basic
squares = {x: x**2 for x in range(1, 6)}
# Result: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
evens = {x: x**2 for x in range(1, 11) if x % 2 == 0}
# Result: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# From list
words = ["apple", "banana", "cherry"]
word_lengths = {w: len(w) for w in words}
# Result: {'apple': 5, 'banana': 6, 'cherry': 6}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
# Result: {1: 'a', 2: 'b', 3: 'c'}
```

### Set Comprehensions

```python
# Basic
squares = {x**2 for x in range(1, 6)}
# Result: {1, 4, 9, 16, 25}

# Remove duplicates
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = {x for x in numbers}
# Result: {1, 2, 3, 4, 5}

# With condition
evens = {x for x in range(1, 11) if x % 2 == 0}
# Result: {2, 4, 6, 8, 10}
```

## Data Processing Examples

### Example 1: Data Transformation

```python
# Raw data
raw_data = [
    "1,Alice,85,90,88",
    "2,Bob,78,82,80",
    "3,Charlie,90,92,91"
]

# Parse and transform
students = []
for line in raw_data:
    fields = line.split(',')
    student = {
        "id": int(fields[0]),
        "name": fields[1],
        "scores": [int(x) for x in fields[2:]]
    }
    student["average"] = sum(student["scores"]) / len(student["scores"])
    students.append(student)

# Display results
for student in students:
    print(f"{student['name']}: Average = {student['average']:.2f}")
```

### Example 2: Data Aggregation

```python
# Sales data
sales = [
    {"product": "A", "amount": 100},
    {"product": "B", "amount": 150},
    {"product": "A", "amount": 200},
    {"product": "C", "amount": 75},
    {"product": "B", "amount": 125}
]

# Aggregate by product
totals = {}
for sale in sales:
    product = sale["product"]
    if product not in totals:
        totals[product] = 0
    totals[product] += sale["amount"]

# Alternative using defaultdict
from collections import defaultdict
totals = defaultdict(int)
for sale in sales:
    totals[sale["product"]] += sale["amount"]

# Display
for product, total in sorted(totals.items()):
    print(f"Product {product}: ${total}")
```

### Example 3: Data Filtering

```python
# Employee records
employees = [
    {"id": 1, "name": "Alice", "salary": 50000, "dept": "IT"},
    {"id": 2, "name": "Bob", "salary": 60000, "dept": "HR"},
    {"id": 3, "name": "Charlie", "salary": 55000, "dept": "IT"},
    {"id": 4, "name": "Diana", "salary": 70000, "dept": "Finance"}
]

# Filter: IT department with salary > 55000
filtered = [e for e in employees if e["dept"] == "IT" and e["salary"] > 55000]

# Extract: Get only names
names = [e["name"] for e in employees]

# Sort: By salary descending
sorted_emp = sorted(employees, key=lambda e: e["salary"], reverse=True)

# Group: By department
from collections import defaultdict
by_dept = defaultdict(list)
for emp in employees:
    by_dept[emp["dept"]].append(emp)
```

---

**Collections Guide Version**: 1.0  
**Last Updated**: June 2026  
**Total Examples**: 120+
