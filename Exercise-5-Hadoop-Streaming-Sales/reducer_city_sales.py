#!/usr/bin/env python3
import sys

current_city = None
current_total = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    city, sales = line.split('\t')
    sales = float(sales)

    if current_city == city:
        current_total += sales
    else:
        if current_city:
            print(f"{current_city}\t{current_total:.2f}")

        current_city = city
        current_total = sales

if current_city:
    print(f"{current_city}\t{current_total:.2f}")
