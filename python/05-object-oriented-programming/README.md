# Notes

Here are all the topics under Object-Oriented Programming (OOP) in Python:
1. OOP Fundamentals

1.1 What is OOP & Why Use It
1.2 Procedural vs Object-Oriented Programming
1.3 Four Pillars of OOP (Encapsulation, Abstraction, Inheritance, Polymorphism)
1.4 Classes and Objects (Core Concept)

2. Classes & Objects

2.1 Defining a Class (class keyword)
2.2 Creating an Object (Instantiation)
2.3 The self Parameter
2.4 Instance Attributes
2.5 Class Attributes (vs Instance Attributes)
2.6 Instance Methods
2.7 Multiple Objects from Same Class

3. Constructors & Initialization

3.1 __init__() Method
3.2 Default Values in Constructor
3.3 __new__() Method (Object Creation, brief)
3.4 Constructor Overloading (Python's Approach — default args)

4. Encapsulation

4.1 What is Encapsulation
4.2 Public Members
4.3 Protected Members (single underscore _var convention)
4.4 Private Members (double underscore __var, name mangling)
4.5 Getter and Setter Methods
4.6 @property Decorator (Pythonic Getters/Setters)
4.7 @<property>.setter Decorator
4.8 @<property>.deleter Decorator

5. Inheritance

5.1 What is Inheritance
5.2 Single Inheritance
5.3 Multiple Inheritance
5.4 Multilevel Inheritance
5.5 Hierarchical Inheritance
5.6 Hybrid Inheritance
5.7 super() Function
5.8 Method Overriding
5.9 Method Resolution Order (MRO) — __mro__, mro()
5.10 Diamond Problem & How Python Resolves It

6. Polymorphism

6.1 What is Polymorphism
6.2 Method Overriding (Runtime Polymorphism)
6.3 Method Overloading (Python's Simulated Approach)
6.4 Operator Overloading
6.5 Duck Typing
6.6 Polymorphism with Functions and Classes

7. Abstraction

7.1 What is Abstraction
7.2 Abstract Base Classes (ABC Module)
7.3 @abstractmethod Decorator
7.4 Abstract Classes vs Interfaces (Python Context)
7.5 Why Use Abstraction (Real-World Use Cases)

8. Magic / Dunder Methods

8.1 What are Dunder (Magic) Methods
8.2 __init__, __new__
8.3 __str__ vs __repr__
8.4 __len__
8.5 __del__ (Destructor)
8.6 __eq__, __ne__, __lt__, __gt__, __le__, __ge__ (Comparison Operators)
8.7 __add__, __sub__, __mul__, etc. (Arithmetic Operator Overloading)
8.8 __getitem__, __setitem__, __delitem__ (Indexing Behavior)
8.9 __iter__, __next__ (Making a Class Iterable)
8.10 __call__ (Making an Object Callable)
8.11 __contains__ (Enables in keyword)
8.12 __enter__, __exit__ (Context Manager Protocol)
8.13 __hash__

9. Class Methods & Static Methods

9.1 Instance Methods (recap)
9.2 @classmethod Decorator
9.3 cls Parameter
9.4 @staticmethod Decorator
9.5 Class Method vs Static Method vs Instance Method (Differences)
9.6 Factory Methods Using @classmethod

10. Composition & Aggregation

10.1 What is Composition ("has-a" relationship)
10.2 What is Aggregation
10.3 Composition vs Inheritance ("has-a" vs "is-a")
10.4 When to Use Composition Over Inheritance

11. Class Relationships & Design

11.1 Association
11.2 Coupling & Cohesion (concept)
11.3 SOLID Principles (brief overview in OOP context)

12. Special Class Types

12.1 Nested Classes (Inner Classes)
12.2 Data Classes (@dataclass decorator)
12.3 Enum Classes (enum module — Enum, IntEnum, auto())
12.4 Named Tuples as Lightweight Classes (collections.namedtuple)
12.5 Singleton Design Pattern (Python Implementation)

13. Metaclasses (Advanced)

13.1 What is a Metaclass
13.2 type() as a Metaclass
13.3 Creating a Custom Metaclass
13.4 __init_subclass__
13.5 Use Cases (ORMs, frameworks like Django)

14. Descriptors (Advanced)

14.1 What is a Descriptor
14.2 __get__, __set__, __delete__
14.3 Use Cases (validation, @property internals)

15. Object Introspection & Utilities

15.1 isinstance()
15.2 issubclass()
15.3 type()
15.4 id()
15.5 dir()
15.6 vars()
15.7 __dict__ Attribute
15.8 hasattr(), getattr(), setattr(), delattr()

16. Object Copying

16.1 Shallow Copy (copy.copy())
16.2 Deep Copy (copy.deepcopy())
16.3 Copy Behavior in Custom Classes

17. Exception Handling in OOP

17.1 Custom Exception Classes (Inheriting from Exception)
17.2 Raising Custom Exceptions from Class Methods

18. Design Patterns (Common Ones Using OOP)

18.1 Singleton Pattern
18.2 Factory Pattern
18.3 Observer Pattern
18.4 Builder Pattern (brief overview)

19. Best Practices

19.1 Favor Composition Over Inheritance
19.2 Keep Classes Focused (Single Responsibility Principle)
19.3 Naming Conventions (PascalCase for classes)
19.4 When to Use OOP vs Functional Approach
