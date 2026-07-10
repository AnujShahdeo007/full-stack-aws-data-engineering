# Python Control Flow — Complete Deep-Dive Notes

Control flow statements control the order in which instructions are executed in a program, based on conditions or repetition. Without control flow, code would just run top to bottom, one line after another, with no decisions or repetition.

---
1. Conditional Statements

1.1 if Statement
1.2 if-else Statement
1.3 if-elif-else Statement
1.4 Nested if
1.5 Ternary Operator (Conditional Expression)
1.6 Logical Operators in Conditions (and, or, not)

2. for Loop

2.1 Looping Through a String
2.2 range() Function
2.3 Looping Through a Dictionary
2.4 enumerate()
2.5 Nested for Loop

3. while Loop

3.1 Infinite Loop
3.2 while with User Input

4. Loop Control Statements

4.1 break
4.2 continue
4.3 pass

5. else with Loops (for-else, while-else)
6. Nested Loops with break/continue
7. match-case (Structural Pattern Matching)
8. Common Mistakes to Avoid
9. Practice Program (FizzBuzz)




# 1. Conditional Statements

## 1.1 `if` Statement

**Definition:**
The `if` statement executes a block of code only when a given condition evaluates to `True`. If the condition is `False`, the block is skipped entirely.

**Use Case:**
Used whenever a decision needs to be made — for example, checking eligibility, validating input, or controlling access.

**Syntax:**

```python
if condition:
    statement(s)
```

**Example:**

```python
age = 20
if age >= 18:
    print("You are eligible to vote")
```

**Real-Time Use Case:**

- Login systems: `if password == stored_password:` grant access
- E-commerce: `if cart_total > 500:` apply free shipping
- Data engineering: `if file_size > 0:` proceed to process the file, else skip

**Important Points:**

- A condition must return a boolean (`True`/`False`)
- Missing `:` causes `SyntaxError`
- Wrong indentation causes `IndentationError`

---

## 1.2 `if-else` Statement

**Definition:**
Executes one block if the condition is `True`, and a different block if it is `False`.

**Syntax:**

```python
if condition:
    statement(s)
else:
    statement(s)
```

**Example:**

```python
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 1.3 `if-elif-else` Statement

**Definition:**
Used to check multiple conditions in sequence. Python evaluates each condition top to bottom and executes the block of the first `True` condition.

**Syntax:**

```python
if condition1:
    statement(s)
elif condition2:
    statement(s)
elif condition3:
    statement(s)
else:
    statement(s)
```

**Example:**

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

## 1.4 Nested `if`

**Definition:**
An `if` statement placed inside another `if` or `else` block.

**Example:**

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not allowed, underage")
```

---

## 1.5 Ternary Operator (Conditional Expression)

**Definition:**
A one-line shorthand for a simple if-else statement.

**Syntax:**

```python
value_if_true if condition else value_if_false
```

**Example:**

```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

## 1.6 Logical Operators in Conditions (`and`, `or`, `not`)

```python
age = 25
income = 50000

if age > 18 and income > 30000:
    print("Eligible for loan")
```

---

# 2. Looping Statements

## 2.1 `for` Loop

**Definition:**
A `for` loop is used to iterate over a sequence such as a list, tuple, string, or range.

**Syntax:**

```python
for variable in sequence:
    statement(s)
```

**Example:**

```python
for i in range(1, 6):
    print(i)
```

---

## 2.2 `range()`

**Definition:**
`range()` generates a sequence of numbers.

**Example:**

```python
for i in range(1, 10, 2):
    print(i)
```

---

## 2.3 `for` Loop with `else`

```python
for i in range(3):
    print(i)
else:
    print("Loop finished without break")
```

---

## 2.4 `while` Loop

**Definition:**
A `while` loop repeatedly executes a block of code as long as the condition remains `True`.

**Syntax:**

```python
while condition:
    statement(s)
```

**Example:**

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

**Important Points:**

- The condition must eventually become `False` to avoid an infinite loop
- A loop variable should be updated inside the loop

---

## 2.5 `break`, `continue`, and `pass`

```python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
```

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

```python
for i in range(1, 3):
    pass
```

---

# 3. Pattern Matching with `match-case`

**Definition:**
`match-case` provides a modern way to compare a value against different patterns.

**Example:**

```python
day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("Weekend is near")
    case _:
        print("Some other day")
```

---

# 4. Common Mistakes to Avoid

- Forgetting `:` after `if`, `for`, or `while`
- Using wrong indentation
- Using `=` instead of `==` in comparisons
- Creating an infinite loop in `while`

---

# 5. Practice Program — FizzBuzz

```python
for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

---

# 6. Quick Recap

- `if`, `elif`, `else` are used for decision-making
- `for` loops iterate over known sequences
- `while` loops repeat until a condition becomes false
- `break` exits a loop early
- `continue` skips the current iteration
- `pass` is a placeholder
- `match-case` is a modern pattern-matching tool
