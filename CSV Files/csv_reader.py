import csv

filename = input('Enter file name: ')

fields = []
rows = []

with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = next(csvreader)

	for row in csvreader:
		rows.append(row)
	
	print("Total number of rows of data is %d" %(csvreader.line_num))

print("Field names are " + ", ".join(field for field in fields))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
	for col in row:
		print("%5s"%col)
	print("\n")