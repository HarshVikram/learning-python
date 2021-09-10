import sys

# Counting in a loop
counter = 0
l = [9, 41, 24, 22, 3, 7, 12, 99]
for i in l:
	counter = counter + 1
print('The list has', counter, 'elements')

# Summing in a loop
sum = 0
l = [9, 41, 24, 22, 3, 7, 12, 99]
for i in l:
	sum = sum + i
print('The sum of elements in the list is', sum)

# Finding the average in a loop
counter = 0
sum = 0
l = [9, 41, 24, 22, 3, 7, 12, 99]
for i in l:
	counter = counter + 1
	sum = sum + i
average = float(sum/counter)
print('The average of elements in the list is', average)

# Searching in a loop
found = False
value = 4
l = [9, 41, 24, 22, 3, 7, 12, 99]
for i in l:
	if i == value:
		found = True
		break
if found == True:
	print('The value ', value, ' was found in the list')
else:
	print('Value', value, 'was not found')

# Finding the largest value in a loop
l = [9, 41, 24, 22, 3, 7, 12, 99]
largest = 0
for i in l:
	if i > largest:
		largest = i
print('The largest value in the list is', largest)

# Finding the smallest value in a loop
l = [9, 41, 24, 22, 3, 7, 12, 99]
smallest = None
for i in l:
	if smallest == None:
		smallest = i
	elif i < smallest:
		smallest = i
print('The smallest value in the list is', smallest)