#!usr/bin/env/ python

import sys
prev_state = None
prev_category = None
total_sale = 0

for line in sys.stdin:
	line = line.strip()
	current_state,current_category,sale_amount =  line.split('\t') 
	sale_amount = float(sale_amount)
	if current_state == prev_state:
		if current_category == prev_category:
			total_sale = sale_amount + total_sale
		else:  
			print '%s\t%s\t%s' % (current_state,prev_category,total_sale)
			prev_category = current_category
			total_sale = sale_amount
	else:
		prev_state = current_state
		prev_category = current_category
                total_sale = sale_amount
if current_state:
	print '%s\t%s\t%s' % (current_state,prev_category,total_sale)

