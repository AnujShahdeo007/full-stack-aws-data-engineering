# Python Fundamentals — Complete Theory Notes
### Variables • Data Types • Operators • Typecasting • Comments • Input/Output
*(Full theory + concepts + examples + use cases — exam/interview/reference ready)*

---

# Introduction: How Python Works (Background Theory)

Before diving into topics, it helps to understand a few foundational facts about Python that explain *why* it behaves the way it does:

| Property | Meaning |
|----------|---------|
| **Interpreted** | Code is executed line-by-line by the Python interpreter (CPython by default), not compiled to machine code ahead of time. |
| **Dynamically Typed** | Variable types are determined at runtime, not declared in advance. The same name can refer to different types over its lifetime. |
| **Strongly Typed** | Python does not silently convert unrelated types (e.g., `"5" + 5` raises an error) — unlike weakly typed languages such as JavaScript. |
| **Object-Oriented (everything is an object)** | Even integers, strings, and functions are objects with a type, an identity, and attached methods. |
| **High-Level** | Memory management (allocation/deallocation) is handled automatically via reference counting and garbage collection. |

This explains why Python "feels flexible" — type safety is enforced at runtime rather than compile time, and every value (no matter how small) is a full-fledged object living in memory.

---

# CHAPTER 1: VARIABLES

## 1.1 Theory: What Is a Variable?

**Definition:** A variable is a symbolic name (identifier) that acts as a reference (or "label") to an object stored in memory. It does **not** store the value directly — it stores a reference/pointer to the object.

This concept is formally called **name binding**. When you write `x = 10`:
1. Python creates an integer object `10` somewhere in memory.
2. The name `x` is *bound* to that object.
3. `x` is added to the current **namespace** (a dictionary-like mapping of names to objects).

```python
x = 10
print(id(x))      # unique memory identity of the object
print(type(x))    # type of the object x refers to
```

### Why This Model Matters
Because variables are references, multiple names can point to the **same object**:
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)   # [1, 2, 3, 4] — 'a' sees the change because both point to the SAME list object
```
This is fundamentally different from "copying a value into a box," which is how many beginners mistakenly imagine variables.

## 1.2 Theory: Namespaces and Scope (Foundational Preview)
A **namespace** is a container that maps names to objects. Python maintains different namespaces:
- **Local namespace** — inside a function
- **Global namespace** — at the module level
- **Built-in namespace** — pre-defined names like `print`, `len`

This is why the same variable name can exist independently inside a function without affecting the global one (covered in detail later under functions/scope).

## 1.3 Theory: Rules and Conventions for Naming Variables

**Syntax rules (enforced by the interpreter):**
- Must begin with a letter (a–z, A–Z) or underscore `_`
- Subsequent characters can be letters, digits, or underscores
- Cannot be a reserved keyword (`if`, `else`, `class`, `def`, etc.)
- Case-sensitive (`Total` ≠ `total`)

**Conventions (PEP8 — not enforced, but expected in professional code):**
- `snake_case` for variables and functions
- `UPPER_CASE` for constants (Python has no true constants — this is a convention signaling "don't reassign this")
- Leading underscore `_var` signals "internal use"
- Double leading underscore `__var` triggers **name mangling** inside classes

```python
total_amount = 1000      # good convention
MAX_LIMIT = 500           # convention for a constant
_temp = "internal"        # convention: internal use
```

## 1.4 Theory: Dynamic Typing vs Static Typing

| Aspect | Static Typing (Java, C++) | Dynamic Typing (Python) |
|--------|----------------------------|---------------------------|
| Type declared | At compile time | Inferred at runtime |
| Type checked | Before execution | During execution |
| Flexibility | Lower | Higher |
| Errors caught | Earlier (compile time) | Later (runtime) |
| Reassignment to different type | Not allowed | Allowed |

```python
x = 10          # x refers to an int object
x = "hello"     # now x refers to a str object — perfectly legal in Python
```

**Theoretical trade-off:** Dynamic typing increases development speed and flexibility but shifts type-related bug discovery to runtime — this is exactly why **type hints** (`x: int = 10`) were later introduced in Python 3.5+, to get some static-analysis benefits without losing dynamic flexibility.

## 1.5 Theory: Mutability and Variable Behavior
This is explained fully in Chapter 3 (Data Types), but the key theoretical point for variables is:

> A variable does not "own" mutability — the **object** it points to does. Reassigning a variable rebinds it to a new object; mutating an object affects every reference to it.

```python
x = 5
y = x
x = x + 1     # creates a NEW int object; x now points elsewhere; y unaffected
print(x, y)   # 6 5
```

## 1.6 Multiple Assignment & Unpacking — Theory + Examples
Python supports **tuple packing and unpacking** at the assignment level — multiple values on the right are implicitly packed into a tuple, then unpacked into names on the left.

```python
a, b, c = 1, 2, 3     # 1,2,3 packed into a tuple (1,2,3), then unpacked

# Extended unpacking (PEP 3132) using *
first, *rest = [1, 2, 3, 4]
print(rest)    # [2, 3, 4]
```

## 1.7 The Walrus Operator `:=` (PEP 572, Python 3.8+)
**Theory:** Normally, assignment is a *statement* (produces no value). The walrus operator makes assignment an *expression* (produces a value), allowing assignment inside conditions/comprehensions.

```python
data = [1, 2, 3, 4, 5]
# Without walrus
results = []
for x in data:
    y = x * 2
    if y > 5:
        results.append(y)

# With walrus (more concise)
results = [y for x in data if (y := x * 2) > 5]
```

## 1.8 Use Case in Data Engineering
- Config variables (`batch_size`, `source_path`, `retry_limit`) driving pipeline behavior
- Understanding mutability prevents subtle bugs when passing record batches (lists/dicts) between transformation functions
- The walrus operator is handy for streaming reads: `while (chunk := file.read(SIZE)):`

---

# CHAPTER 2: COMMENTS

## 2.1 Theory: Purpose of Comments
**Definition:** A comment is a piece of text in source code that the interpreter ignores during execution. Its only purpose is to communicate information to human readers — about *intent*, *reasoning*, or *usage* — that the code itself cannot fully express.

**Why comments matter (theory):**
- Code expresses **how** something is done; comments often need to explain **why**.
- Codebases are read far more often than they are written — comments reduce the cost of future maintenance.
- In collaborative/data engineering environments, comments document assumptions about data (e.g., "assuming UTC timestamps from source API").

## 2.2 Types of Comments — Theory & Syntax

### a) Single-line comments
Begin with `#`; everything after it on that line is ignored.
```python
# Connects to the production database
conn = connect_db()
```

### b) Inline comments
Placed after a code statement, separated by at least two spaces (PEP8 convention).
```python
retry_count = 3  # max retries before failing the job
```

### c) Multi-line / block "comments"
Python has no true multi-line comment syntax. Triple-quoted strings (`'''...'''` or `"""..."""`) are technically string literals, but when not assigned to anything, they have no effect and are commonly (mis)used as block comments.
```python
"""
This block performs the following:
1. Extract data from source
2. Validate schema
3. Load into warehouse
"""
```

### d) Docstrings (PEP 257) — formal documentation comments
**Theory:** A docstring is the *first statement* inside a module, function, class, or method, written as a string literal. Unlike a regular comment, it is stored as an attribute (`__doc__`) and can be retrieved programmatically — making it part of the program's introspectable structure, not just a discarded comment.

```python
def extract(source: str) -> list:
    """Extract raw records from the given data source.

    Args:
        source (str): Path or URI of the data source.

    Returns:
        list: A list of raw record dictionaries.
    """
    pass

print(extract.__doc__)   # prints the docstring text
help(extract)             # formatted help output
```

## 2.3 Theory: Good Commenting Practices
- Explain **why**, not **what** (the code already shows *what*)
- Keep comments synchronized with code changes — a wrong comment is worse than no comment
- Use tags like `# TODO:`, `# FIXME:`, `# NOTE:`, `# HACK:` to flag follow-up work — many IDEs index these automatically

```python
# TODO: Replace with batch API call once rate limits are increased
for record in records:
    api.send(record)
```

## 2.4 Use Case in Data Engineering
- Documenting business logic behind transformation rules (e.g., "subtracting 1 day because source system reports in UTC+1 but warehouse uses UTC")
- Docstrings power auto-generated documentation tools (Sphinx) used in data platform documentation
- Comments flagging data quality assumptions prevent future engineers from silently breaking pipeline logic

---

# CHAPTER 3: DATA TYPES

## 3.1 Theory: What Is a Data Type?
**Definition:** A data type defines the kind of value a variable's underlying object holds, and — crucially — what **operations** are valid on it and how much **memory** it occupies conceptually.

In Python, every object has three core attributes:
1. **Identity** — a unique id (memory address), retrieved via `id()`
2. **Type** — fixed at creation, retrieved via `type()`, determines valid operations
3. **Value** — the actual data the object represents

### Classification of Python Data Types

```
Python Data Types
│
├── Numeric Types ── int, float, complex
├── Sequence Types ── str, list, tuple, range
├── Mapping Type ── dict
├── Set Types ── set, frozenset
├── Boolean Type ── bool
├── Binary Types ── bytes, bytearray, memoryview
└── None Type ── NoneType
```

### Mutable vs Immutable — Core Theory
**Definition:**
- **Immutable** objects cannot be changed after creation. Any "modification" actually creates a brand-new object.
- **Mutable** objects can be changed in place — their identity (`id()`) stays the same even after modification.

```python
s = "hello"
print(id(s))
s += " world"
print(id(s))    # different id — a NEW string object was created

lst = [1, 2]
print(id(lst))
lst.append(3)
print(id(lst))   # SAME id — modified in place
```

**Theoretical implication — Hashability:** Only immutable objects can be hashed (have a fixed hash value for their lifetime), and only hashable objects can be used as dictionary keys or set members. This is why lists cannot be dict keys, but tuples can.

```python
d = {(1,2): "valid"}     # tuple is hashable
d = {[1,2]: "invalid"}    # ❌ TypeError: unhashable type: 'list'
```

## 3.2 Numeric Types — Theory & Examples

### `int` — Theory
Python's `int` has **arbitrary precision** — meaning it can represent integers of any size limited only by available memory (unlike fixed-width integers in C/Java which overflow at a maximum value). Internally, CPython represents large integers using an array of "digits" in a chosen base, growing dynamically.

```python
big = 99999999999999999999999999999
print(big * big)    # computes correctly, no overflow

print(0b1010)   # binary literal → 10
print(0o12)      # octal literal → 10
print(0xA)        # hex literal → 10
```

### `float` — Theory
Floats are implemented using the **IEEE 754 double-precision** standard (64-bit). This representation cannot exactly represent every decimal fraction in binary, which is the root cause of floating-point precision errors.

```python
print(0.1 + 0.2)         # 0.30000000000000004 — binary representation limitation
print(0.1 + 0.2 == 0.3)   # False!
```
**Theoretical fix:** Use the `decimal` module (exact base-10 arithmetic, slower) for money/financial values, or round when comparing floats.
```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))   # 0.3 exactly
```

### `complex` — Theory
Represents numbers with a real and imaginary part (`a + bj`), used in scientific/engineering computation; rarely relevant in typical data engineering work.
```python
z = 2 + 3j
print(z.real, z.imag, abs(z))   # 2.0 3.0 3.605551275463989
```

## 3.3 `str` (String) — Theory & Examples

**Theory:** A string is an **immutable ordered sequence of Unicode code points**. Because it's a sequence, it supports indexing, slicing, and iteration — but because it's immutable, every "modification" method (`.upper()`, `.replace()`, etc.) returns a *new* string rather than altering the original.

```python
s = "Engineering"
print(s[0], s[-1])      # E g
print(s[2:6])             # gine
print(s[::-1])            # gnireenignE (reverse via slicing)

new_s = s.replace("E", "e")
print(s, new_s)           # original unchanged; new_s is a different object
```

**Encoding theory:** Internally, Python 3 strings are sequences of Unicode code points; to store/transmit them as raw bytes (files, network), they must be **encoded** (str → bytes) using a scheme like UTF-8, and **decoded** (bytes → str) on the way back.
```python
encoded = "café".encode("utf-8")     # b'caf\xc3\xa9'
decoded = encoded.decode("utf-8")     # 'café'
```

## 3.4 `list` — Theory & Examples
**Theory:** A list is a **mutable, ordered, dynamically-resizable sequence**. Internally, CPython implements lists as an array of pointers to objects (not a linked list), giving O(1) index access but O(n) insertion/deletion at arbitrary positions (O(1) amortized at the end).

```python
nums = [10, 20, 30]
nums.append(40)        # O(1) amortized
nums.insert(0, 5)       # O(n) — shifts all elements
nums.pop()               # O(1) — removes from end

# List comprehension — theory: a concise, often faster alternative to explicit loops
# because the looping happens in optimized C code internally
squares = [x**2 for x in range(10)]
```

## 3.5 `tuple` — Theory & Examples
**Theory:** A tuple is an **immutable ordered sequence**. Its immutability gives two theoretical advantages: (1) it can be used as a dictionary key/set element (hashable, if all its elements are hashable), and (2) it signals to readers/future maintainers that the contained data should not change — useful for representing fixed records or schemas.

```python
schema = ("id", "name", "salary")     # represents a fixed structure
point = (10, 20)

# Single-element tuple needs a trailing comma
not_a_tuple = (5)      # this is just int 5
a_tuple = (5,)          # this is a tuple
```

## 3.6 `dict` — Theory & Examples
**Theory:** A dictionary is a **mutable mapping of unique, hashable keys to values**, implemented internally as a hash table. This gives average O(1) lookup, insertion, and deletion — far faster than searching a list. Since Python 3.7, dictionaries also guarantee **insertion order** is preserved (an implementation detail formalized into the language spec).

```python
employee = {"id": 1, "name": "Alice"}
print(employee["name"])          # direct access — O(1) average
print(employee.get("salary"))     # safe access, returns None if missing

# Dict comprehension
squares = {x: x**2 for x in range(5)}
```

## 3.7 `set` / `frozenset` — Theory & Examples
**Theory:** A set is a **mutable, unordered collection of unique hashable elements**, also backed by a hash table — giving average O(1) membership testing (`in`), far faster than checking membership in a list (O(n)). `frozenset` is its immutable counterpart.

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a | b)    # union: {1,2,3,4}
print(a & b)    # intersection: {2,3}
print(a - b)    # difference: {1}
print(a ^ b)    # symmetric difference: {1,4}
```
**Theoretical use case:** Set operations map directly onto relational concepts — union, intersection, and difference mirror SQL's `UNION`, `INNER JOIN` (on key matching), and `EXCEPT`/`NOT IN` operations, which is why sets are so useful for reconciling datasets.

## 3.8 `bool` — Theory & Examples
**Theory:** `bool` is technically a subclass of `int` in Python (`True == 1`, `False == 0`), with only two instances: `True` and `False`. Every object in Python has an associated **truthiness** — used implicitly in conditions — determined by its `__bool__()` method (or, if absent, by `__len__()` returning 0).

```python
print(isinstance(True, int))   # True — bool is a subclass of int
print(True + True)              # 2

# Falsy objects: 0, 0.0, "", [], {}, (), set(), None, False
if []:
    print("won't print — empty list is falsy")
```

## 3.9 `NoneType` — Theory & Examples
**Theory:** `None` is the sole instance of `NoneType` — a **singleton** representing "absence of value." Because there is exactly one `None` object for the entire program's lifetime, identity comparison (`is`) is the theoretically correct and idiomatic way to check for it (faster and semantically clearer than `==`).

```python
result = None
if result is None:      # correct
    print("No result yet")
```

## 3.10 Binary Types — Theory & Examples
**Theory:** `bytes` is an immutable sequence of integers (0–255) representing raw binary data; `bytearray` is its mutable counterpart; `memoryview` allows access to an object's internal buffer without copying it — important for performance with large binary datasets.

```python
raw = b"\x48\x65\x6c\x6c\x6f"
print(raw.decode())     # "Hello"

mv = memoryview(bytearray(b"hello"))
print(mv[0])              # 104 (byte value, not copied)
```

## 3.11 Checking and Comparing Types — Theory
```python
x = 10
print(type(x) == int)        # works, but not best practice
print(isinstance(x, int))     # preferred — also respects inheritance (subclasses)
```
**Theory:** `isinstance()` is preferred over `type() ==` because it correctly handles subclassing — a subclass instance should still be considered "of that type" for most practical purposes (polymorphism).

---

# CHAPTER 4: TYPECASTING (TYPE CONVERSION)

## 4.1 Theory: What Is Type Conversion and Why Is It Needed?
**Definition:** Type conversion (typecasting) is the process of converting an object of one data type into an equivalent object of another data type. It is necessary because operations in Python are type-sensitive — many operators and functions only work correctly (or at all) on specific types, and real-world data (especially from files, APIs, and user input) often arrives in the *wrong* type for the operation you need to perform (most commonly: everything arrives as a string).

## 4.2 Implicit Type Conversion (Type Coercion) — Theory
**Definition:** Implicit conversion happens automatically, performed internally by the Python interpreter, when it is "safe" — i.e., when no data/precision is lost in the *widening* direction.

**Theoretical hierarchy (widening conversion only):**
```
bool  →  int  →  float  →  complex
```
Python will automatically widen a "smaller" type to a "larger" one when mixed in an expression, but will **never** narrow automatically (e.g., float → int is never implicit, because it could lose data).

```python
print(True + 1)         # 2          (bool widened to int)
print(1 + 2.0)            # 3.0        (int widened to float)
print(1 + 2.0 + 3j)        # (4+3j)     (float widened to complex)
```

## 4.3 Explicit Type Conversion — Theory
**Definition:** Explicit conversion is performed deliberately by the programmer, using built-in constructor functions (`int()`, `float()`, `str()`, etc.), because the conversion is *not* automatically safe or obvious — it may lose information (narrowing) or require interpreting data in a specific way (e.g., parsing a string as a number).

```python
age_str = "25"
age = int(age_str)         # explicit: string → int

price = 19.999
rounded_price = int(price)  # explicit narrowing: 19 (truncates, doesn't round!)
```

### Complete List of Explicit Conversion Functions

| Function | Theory of Operation | Example |
|----------|----------------------|---------|
| `int(x)` | Parses string as base-10 integer, or truncates float toward zero | `int("42")`→`42`, `int(9.9)`→`9` |
| `float(x)` | Parses string/int as IEEE-754 float | `float("3.14")`→`3.14` |
| `str(x)` | Calls the object's `__str__()` to get a human-readable representation | `str(42)`→`"42"` |
| `bool(x)` | Evaluates truthiness rules | `bool(0)`→`False` |
| `list(x)` | Iterates over `x` and collects elements into a list | `list("ab")`→`['a','b']` |
| `tuple(x)` | Iterates over `x` and collects elements into a tuple | `tuple([1,2])`→`(1,2)` |
| `set(x)` | Iterates over `x`, discarding duplicates, into a set | `set([1,1,2])`→`{1,2}` |
| `dict(x)` | Converts a sequence of key-value pairs into a dict | `dict([(1,'a')])`→`{1:'a'}` |
| `chr(x)` | Converts a Unicode code point (int) to its character | `chr(65)`→`'A'` |
| `ord(x)` | Converts a character to its Unicode code point | `ord('A')`→`65` |
| `bin/oct/hex(x)` | Converts int to its string representation in another base | `hex(255)`→`'0xff'` |

## 4.4 Theoretical Pitfalls of Type Conversion

### a) Truncation vs Rounding
`int()` does not round — it **truncates toward zero**, which is a common source of off-by-one errors in data aggregation.
```python
print(int(9.99))     # 9   (truncated, not rounded to 10)
print(round(9.99))    # 10  (correctly rounded)
```

### b) Truthiness Is Not the Same as "Looks False"
A non-empty string is *always* truthy, even if its content reads as "False":
```python
print(bool("False"))    # True! The string is non-empty.
```
**Theoretical reasoning:** `bool()` on a string checks only `len(string) > 0` — it does not parse the *content* of the string. To convert a textual flag correctly, you must explicitly compare it:
```python
is_active = (raw_value.strip().lower() == "true")
```

### c) Direct String-to-Int Conversion Fails for Decimal Strings
```python
int("3.5")              # ValueError — int() expects a valid integer literal string
int(float("3.5"))        # 3 — must go through float first
```

### d) `eval()` vs `ast.literal_eval()` — Security Theory
`eval()` executes the string as arbitrary Python code — a serious security risk if the string comes from an untrusted source (e.g., a file, API, or user input), since it could execute malicious code. `ast.literal_eval()` only parses *literal* Python data structures (numbers, strings, tuples, lists, dicts, booleans, None) — much safer for converting structured string data.
```python
import ast
safe_dict = ast.literal_eval("{'a': 1, 'b': 2}")   # safe
```

## 4.5 Theory: Type Conversion in Real-World Data Pipelines
Source systems (CSVs, REST APIs, legacy databases) frequently send all values as text, regardless of their logical type. A data engineer's responsibility includes **schema enforcement** — explicitly converting and validating each field's type before it moves further down the pipeline, catching bad data early rather than letting it silently corrupt downstream tables.

```python
def parse_row(row: dict) -> dict:
    try:
        return {
            "id": int(row["id"]),
            "salary": float(row["salary"]),
            "is_active": row["is_active"].strip().lower() == "true",
        }
    except (ValueError, KeyError) as e:
        # log and route to a dead-letter/error table instead of crashing the whole job
        log_error(row, e)
        return None
```

---

# CHAPTER 5: OPERATORS

## 5.1 Theory: What Is an Operator?
**Definition:** An operator is a special symbol that performs a specific operation on one or more **operands** (values/variables) and produces a result. Operators are essentially shorthand syntax for calling underlying special (dunder) methods on objects — e.g., `a + b` is syntactic sugar for `a.__add__(b)`.

```python
class Money:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Money(self.amount + other.amount)

m1, m2 = Money(100), Money(50)
m3 = m1 + m2     # internally calls m1.__add__(m2)
print(m3.amount)  # 150
```
This theoretical fact (operator overloading) explains why the same `+` symbol can mean numeric addition, string/list concatenation, or a custom-defined behavior, depending on the operand's type.

```python
print(5 + 3)          # 8        — numeric addition
print("a" + "b")        # "ab"     — string concatenation
print([1] + [2])         # [1, 2]   — list concatenation
```

## 5.2 Classification of Operators (Theory Overview)

| Category | Purpose |
|----------|---------|
| Arithmetic | Mathematical computation |
| Comparison/Relational | Compare two values, return a boolean |
| Logical | Combine boolean expressions |
| Assignment | Bind/update a variable's reference |
| Bitwise | Operate on the binary representation of integers |
| Membership | Test if a value exists within a collection |
| Identity | Test if two references point to the same object |

## 5.3 Arithmetic Operators — Theory & Examples
```python
a, b = 10, 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333... — true division, ALWAYS returns float
print(a // b)   # 3          — floor division, rounds toward negative infinity
print(a % b)    # 1          — modulus, sign follows the divisor
print(a ** b)   # 1000       — exponentiation

# Theory: floor division rounds toward -infinity, not toward zero
print(-7 // 2)   # -4  (not -3!)
print(-7 % 2)     # 1   (modulus result follows divisor's sign)
```
**Use case:** Floor division and modulus are foundational for pagination logic (`page = offset // page_size`) and partitioning logic in distributed data systems (`partition = hash(key) % num_partitions`).

## 5.4 Comparison Operators — Theory & Examples
**Theory:** These operators compare the *value* of operands and always return a `bool`. For custom objects, comparison behavior is defined by dunder methods (`__eq__`, `__lt__`, etc.) — meaning comparison is not "built-in magic," but a customizable protocol.
```python
print(5 == 5.0)   # True — value equality across types is allowed
print(5 is 5.0)    # False — different types/objects, identity differs
```

## 5.5 Logical Operators — Theory & Examples
**Theory:** `and`/`or` in Python are **short-circuit operators** — they don't necessarily return a `bool`; they return one of the *actual operands*, based on truthiness evaluation, stopping as soon as the result is determined.
```python
print(0 and 5)      # 0   (first operand is falsy, returned as-is)
print(3 and 5)      # 5   (first is truthy, so second is evaluated and returned)
print(0 or 5)        # 5   (first falsy, falls through to second)
print(3 or 5)         # 3   (first truthy, short-circuits, second never evaluated)
```
**Use case:** This enables a common idiom for default values: `name = user_input or "default_value"`.

## 5.6 Assignment & Augmented Assignment — Theory & Examples
**Theory:** Augmented assignment (`+=`, `-=`, etc.) is not purely syntactic sugar for mutable types — for objects implementing `__iadd__`, it performs an **in-place** operation (mutates the existing object) rather than creating a new one, which can be more memory-efficient for large mutable collections.
```python
lst = [1, 2, 3]
original_id = id(lst)
lst += [4]              # in-place extend via __iadd__
print(id(lst) == original_id)   # True — same object, modified in place

x = 5
original_id = id(x)
x += 1                   # int is immutable — a NEW object is created
print(id(x) == original_id)     # False
```

## 5.7 Bitwise Operators — Theory & Examples
**Theory:** Bitwise operators treat integers as sequences of binary bits and operate at that level — useful for low-level flag manipulation, performance-critical computation, and hashing/partitioning schemes.
```python
a, b = 6, 3      # binary: 0110, 0011
print(a & b)      # 0010 -> 2   AND: 1 only if both bits are 1
print(a | b)      # 0111 -> 7   OR:  1 if either bit is 1
print(a ^ b)      # 0101 -> 5   XOR: 1 if bits differ
print(~a)          # -7         NOT: inverts all bits (two's complement: ~x = -x-1)
print(a << 1)      # 12         left shift = multiply by 2^n
print(a >> 1)      # 3          right shift = integer-divide by 2^n
```

## 5.8 Membership Operators — Theory & Examples
**Theory:** `in`/`not in` test whether a value exists within an iterable, internally calling the container's `__contains__()` method. Its performance depends entirely on the container type: O(n) for lists/tuples, O(1) average for sets/dicts (hash-based lookup).
```python
ids_list = [1, 2, 3, 4, 5]          # O(n) lookup
ids_set = {1, 2, 3, 4, 5}            # O(1) average lookup
print(3 in ids_list)                  # True (scans list)
print(3 in ids_set)                    # True (hash lookup)
```
**Use case:** When checking membership repeatedly against a large reference list (e.g., a blocklist of IDs), converting it to a `set` first is a significant performance optimization in data pipelines.

## 5.9 Identity Operators — Theory & Examples
**Theory:** `is`/`is not` check whether two references point to the exact same object in memory (`id(a) == id(b)`), as opposed to `==`, which checks value equality (potentially via custom `__eq__` logic). CPython optimizes memory by caching small integers (-5 to 256) and certain strings (interning), which can make `is` *appear* to work for equality on small values — but this is an implementation detail, not a guarantee, and should never be relied upon.
```python
a = 256
b = 256
print(a is b)     # True — small int caching (implementation detail)

a = 1000
b = 1000
print(a is b)      # False (typically) — outside the cached range
```

## 5.10 Operator Precedence and Associativity — Theory
**Theory:** When an expression contains multiple operators, **precedence** determines which operator is evaluated first, and **associativity** determines the order when operators of equal precedence appear together (most are left-to-right; exponentiation `**` is right-to-left).
```python
print(2 ** 3 ** 2)     # 512, not 64 — ** is right-associative: 2 ** (3 ** 2)
print(10 - 2 - 3)        # 5 — left-associative: (10 - 2) - 3
```

---

# CHAPTER 6: INPUT / OUTPUT

## 6.1 Theory: Streams — The Foundation of I/O
**Definition:** Python (like most languages) models input and output as **streams** — sequences of data flowing into or out of a program. Three standard streams exist by default in every program:

| Stream | Purpose | Python Access |
|--------|---------|-----------------|
| `stdin` | Standard input (keyboard or piped data) | `sys.stdin` |
| `stdout` | Standard output (normal program output) | `sys.stdout` (used internally by `print()`) |
| `stderr` | Standard error (error/diagnostic messages) | `sys.stderr` |

This is why `print()` and `input()` are really just convenient, high-level wrappers around lower-level stream operations.

## 6.2 `input()` — Theory & Examples
**Theory:** `input()` reads one line of text from `stdin`, strips the trailing newline, and **always** returns the result as a `str` — regardless of what was typed — because the interpreter has no way of inferring intended type from raw keyboard text without an explicit conversion step.
```python
value = input("Enter your age: ")
print(type(value))           # <class 'str'> always

age = int(input("Enter your age: "))   # explicit conversion required for numeric use
```

## 6.3 `print()` — Theory & Examples
**Theory:** `print()` is a function that converts its arguments to strings (via their `__str__()` method), joins them with a separator (`sep`, default `" "`), and writes the result followed by a terminator (`end`, default `"\n"`) to a target stream (`file`, default `sys.stdout`).
```python
print("a", "b", "c", sep="-", end="!\n")    # a-b-c!
print("Visible immediately", flush=True)     # bypasses internal output buffering
```
**Theory of buffering:** By default, output may be held in a memory buffer before being physically written (for performance) — `flush=True` forces immediate writing, important for real-time logging in long-running pipeline scripts where you need to see progress as it happens, not after the buffer fills.

## 6.4 String Formatting — Theory
**Theory:** Python's format mini-language (used inside f-strings, `.format()`, and `%`) follows the general structure:
```
{value:[fill][align][sign][width][,][.precision][type]}
```
Understanding this structure lets you construct nearly any output format from a single specifier.
```python
value = 1234567.891
print(f"{value:>15,.2f}")    # right-aligned, width 15, thousands separator, 2 decimals
# Output: "   1,234,567.89"
```

| Symbol | Meaning |
|--------|---------|
| `<`, `>`, `^` | left, right, center alignment |
| `+` | force display of sign |
| `,` | thousands separator |
| `.Nf` | N decimal places (fixed-point) |
| `%` | percentage (multiplies by 100, appends %) |
| `d`, `x`, `o`, `b` | integer base formats: decimal, hex, octal, binary |

## 6.5 File I/O — Theory
**Theory:** Reading/writing files is conceptually identical to console I/O — both are stream operations — except the stream is connected to a file on disk instead of the terminal. `open()` returns a **file object** which acts as an iterable stream; using it as a context manager (`with`) guarantees the underlying OS file handle is released (closed) even if an exception occurs mid-operation — a critical resource-management guarantee.

| Mode | Meaning |
|------|---------|
| `"r"` | Read (default; error if file doesn't exist) |
| `"w"` | Write (creates file; **overwrites** if it exists) |
| `"a"` | Append (creates file if missing; adds to the end) |
| `"x"` | Exclusive creation (error if file already exists) |
| `"b"` | Binary mode (e.g., `"rb"`, `"wb"`) — for non-text data |
| `"+"` | Read and write |

```python
with open("data.csv", "r") as f:
    for line in f:               # streams line by line — memory-efficient for huge files
        process(line.strip())

with open("output.log", "a") as f:
    f.write("Job completed\n")
```

**Theory — why iterate line-by-line instead of `.read()`:** `.read()` loads the *entire* file into memory at once; iterating with a `for` loop reads one line at a time from the OS buffer, which is essential when working with files larger than available RAM — a common situation in data engineering.

## 6.6 Use Case Summary (Theoretical Framing)
- I/O is the **boundary** between a program and the outside world — every data pipeline begins and ends at an I/O operation (reading a source, writing a sink).
- Understanding stream theory explains why large file processing must be done incrementally (line-by-line or chunk-by-chunk) rather than loading everything into memory.
- Formatting theory underlies all human-readable logging, monitoring dashboards, and report generation in production systems.
