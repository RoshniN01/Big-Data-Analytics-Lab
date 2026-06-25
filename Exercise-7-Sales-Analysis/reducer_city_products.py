#!/usr/bin/env python3
import sys

city_sales = {}

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    city, product, sales = line.split('\t')
    sales = float(sales)

    if city not in city_sales:
        city_sales[city] = {}

    city_sales[city][product] = city_sales[city].get(product, 0) + sales

print("TOP SELLING PRODUCT IN EACH CITY")
print("=" * 45)

for city in sorted(city_sales):
    top_product = max(city_sales[city], key=city_sales[city].get)
    print(f"{city}: {top_product} (₹{city_sales[city][top_product]:,.2f})")
