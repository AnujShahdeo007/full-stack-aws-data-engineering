# Python Control Flow 

## 1. What is Control Flow?

Control flow is the order in which individual statements, instructions, or function calls of a program are executed or evaluated. By default, a program runs top to bottom, one line after another — control flow tools let you change that default order based on conditions, repetition, or events.

## 2. Why do we need Control Flow?

Without control flow, every program would just be a flat list of instructions executed once, in order. Real programs need to:
- Make decisions (do X only if some condition is true)
- Repeat actions (process every item in a list)
- Handle errors gracefully instead of crashing
- Skip or stop execution based on changing data

Control flow gives a program the ability to "think" — to react differently depending on input and state.

## 3. How Python Executes Code

- Python reads and executes code line by line, top to bottom, inside a given block (this is called the **interpreter's execution order**).
- Code is grouped into **blocks** using **indentation** (not braces `{}` like C/Java). Consistent indentation (commonly 4 spaces) is mandatory — Python uses it to know what belongs inside an `if`, `for`, function, etc.
- Each line is compiled into bytecode and executed by the Python Virtual Machine (PVM) sequentially, unless a control flow statement (`if`, `for`, `while`, `return`, `break`, etc.) redirects execution.

```python
print("1")   # runs first
print("2")   # runs second
print("3")   # runs third
```

## 4. Sequential Flow

This is the default flow — statements execute one after another in the exact order they're written, with no branching or repetition.

```python
a = 5
b = 10
c = a + b
print(c)   # 15
```

## 5. Conditional Statements

Conditional statements let the program choose between different paths based on whether an expression evaluates to `True` or `False`.

### `if`

Executes a block only when the condition is `True`.

```python
age = 20
if age >= 18:
    print("Eligible to vote")
```

### `if-else`

Provides an alternate path when the condition is `False`.

```python
age = 15
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

### `if-elif-else`

Checks multiple conditions in sequence; the first `True` condition's block runs and the rest are skipped.

```python
marks = 72
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

### Nested if

An `if` statement inside another `if` (or `else`) block — used when a decision depends on another decision.

```python
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Non-positive")
```

### Multiple Conditions

You can combine several checks using comparison chaining or logical operators.

```python
x = 7
if 0 < x < 10:        # chained comparison
    print("Single digit positive")

if x > 0 and x % 2 != 0:
    print("Positive odd number")
```

## 6. Logical Operators inside Conditions

| Operator | Meaning | Example |
|---|---|---|
| `and` | True if both conditions are True | `a > 0 and b > 0` |
| `or` | True if at least one condition is True | `a > 0 or b > 0` |
| `not` | Reverses the boolean result | `not (a > 0)` |

```python
age = 25
income = 50000
if age > 18 and income > 30000:
    print("Loan approved")

is_admin = False
if not is_admin:
    print("Access restricted")
```

Python also short-circuits: in `and`, evaluation stops at the first `False`; in `or`, it stops at the first `True`.

## 7. Ternary Operator

A one-line shorthand for simple `if-else` assignments.

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

Syntax: `value_if_true if condition else value_if_false`

## 8. Match Case (Python 3.10+)

Python's structural pattern matching — similar to `switch` in other languages, but more powerful (supports pattern matching, not just value equality).

```python
def describe(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 6 | 7:
            return "Weekend"
        case _:
            return "Unknown"

print(describe(6))   # Weekend
```

It also supports matching structures like lists/dicts:

```python
point = (0, 5)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"On Y-axis at {y}")
    case (x, 0):
        print(f"On X-axis at {x}")
    case _:
        print("Somewhere else")
```

## 9. Loops

Loops repeat a block of code multiple times.

### `while`

Repeats as long as a condition stays `True`. Used when the number of iterations isn't known in advance.

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### `for`

Iterates over a sequence (list, tuple, string, range, dict, etc.). Used when iterating over a known collection.

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

## 10. Loop Internals

- A `for` loop in Python works by calling `iter()` on the object to get an **iterator**, then repeatedly calling `next()` on it until a `StopIteration` exception is raised internally (Python catches this automatically to end the loop).
- A `while` loop simply re-evaluates its condition expression before every iteration; the loop body keeps running until that expression evaluates to `False`.

```python
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# next(it) again -> raises StopIteration
```

## 11. `range()`

Generates a sequence of numbers, commonly used with `for` loops.

```python
range(stop)               # 0 to stop-1
range(start, stop)        # start to stop-1
range(start, stop, step)  # with step

for i in range(2, 10, 2):
    print(i)   # 2 4 6 8
```

`range()` produces values lazily (it doesn't store the whole list in memory) — it's a memory-efficient sequence type.

## 12. Nested Loops

A loop inside another loop — the inner loop completes all its iterations for each single iteration of the outer loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

Common use case: printing patterns, working with grids/matrices.

```python
for i in range(1, 5):
    print("*" * i)
```

## 13. Loop Control Statements

### `break`

Immediately exits the nearest enclosing loop, skipping any remaining iterations.

```python
for num in range(10):
    if num == 5:
        break
    print(num)   # 0 1 2 3 4
```

### `continue`

Skips the rest of the current iteration and moves to the next one.

```python
for num in range(5):
    if num == 2:
        continue
    print(num)   # 0 1 3 4
```

### `pass`

A null operation — does nothing. Used as a placeholder where syntax requires a statement but no action is needed yet.

```python
for num in range(5):
    if num == 2:
        pass   # placeholder, does nothing
    print(num)
```

## 14. `else` with Loops

Python loops (`for`/`while`) support an `else` block that runs only if the loop completes **without** hitting a `break`.

```python
for n in range(2, 10):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, "is prime")
```

This is useful for search-and-flag patterns (e.g., "search through a list, and if nothing was found, do X").

## 15. Infinite Loops

A loop whose condition never becomes `False` (intentionally or by mistake) — runs forever unless broken externally.

```python
while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == "exit":
        break
```

Common causes of accidental infinite loops: forgetting to update the loop variable, or a condition that can never be `False`. Always have a clear exit condition (`break`, updating the counter, etc.).

## 16. Comprehensions

Compact syntax to build collections using a loop and optional condition in a single line.

### List Comprehension

```python
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### Dictionary Comprehension

```python
square_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Set Comprehension

```python
unique_lengths = {len(word) for word in ["hi", "hello", "hey", "ok"]}
# {2, 5, 3}
```

Comprehensions are generally faster and more readable than building the same collection with an explicit loop and `.append()`.

## 17. Exception-based Control Flow

Exceptions let a program react to errors at runtime instead of crashing — this is also a form of control flow since it changes execution order when something goes wrong.

### `try` / `except`

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

### Multiple `except` blocks

```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
except Exception as e:
    print("Something else went wrong:", e)
```

### `finally`

Always runs, whether an exception occurred or not — typically used for cleanup (closing files, releasing resources).

```python
try:
    f = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Done attempting to open file")
```

### `else` (with try)

Runs only if the `try` block did **not** raise an exception.

```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Division succeeded:", x)
finally:
    print("Execution complete")
```

## 18. Practical Examples

**Check if a number is prime:**
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**Sum of digits:**
```python
n = 1234
total = 0
while n > 0:
    total += n % 10
    n //= 10
print(total)   # 10
```

**FizzBuzz:**
```python
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

**Find the largest of three numbers:**
```python
a, b, c = 12, 45, 7
largest = a if a > b and a > c else (b if b > c else c)
print(largest)
```

## 19. Real World Projects (Ideas using Control Flow)

- **Login system**: `if/elif/else` to validate username/password attempts, with a `while` loop to allow limited retries.
- **ATM simulator**: `match-case` or `if-elif` for menu choices (deposit, withdraw, balance), loops for repeated transactions, exceptions for insufficient funds.
- **Grade calculator**: nested `if-elif` to assign grades, loops to process a whole class list, comprehension to build a results dictionary.
- **To-do list CLI app**: `while True` main loop, `break` to exit, `try/except` for invalid menu input.
- **Number guessing game**: `while` loop until correct guess, `if/elif/else` for hints (too high/low), loop control for limited attempts.
- **File processor**: `try/except/finally` for safe file handling, loops to process each line, comprehension to filter/transform data.
- **Inventory management system**: nested loops for matrix-like stock data, exception handling for invalid stock entries.

## 20. Interview Questions

1. What's the difference between `break`, `continue`, and `pass`?
2. How does Python's `for` loop differ from a C-style `for` loop?
3. What is the purpose of `else` in a loop, and when does it execute?
4. Explain short-circuit evaluation with `and`/`or` with an example.
5. What's the difference between `if-elif-else` and multiple separate `if` statements?
6. How does `match-case` differ from a series of `if-elif` statements?
7. What happens internally when you iterate over a list using a `for` loop? (iterator protocol, `StopIteration`)
8. Write a one-liner using a list comprehension to filter even numbers from a list.
9. What is the difference between `try-except-else` and just `try-except`?
10. Why is `finally` guaranteed to execute, and when would you use it?
11. How would you avoid an infinite loop when accepting repeated user input?
12. What's the output of this code, and why?
```python
for i in range(3):
    if i == 1:
        continue
    print(i)
```
13. Explain the difference between mutable and immutable default conditions affecting loop behavior (e.g., modifying a list while iterating over it).
14. What is the time complexity consideration when using nested loops vs. comprehensions for the same task?
15. How do you implement a `switch`-like structure in Python versions before 3.10?
