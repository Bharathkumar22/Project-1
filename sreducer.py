import sys
total_sales = 0
current_state = None


for lines in sys.stdin:
	lines = lines.strip()
	state,sales = lines.split('\t',1)
	sales = float(sales)
	
	if current_state == state:
		total_sales += sales
		
	else:
		if current_state != None:
			print '%s\t%s' % (current_state,total_sales)

		current_state = state
		total_sales = sales
if current_state:
	print '%s\t%s' % (current_state,total_sales)
		
