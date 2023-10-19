#!/usr/bin/env python3
"""mapper.py"""

import sys
import json


for data in sys.stdin:
	data = data.strip()
	data = data.strip(",")

	try:
		data_array = json.loads(data)
		runs = data_array.get("runs",0)
		balls = data_array.get("balls",0)
		name = data_array["name"]

		if runs!=0 and balls!=0:

			strike_rate = round((runs/balls)*100, 3)	
		else:
			strike_rate = 0.0
			

		count = 1	
		print(f"{name}\t{strike_rate}\t{count}")
			
	except json.JSONDecodeError:
		continue
		

		
