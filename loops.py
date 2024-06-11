#1, 2, 4, 5
# ICU - initialise, compare, update
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

"""
Given the variable my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- create a while loop that prints all elements of my_list 3 times
- when printing the elements, use for loop 
- However if an element of the for loop is equal to Monday, continue without printing
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

j = 0

while j < 3:
    j += 1
    for day in my_list:
        if day == "Monday":
            continue
        print(day)