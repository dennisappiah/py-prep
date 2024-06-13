import time
from datetime import datetime


# returns current time in seconds since the epoch as a floating-point number.
print(time.time())

timestamp = time.time()
"""converting date objects to strings"""
formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
print("Current time:", formatted_time)  # Current time: 2024-02-25 22:04:56


# parse string dates into actual datetime
dt = datetime.strptime("2018/01/02", "%Y/%m/%d")
print(dt)
print(dt.month, dt.year)
