import random
from datetime import datetime, timedelta

cities = ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad"]
products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]

start_date = datetime(2025, 1, 1)

for i in range(50000):
    date = start_date + timedelta(days=random.randint(0, 364))
    city = random.choice(cities)
    product = random.choice(products)
    quantity = random.randint(1, 10)
    price = random.randint(500, 50000)

    print(f"{date.strftime('%Y-%m-%d')},{city},{product},{quantity},{price}")
