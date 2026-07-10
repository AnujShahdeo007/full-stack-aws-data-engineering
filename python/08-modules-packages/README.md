# Notes

Here are all the topics under Modules & Packages in Python:
1. Fundamentals

1.1 What is a Module
1.2 What is a Package
1.3 Module vs Package vs Library vs Framework (Differences)
1.4 Why Use Modules (Code Reusability, Organization)

2. Importing Modules

2.1 import module_name
2.2 import module_name as alias
2.3 from module_name import function_name
2.4 from module_name import function_name as alias
2.5 from module_name import * (Wildcard Import) — and Why to Avoid It
2.6 Importing Multiple Modules in One Line
2.7 Conditional Imports

3. Creating Your Own Modules

3.1 Writing a Custom Module (.py file)
3.2 Importing a Custom Module
3.3 Module Search Path (sys.path)
3.4 Adding Directories to sys.path

4. The __name__ == "__main__" Pattern

4.1 What __name__ Represents
4.2 Why Use if __name__ == "__main__":
4.3 Difference Between Running a Script Directly vs Importing It

5. Module Reloading

5.1 importlib.reload()
5.2 Why Modules Aren't Re-imported Automatically (Caching Behavior)

6. Packages

6.1 What Makes a Directory a Package
6.2 __init__.py File (Purpose & Usage)
6.3 Regular Packages vs Namespace Packages
6.4 Creating a Package (Folder Structure)
6.5 Importing from a Package
6.6 Sub-Packages (Nested Packages)
6.7 Relative Imports (., ..)
6.8 Absolute Imports vs Relative Imports

7. __init__.py Deep Dive

7.1 Empty __init__.py (Marking a Package)
7.2 Controlling What Gets Imported (__all__)
7.3 Initializing Package-Level Variables/Imports

8. The Python Standard Library (Overview)

8.1 What is the Standard Library
8.2 Commonly Used Standard Modules (os, sys, math, random, datetime, re, json, collections, itertools, functools, statistics, string, time, copy, logging, argparse, subprocess)
8.3 Exploring Modules with dir() and help()

9. Package Management with pip

9.1 What is pip
9.2 Installing Packages (pip install package_name)
9.3 Installing Specific Versions (pip install package==version)
9.4 Upgrading Packages (pip install --upgrade)
9.5 Uninstalling Packages (pip uninstall)
9.6 Listing Installed Packages (pip list, pip freeze)
9.7 requirements.txt File (Creating & Installing From It)
9.8 pip show (Package Details)
9.9 Installing from GitHub/Local Source
9.10 pip search (Deprecated) & Alternatives (PyPI website)

10. Virtual Environments

10.1 Why Virtual Environments Are Needed (Dependency Isolation)
10.2 venv Module (Built-in)
10.3 Creating a Virtual Environment (python -m venv env_name)
10.4 Activating/Deactivating a Virtual Environment
10.5 virtualenv (Third-Party Alternative)
10.6 conda Environments (Overview, Data Science Context)
10.7 pipenv (Overview)
10.8 poetry (Overview — Modern Dependency Management)
10.9 Managing .gitignore for Virtual Environments

11. Publishing Your Own Package

11.1 Package Structure for Distribution (setup.py, pyproject.toml)
11.2 setuptools Basics
11.3 Building a Package (build module)
11.4 Publishing to PyPI (twine upload) — Overview
11.5 Versioning Conventions (Semantic Versioning)

12. Module Attributes & Introspection

12.1 __file__ Attribute
12.2 __name__ Attribute (Module Context)
12.3 __doc__ Attribute
12.4 dir(module) — Listing Module Contents
12.5 __package__ Attribute

13. Circular Imports

13.1 What is a Circular Import
13.2 Why It Causes Errors
13.3 How to Resolve Circular Imports (restructuring, local imports)

14. Lazy Imports & Performance

14.1 Importing Inside a Function (Lazy Loading)
14.2 Import Performance Considerations
14.3 __pycache__ and .pyc Files (Compiled Bytecode)

15. Namespace Packages (Advanced)

15.1 What is a Namespace Package (PEP 420)
15.2 Difference from Regular Packages (No __init__.py Required)

16. Best Practices

16.1 One Module, One Responsibility
16.2 Avoid Wildcard Imports (import *)
16.3 Organizing Large Projects into Packages
16.4 Consistent Naming Conventions (lowercase, underscores)
16.5 Keeping requirements.txt Updated
16.6 Using Virtual Environments Per Project

17. Real-World / Applied Topics

17.1 Structuring a Data Engineering Project into Modules/Packages
17.2 Managing Dependencies Across Environments (dev, staging, prod)
17.3 Using requirements.txt in Docker/CI-CD Pipelines
17.4 Third-Party Data Engineering Packages Overview (boto3, pandas, pyspark, sqlalchemy, requests)