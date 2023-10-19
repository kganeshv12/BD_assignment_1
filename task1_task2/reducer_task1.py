#!/usr/bin/python3
"""reducer.py"""

import sys
import json

prev_name = None
prev_count = 1
prev_strike_rate = 0.0
final_strike_rate = 0.0

output_data = []

for line in sys.stdin:
    line = line.strip()
    name, strike_rate, count = line.split('\t')

    strike_rate = float(strike_rate)
    count = int(count)

    if prev_name == name:
        prev_count += count
        prev_strike_rate += strike_rate

    else:
		  if prev_count != 1:
			  final_strike_rate = round(prev_strike_rate / prev_count, 3)
	#				print('{"name": ',prev_name,'"strike_rate": ',final_strike_rate)
				print('{"name": ',prev_name, '"strike_rate": ',final_strike_rate,'}')
      prev_count = 1
      prev_strike_rate = strike_rate
      prev_name = name

final_strike_rate = round(prev_strike_rate / prev_count, 3)
print('{"name": ',prev_name, '"strike_rate": ',final_strike_rate,'}')
#output_data.append({"name": prev_name,"strike_rate": final_strike_rate})
#for j in range(len(output_data)):
	#print(output_data[j])

