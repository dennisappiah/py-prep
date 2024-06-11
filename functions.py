def user_dictionary(firstname, lastname, age) -> dict[str, str]:
    created_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }

    return created_dictionary


user = user_dictionary("dennis", "appiah", 42)
print(user)

for key, value in user.items():
    print(key, value)

user2 = user.copy()
user2.pop("age")
print(user2)

homework_grades = {
    "homework1": 56,
    "homework2": 80,
    "homework3": 100
}


# takes dictionary as parameter
def average_of_grades(homework_grades_args) -> float:
    total_grade = 0
    average_grade = 0
    for grade in homework_grades_args.values():
        total_grade += grade
        average_grade = float(total_grade / len(homework_grades_args))

    return average_grade


print(average_of_grades(homework_grades))


# takes the spread of dictionary as parameter
def mean_of_ages(**homework_grades_args) -> float:
    total_grade = 0
    average_grade = 0
    for grade in homework_grades_args.values():
        total_grade += grade
        average_grade = float(total_grade / len(homework_grades_args))

    return average_grade


print(mean_of_ages(homework1=56, homework2=80, homework3=100))


# takes the spread of a tuple as parameter
def multiply(*numbers) -> int:
    total = 1
    for number in numbers:
        total = number * total
    return total


result = multiply(2, 3, 4, 5, 6)
print(result)
