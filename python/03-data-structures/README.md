# Notes

1. Lists

1.1 Creating a List
1.2 Accessing Elements (Indexing)
1.3 Negative Indexing
1.4 Slicing Lists
1.5 Modifying Lists (Mutability)
1.6 List Methods (append, insert, extend, remove, pop, clear, index, count, sort, reverse, copy)
1.7 Adding Elements
1.8 Removing Elements
1.9 Copying Lists (Shallow vs Deep Copy)
1.10 Nested Lists
1.11 List Comprehension
1.12 Iterating Over Lists
1.13 List Concatenation & Repetition
1.14 Checking Membership (in, not in)
1.15 Sorting Lists (sort() vs sorted())
1.16 List Unpacking

A list is a python data structure that stores multiple values inside a single variable 
st_name1=50
st_name2=90

marks=[95,87.90,78]
fruits=["apple",banana","garphs"]
employee=[
    101,
    "Ravi",
    85000.0,
    True,
    [10,20]
]


Why use Lists?
Lists are used when you have a collection of related data. Instead of creating ⁠student1⁠, ⁠student2⁠, ⁠student3⁠, you simply create a list named ⁠students⁠. This makes your code cleaner, easier to iterate over, and highly scalable.


Syntax
You define a list by placing comma-separated values inside square brackets ⁠[]⁠.

# A simple list of integers
numbers = [10, 20, 30, 40]

# A list with mixed data types
mixed_list = [1, "Hello", 3.14, True]

# An empty list
empty_list = []

# 1.2 Accessing Elements (Indexing)

Indexing means accessing one specific element from list by using its position. 

-- list_name[index]

- Why indesing is required?

    - employee_data =["Rahul",32,"DE",85000]
    - print(employee_data[1]) # 32 
    - print(employee_data[2]) # DE 

    Index can help us:
    - Read an element 
    - Modify an element 
    - Delete 
    - Compare 
    - 


## 1.1 Creating a List

A list is an **ordered, mutable** collection that can hold items of any data type (even mixed types).

```python
# Empty list
empty = []
empty2 = list()

# List of same type
numbers = [1, 2, 3, 4, 5]

# Mixed data types
mixed = [1, "hello", 3.14, True, None]

# Using list() constructor on an iterable
chars = list("hello")        # ['h', 'e', 'l', 'l', 'o']
from_range = list(range(5))  # [0, 1, 2, 3, 4]

# Nested list
matrix = [[1, 2], [3, 4]]
```

**Key points**
- Lists are defined using square brackets `[ ]`.
- Elements are separated by commas.
- A list can contain duplicate values.
- Lists preserve insertion order.

---

## 1.2 Accessing Elements (Indexing)

Each element has an **index** starting from `0`.

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])   # apple  (first element)
print(fruits[2])   # cherry
print(fruits[3])   # date   (last element)

# Accessing an out-of-range index raises IndexError
# print(fruits[10])  -> IndexError
```

| Index | 0 | 1 | 2 | 3 |
|-------|---|---|---|---|
| Value | apple | banana | cherry | date |

---

## 1.3 Negative Indexing

Negative indices count from the **end** of the list, starting at `-1`.

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[-1])   # date    (last element)
print(fruits[-2])   # cherry
print(fruits[-4])   # apple   (first element)
```

| Index | -4 | -3 | -2 | -1 |
|-------|----|----|----|----|
| Value | apple | banana | cherry | date |

---

## 1.4 Slicing Lists

Slicing extracts a **sub-list** using `list[start:stop:step]`.

- `start` — index to begin (inclusive), default `0`
- `stop` — index to end (exclusive), default `len(list)`
- `step` — jump size, default `1`

```python
nums = [10, 20, 30, 40, 50, 60]

print(nums[1:4])     # [20, 30, 40]
print(nums[:3])      # [10, 20, 30]      (start defaults to 0)
print(nums[3:])      # [40, 50, 60]      (stop defaults to end)
print(nums[:])       # full copy of the list
print(nums[::2])     # [10, 30, 50]      (every 2nd element)
print(nums[::-1])    # [60, 50, 40, 30, 20, 10]  (reversed)
print(nums[-3:])     # [40, 50, 60]      (last 3 elements)
```

**Note:** Slicing never raises an `IndexError`, even if indices go out of bounds — it just returns as much as is available.

---

## 1.5 Modifying Lists (Mutability)

Lists are **mutable** — their contents can be changed after creation without changing their identity (`id()`).

```python
fruits = ["apple", "banana", "cherry"]

# Modify a single element
fruits[1] = "blueberry"
print(fruits)   # ['apple', 'blueberry', 'cherry']

# Modify a slice (replace multiple elements at once)
fruits[0:2] = ["kiwi", "mango"]
print(fruits)   # ['kiwi', 'mango', 'cherry']

# Slice assignment can change the list's length
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30, 40]
print(nums)   # [1, 20, 30, 40, 4, 5]
```

Contrast with **immutable** types like tuples or strings, where such in-place changes are not allowed.

---

## 1.6 List Methods — Overview

Python lists come with many built-in methods. Below is the **complete set**, each explained with syntax, behavior, and examples.

### `append(x)`
Adds a single element `x` to the **end** of the list.
```python
lst = [1, 2, 3]
lst.append(4)
print(lst)   # [1, 2, 3, 4]

lst.append([5, 6])   # adds the whole list as ONE element
print(lst)   # [1, 2, 3, 4, [5, 6]]
```

### `insert(index, x)`
Inserts `x` at the given `index`, shifting subsequent elements right.
```python
lst = [1, 2, 4]
lst.insert(2, 3)
print(lst)   # [1, 2, 3, 4]

lst.insert(0, 0)
print(lst)   # [0, 1, 2, 3, 4]
```

### `extend(iterable)`
Adds each element of an iterable to the end of the list (unpacks it, unlike `append`).
```python
lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)   # [1, 2, 3, 4, 5]

lst.extend("ab")
print(lst)   # [1, 2, 3, 4, 5, 'a', 'b']
```

### `remove(x)`
Removes the **first occurrence** of value `x`. Raises `ValueError` if not found.
```python
list_name.remove(x)
lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)   # [1, 3, 2]
```

### `pop(index=-1)`
Removes and **returns** the element at `index` (default: last element).
```python
lst = [1, 2, 3, 4]
last = lst.pop()
print(last, lst)   # 4  [1, 2, 3]

first = lst.pop(0)
print(first, lst)  # 1  [2, 3]
```

### `clear()`
Removes **all** elements, leaving an empty list.
```python
lst = [1, 2, 3]
lst.clear()
print(lst)   # []
```

### `index(x, start=0, end=len)`
Returns the index of the **first occurrence** of `x`. Raises `ValueError` if not found.
```python
lst = [10, 20, 30, 20]
print(lst.index(20))       # 1
print(lst.index(20, 2))    # 3  (search starts from index 2)
```

### `count(x)`
Returns the number of times `x` appears in the list.
```python
lst = [1, 2, 2, 3, 2]
print(lst.count(2))   # 3
```

### `sort(key=None, reverse=False)`
Sorts the list **in place** (modifies original, returns `None`).
```python
lst = [3, 1, 4, 1, 5]
lst.sort()
print(lst)   # [1, 1, 3, 4, 5]

lst.sort(reverse=True)
print(lst)   # [5, 4, 3, 1, 1]

words = ["banana", "kiwi", "apple"]
words.sort(key=len)
print(words)   # ['kiwi', 'apple', 'banana']
```

### `reverse()`
Reverses the list **in place**.
```python
lst = [1, 2, 3]
lst.reverse()
print(lst)   # [3, 2, 1]
```

### `copy()`
Returns a **shallow copy** of the list.
```python
lst = [1, 2, 3]
new_lst = lst.copy()
new_lst.append(4)
print(lst, new_lst)   # [1, 2, 3]  [1, 2, 3, 4]
```

Adding elements

append(x) — Adds a single item x to the end of the list.
extend(iterable) — Adds all items from an iterable to the end of the list.
insert(i, x) — Inserts item x at index i.

Removing elements

remove(x) — Removes the first item whose value equals x. Raises ValueError if not found.
pop([i]) — Removes and returns the item at index i (default: last item).
clear() — Removes all items from the list.

Searching / counting

index(x[, start[, end]]) — Returns the index of the first item equal to x. Raises ValueError if not found.
count(x) — Returns the number of times x appears in the list.

Ordering

sort(key=None, reverse=False) — Sorts the list in place.
reverse() — Reverses the list in place.

Copying

copy() — Returns a shallow copy of the list (equivalent to list[:]).


### Quick Reference Table

| Method | Purpose | Modifies in place? | Returns |
|--------|---------|--------------------|---------|
| `append(x)` | Add one item to end | Yes | `None` |
| `insert(i, x)` | Add item at index `i` | Yes | `None` |
| `extend(iter)` | Add all items from iterable | Yes | `None` |
| `remove(x)` | Delete first matching value | Yes | `None` |
| `pop(i)` | Delete & return item at index | Yes | item |
| `clear()` | Delete all items | Yes | `None` |
| `index(x)` | Find index of first match | No | int |
| `count(x)` | Count occurrences | No | int |
| `sort()` | Sort ascending (or by key) | Yes | `None` |
| `reverse()` | Reverse order | Yes | `None` |
| `copy()` | Shallow copy | No | new list |

---

## 1.7 Adding Elements

Ways to add elements to a list:

```python
lst = [1, 2, 3]

lst.append(4)          # add single item at end -> [1, 2, 3, 4]
lst.insert(0, 0)        # add at specific position -> [0, 1, 2, 3, 4]
lst.extend([5, 6])      # add multiple items at end -> [0, 1, 2, 3, 4, 5, 6]
lst += [7]              # + operator (creates a new combined list) -> [..., 7]
lst[len(lst):] = [8]    # slice assignment at end -> [..., 8]
```

---

## 1.8 Removing Elements

Ways to remove elements from a list:

```python
lst = [10, 20, 30, 40, 50]

lst.remove(30)      # removes value 30       -> [10, 20, 40, 50]
lst.pop()            # removes & returns last  -> [10, 20, 40]
lst.pop(0)            # removes & returns index 0 -> [20, 40]
del lst[0]            # delete by index (no return value)
lst.clear()           # remove everything -> []

# del can also remove a slice
nums = [1, 2, 3, 4, 5]
del nums[1:3]
print(nums)   # [1, 4, 5]
```

**Comparison of removal tools**

| Tool | Removes by | Returns value? | Raises error if missing/invalid |
|---|---|---|---|
| `remove(x)` | value | No | `ValueError` |
| `pop(i)` | index | Yes | `IndexError` |
| `del lst[i]` | index | No | `IndexError` |
| `clear()` | everything | No | — |

---

## 1.9 Copying Lists (Shallow vs Deep Copy)

**Assignment (`=`) does NOT copy** — it just creates another reference to the same list.

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)   # [1, 2, 3, 4]  <- a changed too!
```

### Shallow Copy
Creates a new outer list, but nested (mutable) objects inside are still shared references.

```python
import copy

original = [1, 2, [3, 4]]

shallow1 = original.copy()
shallow2 = list(original)
shallow3 = original[:]
shallow4 = copy.copy(original)

shallow1[0] = 100          # top-level change: doesn't affect original
shallow1[2].append(5)      # nested change: DOES affect original!

print(original)  # [1, 2, [3, 4, 5]]
print(shallow1)  # [100, 2, [3, 4, 5]]
```

### Deep Copy
Recursively copies **everything**, including nested objects, so no shared references remain.

```python
import copy

original = [1, 2, [3, 4]]
deep = copy.deepcopy(original)

deep[2].append(5)
print(original)  # [1, 2, [3, 4]]      <- unaffected
print(deep)       # [1, 2, [3, 4, 5]]
```

| Copy type | Top-level independent? | Nested objects independent? |
|---|---|---|
| `=` (reference) | No | No |
| Shallow copy | Yes | No |
| Deep copy | Yes | Yes |

---

## 1.10 Nested Lists

A list can contain other lists — useful for matrices, tables, and grouped data.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])       # [1, 2, 3]        (first row)
print(matrix[1][2])    # 6                (row 1, column 2)

# Modifying a nested element
matrix[0][0] = 100
print(matrix)   # [[100, 2, 3], [4, 5, 6], [7, 8, 9]]

# Iterating through a nested list
for row in matrix:
    for item in row:
        print(item, end=" ")
```

⚠️ **Common pitfall:** `[[0]*3]*3` creates 3 references to the *same* inner list.
```python
wrong = [[0]*3]*3
wrong[0][0] = 1
print(wrong)   # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  <- all rows changed!

# Correct way:
correct = [[0]*3 for _ in range(3)]
correct[0][0] = 1
print(correct)   # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 1.11 List Comprehension

A concise way to build lists in a single line.

**Syntax:** `[expression for item in iterable if condition]`

```python
# Basic
squares = [x**2 for x in range(6)]
print(squares)   # [0, 1, 4, 9, 16, 25]

# With condition (filter)
evens = [x for x in range(10) if x % 2 == 0]
print(evens)   # [0, 2, 4, 6, 8]

# With if-else (expression-level)
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labels)   # ['even', 'odd', 'even', 'odd', 'even']

# Nested loops
pairs = [(x, y) for x in range(2) for y in range(2)]
print(pairs)   # [(0, 0), (0, 1), (1, 0), (1, 1)]

# Flattening a nested list
matrix = [[1, 2], [3, 4]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4]

# String manipulation
words = ["hello", "world"]
upper = [w.upper() for w in words]
print(upper)   # ['HELLO', 'WORLD']
```

---

## 1.12 Iterating Over Lists

```python
fruits = ["apple", "banana", "cherry"]

# Basic for loop
for fruit in fruits:
    print(fruit)

# With index using enumerate()
for i, fruit in enumerate(fruits):
    print(i, fruit)
# 0 apple
# 1 banana
# 2 cherry

# enumerate() with custom start
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# Using range() and len()
for i in range(len(fruits)):
    print(fruits[i])

# while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Iterating two lists together with zip()
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
```

---

## 1.13 List Concatenation & Repetition

### Concatenation (`+`)
Combines two lists into a **new** list.
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)   # [1, 2, 3, 4, 5, 6]

# += extends the list in place
a += b
print(a)   # [1, 2, 3, 4, 5, 6]
```

### Repetition (`*`)
Repeats the list's elements a given number of times.
```python
lst = [1, 2] * 3
print(lst)   # [1, 2, 1, 2, 1, 2]

zeros = [0] * 5
print(zeros)   # [0, 0, 0, 0, 0]
```

⚠️ Repetition with nested mutable objects creates shared references (same pitfall as 1.10).

---

## 1.14 Checking Membership (`in`, `not in`)

```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)        # True
print("mango" in fruits)        # False
print("mango" not in fruits)    # True

# Common usage inside conditionals
if "banana" in fruits:
    print("Found banana!")

# Membership check inside a comprehension
nums = [1, 2, 3, 4, 5]
present = [x for x in [2, 6, 3] if x in nums]
print(present)   # [2, 3]
```

Membership testing (`in`) on a list is **O(n)** — for large datasets where frequent lookups are needed, consider converting to a `set` for O(1) average lookups.

---

## 1.15 Sorting Lists (`sort()` vs `sorted()`)

| Feature | `list.sort()` | `sorted(list)` |
|---|---|---|
| Modifies original? | Yes (in place) | No (returns new list) |
| Works on any iterable? | No (list method only) | Yes |
| Return value | `None` | new sorted list |

```python
nums = [5, 2, 4, 1, 3]

# sort() - in place
nums.sort()
print(nums)   # [1, 2, 3, 4, 5]

# sorted() - returns a new list, original untouched
nums2 = [5, 2, 4, 1, 3]
result = sorted(nums2)
print(result)   # [1, 2, 3, 4, 5]
print(nums2)    # [5, 2, 4, 1, 3]   <- unchanged

# Descending order
print(sorted(nums2, reverse=True))   # [5, 4, 3, 2, 1]

# Custom sort key
words = ["banana", "kiwi", "fig", "apple"]
print(sorted(words, key=len))          # ['fig', 'kiwi', 'banana', 'apple']
print(sorted(words, key=lambda w: w[-1]))  # sort by last letter

# Sorting list of tuples/dicts by a specific field
people = [("Alice", 30), ("Bob", 25), ("Eve", 35)]
print(sorted(people, key=lambda p: p[1]))   # sort by age
```

---

## 1.16 List Unpacking

Assigning list elements directly to variables.

```python
# Basic unpacking (number of variables must match length)
a, b, c = [1, 2, 3]
print(a, b, c)   # 1 2 3

# Using * to capture remaining items
first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

*start, last = [1, 2, 3, 4, 5]
print(start, last)   # [1, 2, 3, 4] 5

# Unpacking in a for loop (list of tuples)
points = [(1, 2), (3, 4)]
for x, y in points:
    print(x, y)

# Unpacking into function calls
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))   # 6

# Swapping values via unpacking
a, b = 1, 2
a, b = b, a
print(a, b)   # 2 1
```

---

## Summary Cheat Sheet

| Operation | Example | Result |
|---|---|---|
| Create | `[1, 2, 3]` | new list |
| Access | `lst[0]` | first element |
| Negative index | `lst[-1]` | last element |
| Slice | `lst[1:3]` | sub-list |
| Add (end) | `lst.append(x)` | list + 1 item |
| Add (position) | `lst.insert(i, x)` | list + 1 item at `i` |
| Add (multiple) | `lst.extend(iter)` | list + many items |
| Remove (value) | `lst.remove(x)` | first `x` removed |
| Remove (index) | `lst.pop(i)` | item removed & returned |
| Clear | `lst.clear()` | `[]` |
| Search | `lst.index(x)` | index of `x` |
| Count | `lst.count(x)` | occurrences |
| Sort in place | `lst.sort()` | sorted, `None` returned |
| Sort new list | `sorted(lst)` | new sorted list |
| Reverse | `lst.reverse()` | reversed in place |
| Copy | `lst.copy()` | shallow copy |
| Concatenate | `lst1 + lst2` | new combined list |
| Repeat | `lst * n` | repeated elements |
| Membership | `x in lst` | `True`/`False` |
| Comprehension | `[x*2 for x in lst]` | transformed list |
| Unpack | `a, b = lst` | variables |



2. Tuples

2.1 Creating a Tuple
2.2 Accessing Elements
2.3 Immutability of Tuples
2.4 Tuple Methods (count, index)
2.5 Tuple Packing & Unpacking
2.6 Nested Tuples
2.7 Single-Element Tuple
2.8 Tuple vs List (Differences)
2.9 Why Use Tuples (Use Cases)

# 2. Tuples

A **tuple** is an ordered, **immutable** collection of items in Python. Tuples are written using parentheses `()`, though the parentheses are technically optional in many cases (it's the comma that actually creates a tuple).

---

## 2.1 Creating a Tuple

There are several ways to create a tuple:

```python
# Empty tuple
t1 = ()
print(t1)          # ()

# Tuple with multiple elements
t2 = (1, 2, 3)
print(t2)           # (1, 2, 3)

# Without parentheses (tuple packing) — this also works
t3 = 1, 2, 3
print(t3)            # (1, 2, 3)
print(type(t3))       # <class 'tuple'>

# Mixed data types
t4 = (1, "hello", 3.14, True)
print(t4)              # (1, 'hello', 3.14, True)

# Using the tuple() constructor
t5 = tuple([1, 2, 3])       # from a list
t6 = tuple("hello")          # from a string
t7 = tuple(range(5))          # from a range
print(t5, t6, t7)
# (1, 2, 3) ('h', 'e', 'l', 'l', 'o') (0, 1, 2, 3, 4)
```

**Exception example:**
```python
tuple(5)   # TypeError: 'int' object is not iterable
```
`tuple()` requires an **iterable** argument — passing a single non-iterable value raises `TypeError`.

---

## 2.2 Accessing Elements

Elements are accessed using **indexing** (zero-based) and **slicing**, just like lists.

```python
t = (10, 20, 30, 40, 50)

print(t[0])       # 10   (first element)
print(t[-1])      # 50   (last element)
print(t[1:4])     # (20, 30, 40)  (slicing)
print(t[::-1])    # (50, 40, 30, 20, 10)  (reversed)
```

**Exception example:**
```python
t = (10, 20, 30)
print(t[5])
# IndexError: tuple index out of range
```
Accessing an index that doesn't exist raises `IndexError`. Slicing, however, never raises this error — it just returns an empty tuple if out of range:
```python
print(t[10:20])   # () -- no error
```

---

## 2.3 Immutability of Tuples

Once a tuple is created, its elements **cannot be changed, added, or removed**. This is the defining feature of a tuple.

```python
t = (1, 2, 3)
t[0] = 100
# TypeError: 'tuple' object does not support item assignment
```

```python
t = (1, 2, 3)
del t[1]
# TypeError: 'tuple' object doesn't support item deletion
```

You **can** delete the entire tuple object itself:
```python
t = (1, 2, 3)
del t
print(t)   # NameError: name 't' is not defined
```

**Important nuance — mutable objects inside a tuple:**
If a tuple contains a mutable object (like a list), that inner object *can* still be modified, because the tuple only guarantees that the **reference** it holds doesn't change, not the contents of that reference.

```python
t = (1, 2, [3, 4])
t[2].append(5)
print(t)   # (1, 2, [3, 4, 5])  -- allowed! list inside tuple was mutated
```

---

## 2.4 Tuple Methods (`count`, `index`)

Tuples support only **two** built-in methods (because they're immutable, there's no need for add/remove methods).

### `count(x)`
Returns the number of times `x` appears in the tuple.
```python
t = (1, 2, 2, 3, 2, 4)
print(t.count(2))    # 3
print(t.count(9))    # 0  (no error if not found)
```

### `index(x, start=0, end=len(t))`
Returns the index of the **first** occurrence of `x`.
```python
t = (10, 20, 30, 20, 40)
print(t.index(20))          # 1
print(t.index(20, 2))       # 3  (search starting from index 2)
```

**Exception example:**
```python
t = (10, 20, 30)
t.index(99)
# ValueError: tuple.index(x): x not in tuple
```
Unlike `count()`, `index()` **raises `ValueError`** if the element is not found.

---

## 2.5 Tuple Packing & Unpacking

**Packing** — assigning multiple values to one tuple variable without explicit parentheses:
```python
person = "Alice", 25, "Engineer"
print(person)   # ('Alice', 25, 'Engineer')
```

**Unpacking** — assigning tuple values to multiple variables at once:
```python
name, age, job = person
print(name, age, job)   # Alice 25 Engineer
```

**Exception example (mismatched count):**
```python
a, b = (1, 2, 3)
# ValueError: too many values to unpack (expected 2)

a, b, c, d = (1, 2, 3)
# ValueError: not enough values to unpack (expected 4, got 3)
```

**Extended unpacking with `*` (Python 3+):**
```python
t = (1, 2, 3, 4, 5)
first, *middle, last = t
print(first)     # 1
print(middle)    # [2, 3, 4]   -- note: this becomes a list
print(last)      # 5

a, *rest = t
print(rest)      # [2, 3, 4, 5]
```

**Swapping values using tuple packing/unpacking:**
```python
x, y = 5, 10
x, y = y, x
print(x, y)   # 10 5
```

---

## 2.6 Nested Tuples

Tuples can contain other tuples (or any other data types) as elements.

```python
nested = (1, (2, 3), (4, 5, (6, 7)))

print(nested[1])        # (2, 3)
print(nested[2][2])     # (6, 7)
print(nested[2][2][0])  # 6
```

Iterating through nested tuples:
```python
matrix = ((1, 2), (3, 4), (5, 6))
for row in matrix:
    for val in row:
        print(val, end=" ")
# 1 2 3 4 5 6
```

**Exception example:**
```python
nested = (1, (2, 3))
print(nested[1][5])
# IndexError: tuple index out of range
```

---

## 2.7 Single-Element Tuple

A common beginner mistake: parentheses alone do **not** make a tuple — you need a **trailing comma**.

```python
t1 = (5)
print(type(t1))    # <class 'int'>  -- NOT a tuple! Just an int in parentheses.

t2 = (5,)
print(type(t2))    # <class 'tuple'>  -- correct single-element tuple

t3 = 5,
print(type(t3))    # <class 'tuple'>  -- comma alone also works
```

**Common error caused by forgetting the comma:**
```python
t = (5)
t.count(5)
# AttributeError: 'int' object has no attribute 'count'
```

---

## 2.8 Tuple vs List (Differences)

| Feature              | Tuple                          | List                          |
|----------------------|----------------------------------|--------------------------------|
| Syntax                | `(1, 2, 3)`                     | `[1, 2, 3]`                    |
| Mutability            | Immutable                       | Mutable                        |
| Methods available     | Only 2 (`count`, `index`)       | Many (`append`, `sort`, etc.)  |
| Performance           | Faster (lower memory overhead)  | Slower (more overhead)          |
| Usage as dict key     | Allowed (if hashable elements)  | Not allowed (unhashable)        |
| Use case              | Fixed data / records            | Dynamic, changing data          |

**Demonstrating the dict-key difference:**
```python
d = {}
d[(1, 2)] = "point A"       # works — tuple is hashable
print(d)                      # {(1, 2): 'point A'}

d[[1, 2]] = "point B"
# TypeError: unhashable type: 'list'
```

**Demonstrating performance/memory difference:**
```python
import sys
t = (1, 2, 3, 4, 5)
l = [1, 2, 3, 4, 5]
print(sys.getsizeof(t))   # smaller size
print(sys.getsizeof(l))   # larger size
```

---

## 2.9 Why Use Tuples (Use Cases)

1. **Data integrity** — When you want to ensure data cannot be accidentally modified (e.g., coordinates, RGB color values, database records).
   ```python
   coordinates = (28.6139, 77.2090)   # latitude, longitude — shouldn't change
   ```

2. **Dictionary keys** — Since tuples are hashable, they can be used as keys where lists cannot.
   ```python
   locations = {(28.6139, 77.2090): "Delhi", (19.0760, 72.8777): "Mumbai"}
   ```

3. **Function returns (multiple values)** — Functions often return multiple values packed as a tuple.
   ```python
   def min_max(numbers):
       return min(numbers), max(numbers)

   low, high = min_max([4, 2, 9, 1])
   print(low, high)   # 1 9
   ```

4. **Faster performance** — Since tuples are immutable, Python can optimize their storage and iteration, making them faster than lists for read-only data.

5. **Safer code** — Passing a tuple instead of a list to a function guarantees the function can't modify your original data.

6. **Unpacking convenience** — Cleanly return/assign multiple related values in one line (as seen in packing/unpacking).

---

### Quick Summary Table of All Tuple Methods

| Method         | Description                                  | Raises Exception?              |
|----------------|-----------------------------------------------|----------------------------------|
| `count(x)`      | Counts occurrences of `x`                     | No — returns `0` if not found   |
| `index(x)`      | Returns first index of `x`                    | Yes — `ValueError` if not found |

Tuples deliberately have very few methods since their immutability means there's nothing to "modify" — only to **read/search**.

3. Sets

3.1 Creating a Set
3.2 Properties of Sets (Unordered, Unique, Mutable)
3.3 Adding Elements (add, update)
3.4 Removing Elements (remove, discard, pop, clear)
3.5 Set Operations (union, intersection, difference, symmetric_difference)
3.6 Set Comprehension
3.7 Frozenset (Immutable Set)
3.8 Checking Subset/Superset
3.9 Iterating Over Sets
3.10 Use Cases of Sets

# 3. Sets

A **set** is an unordered collection of **unique**, **mutable** items in Python, written using curly braces `{}` or the `set()` constructor. Sets are optimized for membership testing and eliminating duplicates.

---

## 3.1 Creating a Set

```python
# Empty set — MUST use set(), not {}
s1 = set()
print(type(s1))    # <class 'set'>

# Set with elements
s2 = {1, 2, 3}
print(s2)           # {1, 2, 3}

# Duplicates are automatically removed
s3 = {1, 2, 2, 3, 3, 3}
print(s3)             # {1, 2, 3}

# Using set() constructor from an iterable
s4 = set([1, 2, 3])          # from a list
s5 = set("hello")             # from a string
print(s4)                       # {1, 2, 3}
print(s5)                        # {'h', 'e', 'l', 'o'}  (order not guaranteed)

# Mixed data types (must be hashable)
s6 = {1, "hello", 3.14, True}
print(s6)
```

**Critical gotcha:**
```python
s = {}
print(type(s))   # <class 'dict'>  -- NOT a set! {} always creates an empty dict.
```
To create an empty set, you **must** use `set()`.

**Exception example:**
```python
s = {1, 2, [3, 4]}
# TypeError: unhashable type: 'list'
```
Sets can only contain **hashable** (immutable) elements — lists, dicts, and other sets cannot be added directly.

---

## 3.2 Properties of Sets (Unordered, Unique, Mutable)

**Unordered** — sets don't maintain insertion order; you cannot rely on a consistent position.
```python
s = {5, 1, 4, 2, 3}
print(s)   # order not guaranteed — e.g. {1, 2, 3, 4, 5} or some other arrangement
```

**Exception — indexing is not supported:**
```python
s = {1, 2, 3}
print(s[0])
# TypeError: 'set' object is not subscriptable
```

**Unique** — duplicate values are automatically discarded.
```python
s = {1, 1, 2, 2, 3}
print(s)   # {1, 2, 3}
```

**Mutable** — the set itself can be changed (elements added/removed) after creation, unlike tuples.
```python
s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}
```

---

## 3.3 Adding Elements (`add`, `update`)

### `add(x)`
Adds a single element `x` to the set.
```python
s = {1, 2, 3}
s.add(4)
print(s)          # {1, 2, 3, 4}

s.add(2)           # adding a duplicate — no effect, no error
print(s)             # {1, 2, 3, 4}
```

**Exception example:**
```python
s = {1, 2, 3}
s.add([4, 5])
# TypeError: unhashable type: 'list'
```

### `update(iterable)`
Adds multiple elements from an iterable (list, tuple, another set, etc.) to the set.
```python
s = {1, 2, 3}
s.update([4, 5])
print(s)             # {1, 2, 3, 4, 5}

s.update([5, 6], (7, 8), {9, 10})   # accepts multiple iterables at once
print(s)                              # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

**Exception example:**
```python
s = {1, 2, 3}
s.update(5)
# TypeError: 'int' object is not iterable
```
`update()` requires iterable argument(s), unlike `add()` which takes a single hashable value.

---

## 3.4 Removing Elements (`remove`, `discard`, `pop`, `clear`)

### `remove(x)`
Removes `x` from the set. **Raises `KeyError`** if `x` is not found.
```python
s = {1, 2, 3}
s.remove(2)
print(s)     # {1, 3}

s.remove(99)
# KeyError: 99
```

### `discard(x)`
Removes `x` from the set if present. **Does NOT raise an error** if `x` is not found — safer alternative to `remove()`.
```python
s = {1, 2, 3}
s.discard(2)
print(s)      # {1, 3}

s.discard(99)   # no error, silently does nothing
print(s)          # {1, 3}
```

### `pop()`
Removes and returns an **arbitrary** element (since sets are unordered, you can't control which one).
```python
s = {1, 2, 3}
x = s.pop()
print(x)     # some element, e.g. 1
print(s)      # remaining set, e.g. {2, 3}
```

**Exception example:**
```python
s = set()
s.pop()
# KeyError: 'pop from an empty set'
```

### `clear()`
Removes all elements, leaving an empty set.
```python
s = {1, 2, 3}
s.clear()
print(s)    # set()
```

---

## 3.5 Set Operations (`union`, `intersection`, `difference`, `symmetric_difference`)

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### Union (`|` or `.union()`)
All elements from both sets (no duplicates).
```python
print(A | B)              # {1, 2, 3, 4, 5, 6}
print(A.union(B))          # {1, 2, 3, 4, 5, 6}
```

### Intersection (`&` or `.intersection()`)
Elements common to both sets.
```python
print(A & B)                     # {3, 4}
print(A.intersection(B))          # {3, 4}
```

### Difference (`-` or `.difference()`)
Elements in `A` but **not** in `B`.
```python
print(A - B)                    # {1, 2}
print(A.difference(B))           # {1, 2}
print(B - A)                       # {5, 6}
```

### Symmetric Difference (`^` or `.symmetric_difference()`)
Elements in either set, but **not** in both (i.e. excludes the intersection).
```python
print(A ^ B)                              # {1, 2, 5, 6}
print(A.symmetric_difference(B))           # {1, 2, 5, 6}
```

### In-place versions (modify the original set)
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.update(B)                  # same as |=  -> union in place
A.intersection_update(B)      # same as &=  -> intersection in place
A.difference_update(B)         # same as -=  -> difference in place
A.symmetric_difference_update(B)  # same as ^= -> symmetric difference in place
```

**Exception example:**
```python
A = {1, 2, 3}
A.union([4, 5])    # works fine — union() accepts any iterable
A & [4, 5]
# TypeError: unsupported operand type(s) for &: 'set' and 'list'
```
Note: operator forms (`&`, `|`, `-`, `^`) require both operands to be **sets**, but method forms (`.union()`, `.intersection()`, etc.) accept any iterable.

---

## 3.6 Set Comprehension

Similar to list comprehension, but produces a set (duplicates auto-removed).

```python
squares = {x**2 for x in range(6)}
print(squares)     # {0, 1, 4, 9, 16, 25}

# With a condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)    # {0, 4, 16, 36, 64}

# From a string — removes duplicate characters
vowels_in_word = {ch for ch in "programming" if ch in "aeiou"}
print(vowels_in_word)    # {'o', 'a', 'i'}
```

**Exception example:**
```python
s = {x/0 for x in range(3)}
# ZeroDivisionError: division by zero
```
Errors inside the comprehension expression propagate just like in a loop.

---

## 3.7 Frozenset (Immutable Set)

A `frozenset` is an **immutable** version of a set — once created, it cannot be modified. Useful when you need a hashable, set-like object (e.g., as a dictionary key or an element of another set).

```python
fs = frozenset([1, 2, 3, 4])
print(fs)          # frozenset({1, 2, 3, 4})

fs2 = frozenset({3, 4, 5})
print(fs | fs2)     # frozenset({1, 2, 3, 4, 5}) -- read-only operations work fine
```

**Exception example:**
```python
fs = frozenset([1, 2, 3])
fs.add(4)
# AttributeError: 'frozenset' object has no attribute 'add'
```
All mutating methods (`add`, `remove`, `discard`, `pop`, `clear`, `update`) are unavailable on `frozenset`.

**Using frozenset as a dict key or set element:**
```python
d = {frozenset([1, 2]): "pair A"}
print(d)   # {frozenset({1, 2}): 'pair A'}

nested = {frozenset([1, 2]), frozenset([3, 4])}
print(nested)   # a set containing frozensets
```

---

## 3.8 Checking Subset/Superset

```python
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
```

### `issubset()` / `<=`
Checks if every element of `A` is in `B`.
```python
print(A.issubset(B))     # True
print(A <= B)              # True
```

### `issuperset()` / `>=`
Checks if `A` contains every element of `B`.
```python
print(B.issuperset(A))    # True
print(B >= A)                # True
```

### Proper subset/superset (`<`, `>`)
True only if the sets are subsets/supersets **and not equal**.
```python
C = {1, 2, 3}
print(A < C)    # False -- A == C, not a proper subset
print(A <= C)     # True -- still a valid (non-proper) subset
```

### `isdisjoint()`
Checks if two sets have **no elements in common**.
```python
X = {1, 2, 3}
Y = {4, 5, 6}
print(X.isdisjoint(Y))   # True

Z = {3, 4, 5}
print(X.isdisjoint(Z))    # False -- they share element 3
```

**Note:** There's no exception risk here — these methods always return a boolean, even for empty sets.

---

## 3.9 Iterating Over Sets

```python
s = {10, 20, 30, 40}

for item in s:
    print(item, end=" ")
# order not guaranteed, e.g.: 40 10 20 30
```

Using `enumerate()` with a set:
```python
for i, val in enumerate(s):
    print(i, val)
# index order corresponds to iteration order, not sorted/insertion order
```

**Exception example — modifying a set while iterating:**
```python
s = {1, 2, 3, 4}
for x in s:
    if x == 2:
        s.remove(x)
# RuntimeError: Set changed size during iteration
```
To safely remove elements while iterating, iterate over a copy:
```python
s = {1, 2, 3, 4}
for x in s.copy():
    if x == 2:
        s.remove(x)
print(s)   # {1, 3, 4}
```

---

## 3.10 Use Cases of Sets

1. **Removing duplicates from a collection:**
   ```python
   nums = [1, 2, 2, 3, 3, 3, 4]
   unique_nums = list(set(nums))
   print(unique_nums)   # [1, 2, 3, 4]
   ```

2. **Fast membership testing** — checking `x in s` is O(1) on average for sets vs O(n) for lists.
   ```python
   allowed_users = {"alice", "bob", "carol"}
   print("alice" in allowed_users)   # True — very fast even for large sets
   ```

3. **Mathematical set operations** — finding common elements, differences, etc. (e.g., comparing two datasets, finding mutual friends).
   ```python
   friends_a = {"Tom", "Jerry", "Spike"}
   friends_b = {"Jerry", "Tyke", "Spike"}
   mutual_friends = friends_a & friends_b
   print(mutual_friends)   # {'Jerry', 'Spike'}
   ```

4. **Filtering unique data streams** — e.g., tracking unique visitors, unique words in a document.
   ```python
   text = "the quick brown fox the lazy dog the fox"
   unique_words = set(text.split())
   print(unique_words)  # {'the', 'quick', 'brown', 'fox', 'lazy', 'dog'}
   ```

5. **Using `frozenset` as dictionary keys** — when you need an immutable, hashable set-like structure (e.g., caching results based on unordered combinations).

---

### Quick Summary Table of All Set Methods

| Method                          | Description                                       | Raises Exception?                  |
|----------------------------------|-----------------------------------------------------|--------------------------------------|
| `add(x)`                          | Adds a single element                                | `TypeError` if unhashable            |
| `update(iterable)`                 | Adds multiple elements                                | `TypeError` if arg not iterable      |
| `remove(x)`                         | Removes element `x`                                    | `KeyError` if not found              |
| `discard(x)`                         | Removes element `x` if present                          | No error if not found                |
| `pop()`                               | Removes & returns arbitrary element                       | `KeyError` if set is empty           |
| `clear()`                              | Removes all elements                                         | No                                    |
| `union(*sets)` / `\|`                    | Combines sets                                                   | No                                    |
| `intersection(*sets)` / `&`               | Common elements                                                  | No (operator form: `TypeError` on non-set) |
| `difference(*sets)` / `-`                   | Elements only in first set                                         | No (operator form: `TypeError` on non-set) |
| `symmetric_difference(s)` / `^`               | Elements in either but not both                                      | No (operator form: `TypeError` on non-set) |
| `issubset(s)` / `<=`                            | Checks subset relationship                                             | No                                    |
| `issuperset(s)` / `>=`                             | Checks superset relationship                                            | No                                    |
| `isdisjoint(s)`                                       | Checks for no common elements                                             | No                                    |
| `copy()`                                                | Returns a shallow copy                                                       | No                                    |

Sets are ideal when **order doesn't matter**, **duplicates aren't allowed**, and you need **fast lookups** or **mathematical set logic**.

4. Dictionaries

4.1 Creating a Dictionary
4.2 Accessing Values (keys, get())
4.3 Adding/Updating Key-Value Pairs
4.4 Removing Elements (pop, popitem, del, clear)
4.5 Dictionary Methods (keys, values, items, update, copy, setdefault)
4.6 Iterating Over Dictionaries
4.7 Nested Dictionaries
4.8 Dictionary Comprehension
4.9 Checking Key Existence
4.10 Merging Dictionaries
4.11 Dictionary Ordering (insertion order)

# 4. Dictionaries

A **dictionary** is an ordered (since Python 3.7+) collection of **key-value pairs**. Keys must be unique and hashable; values can be of any type and can be duplicated. Dictionaries are written using curly braces `{key: value}`.

---

## 4.1 Creating a Dictionary

```python
# Empty dictionary
d1 = {}
print(type(d1))    # <class 'dict'>

# Dictionary with key-value pairs
d2 = {"name": "Alice", "age": 25, "city": "Delhi"}
print(d2)            # {'name': 'Alice', 'age': 25, 'city': 'Delhi'}

# Using dict() constructor
d3 = dict(name="Bob", age=30)             # keyword arguments
d4 = dict([("a", 1), ("b", 2)])            # from list of tuples
d5 = dict(zip(["x", "y", "z"], [1, 2, 3]))  # from two lists using zip
print(d3, d4, d5)

# Keys can be any hashable type
d6 = {1: "one", (2, 3): "tuple key", "str": "string key"}
print(d6)

# From another dict
d7 = dict(d2)
print(d7)
```

**Exception example — unhashable keys:**
```python
d = {[1, 2]: "value"}
# TypeError: unhashable type: 'list'

d = {{1, 2}: "value"}
# TypeError: unhashable type: 'set'
```
Only immutable/hashable types (`str`, `int`, `float`, `tuple`, `frozenset`, `bool`) can be used as dictionary keys.

**Duplicate keys — last one wins:**
```python
d = {"a": 1, "a": 2}
print(d)   # {'a': 2}
```

---

## 4.2 Accessing Values (`keys`, `get()`)

### Using square brackets `[]`
```python
d = {"name": "Alice", "age": 25}
print(d["name"])    # Alice
```

**Exception example:**
```python
print(d["email"])
# KeyError: 'email'
```
Accessing a non-existent key with `[]` raises `KeyError`.

### Using `get(key, default=None)`
Safer alternative — returns `None` (or a specified default) instead of raising an error.
```python
print(d.get("name"))            # Alice
print(d.get("email"))             # None
print(d.get("email", "N/A"))       # N/A -- custom default value
```

---

## 4.3 Adding/Updating Key-Value Pairs

```python
d = {"name": "Alice", "age": 25}

# Adding a new key
d["city"] = "Delhi"
print(d)   # {'name': 'Alice', 'age': 25, 'city': 'Delhi'}

# Updating an existing key
d["age"] = 26
print(d)    # {'name': 'Alice', 'age': 26, 'city': 'Delhi'}
```

**Exception example — using unhashable key when assigning:**
```python
d = {}
d[[1, 2]] = "value"
# TypeError: unhashable type: 'list'
```

---

## 4.4 Removing Elements (`pop`, `popitem`, `del`, `clear`)

### `pop(key, default)`
Removes the specified key and returns its value.
```python
d = {"a": 1, "b": 2, "c": 3}
val = d.pop("b")
print(val)    # 2
print(d)       # {'a': 1, 'c': 3}
```

**Exception example:**
```python
d.pop("z")
# KeyError: 'z'

d.pop("z", "not found")   # safe version with default
print(d.pop("z", "not found"))   # not found -- no error
```

### `popitem()`
Removes and returns the **last inserted** key-value pair (as a tuple) — LIFO order since Python 3.7+.
```python
d = {"a": 1, "b": 2, "c": 3}
item = d.popitem()
print(item)   # ('c', 3)
print(d)       # {'a': 1, 'b': 2}
```

**Exception example:**
```python
d = {}
d.popitem()
# KeyError: 'popitem(): dictionary is empty'
```

### `del` statement
Deletes a specific key, or the entire dictionary.
```python
d = {"a": 1, "b": 2}
del d["a"]
print(d)    # {'b': 2}
```

**Exception example:**
```python
del d["z"]
# KeyError: 'z'
```

### `clear()`
Removes all key-value pairs.
```python
d = {"a": 1, "b": 2}
d.clear()
print(d)   # {}
```

---

## 4.5 Dictionary Methods (`keys`, `values`, `items`, `update`, `copy`, `setdefault`)

### `keys()`
Returns a **view object** of all keys (dynamically reflects changes to the dict).
```python
d = {"a": 1, "b": 2}
print(d.keys())    # dict_keys(['a', 'b'])
print(list(d.keys()))   # ['a', 'b']
```

### `values()`
Returns a view object of all values.
```python
print(d.values())    # dict_values([1, 2])
```

### `items()`
Returns a view object of key-value pairs as tuples.
```python
print(d.items())    # dict_items([('a', 1), ('b', 2)])
```

**Dynamic view behavior:**
```python
d = {"a": 1}
keys_view = d.keys()
d["b"] = 2
print(keys_view)   # dict_keys(['a', 'b']) -- automatically updated!
```

### `update(other)`
Merges another dict (or iterable of key-value pairs) into the current one, overwriting existing keys.
```python
d = {"a": 1, "b": 2}
d.update({"b": 20, "c": 3})
print(d)    # {'a': 1, 'b': 20, 'c': 3}

d.update(x=100)          # keyword argument form
d.update([("y", 200)])     # list of tuples form
print(d)
```

**Exception example:**
```python
d = {}
d.update([1, 2, 3])
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
```
Each element in the iterable passed to `update()` must itself be a 2-item iterable (key, value).

### `copy()`
Returns a shallow copy of the dictionary.
```python
d = {"a": 1, "b": [1, 2]}
d2 = d.copy()
d2["a"] = 100
print(d, d2)   # {'a': 1, 'b': [1, 2]}  {'a': 100, 'b': [1, 2]}

# shallow copy caveat -- nested mutable objects are shared
d2["b"].append(3)
print(d["b"])   # [1, 2, 3] -- original also affected!
```

### `setdefault(key, default=None)`
Returns the value of `key` if it exists; otherwise inserts `key` with `default` and returns that.
```python
d = {"a": 1}
val = d.setdefault("a", 100)
print(val)   # 1 -- key already existed, default ignored
print(d)      # {'a': 1}

val = d.setdefault("b", 100)
print(val)     # 100 -- key didn't exist, so it's added
print(d)        # {'a': 1, 'b': 100}
```
Useful for building dictionaries of lists:
```python
groups = {}
pairs = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana")]
for category, item in pairs:
    groups.setdefault(category, []).append(item)
print(groups)   # {'fruit': ['apple', 'banana'], 'veg': ['carrot']}
```

---

## 4.6 Iterating Over Dictionaries

```python
d = {"a": 1, "b": 2, "c": 3}

# Iterating over keys (default)
for key in d:
    print(key)

# Iterating over keys explicitly
for key in d.keys():
    print(key)

# Iterating over values
for value in d.values():
    print(value)

# Iterating over key-value pairs
for key, value in d.items():
    print(key, value)
```

**Exception example — modifying keys while iterating:**
```python
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    if key == "b":
        del d[key]
# RuntimeError: dictionary changed size during iteration
```
Safe approach — iterate over a copy of the keys:
```python
d = {"a": 1, "b": 2, "c": 3}
for key in list(d.keys()):
    if key == "b":
        del d[key]
print(d)   # {'a': 1, 'c': 3}
```

---

## 4.7 Nested Dictionaries

Dictionaries can contain other dictionaries as values, useful for representing structured/hierarchical data.

```python
students = {
    "student1": {"name": "Alice", "age": 22, "grades": [85, 90, 95]},
    "student2": {"name": "Bob", "age": 24, "grades": [70, 75, 80]}
}

print(students["student1"]["name"])     # Alice
print(students["student2"]["grades"][1])  # 75

# Adding a new nested key
students["student1"]["email"] = "alice@example.com"
print(students["student1"])
```

**Exception example:**
```python
print(students["student3"]["name"])
# KeyError: 'student3'
```

Safe nested access using `.get()`:
```python
print(students.get("student3", {}).get("name", "Not Found"))
# Not Found
```

---

## 4.8 Dictionary Comprehension

```python
squares = {x: x**2 for x in range(6)}
print(squares)    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With a condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)   # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# From two lists
names = ["a", "b", "c"]
scores = [90, 85, 95]
result = {k: v for k, v in zip(names, scores)}
print(result)    # {'a': 90, 'b': 85, 'c': 95}

# Swapping keys and values
d = {"a": 1, "b": 2}
swapped = {v: k for k, v in d.items()}
print(swapped)    # {1: 'a', 2: 'b'}
```

**Exception example:**
```python
d = {x: 10/x for x in range(-2, 3)}
# ZeroDivisionError: division by zero  (fails when x == 0)
```

---

## 4.9 Checking Key Existence

```python
d = {"a": 1, "b": 2}

print("a" in d)         # True  -- checks keys by default
print("z" in d)          # False
print("z" not in d)       # True

# Checking values (less common, requires .values())
print(1 in d.values())    # True

# Checking key-value pair
print(("a", 1) in d.items())   # True
```

Using `in` avoids `KeyError` entirely — it's the recommended way to check existence before direct access:
```python
if "a" in d:
    print(d["a"])
else:
    print("Key not found")
```

---

## 4.10 Merging Dictionaries

### Using `update()` (in-place, mutates original)
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
d1.update(d2)
print(d1)   # {'a': 1, 'b': 20, 'c': 3}
```

### Using `**` unpacking (creates a new dict)
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
merged = {**d1, **d2}
print(merged)    # {'a': 1, 'b': 20, 'c': 3}  -- d2 values take precedence on conflict
```

### Using the merge operator `|` (Python 3.9+)
```python
merged = d1 | d2
print(merged)     # {'a': 1, 'b': 20, 'c': 3}

d1 |= d2            # in-place merge
print(d1)             # {'a': 1, 'b': 20, 'c': 3}
```

**Exception example:**
```python
merged = d1 | [("x", 1)]
# TypeError: unsupported operand type(s) for |: 'dict' and 'list'
```
The `|` operator requires both operands to be dictionaries (unlike `update()`, which also accepts iterables of pairs).

---

## 4.11 Dictionary Ordering (Insertion Order)

Since **Python 3.7**, dictionaries officially guarantee they maintain **insertion order** — the order in which keys were first added is preserved when iterating.

```python
d = {}
d["z"] = 1
d["a"] = 2
d["m"] = 3
print(d)    # {'z': 1, 'a': 2, 'm': 3}  -- insertion order preserved, NOT sorted

for key in d:
    print(key)
# z, a, m -- in the order they were inserted
```

**Important nuance — updating a key does not change its position:**
```python
d = {"a": 1, "b": 2, "c": 3}
d["a"] = 100
print(d)   # {'a': 100, 'b': 2, 'c': 3} -- 'a' stays in its original position
```

**Deleting and re-adding a key moves it to the end:**
```python
d = {"a": 1, "b": 2, "c": 3}
del d["a"]
d["a"] = 1
print(d)   # {'b': 2, 'c': 3, 'a': 1} -- 'a' is now last
```

**Note:** In Python versions **before 3.7** (e.g., 3.6 as an implementation detail, and officially unordered before that), dictionaries did **not** guarantee order. If working with legacy code or needing explicit ordering guarantees historically, `collections.OrderedDict` was used — though it's largely unnecessary now.

---

### Quick Summary Table of Common Dictionary Methods

| Method                     | Description                                         | Raises Exception?                     |
|------------------------------|--------------------------------------------------------|------------------------------------------|
| `d[key]`                       | Access value by key                                       | `KeyError` if key missing                |
| `get(key, default)`              | Access value safely                                          | No                                        |
| `keys()`                           | Returns view of keys                                            | No                                        |
| `values()`                           | Returns view of values                                            | No                                        |
| `items()`                              | Returns view of key-value pairs                                      | No                                        |
| `update(other)`                          | Merges another dict/iterable in place                                   | `ValueError`/`TypeError` on malformed input |
| `pop(key, default)`                        | Removes key, returns value                                                | `KeyError` if missing & no default        |
| `popitem()`                                  | Removes last inserted pair                                                  | `KeyError` if dict is empty               |
| `setdefault(key, default)`                     | Gets value or inserts default                                                  | No                                        |
| `copy()`                                          | Shallow copy                                                                       | No                                        |
| `clear()`                                            | Removes all items                                                                     | No                                        |
| `del d[key]`                                            | Deletes a key                                                                             | `KeyError` if missing                     |

Dictionaries are the backbone of most Python data-handling tasks — ideal for **fast key-based lookups**, **structured/labeled data**, and **counting/grouping** operations.

5. Strings (as a Data Structure)

5.1 String Creation & Immutability
5.2 Indexing & Slicing
5.3 String Methods (upper, lower, strip, split, join, replace, find, count, startswith, endswith, etc.)
5.4 String Concatenation & Repetition
5.5 String Formatting (f-string, format(), %)
5.6 Escape Characters
5.7 Multiline Strings
5.8 String Iteration

6. Comprehensions (Consolidated)

6.1 List Comprehension
6.2 Set Comprehension
6.3 Dictionary Comprehension
6.4 Nested Comprehensions
6.5 Conditional (if-else) in Comprehensions

7. Arrays

7.1 Python array Module
7.2 Array vs List

8. Comparison & Selection

8.1 List vs Tuple vs Set vs Dictionary (When to Use What)
8.2 Mutable vs Immutable Data Structures
8.3 Time Complexity of Operations (Big-O for each structure)

9. Real-World / Practical Topics

9.1 Choosing the Right Data Structure for a Problem
9.2 Common Interview Problems on Data Structures
9.3 Memory Considerations
