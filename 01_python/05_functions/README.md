# Python Functions - Complete Guide

## Table of Contents
1. [Function Basics](#function-basics)
2. [Parameters and Arguments](#parameters-and-arguments)
3. [Return Values](#return-values)
4. [Scope and Lifetime](#scope-and-lifetime)
5. [Advanced Functions](#advanced-functions)
6. [Decorators](#decorators)
7. [Data Engineering Examples](#data-engineering-examples)

## Function Basics

### Function Definition

```python
# Basic function
def greet():
    """Greet the user."""
    print("Hello, World!")

greet()  # Call the function

# Function with parameter
def greet_user(name):
    """Greet a specific user."""
    print(f"Hello, {name}!")

greet_user("Alice")

# Function with multiple parameters
def add(a, b):
    """Add two numbers."""
    result = a + b
    return result

sum_result = add(5, 3)
print(sum_result)  # Output: 8
```

### Docstrings

```python
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius: The radius of the circle
        
    Returns:
        The area of the circle
        
    Raises:
        ValueError: If radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    
    import math
    return math.pi * radius ** 2

# Access docstring
print(calculate_area.__doc__)
help(calculate_area)
```

## Parameters and Arguments

### Positional Arguments

```python
def print_info(name, age, city):
    """Print user information."""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Positional arguments
print_info("Alice", 30, "NYC")

# Order matters
print_info("Bob", "Chicago", 25)  # Wrong order!
```

### Keyword Arguments

```python
def print_info(name, age, city):
    """Print user information."""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Keyword arguments (order doesn't matter)
print_info(age=30, city="NYC", name="Alice")
print_info(name="Bob", age=25, city="Chicago")

# Mix positional and keyword
print_info("Charlie", age=35, city="LA")
```

### Default Parameters

```python
def greet(name, greeting="Hello"):
    """Greet someone with optional greeting."""
    return f"{greeting}, {name}!"

print(greet("Alice"))              # Hello, Alice!
print(greet("Bob", "Hi"))          # Hi, Bob!
print(greet("Charlie", greeting="Hey"))  # Hey, Charlie!

# Multiple defaults
def create_user(name, email="", role="user", active=True):
    """Create a user with defaults."""
    return {
        "name": name,
        "email": email,
        "role": role,
        "active": active
    }

user1 = create_user("Alice")
user2 = create_user("Bob", "bob@example.com", "admin")
user3 = create_user("Charlie", role="moderator", active=False)
```

### Variable-Length Arguments

```python
# *args - Non-keyword variable arguments (tuple)
def sum_numbers(*args):
    """Sum any number of arguments."""
    return sum(args)

print(sum_numbers(1, 2, 3))           # 6
print(sum_numbers(1, 2, 3, 4, 5))     # 15

# Practical example
def print_items(*items):
    """Print all items."""
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

print_items("apple", "banana", "cherry")

# **kwargs - Keyword variable arguments (dictionary)
def print_info(**kwargs):
    """Print information from keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# Output:
# name: Alice
# age: 30
# city: NYC

# Combine all types
def flexible_function(a, b, *args, default="value", **kwargs):
    """Function with all parameter types."""
    print(f"Required: {a}, {b}")
    print(f"Additional args: {args}")
    print(f"Default: {default}")
    print(f"Keywords: {kwargs}")

flexible_function(1, 2, 3, 4, default="custom", x=10, y=20)
# Output:
# Required: 1, 2
# Additional args: (3, 4)
# Default: custom
# Keywords: {'x': 10, 'y': 20}
```

### Unpacking Arguments

```python
# Unpacking in function call
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)  # Unpacking
print(result)  # 6

# Dictionary unpacking
def print_person(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person_dict = {"name": "Alice", "age": 30, "city": "NYC"}
print_person(**person_dict)
```

## Return Values

### Single Return Value

```python
def square(x):
    """Return square of x."""
    return x ** 2

result = square(5)
print(result)  # 25

# Early return
def is_adult(age):
    """Check if person is adult."""
    if age < 18:
        return False
    return True

print(is_adult(25))  # True
print(is_adult(15))  # False
```

### Multiple Return Values

```python
# Return tuple
def get_coordinates():
    """Return x and y coordinates."""
    return 10, 20  # Returns tuple (10, 20)

x, y = get_coordinates()
print(f"X: {x}, Y: {y}")

# Return multiple values - unpacking
def get_user_info():
    """Return user information."""
    return "Alice", 30, "alice@example.com"

name, age, email = get_user_info()

# Return dictionary
def calculate_stats(numbers):
    """Calculate statistics."""
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers)
    }

stats = calculate_stats([1, 2, 3, 4, 5])
print(f"Average: {stats['average']}")
```

### None Return

```python
def print_message(msg):
    """Print message and return None."""
    print(msg)
    # Implicitly returns None

result = print_message("Hello")
print(result)  # None

# Explicit return None
def process_data(data):
    """Process data or return None if invalid."""
    if not data:
        return None
    return len(data)

result = process_data([1, 2, 3])
print(result)  # 3

result = process_data([])
print(result)  # None
```

## Scope and Lifetime

### Local vs Global Scope

```python
x = 10  # Global variable

def local_scope():
    """Demonstrate local scope."""
    x = 20  # Local variable
    print(f"Inside function: x = {x}")

local_scope()           # Inside function: x = 20
print(f"Outside function: x = {x}")  # Outside function: x = 10

# Modify global variable
counter = 0

def increment():
    """Increment global counter."""
    global counter
    counter += 1

increment()
print(counter)  # 1

# Nonlocal (nested functions)
def outer():
    """Outer function."""
    count = 0
    
    def inner():
        """Inner function."""
        nonlocal count
        count += 1
        return count
    
    return inner

func = outer()
print(func())  # 1
print(func())  # 2
print(func())  # 3
```

### Variable Lifetime

```python
def example():
    """Demonstrate variable lifetime."""
    local_var = 100
    print(f"Inside: {local_var}")

example()
# print(local_var)  # ✗ NameError: name 'local_var' is not defined

# Static-like behavior with default arguments
def counter(n=[]):
    """Count function calls."""
    n.append(1)
    return len(n)

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## Advanced Functions

### Lambda Functions

```python
# Lambda: Anonymous function
square = lambda x: x ** 2
print(square(5))  # 25

# With multiple parameters
add = lambda x, y: x + y
print(add(3, 4))  # 7

# Use with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Filter with lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Sort with lambda
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_by_age = sorted(people, key=lambda p: p["age"])
```

### map(), filter(), reduce()

```python
# map() - Apply function to each item
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# filter() - Keep items where function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# reduce() - Combine items
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)

# With initial value
total = reduce(lambda x, y: x + y, numbers, 100)
print(total)  # 115 (100 + 1 + 2 + 3 + 4 + 5)
```

### Closures

```python
def outer(x):
    """Create a closure."""
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(3))  # 8 (5 + 3)
print(add_5(10)) # 15 (5 + 10)

# Practical closure example
def multiply_by(factor):
    """Return a function that multiplies by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = multiply_by(2)
triple = multiply_by(3)

print(double(5))  # 10
print(triple(5))  # 15
```

## Decorators

### Basic Decorators

```python
# Simple decorator
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call

# Decorator with arguments
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(3, 4)
```

### Decorators with Parameters

```python
# Decorator that takes parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

### Common Decorators

```python
# Timing decorator
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()

# Caching decorator
def cache(func):
    cached_result = {}
    def wrapper(x):
        if x not in cached_result:
            cached_result[x] = func(x)
        return cached_result[x]
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
```

## Data Engineering Examples

### Example 1: Data Validation

```python
def validate_email(email):
    """Validate email format."""
    if "@" not in email or "." not in email:
        return False
    return True

def validate_age(age):
    """Validate age."""
    if not isinstance(age, int) or age < 0 or age > 150:
        return False
    return True

def validate_record(record):
    """Validate a user record."""
    required_fields = ["name", "email", "age"]
    
    # Check required fields
    for field in required_fields:
        if field not in record:
            return False, f"Missing field: {field}"
    
    # Validate email
    if not validate_email(record["email"]):
        return False, "Invalid email format"
    
    # Validate age
    if not validate_age(record["age"]):
        return False, "Invalid age"
    
    return True, "Valid record"

# Test
record = {"name": "Alice", "email": "alice@example.com", "age": 30}
valid, message = validate_record(record)
print(f"Valid: {valid}, Message: {message}")
```

### Example 2: Data Transformation Pipeline

```python
def extract_numbers(text):
    """Extract numbers from text."""
    import re
    return [int(x) for x in re.findall(r'\d+', text)]

def process_numbers(numbers):
    """Process numbers."""
    return [x * 2 for x in numbers if x > 0]

def aggregate_data(numbers):
    """Aggregate data."""
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers) if numbers else 0,
        "max": max(numbers) if numbers else None,
        "min": min(numbers) if numbers else None
    }

def pipeline(text):
    """Data processing pipeline."""
    numbers = extract_numbers(text)
    processed = process_numbers(numbers)
    result = aggregate_data(processed)
    return result

# Test
text = "Values: 10, -5, 20, -3, 30, 15"
result = pipeline(text)
print(result)
# Output: {'count': 4, 'sum': 110, 'average': 27.5, 'max': 30, 'min': 10}
```

### Example 3: Batch Processing

```python
def process_record(record):
    """Process single record."""
    return {
        **record,
        "processed": True,
        "timestamp": __import__("datetime").datetime.now()
    }

def batch_process(records, batch_size=10):
    """Process records in batches."""
    results = []
    errors = []
    
    for i, record in enumerate(records):
        try:
            processed = process_record(record)
            results.append(processed)
        except Exception as e:
            errors.append((i, str(e)))
        
        # Report progress
        if (i + 1) % batch_size == 0:
            print(f"Processed {i + 1} records")
    
    return results, errors

# Test
records = [
    {"id": 1, "name": "Alice", "value": 100},
    {"id": 2, "name": "Bob", "value": 200},
    {"id": 3, "name": "Charlie", "value": 300}
]

results, errors = batch_process(records, batch_size=2)
print(f"Processed: {len(results)}, Errors: {len(errors)}")
```

### Example 4: Error Handling

```python
def safe_divide(a, b):
    """Divide with error handling."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid type for division")
        return None

def retry_operation(func, max_retries=3, delay=1):
    """Retry a function call."""
    import time
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
            time.sleep(delay)

def operation_with_retry():
    """Example operation that might fail."""
    import random
    if random.random() > 0.7:
        return "Success"
    else:
        raise Exception("Random failure")

# Test
try:
    result = retry_operation(operation_with_retry, max_retries=5)
    print(f"Result: {result}")
except Exception as e:
    print(f"Failed after retries: {e}")
```

---

**Functions Guide Version**: 1.0  
**Last Updated**: June 2026  
**Total Examples**: 100+
