# EXAMPLE 1

import sys

largest = 0
smallest = sys.maxint - 1
count = 0
total = 0
for i in [9, 41, 12, 3, 74, 15] :
    total = total + i
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
    count = count + 1
print(largest)
print(smallest)
print(count)
print(total)

# EXAMPLE 2

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:',  friend)
print('Done!')
