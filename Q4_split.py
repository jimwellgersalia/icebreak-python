# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and
# a tuple which contains every number.

num = input('Enter multiple numbers separated by comma: ')
my_list = num.split(',')
my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)
