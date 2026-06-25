#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split(',')

    if len(parts) != 4:
        continue

    try:
        product = parts[1]
        sales = float(parts[2])

        print(f"{product}\t{sales}")

    except ValueError:
        continue
