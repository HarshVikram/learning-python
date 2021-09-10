# Functions
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

## Creating and Calling a Function
In Python a function is defined using the **def** keyword, and to call a function, use the function name followed by parenthesis.
```python
def thing():
	print("HELLO")

thing()
```

## Arguments and Parameters
Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

### Parameters or Arguments?
The terms parameter and argument can be used for the same thing, information that are passed into a function.
From a function's perspective, A parameter is the variable listed inside the parentheses in the function definition. An argument is the value that is sent to the function when it is called.
```python
def number(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

number(2)
number(3)
```

### Default Arguments
A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.
```python
def home(country = "Norway"):
  	print("I am from " + country)

home("Sweden")
home("India")
home()
home("Brazil")
```

### Keyword Arguments
You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
```python
def family(child_3, child_2, child_1):
  	print("The youngest child is " + child3)

family(child_1 = "Emil", child_2 = "Tobias", child_3 = "Linus")
```

### Arbitrary Arguments ```*args```
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly.
```python
def family(*kids):
  	print("The youngest child is " + kids[2])

family("Emil", "Tobias", "Linus")
```

### Arbitrary Keyword Arguments ```**kwargs```
If you do not know how many keyword arguments that will be passed into your function, add two asterisk ** before the parameter name in the function definition. This way the function will receive a dictionary of arguments, and can access the items accordingly.
```python
def family(**kid):
  	print("His last name is " + kid["lname"])

family(fname = "Tobias", lname = "Refsnes")
```

### Passing Data Types as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
```python
def basket(food):
  	for x in food:
    	print(x)

fruits = ["apple", "banana", "cherry"]
basket(fruits)
```

### Return Values
To let a function return a value, use the return statement,
```python
def solve(x):
  	return 5 * x

print(solve(3))
print(solve(5))
print(solve(9))
```

### Function Recursion
Python also accepts function recursion, which means a defined function can call itself. Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result. The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
```python
def recursion(k):
  	if k > 0:
 		result = k + recursion(k - 1)
    	print(result)
  	else:
    	result = 0
  	return result
print("\n\nRecursion Example Results")
recursion(6)
```