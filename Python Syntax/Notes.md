# Conditional Statements
Python supports the usual logical conditions from mathematics:
* Equals: a == b
* Not Equals: a != b
* Less than: a < b
* Less than or equal to: a <= b
* Greater than: a > b
* Greater than or equal to: a >= b

## If-Else statements

### If
```python
a = 33
b = 200
if b > a:
	print("b is greater than a")
```
**Indentation**
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

### Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
```python
a = 33
b = 33
if b > a:
	print("b is greater than a")
elif a == b:
	print("a and b are equal")
```

### Else
The else keyword catches anything which isn't caught by the preceding conditions.
```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
```
You can also have an else without the elif,
```python
a = 200
b = 33
if b > a:
	print("b is greater than a")
else:
	print("b is not greater than a")
```

### Nested If
You can have if statements inside if statements, this is called nested if statements.
```python
x = 41
if x > 10:
  	print("Above ten,")
  	if x > 20:
    	print("and also above 20!")
  	else:
    	print("but not above 20.")
```

### The Pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
```python
a = 33
b = 200
if b > a:
  	pass
```

### And and Or
The and keyword is a logical operator, and is used to combine conditional statements:
```python
a = 200
b = 33
c = 500
if a > b and c > a:
  	print("Both conditions are True")
```
The or keyword is a logical operator, and is used to combine conditional statements:
```python
a = 200
b = 33
c = 500
if a > b or a > c:
  	print("At least one of the conditions is True")
```

### Short Hand If-Else (or Ternary Operators)
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
```python
a = 2
b = 330
print("A") if a > b else print("B")
```

## Try Except
The **try** block lets you test a block of code for errors. The **except** block lets you handle the error. The **finally** block lets you execute code, regardless of the result of the try and except blocks.
```python
try:
  	print(x)
except:
  	print("An exception occurred")
```
Since the try block raises an error, the except block will be executed. Without the try block, the program will crash and raise an error like,
```python
print("x")
```

You can define as many exception blocks as you want, if you want to execute a special block of code for a special kind of error,
```python
try:
  	print(x)
except NameError:
  	print("Variable x is not defined")
except:
  	print("Something else went wrong")
```

You can use the else keyword to define a block of code to be executed if no errors were raised,
```python
try:
  	print("Hello")
except:
  	print("Something went wrong")
else:
  	print("Nothing went wrong")
```

The finally block, if specified, will be executed regardless if the try block raises an error or not.
```python
try:
  	print(x)
except:
  	print("Something went wrong")
finally:
  	print("The 'try except' is finished")
```
This can be useful to close objects and clean up resources,
```python
try:
  	f = open("demofile.txt")
  	try:
    	f.write("Lorum Ipsum")
  	except:
    	print("Something went wrong when writing to the file")
  	finally:
    	f.close()
except:
  	print("Something went wrong when opening the file")
```
The program can continue, without leaving the file object open.

You can choose to throw an exception if a condition occurs. To throw (or raise) an exception, use the raise keyword.
```python
x = -1
if x < 0:
  	raise Exception("Sorry, no numbers below zero")
```
The raise keyword is used to raise an exception.
```python
x = "hello"
if not type(x) is int:
  	raise TypeError("Only integers are allowed")
```
You can define what kind of error to raise, and the text to print to the user.

## While Loop statements
While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed. While loop falls under the category of indefinite iteration, ehich means that the number of times the loop is executed isn’t specified explicitly in advance.
```python
count = 0
while count < 3:
    count = count + 1
    print("Hello")
```

### Short Hand While Block
If the while block consists of a single statement we can declare the entire loop in a single line. If there are multiple statements in the block that makes up the loop body, they can be separated by semicolons (;). 
```python
count = 0
while (count < 5): count += 1; print("Hello")
```

### Continue Statement
With the continue statement we can stop the current iteration, and continue with the next:
```python
i = 0
a = 'hello'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue        
    print('Current Letter :', a[i])
    i += 1
```

### Break Statement
With the break statement we can stop the loop even if the while condition is true:
```python
i = 0
a = 'hello'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break     
    print('Current Letter :', a[i])
    i += 1
```

### Pass Statement
The pass statement is used to write empty loops. Pass is also used for empty control statements, functions, and classes.
```python
a = 'hello'
i = 0
while i < len(a):
    i += 1
    pass
print('Value of i :', i)
```

### Else Statement
With the else statement we can run a block of code once when the condition no longer is true:
```python
i = 1
while i < 6:
  	print(i)
  	i += 1
else:
  	print("i is no longer less than 6")
```

## For Loop Statements
For loop is used for sequential traversal i.e. it is used for iterating over an iterable like string, tuple, list, etc. It falls under the category of definite iteration. Definite iterations mean the number of repetitions is specified explicitly in advance.
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```
The for loop does not require an indexing variable to set beforehand.

### Looping Through a String, List, and Dictionary
Even strings are iterable objects, they contain a sequence of characters,
```python
# Iterating over a list
l = ["apple", "banana", "cherry"]
for i in l:
    print(i)
 
# Iterating over a tuple (immutable)
t = ("apple", "banana", "cherry")
for i in t:
    print(i)
 
# Iterating over a String
s = "apple"
for i in s:
    print(i)
 
# Iterating over dictionary
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))
```

### The range() Function
range() is a built-in function that is used when a user needs to perform an action a specific number of times.The range() function is used to generate a sequence of numbers. Depending on how many arguments user is passing to the function, user can decide where that series of numbers will begin and end as well as how big the difference will be between one number and the next. The range() function takes mainly three arguments. 
range(start, stop, step)
* **start**: integer starting from which the sequence of integers is to be returned.
* **stop**: integer before which the sequence of integers is to be returned. The range of integers end at stop – 1.
* **step**: integer value which determines the increment between each integer in the sequence.
```python
# printing a number
for i in range(10):
    print(i, end=" ")
print()
 
# using range for iteration
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")
print()
 
# performing sum of first 10 numbers
sum = 0
for i in range(1, 10):
    sum = sum + i
print("Sum of first 10 numbers :", sum)
```

### Nested For Loops
A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop".
```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
```

### The break Statement
With the break statement we can stop the loop before it has looped through all the items:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
```

### The continue Statement
With the continue statement we can stop the current iteration of the loop, and continue with the next:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
```

### Else in For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
```python
for x in range(6):
    print(x)
else:
    print("Finally finished!")
```