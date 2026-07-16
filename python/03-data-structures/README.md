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
