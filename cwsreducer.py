#!/usr/bin/env python

import sys
prev_category = None
total_sale = 0

for line in sys.stdin:
	category_type,sale_amount = line.strip().split('\t')
	sale_amount = float(sale_amount)
	if prev_category == category_type:
		total_sale = sale_amount + total_sale
	else :
		if prev_category != None :
			print '%s\t%s' % (prev_category, total_sale)
		prev_category = category_type
		total_sale = sale_amount
if prev_category:
	print '%s\t%s' % (prev_category, total_sale)

		
