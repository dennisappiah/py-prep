import time
from datetime import datetime


"""returns current time in seconds since the epoch as a floating-point number"""
timestamp = time.time()
print(timestamp)


"""converting date objects to strings"""
formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
print("Current time:", formatted_time)


"""parse string dates into actual datetime"""
dt = datetime.strptime("2018/01/02", "%Y/%m/%d")
print(dt)
print(dt.month, dt.year)
