n = 0
print(f"n = {n}")

n = "abc"
print(f"n = {n}")

# Multiple assignments
n, m = 0, "abc"

n, m, z = 0.125, "abc", False

# Increment
n = n + 1
n +=1
# n++ not used.

# None is null (absence of value)
n = 4
n = None
print("n =",n)

# If statements
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n +=2
    
# Parentheses only needed when multi-line conditions.
# and = &&
# or = ||
n , m = 1, 2
if ((n>2 and n!=m) or n == m):
    n +=1  
    
# while loops 
n = 0
while n < 5:
    print(n)
    n += 1
    
# For loops
for i in range(5):
    print(i) 
    
for i in range(2, 6): # Start at 2 but not include 6
    print(i)

for i in range(5, 1, -1): # decrements to -1.
    print(i)
 
# Division is demical by default
print(5 / 2)

# Rounded numbers
print(5 // 2)

# decimal division
print(int(-3/2))

# Modular
print(10 % 3)

#Except for negatives
print(-10 % 3)

# To be consistent
import math
print(math.fmod(-10,3))
# Helpers
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

# Max / Min Int
float("inf")
float("inf")

# numbers are infinite
print(math.pow(2,200))

# Check if less than infinity
print(math.pow(2,200) < float("inf"))

# Array (called lists)
arr = [1,2,3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr.insert(1,7)
print(arr)

arr[0] = 0
arr[3] = 0

print(arr)

# Init arr of size n with default val of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful: -1 is not out of bound but last val
arr = [1,2,3]
print(arr[-1])
print(arr[-2])

# Subtlists (slicing)
arr = [1,2,3,4]
print(arr[1:3]) # 2,3
print(arr[0:3]) # 1,2,3

# Unpacking (variables must match)
a, b, c = [1,2,3]
print(a,b,c)

# Loop through arrays
nums = [1,2,3]

for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)
    
# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Loop through multiple arrays simultaneously 
# with unpacking
nums1 = [1,3,5]
nums2 = [2,4,6]

for n1, n2 in zip(nums1, nums2):
    print(f"{n1,n2}")    

# Reverse
nums = [1,2,3]
nums.reverse()
print(nums)

# Sorting
nums = [5,4,7, 3, 8]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

arr = ['bob', 'alice', 'john','doe']
arr.sort()
print(arr)

# Custom sort (by length of string)
arr.sort(key=lambda x: len(x))
print(arr)

# List comprehension
arr = [i for i in range(5)]
print(arr)

# List comprehension (add a value)
arr = [i+i for i in range(5)]
print(arr)

# 2D list
arr = [[0] * 4 for i in range(4)]
print(arr)

# String are arrays too
s = "abc"
print(s[0:2])
# But they are immutable
# So this creates a new string
s += "def"
print(s)

# Valid numeric strings can be converted
print(int("123") + int("123"))

# And numbers can be converted to strings
print(str(123) + str(123))

# To get ASCII value of a char
print(ord("a"))
print(ord("b"))

# Combine a list of strings (with an empty string delimiter)
strings = ["ab", "cd", "ef"]
print("".join(strings))

# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)

# HashSet (you can search them in constant time)
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

# list to set
print(set([1,2,3]))

# Set comprehension
mySet = { i for i in range(5)}
print(mySet)

# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice":90,"bob":70}
print(myMap)

# Dict comprehension
myMap = {i: 2*i for i in range(3)}
print(myMap)

# Looping thru a map
myMap = {"alice":90,"bob":70}
for key in myMap:
    print(key, myMap[key])
    
for val in myMap.values():
    print(val)
    
for key, val in myMap.items():
    print(key, val)
    
# Tuples are like arrays but immutable
tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1])

# Can't modify 
# tup[0] = 0

# Can be used as key for hash map/set
myMap = { (1,2): 3 }
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# Lists can't be keys
# myMap[[3,4]] = 5

# Heaps
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))
    
# No max heaps by default, work around is
# to use min heap and multiply by -1 when
# push and pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
    
# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))
    
# Funtions
def myFunc(n, m):
    return n * m

print(myFunc(3,4))

# Nested functions have access to outer
# variables
def outer(a, b):
    c = "c"
    def inner():
        return a + b + c
    return inner()

print(outer("a","b"))

# Can modify objects but not reassign
# unless using nonlolcal keyword
def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2
            
        # will only modify val in the helper scope
        # val *= 2
        
        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)
    
nums = [1, 2]
val = 3
double(nums, val)

# Class

class MyClass:
    # Constructor
    def __init__(self, nums):
       # Create member variables
       self.nums = nums
       self.size = len(nums)
    
    # self key word required as param   
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()            