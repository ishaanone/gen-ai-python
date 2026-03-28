# Python Naming Conventions (OOP Basics)

## 🧠 Class Naming in Python

In Python, class names should follow **PascalCase (CapWords)**:

* Every word starts with a **capital letter**
* No underscores are used
* Same convention as Java

### ✅ Correct:

```python
class Student:
    pass

class BankAccount:
    pass
```

### ❌ Incorrect:

```python
class student:      # wrong style
    pass

class bank_account:  # wrong for class
    pass
```

---

## 📌 Important Distinction

| Type     | Naming Style | Example               |
| -------- | ------------ | --------------------- |
| Class    | PascalCase   | `Student`, `CarModel` |
| Variable | snake_case   | `student_name`        |
| Function | snake_case   | `get_data()`          |

---

## ❓ Is PascalCase same as camelCase?

👉 **No, they are NOT the same**

### 🧠 Difference:

### 🔹 PascalCase (CapWords)

* Every word starts with a **capital letter**
* No underscores

```python
class BankAccount:
class StudentDetails:
```

### 🔹 camelCase

* First word starts with a **small letter**
* Next words start with **capital letters**

```python
bankAccount
studentDetails
```

---

## 📊 Comparison

| Style      | Example       | Used for                   |
| ---------- | ------------- | -------------------------- |
| PascalCase | `BankAccount` | Class names (Python, Java) |
| camelCase  | `bankAccount` | Variables (Java, JS)       |

---

## 🎯 Interview Answer

👉 PascalCase capitalizes every word, while camelCase starts with a lowercase letter and capitalizes subsequent words.

---

## 📂 Class Name vs File Name in Python

👉 **They are NOT required to be the same (unlike Java)**

### ✅ Recommended:

* Use **snake_case** for file names

```bash
student.py
```

---

## 🧠 Rule (PEP 8):

* File names → **snake_case**
* Class names → **PascalCase**

---

## 📦 Example (Multiple Words)

### 👉 Class:

```python
class BankAccount:
    pass
```

### 👉 File:

```bash
bank_account.py
```

---

## ❌ Not Recommended:

```bash
Student.py        # ❌ not Python style
bankAccount.py    # ❌ camelCase
```

🔍 Important detail (very useful for interviews):

Technically:

__init__ is NOT the real constructor
Real constructor is __new__ (rarely used)

class Student:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")

s1 = Student()

Output:
    Creating object
    Initializing object

    🎯 Interview answer:

👉 Use .lower() or .casefold() to perform case-insensitive string comparison in Python.