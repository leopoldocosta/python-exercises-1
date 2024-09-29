Here is an improved version of my Python automation course notes, formatted for better readability, clarity, and usability.


## Table of Contents
1. [Installing Python](#1-installing-python)
2. [Creating a Virtual Environment](#2-creating-a-virtual-environment)
3. [Activating the Created Environment](#3-activating-the-created-environment)
4. [Updating PIP](#4-updating-pip)
5. [Checking Installed Modules](#5-checking-installed-modules)
6. [Installing Requirements](#6-installing-requirements)
7. [Configuring IPython Autocomplete](#7-configuring-ipython-autocomplete)
8. [Using IPython REPL](#8-using-ipython-repl)
9. [Python Variables and Naming Conventions](#9-python-variables-and-naming-conventions)
10. [String Operations](#10-string-operations)
11. [Python Best Practices](#11-python-best-practices)
12. [Working with Columns](#12-working-with-columns)


---

# Python Automation for Network Engineers

This document contains useful Python commands and tips for network engineers, focused on automating tasks using Python. It covers setting up environments, using IPython for interactive programming, and best practices for writing Pythonic code.

---

## 1. Installing Python

**Steps to install Python for the development environment.**

- You can install Python from the [official website](https://www.python.org/downloads/).

---

## 2. Creating a Virtual Environment

```bash
# Create a virtual environment
py -m venv py311_venv
```

A virtual environment isolates your Python setup and dependencies, ensuring consistent behavior across projects.

---

## 3. Activating the Created Environment

To activate the virtual environment on Windows:

```bash
# Command to activate the virtual environment
py311_venv\Scripts\activate
```

---

## 4. Updating PIP

PIP is Python’s package manager. It's recommended to keep it updated.

```bash
# Upgrade pip to a specific version
python.exe -m pip install --upgrade pip
```

---

## 5. Checking Installed Modules

To list all installed Python packages in the virtual environment:

```bash
pip list
```

---

## 6. Installing Requirements

You can install the required packages by specifying them in a `requirements.txt` file:

```bash
# Sample requirements.txt
ipython==8.6.0
pylama==8.4.1
black==23.3.0
rich==13.3.3
netmiko==4.2.0
emoji==2.2.0
```

Install the packages by running:

```bash
pip install -r requirements.txt
```

---

## 7. Configuring IPython Autocomplete

To enable autocompletion in IPython, create a profile:

```bash
ipython profile create
```

Edit the generated config file (`ipython_config.py`) and add:

```python
c = get_config()
c.TerminalInteractiveShell.autosuggestions_provider = None
```

This configuration disables autosuggestions.

---

## 8. Using IPython REPL

IPython provides an interactive shell for experimenting with Python code. Start it with:

```bash
python -m IPython
```

---

## 9. Dunder Variables (Magic Variables)

Python provides built-in magic variables (dunder variables), such as:

- `__name__`: Identifies the name of the module being run.
- `_`: A throwaway variable for the last output in the REPL.

Example:

```python
# Check the special __name__ variable
__name__  # Output: '__main__'
```

---

## 10. Naming Conventions in Python

- **Class Names**: Use `PascalCase`.
- **Constants**: Use `ALL_CAPS`.
- **Throwaway Variables**: Use `_`.

Adhering to these conventions helps maintain clean and readable code.

---

## 11. Print and Input in Python

Python's `print()` and `input()` functions are essential for interacting with users:

```python
# Print examples
print("Hello World")
print(22)

# Taking user input
my_var = input("Enter an IP address: ")
print(my_var)
```

---

## 12. Indentation Matters in Python

**Always use spaces** instead of tabs for indentation in Python (recommended: 4 spaces). Python enforces proper indentation as part of its syntax.

- Style guide reference: [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

---

## 13. Append vs. Extend for Lists

- **`append()`**: Adds a single element to the end of a list.
- **`extend()`**: Adds elements from an iterable to the list.

```python
my_list = [1, 2, 3]
my_list.append(4)  # [1, 2, 3, 4]
my_list.extend([5, 6])  # [1, 2, 3, 4, 5, 6]
```

---

## 14. Tuples in Python

Tuples are immutable sequences used to store collections of data.

```python
my_tuple = (1, 2, 3)
```

- More on tuples: [Tuple Data Type](https://www.w3schools.com/python/python_tuples.asp)

---

## 15. Executing a Script in Python

To run a Python script:

```bash
#!/usr/bin/env python

chmod 755 my_script.py
./my_script.py
```

Make sure the script is executable (`chmod 755`) before running it.

---

## 16. Using the `dir()` Method

The `dir()` function returns a list of attributes and methods of an object.

```python
my_var = "a string"
dir(my_var)
```

---

## 17. Using the `help()` Method

Use the `help()` function to learn more about any Python object or method:

```python
help(my_var.strip)
```

---

## 18. Multi-line Strings

You can create multi-line strings with triple quotes (`"""` or `'''`):

```python
multi_line = """
This is a 
multi-line string.
"""
```

---

## 19. String Methods and Operations

**Examples of string methods:**

```python
my_var = "a string"
my_var.upper()  # 'A STRING'
```

- `split()`: Breaks a string into a list based on a delimiter.
- `join()`: Joins elements of a list into a string.

---

## 20. F-strings in Python

F-strings provide a concise way to embed expressions in strings:

```python
my_var = "a string"
f"This is {my_var}"  # 'This is a string'
```

You can also embed expressions:

```python
f"2 + 2 is {2 + 2}"  # '2 + 2 is 4'
```

---

## 21. String Membership and Raw Strings

- **Membership**: Check if a substring exists within a string:

```python
"is" in "this is a string"  # True
```

- **Raw Strings**: Disable escape sequences with an `r` prefix:

```python
win_path = r"c:\windows\system32"
print(win_path)  # 'c:\windows\system32'
```

---

## 22. String Concatenation

You can concatenate strings using `+` or `+=`:

```python
city = "New York"
state = "NY"
location = city + ", " + state
```

---

## 23. Accessing String Indexes

Strings in Python can be accessed using index positions:

```python
my_var = "Hello"
my_var[1]  # 'e'
```

---

## 24. Working with Columns

You can format and align text in columns using F-strings:

```python
ip_addr1 = "192.168.0.1"
ip_addr2 = "10.0.0.1"
print(f"{ip_addr1:<20}{ip_addr2:<20}")
```

---

### Suggestions for Further Improvement:
1. **Organize Notes into Sections**: Group topics like "String Operations", "Python Best Practices", "File I/O", etc., to improve flow.
2. **Add More Links to References**: Where applicable, link to specific tutorials or documentation for a deeper understanding.
3. **Enhance Example Codes**: Add more context or use-case examples for each Python snippet to make it more practical for network automation.

Let me know if you'd like to proceed with these suggestions!
