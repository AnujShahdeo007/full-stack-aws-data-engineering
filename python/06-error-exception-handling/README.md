# Notes

Here are all the topics under Error & Exception Handling in Python:
1. Fundamentals

1.1 What is an Error vs an Exception (Difference)
1.2 Syntax Errors vs Runtime Errors (Exceptions)
1.3 Why Exception Handling is Needed
1.4 Python's Exception Hierarchy (BaseException → Exception → specific exceptions)

2. Basic Exception Handling

2.1 try Block
2.2 except Block
2.3 Catching a Specific Exception
2.4 Catching Multiple Exceptions (Multiple except Blocks)
2.5 Catching Multiple Exceptions in a Single except (Tuple of Exceptions)
2.6 Catching All Exceptions (Bare except:) — and Why to Avoid It
2.7 Accessing Exception Details (except Exception as e)

3. else and finally

3.1 else Block (Runs Only if No Exception Occurred)
3.2 finally Block (Always Runs — Cleanup Code)
3.3 Order of Execution: try → except → else → finally
3.4 finally with return (Behavior Nuances)

4. Raising Exceptions

4.1 raise Statement
4.2 Raising a Built-in Exception Manually
4.3 Re-raising an Exception (raise inside except)
4.4 Raising an Exception with a Custom Message
4.5 Exception Chaining (raise ... from ...)

5. Custom (User-Defined) Exceptions

5.1 Why Create Custom Exceptions
5.2 Creating a Custom Exception Class (Inheriting from Exception)
5.3 Adding Custom Attributes/Messages to Custom Exceptions
5.4 Custom Exception Hierarchies (Base Exception + Sub-Exceptions)
5.5 Real-World Use Cases (validation errors, business logic errors)

6. Built-in Exception Types (Commonly Used)

6.1 ValueError
6.2 TypeError
6.3 KeyError
6.4 IndexError
6.5 AttributeError
6.6 NameError
6.7 ZeroDivisionError
6.8 FileNotFoundError
6.9 ImportError / ModuleNotFoundError
6.10 StopIteration
6.11 RuntimeError
6.12 OverflowError
6.13 RecursionError
6.14 PermissionError
6.15 ConnectionError / TimeoutError
6.16 KeyboardInterrupt
6.17 MemoryError
6.18 UnicodeDecodeError / UnicodeEncodeError

7. assert Statement

7.1 What is assert & Why Use It
7.2 Syntax and Custom Assert Messages
7.3 AssertionError
7.4 Assert vs Exception Handling (When to Use Which)
7.5 Disabling Assertions in Production (-O flag, __debug__)

8. Context Managers & Exception Handling

8.1 with Statement (Automatic Cleanup on Exceptions)
8.2 How with Relates to Exception Handling (__exit__ suppressing exceptions)
8.3 Writing Custom Context Managers for Error Handling (contextlib)

9. Nested & Advanced Exception Handling

9.1 Nested try-except Blocks
9.2 Exception Groups (ExceptionGroup, Python 3.11+)
9.3 except* Syntax (Python 3.11+)
9.4 Catching Exceptions in Loops (continue vs break on error)
9.5 Exception Handling in Recursive Functions

10. Exception Object & Traceback

10.1 The Exception Object (args, __str__)
10.2 traceback Module (print_exc(), format_exc())
10.3 sys.exc_info()
10.4 Getting Line Number/File Where Exception Occurred
10.5 __traceback__ Attribute

11. Logging Exceptions

11.1 Using logging Module Instead of print() for Errors
11.2 logging.exception()
11.3 Logging Levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) in Error Context

12. Warnings (Related but Distinct from Exceptions)

12.1 warnings Module
12.2 warnings.warn()
12.3 Warning Categories (DeprecationWarning, UserWarning, etc.)
12.4 Warnings vs Exceptions

13. Best Practices

13.1 Catch Specific Exceptions, Not Generic Ones
13.2 Avoid Empty except: pass (Silent Failures)
13.3 Use finally for Resource Cleanup (files, DB connections, network)
13.4 Fail Fast vs Fail Gracefully (When to Use Each)
13.5 Don't Use Exceptions for Normal Control Flow
13.6 EAFP vs LBYL (Python Philosophy — "Easier to Ask Forgiveness than Permission" vs "Look Before You Leap")
13.7 Meaningful Error Messages for Debugging

14. Real-World / Applied Topics

14.1 Exception Handling in File I/O
14.2 Exception Handling in API Calls / Network Requests
14.3 Exception Handling in Database Operations
14.4 Exception Handling in Data Pipelines (retry logic, dead-letter queues)
14.5 Global Exception Handling (top-level try-except in main())
