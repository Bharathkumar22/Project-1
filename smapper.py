
import sys

for lines in sys.stdin:
	data = lines.strip().split(',')
	sales = data[-1]
	state = data[-2]
	print '%s\t%s' %(state,sales)


