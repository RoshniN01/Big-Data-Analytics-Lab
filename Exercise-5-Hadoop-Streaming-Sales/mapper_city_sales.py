#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    fields = line.split(',')

    if len(fields) != 5:
        continue

    date, city, product, quantity, price = fields

    try:
        quantity = int(quantity)
        price = float(price)
        sales = quantity * price
        print(f"{city}\t{sales}")
    except:
        continue
