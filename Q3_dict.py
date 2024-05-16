# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an
# integral number between 1 and n (both included). and then the program should print the dictionary

num = int(input('Enter a number to generate dict: '))
# using comprehension
# my_dict = {i: i*i for i in range(1, num+1)}

my_dict = {}

for i in range(1, num+1):
    my_dict.update({i: i*i})

print(my_dict)
