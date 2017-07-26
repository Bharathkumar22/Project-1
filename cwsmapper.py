import sys

for line in sys.stdin:
	line = line.strip().split(',')
	category_type = line[2]
	sale_amount = float(line[-1])

	print"%s\t%s" % (category_type, sale_amount)
