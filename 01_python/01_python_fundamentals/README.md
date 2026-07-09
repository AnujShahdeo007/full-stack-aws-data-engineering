# Python Fundamentals - Complete Guide

## Table of Contents
1. [Variables](#variables)
2. [Data Types](#data-types)
3. [Input & Output](#input--output)
4. [Operators](#operators)
5. [Type Casting](#type-casting)
6. [Best Practices](#best-practices)

## Variables

### What is a Variable?

A variable is a named container that stores a value in memory. It allows you to:
- Store data for later use
- Reference data by meaningful names
- Update values dynamically
- Track state in programs

### Variable Declaration & Assignment

```python
# Simple assignment
name = "Alice"
age = 30
salary = 50000.00

# Multiple assignment
x, y, z = 1, 2, 3

# Multiple assignment (same value)
a = b = c = 10

# Unpacking
first, second, third = ["Python", "Java", "C++"]
print(first)   # Output: Python
print(second)  # Output: Java

# Swap variables
a, b = 10, 20
a, b = b, a  # Now a=20, b=10
print(f"a={a}, b={b}")  # Output: a=20, b=10
```

### Naming Conventions

```python
# ✓ Good variable names (Python convention: snake_case)
customer_name = "John"
order_total = 150.50
is_active = True
max_retries = 3

# ✓ Good - descriptive
total_revenue_2024 = 1000000
user_count_by_region = {}

# ✗ Avoid - unclear
x = 10
data = "something"
temp = 42

# ✗ Avoid - Python reserved words
# class, def, import, if, for, while, etc.

# Case sensitivity matters
name = "Alice"  # lowercase 'n'
Name = "Bob"    # uppercase 'N'
# These are two different variables!
print(name)  # Output: Alice
print(Name)  # Output: Bob
```

### Variable Scope

```python
# Global scope
global_var = "I'm global"

def my_function():
    # Local scope
    local_var = "I'm local"
    print(global_var)  # ✓ Can access global
    print(local_var)   # ✓ Can access local

my_function()
print(global_var)  # ✓ Accessible
# print(local_var)  # ✗ Error: NameError

# Global keyword
counter = 0

def increment():
    global counter  # Modify global variable
    counter += 1

increment()
print(counter)  # Output: 1
```

### Checking Variable Type

```python
x = 10
y = "hello"
z = 3.14
flag = True

print(type(x))     # Output: <class 'int'>
print(type(y))     # Output: <class 'str'>
print(type(z))     # Output: <class 'float'>
print(type(flag))  # Output: <class 'bool'>

# Using isinstance()
print(isinstance(x, int))      # Output: True
print(isinstance(y, str))      # Output: True
print(isinstance(z, float))    # Output: True
```

## Data Types

### 1. Integers (int)

```python
# Integer literals
count = 42
negative = -100
zero = 0

# Large numbers
population = 1_000_000_000  # Underscore for readability

# Different bases
binary = 0b1010      # Binary: 10
octal = 0o755        # Octal: 493
hexadecimal = 0xFF   # Hex: 255

print(binary)        # Output: 10
print(octal)         # Output: 493
print(hexadecimal)   # Output: 255

# Integer operations
a = 10
b = 3

print(a + b)       # Output: 13 (addition)
print(a - b)       # Output: 7 (subtraction)
print(a * b)       # Output: 30 (multiplication)
print(a / b)       # Output: 3.333... (float division)
print(a // b)      # Output: 3 (integer division)
print(a % b)       # Output: 1 (modulo/remainder)
print(a ** b)      # Output: 1000 (exponentiation)
```

### 2. Floats (float)

```python
# Float literals
price = 19.99
pi = 3.14159
scientific = 1.23e-4  # 0.000123
large = 5.6e10        # 56000000000

# Float operations
x = 10.5
y = 3.2

print(x + y)       # Output: 13.7
print(x - y)       # Output: 7.3
print(x * y)       # Output: 33.6
print(x / y)       # Output: 3.281...
print(x // y)      # Output: 3.0
print(x ** 2)      # Output: 110.25

# Rounding
value = 3.14159
print(round(value))      # Output: 3
print(round(value, 2))   # Output: 3.14
print(round(value, 3))   # Output: 3.142

# Float precision issues
print(0.1 + 0.2)         # Output: 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # Output: False (!)

# Solution: Use Decimal for precise calculations
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))
```

### 3. Strings (str)

```python
# String creation
name = "John"
message = 'Hello World'
multiline = """This is a
multiline string"""

# String concatenation
first = "Hello"
second = "World"
result = first + " " + second  # "Hello World"

# String repetition
dash = "-" * 10  # "----------"
pattern = "Ha" * 3  # "HaHaHa"

# String length
text = "Python"
print(len(text))  # Output: 6

# Accessing characters
text = "Python"
print(text[0])    # Output: P (first char)
print(text[-1])   # Output: n (last char)
print(text[1:4])  # Output: yth (substring)

# String methods
text = "hello world"
print(text.upper())           # OUTPUT: HELLO WORLD
print(text.capitalize())      # Output: Hello world
print(text.replace("world", "python"))  # Output: hello python
print("HELLO".lower())        # Output: hello
print(text.split())           # Output: ['hello', 'world']
```

### 4. Booleans (bool)

```python
# Boolean values
active = True
inactive = False

# Boolean operations
x = 10
y = 5

print(x > y)        # Output: True
print(x < y)        # Output: False
print(x == y)       # Output: False
print(x != y)       # Output: True
print(x >= 10)      # Output: True

# Logical operations
a = True
b = False

print(a and b)      # Output: False
print(a or b)       # Output: True
print(not a)        # Output: False

# Truthy and Falsy
# Falsy values: 0, "", [], {}, None, False
# Truthy values: everything else

print(bool(0))      # Output: False
print(bool(""))     # Output: False
print(bool([]))     # Output: False
print(bool(1))      # Output: True
print(bool("hello")) # Output: True
```

### 5. None Type

```python
# None represents absence of value
result = None

# Check for None
if result is None:
    print("Result is None")

# Default parameter
def process(data=None):
    if data is None:
        data = []
    return data

# Function with no return statement
def no_return():
    print("Hello")
    # Implicitly returns None

value = no_return()
print(value)  # Output: None
print(type(value))  # Output: <class 'NoneType'>
```

## Input & Output

### Input from User

```python
# Get string input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Get multiple inputs
x = input("Enter first number: ")
y = input("Enter second number: ")

# Convert to numbers
x = int(input("Enter an integer: "))
y = float(input("Enter a decimal: "))

# Example: Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"

print(f"Result: {result}")
```

### Output to User

```python
# Basic print
print("Hello, World!")

# Multiple values
name = "Alice"
age = 30
print("Name:", name, "Age:", age)

# Formatted strings (f-strings) - BEST PRACTICE
name = "Bob"
age = 25
salary = 50000

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Salary: ${salary:,.2f}")  # Output: Salary: $50,000.00

# Format with expressions
x = 10
y = 20
print(f"Sum: {x + y}")
print(f"Product: {x * y}")

# String formatting (older style)
print("Name: %s, Age: %d" % (name, age))

# Using .format()
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))

# Separator and end parameters
print("A", "B", "C", sep="-")  # Output: A-B-C
print("Loading", end="")
print(".", end="")
print(" Done!")  # Output: Loading... Done!
```

### String Formatting Examples

```python
# Number formatting
value = 1234.5678

print(f"{value:.2f}")        # Output: 1234.57
print(f"{value:.0f}")        # Output: 1235
print(f"{value:,.2f}")       # Output: 1,234.57 (with comma)
print(f"{value:e}")          # Output: 1.234568e+03 (scientific)

# Padding
text = "hello"
print(f"{text:>10}")         # Output: "     hello"
print(f"{text:<10}")         # Output: "hello     "
print(f"{text:^10}")         # Output: "  hello   "
print(f"{text:*^10}")        # Output: "**hello***"

# Zero padding for numbers
num = 42
print(f"{num:05d}")          # Output: 00042

# Percentage
percentage = 0.75
print(f"{percentage:.1%}")   # Output: 75.0%

# Data Engineering Example: Log Formatting
timestamp = "2024-01-15 10:30:45"
event = "Data processed"
count = 150000
print(f"[{timestamp}] {event:20s} - Records: {count:>10,}")
# Output: [2024-01-15 10:30:45] Data processed     - Records:     150,000
```

## Operators

### Arithmetic Operators

```python
# Basic arithmetic
print(10 + 5)      # Output: 15 (addition)
print(10 - 5)      # Output: 5 (subtraction)
print(10 * 5)      # Output: 50 (multiplication)
print(10 / 5)      # Output: 2.0 (division)
print(10 // 3)     # Output: 3 (floor division)
print(10 % 3)      # Output: 1 (modulo)
print(10 ** 2)     # Output: 100 (exponentiation)

# Data engineering examples
total_records = 1000000
batch_size = 10000
num_batches = total_records // batch_size  # 100
remaining = total_records % batch_size      # 0

# Calculate percentage
processed = 750
total = 1000
percentage = (processed / total) * 100  # 75.0
print(f"Processed: {percentage:.1f}%")
```

### Comparison Operators

```python
# Equal to
print(10 == 10)    # Output: True
print(10 == 11)    # Output: False

# Not equal to
print(10 != 11)    # Output: True
print(10 != 10)    # Output: False

# Greater than
print(10 > 5)      # Output: True
print(5 > 10)      # Output: False

# Less than
print(5 < 10)      # Output: True
print(10 < 5)      # Output: False

# Greater than or equal
print(10 >= 10)    # Output: True
print(10 >= 9)     # Output: True

# Less than or equal
print(10 <= 10)    # Output: True
print(9 <= 10)     # Output: True

# String comparison
print("apple" < "banana")      # Output: True (alphabetical)
print("hello" == "hello")      # Output: True
```

### Logical Operators

```python
# AND operator
print(True and True)      # Output: True
print(True and False)     # Output: False
print(False and False)    # Output: False

age = 25
is_employed = True
if age >= 18 and is_employed:
    print("Eligible for loan")

# OR operator
print(True or False)      # Output: True
print(False or False)     # Output: False

credit_score = 500
income = 30000
if credit_score > 600 or income > 50000:
    print("Eligible for credit")

# NOT operator
active = True
print(not active)         # Output: False

inactive_users = []
if not inactive_users:
    print("No inactive users found")

# Complex conditions
age = 30
income = 60000
employed = True

if (age >= 25) and (income >= 50000 or employed):
    print("Eligible for mortgage")
```

### Assignment Operators

```python
# Simple assignment
x = 10

# Addition assignment
x += 5   # x = x + 5 = 15

# Subtraction assignment
x -= 3   # x = x - 3 = 12

# Multiplication assignment
x *= 2   # x = x * 2 = 24

# Division assignment
x /= 4   # x = x / 4 = 6.0

# Floor division assignment
x //= 2  # x = x // 2 = 3.0

# Modulo assignment
x %= 2   # x = x % 2 = 1.0

# Exponentiation assignment
x **= 2  # x = x ** 2 = 1.0

# Data processing example
total_amount = 1000
commission_rate = 0.05
commission = total_amount * commission_rate  # 50
total_amount -= commission  # 950
```

### Membership Operators

```python
# in operator
print(3 in [1, 2, 3, 4])        # Output: True
print(5 in [1, 2, 3, 4])        # Output: False
print("a" in "apple")            # Output: True
print("hello" in "hello world")   # Output: True

# not in operator
print(5 not in [1, 2, 3, 4])    # Output: True
print("z" not in "apple")        # Output: True

# Data engineering example
required_columns = ['id', 'name', 'email']
csv_columns = ['id', 'name', 'email', 'phone']

for col in required_columns:
    if col not in csv_columns:
        print(f"Missing column: {col}")
```

### Identity Operators

```python
# is operator
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)      # Output: False (different objects)
print(a is c)      # Output: True (same object)
print(a == b)      # Output: True (same content)

# None check
result = None
if result is None:
    print("No result yet")

# Singleton check
x = True
y = True
print(x is y)      # Output: True (True is singleton)
```

### Operator Precedence

```
**          Exponentiation
+x, -x, ~x  Unary plus, minus, bitwise NOT
*, /, //, % Multiplication, division, floor div, modulo
+, -        Addition, subtraction
<<, >>      Bitwise shifts
&           Bitwise AND
^           Bitwise XOR
|           Bitwise OR
==, !=, <, >, <=, >= Comparison
is, is not  Identity
in, not in  Membership
not         Logical NOT
and         Logical AND
or          Logical OR
```

```python
# Examples
print(2 + 3 * 4)           # Output: 14 (* before +)
print((2 + 3) * 4)         # Output: 20 (parentheses first)
print(10 - 5 - 2)          # Output: 3 (left to right)
print(2 ** 3 ** 2)         # Output: 512 (** is right to left)
```

## Type Casting

### Converting Between Types

```python
# String to Integer
age_str = "25"
age = int(age_str)
print(age)         # Output: 25
print(type(age))   # Output: <class 'int'>

# String to Float
price_str = "19.99"
price = float(price_str)
print(price)       # Output: 19.99

# Integer to String
count = 100
count_str = str(count)
print(count_str)   # Output: "100"

# Float to Integer (truncates)
value = 3.7
integer = int(value)
print(integer)     # Output: 3

# Integer to Float
age = 25
age_float = float(age)
print(age_float)   # Output: 25.0

# String to Boolean
print(bool("hello"))     # Output: True
print(bool(""))          # Output: False
```

### Type Conversion Examples

```python
# Data processing example
csv_line = "1001,John,25,50000.50,true"
fields = csv_line.split(',')

# Convert types
customer_id = int(fields[0])
name = fields[1]
age = int(fields[2])
salary = float(fields[3])
is_active = fields[4] == 'true'

print(f"Customer ID: {customer_id} (type: {type(customer_id).__name__})")
print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Salary: {salary} (type: {type(salary).__name__})")
print(f"Active: {is_active} (type: {type(is_active).__name__})")

# Try-except for safe conversion
def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert '{value}' to integer")
        return None

print(safe_int_conversion("123"))    # Output: 123
print(safe_int_conversion("abc"))    # Output: Cannot convert... None
```

## Best Practices

### 1. Naming Conventions

```python
# ✓ Use descriptive names
customer_name = "John"
total_amount = 1000
is_active = True
max_retries = 3
_private_var = "internal"

# ✗ Avoid unclear names
x = 10
data = "something"
temp = 42

# Constants (all caps)
MAX_FILE_SIZE = 1000000
DATABASE_URL = "localhost:5432"
API_TIMEOUT = 30
```

### 2. Type Hints

```python
def calculate_total(price: float, tax_rate: float) -> float:
    """Calculate total with tax."""
    return price * (1 + tax_rate)

def process_records(records: list) -> dict:
    """Process records and return statistics."""
    return {'count': len(records)}

# Using Type annotation
from typing import List, Dict, Optional

def get_customer(customer_id: int) -> Optional[Dict]:
    """Get customer by ID, return None if not found."""
    return None
```

### 3. Documentation

```python
def calculate_discount(amount: float, discount_percent: float) -> float:
    """
    Calculate the discounted amount.
    
    Args:
        amount (float): Original amount
        discount_percent (float): Discount percentage (0-100)
        
    Returns:
        float: Amount after discount
        
    Example:
        >>> calculate_discount(100, 10)
        90.0
    """
    return amount * (1 - discount_percent / 100)
```

### 4. Error Handling

```python
# Good error handling
def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"Error: Cannot convert '{value}' to integer")
        return None
    except TypeError:
        print(f"Error: Type error converting '{value}'")
        return None

# Data validation
def process_order(order_id, amount):
    if not isinstance(order_id, int):
        raise TypeError("order_id must be an integer")
    
    if order_id <= 0:
        raise ValueError("order_id must be positive")
    
    if amount < 0:
        raise ValueError("amount cannot be negative")
    
    return f"Order {order_id} for ${amount:.2f} processed"
```

---

**Fundamentals Guide Version**: 1.0  
**Last Updated**: June 2026  
**Total Examples**: 150+
