# Notes

1. Function Basics

1.1 What is a Function & Why Use Functions
1.2 Defining a Function (def keyword)
1.3 Calling a Function
1.4 Function Naming Conventions
1.5 The return Statement
1.6 Functions with No Return (returns None)
1.7 Docstrings

2. Function Parameters & Arguments

2.1 Parameters vs Arguments (Difference)
2.2 Positional Arguments
2.3 Keyword Arguments
2.4 Default Arguments
2.5 Variable-Length Arguments (*args)
2.6 Variable-Length Keyword Arguments (**kwargs)
2.7 Combining Positional, Default, *args, **kwargs (Order Rules)
2.8 Positional-Only Parameters (/)
2.9 Keyword-Only Parameters (*)
2.10 Argument Unpacking (* and ** while calling functions)

3. Scope & Lifetime of Variables

3.1 Local Scope
3.2 Global Scope
3.3 global Keyword
3.4 Enclosing Scope (Nested Functions)
3.5 nonlocal Keyword
3.6 LEGB Rule (Local, Enclosing, Global, Built-in)

4. Lambda Functions

4.1 Syntax & Definition
4.2 Lambda vs Regular Function
4.3 Using Lambda with map()
4.4 Using Lambda with filter()
4.5 Using Lambda with reduce()
4.6 Using Lambda with sorted()/sort() (key parameter)
4.7 When to Use / Avoid Lambda

5. Higher-Order Functions

5.1 What is a Higher-Order Function
5.2 map()
5.3 filter()
5.4 reduce() (from functools)
5.5 Functions as Arguments
5.6 Functions Returning Functions

6. Recursion

6.1 What is Recursion
6.2 Base Case & Recursive Case
6.3 Recursive Function Examples (factorial, fibonacci)
6.4 Recursion vs Iteration
6.5 Stack Overflow / Recursion Limit (sys.setrecursionlimit)
6.6 Tail Recursion (concept, Python doesn't optimize it)
6.7 Memoization with Recursion

7. Closures

7.1 What is a Closure
7.2 Nested Functions
7.3 Free Variables
7.4 Practical Use Cases of Closures

8. Decorators

8.1 What is a Decorator
8.2 Functions as First-Class Objects (prerequisite concept)
8.3 Writing a Basic Decorator
8.4 @decorator Syntax (Syntactic Sugar)
8.5 Decorators with Arguments (*args, **kwargs in wrapper)
8.6 Decorators That Accept Arguments (Decorator Factories)
8.7 Chaining Multiple Decorators
8.8 functools.wraps (Preserving Metadata)
8.9 Class-Based Decorators
8.10 Real-World Built-in Decorators (@staticmethod, @classmethod, @property)
8.11 Practical Use Cases (logging, timing, authentication, caching)

9. Generators

9.1 What is a Generator
9.2 yield Keyword
9.3 Generator Functions vs Regular Functions
9.4 Generator Expressions
9.5 next() and StopIteration
9.6 Generators vs Lists (Memory Efficiency)
9.7 Infinite Generators
9.8 yield from
9.9 Sending Values into a Generator (.send())

10. Function Annotations & Type Hints

10.1 What are Type Hints
10.2 Annotating Parameters and Return Types
10.3 typing Module (List, Dict, Optional, Union, etc.)
10.4 Why Type Hints Matter (readability, tooling, static analysis)

11. Built-in Functions Relevant to Functional Style

11.1 zip()
11.2 enumerate() (revisited in function context)
11.3 any() and all()
11.4 sorted() with custom key functions

12. functools Module

12.1 functools.reduce
12.2 functools.partial
12.3 functools.lru_cache (Caching/Memoization)
12.4 functools.wraps
12.5 functools.singledispatch

13. Function Documentation & Introspection

13.1 __doc__ attribute
13.2 help() function
13.3 __name__ attribute of functions
13.4 Inspecting function signatures (inspect module basics)

14. Best Practices

14.1 Single Responsibility Principle for Functions
14.2 Avoiding Mutable Default Arguments (common bug)
14.3 Pure Functions vs Functions with Side Effects
14.4 Naming Conventions & Readability


5. Anonymous & Callback-Style Usage

15.1 Callback Functions (passing a function to be called later — common in async/event-driven code)

16. Function Overloading (Python's Approach)

16.1 Python Doesn't Support True Overloading (concept)
16.2 Simulating Overloading with Default Args / *args
16.3 functools.singledispatch (already listed under functools, but worth calling out here as the "overloading" solution)

17. Iterators vs Generators (Function Context)

17.1 Difference Between Iterators and Generators
17.2 Building a Custom Iterator (__iter__, __next__) — bridges into OOP

18. Async Functions (Preview — Full Topic Lives Under Concurrency)

18.1 async def and await (just the function-definition side)
18.2 Coroutine Functions vs Regular Functions

19. Exception Handling Inside Functions

19.1 Raising Exceptions from Functions
19.2 try-except Within a Function Body
19.3 Functions with finally for Cleanup
