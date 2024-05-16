# You are required to write a program to sort the (name, age, score) tuples by ascending order where name
# is string, age and score are numbers. The tuples are input by console. The sort criteria is:

# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.

# If the following tuples are given as input to the program:
lst = []

while True:
    person_info = tuple(
        input('Please enter your name, age, and score separated by commas: ').split(','))
    if not person_info[0]:
        break
    lst.append(person_info)

print(sorted(lst, key=lambda x: (x[0], int(x[1]), int(x[2]))))
