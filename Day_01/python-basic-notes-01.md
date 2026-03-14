# Python Basics – Revision Notes

## 1. First Python Script

Example file: `first-script.py`

```python
print("hello ishaan.")

#Explanation

print() is used to display output on the console.
Strings must be written inside quotes ("" or '').

#Output:
hello ishaan.

## 2. Variables in Python
Example file: second-script.py
fruit = "apple"
vegetable = "carrot"
age = 45

print("fruit")
print(fruit)
print("vegetable")
print(vegetable)
print("age")
print(age)

#Concept
A variable is used to store data.
variable_name = value

Examples:
| Variable  | Value  | Type    |
| --------- | ------ | ------- |
| fruit     | apple  | string  |
| vegetable | carrot | string  |
| age       | 45     | integer |

# String Formatting
Method 1 – f-string (Recommended)
print(f"The fruit is {fruit}, the vegetable is {vegetable}, and the age is {age}")
Output:
The fruit is apple, the vegetable is carrot, and the age is 45

Method 2 – Comma Separation
print("The fruit is", fruit ,"the vegetable is", vegetable, "and the age is", age)

## 3 User Input in Python
Example file: input.py
name = input("enter your name: ")
print(f"your name is {name}")

age = input("enter you age: ")
print(f"your name is {name}, your age is {age}")

#Concept:
input() is used to take input from the user.

#Syntax
input("message")

Example
enter your name: Ishaan
your name is Ishaan

⚠️ Important:
input() always returns string data type.

## 5. Strings in Python
Example file: string.py
# Using Quotes
print("it's a beautiful day.")
print("he is called 'Johny'")
print('he is called "Johny"')

Python allows:
    Single quotes '
    Double quotes "
# Storing Strings in Variables
a = "Hello"
print(a)
Output:
Hello
# Multi-line Strings
b = """hello today is wonderful day
we are learning python
and we are having fun.."""
print(b)

Triple quotes """ """ allow multi-line text.

#Escape Characters
c = 'My friends are "Johny" and \'Tommy\''
print(c)

\ is called an escape character.
Used to include quotes inside strings.
Output:
My friends are "Johny" and 'Tommy'

# String Length
a = "hello world"
print(len(a))

len() returns the number of characters.
Output:
11
# Accessing Characters (Indexing):
a = "hello world"

print(a[0])
print(a[1])
print(a[2])

Index starts from 0.
Example:
| Index | Character |
| ----- | --------- |
| 0     | h         |
| 1     | e         |
| 2     | l         |
| 3     | l         |
| 4     | o         |

# Loop Through a String
a = "hello world"

for i in a:
    print(i)

#Concept
A string is a sequence of characters.
for loop allows us to iterate through them.
Output:
h
e
l
l
o
...
# String Slicing
b = "akshat,lets learn python"

print(b[0:6])
print(b[7:11])
print(b[:6])
print(b[18:24])
print(b[18:])

Syntax:
string[start:end]

Important rules:
    start index included
    end index excluded
Example:
b[0:6] → akshat

# Slice Variations
| Syntax   | Meaning               |
| -------- | --------------------- |
| b[:6]    | from start to index 6 |
| b[18:]   | from index 18 to end  |
| b[:]     | full string           |

Example:
print(b)
print(b[:])
Both print the entire string.

# Quick Summary
| Concept                | Function  |
| ---------------------- | --------- |
| Print output           |  print()  |
| Store data             | variables |
| Take user input        |  input()  |
| String length          |  len()    |
| Loop through string    |  for      |
| Extract part of string | slicing   |
