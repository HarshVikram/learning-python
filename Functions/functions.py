# Basic examples of Functions
def thing() :
    print("Hello")
    print("Fun")

thing()
print("Zip")
thing()

# Using max and min in-built functions
x = 'banana'
y = max(x)
print(y)

# Function with Paramaeters
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

# Default value Parameter Functions
def addtwo(a, b, c = None):
    if (c == None):
        return a + b
    else:
        return a + b + c

# Recursive Function
def recursion(k):
    if k > 0:
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("Recursion Example Results")
recursion(10)