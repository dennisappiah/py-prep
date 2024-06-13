# variables
name: str = "kofi"
student_count: int = 5
is_published: bool = True
message: str = """
Hi Dennis is awesome ...
"""
print(student_count)
print(is_published)
print(message)

# Escape Sequence
print('Python " Programming')
print("Python \nProgramming")

# Formatted Strings
first_name: str = "Dennis"
last_name: str = "Appiah"
fullName = f"I am {len(first_name)} {last_name}"
print(fullName)

# String Methods
course: str = " Python Programming"
capitalized_course = course.upper()
lowercase_course = capitalized_course.lower()
no_space = course.strip()
findIndex = course.find("ython")
replace_value = course.replace("y", "p")
print("swift" not in course)  # return true
print("python" in course)  # returns true
print(findIndex)
print(capitalized_course)
print(lowercase_course)
print(no_space)
print(replace_value)

# input operator
x = input("x: ")
y = int(x) + 1
print(y)
