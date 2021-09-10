size = input('Enter the size of shirt: ')
value = int(size)
if value == 40:
    print(' is S')
elif value == 42:
    print(size + ' is M')
elif value == 44:
    print(size + ' is L')
elif value > 44:
	print('Size is not available')
else:
	print('We would have to place a custom order')

