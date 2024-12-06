# Python Basics Tutorial

This script serves as a comprehensive tutorial covering fundamental Python programming concepts. Each section demonstrates key language features and programming patterns.

## Table of Contents
- [Variables and Type Conversion](#variables-and-type-conversion)
- [Conditional Statements](#conditional-statements)
- [Loops](#loops)
- [Mathematical Operations](#mathematical-operations)
- [Lists](#lists)
- [String Manipulation](#string-manipulation)
- [Data Structures](#data-structures)
  - [Deque](#deque)
  - [HashSet](#hashset)
  - [HashMap](#hashmap)
  - [Tuples](#tuples)
  - [Heaps](#heaps)
- [Functions](#functions)
- [Classes](#classes)

## Variables and Type Conversion

### Basic Variable Assignment
```python
n = 0  # Integer assignment
n = "abc"  # Dynamic typing allows changing types
n, m = 0, "abc"  # Multiple assignments
```

### Type Conversions
```python
# Numeric string to integer
print(int("123") + int("123"))

# Number to string
print(str(123) + str(123))

# ASCII value of characters
print(ord("a"))  # Get ASCII value
```

## Conditional Statements

### If-Elif-Else Structure
```python
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Logical operators
if ((n > 2 and n != m) or n == m):
    n += 1
```

## Loops

### While Loops
```python
n = 0
while n < 5:
    print(n)
    n += 1
```

### For Loops
```python
# Basic range
for i in range(5):
    print(i)

# Custom range
for i in range(2, 6):  # Start at 2, exclude 6
    print(i)

# Reverse range
for i in range(5, 1, -1):
    print(i)
```

## Mathematical Operations

### Division Types
```python
print(5 / 2)    # Decimal division (2.5)
print(5 // 2)   # Integer division (2)
print(int(-3/2))  # Rounded division

# Modulo operations
print(10 % 3)   # Standard modulo
print(math.fmod(-10, 3))  # Consistent modulo for negative numbers
```

### Math Helpers
```python
import math
print(math.floor(3/2))  # Floor division
print(math.ceil(3/2))   # Ceiling division
print(math.sqrt(2))     # Square root
print(math.pow(2, 3))   # Power
```

## Lists

### List Operations
```python
arr = [1, 2, 3]
arr.append(4)   # Add to end
arr.pop()       # Remove last element
arr.insert(1, 7)  # Insert at specific index

# List initialization
arr = [1] * 5   # [1, 1, 1, 1, 1]

# Slicing
print(arr[1:3])  # Sublist

# List comprehensions
arr = [i for i in range(5)]  # [0, 1, 2, 3, 4]
arr = [i+i for i in range(5)]  # [0, 2, 4, 6, 8]

# 2D list
arr = [[0] * 4 for i in range(4)]
```

### List Iteration
```python
nums = [1, 2, 3]
for i in range(len(nums)):
    print(nums[i])

for n in nums:
    print(n)

for i, n in enumerate(nums):
    print(i, n)
```

## String Manipulation
```python
s = "abc"
print(s[0:2])  # Substring
s += "def"     # String concatenation

# Join strings
strings = ["ab", "cd", "ef"]
print("".join(strings))
```

## Data Structures

### Deque (Double-Ended Queue)
```python
from collections import deque
queue = deque()
queue.append(1)
queue.appendleft(1)
queue.popleft()
queue.pop()
```

### HashSet
```python
mySet = set()
mySet.add(1)
print(2 in mySet)
mySet.remove(2)
```

### HashMap (Dictionary)
```python
myMap = {}
myMap["alice"] = 88
print(myMap["alice"])
print("alice" in myMap)

# Iteration
for key, val in myMap.items():
    print(key, val)
```

### Tuples
```python
tup = (1, 2, 3)
# Immutable, can be used as dict/set keys
myMap = {(1, 2): 3}
```

### Heaps
```python
import heapq

# Min Heap
minHeap = []
heapq.heappush(minHeap, 3)
min_val = heapq.heappop(minHeap)

# Max Heap (workaround)
maxHeap = []
heapq.heappush(maxHeap, -3)
max_val = -1 * heapq.heappop(maxHeap)
```

## Functions

### Basic Function
```python
def myFunc(n, m):
    return n * m

# Nested functions
def outer(a, b):
    def inner():
        return a + b
    return inner()
```

### Modifying Variables
```python
def double(arr, val):
    def helper():
        nonlocal val
        val *= 2
    helper()
```

## Classes

```python
class MyClass:
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)
    
    def getLength(self):
        return self.size
```

## Key Takeaways
- Python is dynamically typed
- Lists are zero-indexed
- Slicing is powerful for list/string manipulation
- Many built-in data structures and methods
- Functions can be nested
- Classes use `self` keyword

## Recommended Practice
1. Experiment with each concept
2. Try combining different techniques
3. Write small programs to reinforce learning

## Resources
- [Official Python Documentation](https://docs.python.org/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

*Note: This README is based on a comprehensive Python basics script, covering fundamental programming concepts.*# pylearn
