#!usr/bin/env python

import sys

for line in sys.stdin:
	line = line.strip().split(',')
	sale_amount = line[4]
	current_state = line[3]
	current_category = line[2]
	
	print "%s\t%s\t%s" % (current_state,current_category,sale_amount)


