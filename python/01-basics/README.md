# Python Basics – Complete Notes

## 1. What is Python?

Python is a high-level, interpreted, general-purpose programming language.

- High-level → you don't manage memory manually, close to human language
- Interpreted → code runs line by line (no separate compile step)
- General-purpose → used in web development, data science, automation, AI, and more

---

## 2. Installing & Running Python

- Check version: `python --version` or `python3 --version`
- Run a file: `python filename.py`
- Interactive mode: type `python` in the terminal

---

## 3. Comments

Comments are ignored by Python and are used to explain code.

```python
# This is a single-line comment

"""
This is a
multi-line comment (docstring)
"""
```

---

## 4. Indentation (Very Important in Python)

Python uses indentation (spaces) instead of braces `{}` to define code blocks.

```python
if True:
    print("Indented correctly")
```

⚠️ Wrong indentation causes an `IndentationError`.

---

## 5. Variables

A variable stores a value. You do not need to declare a type explicitly.

```python
name = "Alex"
age = 25
price = 99.99
is_active = True
```

### Rules for naming variables

- Must start with a letter or underscore (`_`)
- Cannot start with a number
- Case-sensitive (`age` and `Age` are different)
- Cannot use Python keywords like `if`, `for`, `class`

---

## 6. Data Types

| Type | Example | Description |
|------|---------|-------------|
| `int` | `10` | Whole numbers |
| `float` | `10.5` | Decimal numbers |
| `str` | `"hello"` | Text |
| `bool` | `True/False` | Boolean values |
| `complex` | `2+3j` | Complex numbers |
| `NoneType` | `None` | Represents no value |

Check the type of a variable:

```python
print(type(age))
```

---

## 7. Type Casting (Converting Types)

```python
x = "10"
y = int(x)      # string -> int
z = str(25)     # int -> string
f = float(10)   # int -> float
```

---

## 8. Taking Input & Printing Output

```python
name = input("Enter your name: ")
print("Hello", name)
```

⚠️ `input()` always returns a string, even if the user enters a number.

```python
age = int(input("Enter age: "))
```

---

## 9. String Formatting

```python
name = "Alex"
age = 25

# f-string (best and most used)
print(f"My name is {name} and I am {age} years old")

# .format() method
print("My name is {} and I am {} years old".format(name, age))

# % formatting (older style)
print("My name is %s and I am %d years old" % (name, age))
```

---

## 10. Operators

### Arithmetic Operators

```python
+   # addition
-   # subtraction
*   # multiplication
/   # division (always returns float)
//  # floor division
%   # modulus (remainder)
**  # exponent (power)
```

### Comparison Operators

```python
==  # equal to
!=  # not equal to
>   # greater than
<   # less than
>=  # greater than or equal to
<=  # less than or equal to
```

### Logical Operators

```python
and
or
not
```

---

## 11. Conditional Statements

```python
age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

---

## Quick Recap (Cheat Sheet)

| Concept | Key Point |
|---------|-----------|
| Comments | `#` for single-line, `""""""` for multi-line |
| Indentation | 4 spaces define code blocks |
| Variables | No type declaration needed |
| Data Types | `int`, `float`, `str`, `bool`, `complex`, `None` |
| Type Casting | `int()`, `str()`, `float()` |
| Input | Always returns a string |
| Formatting | f-strings are the best method |

---

## Extra Notes

- Python is beginner-friendly and widely used in real-world projects.
- Write clean, readable code with meaningful variable names.
- Practice small programs daily to improve logic and confidence.
