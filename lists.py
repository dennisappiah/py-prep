from typing import Tuple
from pprint import pprint

numbers = list(range(1, 10))

print(numbers[::2])
print(numbers[::-1])

# unpacking list
first, second, *other = numbers
print(first)
print(second)
print(other)

# unpacking dictionary
one = {"x": 2, "y": 4}
two = {"x": 5}

combined = {**one, **two, "z": 5}
print(combined)

# looping over list
for index, number in enumerate(numbers):
    print(index, number)

# list methods
letters = ["a", "b", "c", "d"]
# these list methods return None
# Add
letters.append("e")
letters.insert(2, "-")

# remove
letters.remove("c")
letters.pop(0)
del letters[:2]
print(letters)

# sort
numbers.sort(reverse=False)
print(letters)

# find items
index = letters.index("d")
print(index)
count = letters.count("f")
print(count)

# sorting list of tuples
items = [
    ("Product1", 8),
    ("Product2", 4),
    ("Product3", 5),
]

items.sort(key=lambda item: item[1])

print(items)

# Map Functions - transform a list state into something else
"""Say we are only interested in a list of prices from the items list"""
prices = []
for item in items:
    prices.append(item[1])

print(prices)

prices_ = list(map(lambda item: item[1], items))
print(prices_)

# filter functions
"""Say we are only interested in an item where price is greater than 4"""
filtered = list(filter(lambda item: item[1] > 4, items))
print(filtered)

# List comprehensions -can be used to achieve both result of map & filter functions
prices = [item[1] for item in items]
print(prices)

filtered = [item for item in items if item[1] >= 4]

# Zip function - returns a list of tuples of combined list
list1 = [2, 4, 5]
list2 = [6, 7, 8]

print(list(zip(list1, list2)))

# swap two variables
x = 6
y = 8
x, y = y, x
print(x, y)

# Arrays (numpy)

# Dictionaries
point = {"x": 2, "y": 3}
print(point["x"])
point["x"] = 4
print(point)

# get method returns None
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
# dictionaries methods
del point["y"]
print(point)

for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)

# Dictionary comprehension
values = {}
for key in range(5):
    values[key] = key * 2

print(values)

values = {x: x * 2 for x in range(5)}
print(values)

# Generators - when dealing with large datasets to create comprehension, use generator
"""generator functions are a special kind of function that return a lazy iterator.
 These are objects that you can loop over like a list. However, 
unlike lists, lazy iterators do not store their contents in memory."""

values = (x * 2 for x in range(50000000))
# print(values) -> generator object


# Most repeated value (word distribution)

sentence = "This is a common interview question"
word_distribution = {}

for word in sentence:
    if word in word_distribution:
        word_distribution[word] = word_distribution.get(word, 0) + 1
    else:
        word_distribution[word] = 1
pprint(word_distribution)

pprint(sorted(word_distribution.items(), key=lambda item: item[1], reverse=True))
