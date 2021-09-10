# EXAMPLE 1

n = input("Enter the length of countdown: ")
countdown = int(n)
while countdown >= 0 :
    print(countdown)
    countdown = countdown - 1
print("Prepare for blaastoffffff")

# EXAMPLE 2

num = 0
tot = 0.0
while True:
	sval = input('ENter a number: ')
	if sval == 'done':
		break
	try:
		fval = float(sval)
	except:
		print('invalid input')
		continue
	num = num + 1
	tot = tot + fval
print(tot, num, tot / num)